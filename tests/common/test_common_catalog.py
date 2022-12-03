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
            ra=193.299, 
            dec=19.08851, 
            radius=2, 
            catalog_name='gaia3', 
            min_mag=-1, 
            max_mag=-1, 
            obstime = -1, 
            limit = 0
        )
        print(result)
        # dt = self.api.to_table(result)
        # df = dt.to_pandas()
        # print(df.head())
        print('used:', time.time()-t)
        # print('return:', result['totalCount'\])
