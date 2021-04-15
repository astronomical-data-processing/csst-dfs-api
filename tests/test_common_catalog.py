import os
import unittest
from astropy.io import fits

from csst_dfs_api.common.catalog import CatalogApi

class CommonCatalogTestCase(unittest.TestCase):

    def setUp(self):
        self.api = CatalogApi()

    def test_gaia3_query(self):
        result = self.api.gaia3_query(ra=160, dec=-17, radius=0.2, min_mag=-1, max_mag=-1, obstime = -1, limit = 2)
        print('return:', result)
