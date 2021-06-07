import os
import unittest
from astropy.io import fits

from csst_dfs_api.common.catalog import CatalogApi

class CommonCatalogTestCase(unittest.TestCase):

    def setUp(self):
        self.api = CatalogApi()

    def test_catalog_query(self):
        result = self.api.catalog_query(
            ra=160, 
            dec=-17, 
            radius=0.2, 
            catalog_name='gaia3', 
            min_mag=-1, 
            max_mag=-1, 
            obstime = -1, 
            limit = 2
        )
        print('return:', result)
