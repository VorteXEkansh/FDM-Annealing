import json, tempfile, unittest
from pathlib import Path
from ansys.run_case import load_case

class TestAutomationGate(unittest.TestCase):
    def write(self, data):
        f=tempfile.NamedTemporaryFile("w",suffix=".json",delete=False,encoding="utf-8")
        json.dump(data,f); f.close(); return Path(f.name)
    def test_smoke_admitted(self):
        p=self.write({"case_id":"s","case_kind":"environment_smoke","parameters":{},"admission":{"zero_analysis_only":True}})
        self.assertEqual(load_case(p)["case_id"],"s")
    def test_unknown_kind_rejected(self):
        p=self.write({"case_id":"s","case_kind":"unknown","parameters":{},"admission":{}})
        with self.assertRaises(ValueError): load_case(p)
    def test_missing_key_rejected(self):
        p=self.write({"case_id":"s"})
        with self.assertRaises(ValueError): load_case(p)
    def test_production_parameters_required(self):
        p=self.write({"case_id":"p","case_kind":"production","parameters":{},"admission":{}})
        with self.assertRaises(ValueError): load_case(p)
    def test_failed_gate_blocks_production(self):
        p=self.write({"case_id":"p","case_kind":"production","parameters":{"temperature_C":80,"hold_time_s":1800,"fixture_gap_mm":0.1,"material_id":"x"},"admission":{"thermal":False}})
        with self.assertRaises(RuntimeError): load_case(p)
    def test_all_true_gates_validate_only(self):
        p=self.write({"case_id":"p","case_kind":"production","parameters":{"temperature_C":80,"hold_time_s":1800,"fixture_gap_mm":0.1,"material_id":"x"},"admission":{"all":True}})
        self.assertEqual(load_case(p)["case_kind"],"production")

if __name__=="__main__": unittest.main()

