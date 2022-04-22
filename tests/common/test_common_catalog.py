import os
import unittest
from astropy.io import fits
import time

from csst_dfs_api.common.catalog import CatalogApi

class CommonCatalogTestCase(unittest.TestCase):

    def setUp(self):
        self.api = CatalogApi()

    def test_catalog_query(self):
        t= time.time()
        result = self.api.catalog_query(
            ra=128, # 15415
            dec=-40, 
            radius=0.5, 
            catalog_name='gaia3', 
            min_mag=-1, 
            max_mag=-1, 
            obstime = -1, 
            limit = 2
        )
        print('used:', time.time()-t)
        print('return:', result)
