import json, unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

class TestGeometryDefinition(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.d=json.loads((ROOT/'geometry/geometry_definition.json').read_text())
    def test_specimen_dimensions(self):
        s=self.d['specimen']; self.assertEqual((s['length_mm'],s['width_mm'],s['thickness_mm']),(60.0,10.0,4.0))
    def test_specimen_volume(self):
        s=self.d['specimen']; self.assertEqual(s['length_mm']*s['width_mm']*s['thickness_mm'],2400.0)
    def test_contact_face_area(self):
        s=self.d['specimen']; self.assertEqual(s['length_mm']*s['width_mm'],600.0)
    def test_aspect_ratios(self):
        s=self.d['specimen']; self.assertEqual((s['length_mm']/s['thickness_mm'],s['width_mm']/s['thickness_mm'],s['length_mm']/s['width_mm']),(15.0,2.5,6.0))
    def test_fixture_margin(self):
        s=self.d['specimen']; f=self.d['fixture']; m=f['planar_margin_each_side_mm']; self.assertEqual((f['plate_length_mm'],f['plate_width_mm']),(s['length_mm']+2*m,s['width_mm']+2*m))
    def test_clearance_normalization(self):
        s=self.d['specimen']; c=self.d['clearance_design']; self.assertTrue(all(abs(gamma-gap/s['thickness_mm'])<1e-12 for gamma,gap in zip(c['levels_gamma'],c['levels_total_gap_mm'])))
    def test_clearance_monotonic_and_nonnegative(self):
        levels=self.d['clearance_design']['levels_total_gap_mm']; self.assertEqual(levels,sorted(set(levels))); self.assertGreaterEqual(levels[0],0)

if __name__=='__main__': unittest.main()

