import os
import unittest
from astropy.io import fits

from csst_dfs_api.facility.level1 import Level1DataApi

class SLSLevel1DataTestCase(unittest.TestCase):

    def setUp(self):
        self.api = Level1DataApi()

    def test_find_by_qc1_status(self):
        recs = self.api.sls_find_by_qc1_status(qc1_status=-1)
        print('find_by_qc1_status:', recs)

    def test_find(self):
        recs = self.api.find(
            ra_cen = 1,
            dec_cen =2,
            radius_cen = 1
        )
        print('find:', recs)        
