"""Archive and provenance regressions. No solver is run; examples are synthetic."""
import contextlib
import csv
import hashlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from analysis.extract_results import validate_export
from ansys import run_case


class MasterEvidenceTests(unittest.TestCase):
    def setUp(self):
        td=tempfile.TemporaryDirectory();self.addCleanup(td.cleanup);self.root=Path(td.name)
        self.spec=self.root/'case.json'
        self.spec.write_text(json.dumps({'case_id':'same','case_kind':'environment_smoke',
                                         'admission':{'zero_analysis_only':True},'parameters':{}}))
        self.dest=self.root/'simulation'/'runs'/'same'
        self.table=self.root/'export.csv'
        self.raw=self.root/'raw.csv';self.raw.write_bytes(b'test source bytes')

    def run_smoke(self,*args):
        with patch.object(run_case,'ROOT',self.root),patch.object(run_case,'MAPDL',self.raw),\
             patch.object(sys,'argv',['run_case',str(self.spec),*args]),contextlib.redirect_stdout(io.StringIO()):
            run_case.main()

    def test_dry_run_creates_no_archive(self):
        self.run_smoke()
        self.assertFalse(self.dest.exists())

    def test_existing_archive_never_overwritten(self):
        self.dest.mkdir(parents=True);manifest=self.dest/'manifest.json';manifest.write_bytes(b'prior record')
        with self.assertRaises(FileExistsError):self.run_smoke('--execute')
        self.assertEqual(manifest.read_bytes(),b'prior record')

    def test_launch_failure_preserves_evidence(self):
        deck=self.root/'ansys'/'apdl'/'environment_smoke.dat';deck.parent.mkdir(parents=True);deck.write_text('/EXIT,NOSAVE')
        with patch.object(run_case.subprocess,'run',side_effect=OSError('test launch rejection')):
            with self.assertRaises(RuntimeError):self.run_smoke('--execute')
        record=json.loads((self.dest/'manifest.json').read_text())
        self.assertFalse(record['executed']);self.assertTrue(record['launch_attempted'])
        self.assertIsNone(record['returncode'])
        self.assertEqual(record['outputs']['input.dat'],hashlib.sha256(deck.read_bytes()).hexdigest())

    def export(self,time='1',value='1',source='raw.csv'):
        with self.table.open('w',newline='',encoding='utf-8') as f:
            w=csv.writer(f);w.writerow(['case_id','time_s','quantity','value','unit','location','solver_file'])
            w.writerow(['test',time,'temperature',value,'°C','node1',source])
        return validate_export(self.table)

    def test_numeric_and_source_integrity(self):
        self.assertEqual(self.export()['raw_sha256'],{'raw.csv':hashlib.sha256(self.raw.read_bytes()).hexdigest()})
        for time,value in [('0','NaN'),('inf','1'),('-1','1')]:
            with self.subTest(time=time,value=value), self.assertRaises(ValueError):self.export(time,value)
        with self.assertRaises(FileNotFoundError):self.export(source='absent')
        for invalid in ['export.csv','../neighbor']:
            with self.subTest(source=invalid),self.assertRaises(ValueError):self.export(source=invalid)
