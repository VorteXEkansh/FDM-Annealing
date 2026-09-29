"""Missing evidence and superficial flag changes must never admit a validation run."""
import unittest
from scripts.run_validation_cases import blockers,REQUIRED

class AdmissionTests(unittest.TestCase):
    def test_missing_case(self):
        self.assertEqual(set(blockers({})),set(REQUIRED)|{'source_specific_solver_adapter_not_implemented'})
    def test_true_flags_are_not_evidence(self):
        self.assertEqual(len(blockers({'required_evidence':dict.fromkeys(REQUIRED,True)})),9)
    def test_nonexistent_evidence_rejected(self):
        evidence={k:{'path':'validation/nonexistent.json','sha256':'0'*64} for k in REQUIRED}
        self.assertEqual(len(blockers({'required_evidence':evidence})),9)
    def test_wrong_hash_rejected(self):
        evidence={k:{'path':'docs/validation_protocol.md','sha256':'0'*64} for k in REQUIRED}
        self.assertEqual(len(blockers({'required_evidence':evidence})),9)

if __name__=='__main__':unittest.main()
