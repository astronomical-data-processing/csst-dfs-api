import os
import unittest
from astropy.io import fits

from csst_dfs_api.msc.level1 import Level1DataApi

class MSCLevel1DataTestCase(unittest.TestCase):

    def setUp(self):
        self.api = Level1DataApi()

    def test_find(self):
        recs = self.api.find(
            level0_id='000001201',
            create_time = ("2021-06-01 11:12:13","2021-06-08 11:12:13"))
        print('find:', recs)

    def test_get(self):
        rec = self.api.get(id = 2)
        print('get:', rec)

    def test_update_proc_status(self):
        rec = self.api.update_proc_status(id = 2, status = 4)
        print('update_proc_status:', rec)

    def test_update_qc1_status(self):
        rec = self.api.update_qc1_status(id = 2, status = 7)
        print('update_qc1_status:', rec)

    def test_write(self):
        rec = self.api.write(
            level0_id='000001201', 
            data_type = "sci",
            cor_sci_id = 1,
            prc_params = "/opt/dddasd.params",
            prc_status = 3,
            prc_time = '2021-10-22 11:12:13',
            filename = "MSC_MS_210525121500_100000001_09_raw",
            file_path = "/opt/temp/csst/msc/level1/MSC_210304093000_0000000_06_img.fits.fz",
            pipeline_id = "P1",
            refs = {'dark': 1, 'bias': 2, 'flat': 3 })
        print('write:', rec)