"""Run analytical material-relation tests and preserve failures with content hashes."""
from pathlib import Path
import hashlib, json, sys, unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))


class RecordedResult(unittest.TextTestResult):
    def startTest(self,test):
        super().startTest(test)
        self.records.append({'test':test.id(),'status':'running'})
    def addSuccess(self,test):
        super().addSuccess(test)
        self.records[-1]['status']='pass'
    def addFailure(self,test,err):
        super().addFailure(test,err)
        self.records[-1]['status']='fail'
    def addError(self,test,err):
        super().addError(test,err)
        self.records[-1]['status']='error'
    def addSubTest(self,test,subtest,err):
        super().addSubTest(test,subtest,err)
        if err is not None:
            self.records[-1]['status']='fail'


def main():
    RecordedResult.records=[]
    suite=unittest.defaultTestLoader.discover(str(ROOT/'tests'),pattern='test_constitutive.py')
    result=unittest.TextTestRunner(verbosity=1,resultclass=RecordedResult).run(suite)
    paths=['src/constitutive.py','tests/test_constitutive.py','scripts/check_constitutive.py','material/pla_properties.csv','material/fixture_properties.csv']
    report={'stage':5,'date':'2026-09-12','scope':'Analytical and synthetic material-point verification; not ANSYS results, specimen experiments or independent material validation. Test strain, time and panel choices are numerical fixtures.','tests_run':result.testsRun,'passed':result.wasSuccessful(),'tests':result.records,'failures':[{'test':t.id(),'traceback':trace} for t,trace in result.failures+result.errors],'sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}
    payload=json.dumps(report,indent=2,ensure_ascii=False)+'\n'
    (ROOT/'docs/stage_05_constitutive_tests.json').write_text(payload,encoding='utf-8',newline='\n')
    if not result.wasSuccessful():
        archive=ROOT/'tests/failure_records';archive.mkdir(exist_ok=True)
        (archive/(hashlib.sha256(payload.encode()).hexdigest()+'.json')).write_text(payload,encoding='utf-8',newline='\n')
        sys.exit(1)
    print(f'{result.testsRun} constitutive unit tests passed')


if __name__=='__main__': main()
