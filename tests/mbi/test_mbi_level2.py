import os
import unittest
from astropy.io import fits
from csst_dfs_api.common.utils import to_table as to_fits_table
from csst_dfs_api.mbi.level2 import Level2DataApi

class MBILevel2DataTestCase(unittest.TestCase):

    def setUp(self):
        self.api = Level2DataApi()

    def test_find(self):
        recs = self.api.find(
            level1_id=1,
            create_time = ("2022-06-15 11:12:13","2022-06-16 11:12:13"))
        print('find:', recs)

    def test_catalog_query(self):
        result = self.api.catalog_query(
            obs_id = '100000133',
            detector_no = '13',
            ra = 192,
            dec = 26,
            radius = 1,
            limit = 2)
        print(result)
        if result.success and result['totalCount'] > 0:
            dt = to_fits_table(result)
            dt.pprint()

    def test_catalog_query_file(self):
        result = self.api.catalog_query_file(
            ra = 192,
            dec = 26,
            radius = 1)
        print(result)

    def test_get(self):
        rec = self.api.get(id = 1)
        print('get:', rec)

    def test_update_proc_status(self):
        rec = self.api.update_proc_status(id = 1, status = 4)
        print('update_proc_status:', rec)

    def test_update_qc2_status(self):
        rec = self.api.update_qc2_status(id = 1, status = 7)
        print('update_qc2_status:', rec)

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
