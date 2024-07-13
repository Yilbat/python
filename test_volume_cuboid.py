# from volume_cuboid import *
import unittest

def cuboid_volume(l):
    return (l*l*l)
class TestCuboid(unittest.TestCase):
    def test_volume(self):
        self.assertAlmostEqual(cuboid_volume(2),8)
        self.assertAlmostEqual(cuboid_volume(1),1)
        self.assertAlmostEqual(cuboid_volume(0),4)

print("hello")