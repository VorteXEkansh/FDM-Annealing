import unittest
import numpy as np
from analysis.surface_metrics import plane_warpage, fiducial_change

class SurfaceMetrics(unittest.TestCase):
    def test_rigid_transform_and_known_saddle(self):
        p=np.array([[x,y,.01*x*y] for x in [-2.,-1.,0.,1.,2.] for y in [-2.,-1.,0.,1.,2.]])
        q,_=np.linalg.qr(np.array([[1.,2.,3.],[2.,-1.,4.],[3.,1.,-2.]]))
        a=plane_warpage(p);b=plane_warpage(p@q+[80,-31,12])
        self.assertAlmostEqual(a['W_max_mm'],.04)
        self.assertAlmostEqual(a['W_RMS_mm'],.02)
        for k in ['W_max_mm','W_RMS_mm']:self.assertAlmostEqual(a[k],b[k],places=12)
    def test_vertical_plane(self):
        self.assertLess(plane_warpage([[2,x,y] for x in range(3) for y in range(3)])['W_max_mm'],1e-14)
    def test_weights(self):
        p=np.array([[x,y,.01*x*y] for x in [-2.,0.,2.] for y in [-2.,0.,2.]])
        self.assertAlmostEqual(plane_warpage(p,np.ones(9))['W_RMS_mm'],plane_warpage(p)['W_RMS_mm'])
        with self.assertRaises(ValueError):plane_warpage(p,[0]*9)
    def test_reject_invalid(self):
        for p in ([[0,0,0],[1,1,1],[2,2,2]],[[0,0,0],[1,0,0],[0,1,float('nan')]]):
            with self.assertRaises(ValueError):plane_warpage(p)
    def test_signed_gauge_rotation(self):
        r=fiducial_change([[0,0,0],[60,0,0]],[[7,3,1],[7,62.4,1]])
        self.assertAlmostEqual(r['change_mm'],-.6)
        self.assertAlmostEqual(r['strain'],-.01)

if __name__=='__main__':unittest.main()
