import os
import unittest
from astropy.io import fits

from csst_dfs_api.mbi.level2co import Level2CoApi

class MSCLevel2CoDataTestCase(unittest.TestCase):

    def setUp(self):
        self.api = Level2CoApi()

    def test_find(self):
        recs = self.api.find(
            level1_id=1,
            create_time = ("2022-06-15 11:12:13","2022-06-16 11:12:13"))
        print('find:', recs)

    def test_catalog_query(self):
        result = self.api.catalog_query(
            obs_id='100000000',
            obs_time = ("2021-05-24 11:12:13","2021-05-25 13:12:13"),
            limit = 2)
        if result.success:
            dt = self.api.to_table(result)
            dt.pprint()
        else:
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
