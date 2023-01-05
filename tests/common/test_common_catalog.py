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
            ra=90, 
            dec=24.5, 
            radius=1, 
            columns = ('ref_epoch','ra','ra_error','dec','dec_error','parallax','parallax_error','pmra','pmra_error','pmdec','pmdec_error','phot_g_mean_mag','source_id'),            
            catalog_name='gaia3', 
            min_mag=-1, 
            max_mag=-1, 
            obstime = -1, 
            limit = 0
        )
        # print(result)
        dt = self.api.to_table(result)
        dt.pprint()
        # df = dt.to_pandas()
        # print(df.head())
        print('used:', time.time()-t)
        print('return:', len(result.data))
