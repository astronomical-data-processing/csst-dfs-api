import os
import unittest

from csst_dfs_api.facility.brick import BrickApi

class FacilityBrickTestCase(unittest.TestCase):

    def setUp(self):
        self.api = BrickApi()

    def test_find(self):
        recs = self.api.find(limit = 0)
        print('find:', recs)

    def test_get(self):
        rec = self.api.get(id=1)
        print('get:', rec)

    def test_write(self):
        rec = self.api.write(id=1, ra = 3.2, dec = 3.3, boundingbox = '12,12')
        print('test_write:', rec)

    def test_find_obs_status(self):
        rec = self.api.find_obs_status(brick_id=1, band = 'r')
        print('find_obs_status:', rec)

    def test_find_level1_data(self):
        rec = self.api.find_level1_data(brick_id=1, level1_id = 1, module = 'msc')
        print('find_level1_data:', rec) 
