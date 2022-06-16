import os
import unittest
from astropy.io import fits

from csst_dfs_api.msc.level2 import Level2DataApi

class MSCLevel2DataTestCase(unittest.TestCase):

    def setUp(self):
        self.api = Level2DataApi()

    def test_find(self):
        recs = self.api.find(
            level0_id='000001201',
            create_time = ("2021-06-01 11:12:13","2021-06-08 11:12:13"))
        print('find:', recs)

    def test_catalog_query(self):
        result = self.api.catalog_query(
            obs_id='100000000',
            obs_time = ("2021-05-24 11:12:13","2021-05-25 13:12:13"),
            limit = 2)
        dt = self.api.to_table(result)
        print()
        dt.pprint()

    def test_get(self):
        rec = self.api.get(id = 2)
        print('get:', rec)

    def test_update_proc_status(self):
        rec = self.api.update_proc_status(id = 2, status = 4)
        print('update_proc_status:', rec)

    def test_update_qc2_status(self):
        rec = self.api.update_qc2_status(id = 2, status = 7)
        print('update_qc1_status:', rec)

    def test_write(self):
        rec = self.api.write(
            level1_id= 1, 
            data_type = "sci",
            prc_status = 3,
            prc_time = '2021-10-22 11:12:13',
            filename = "MSC_MS_210525120000_100000000_20_cat.fits",
            file_path = "/opt/temp/csst/msc_data/MSC_MS_210525120000_100000000_20_cat.fits"
            )
        print('write:', rec)
