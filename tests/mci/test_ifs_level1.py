import os
import unittest
from astropy.io import fits

from csst_dfs_api.mci.level1 import Level1DataApi

class MCILevel1DataTestCase(unittest.TestCase):

    def setUp(self):
        self.api = Level1DataApi()

    def test_find(self):
        recs = self.api.find(
            level0_id='000001201',
            create_time = ("2021-10-01 11:12:13","2021-11-08 11:12:13"))
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
            cor_sci_id = 2,
            prc_params = "/opt/dddasd.params",
            prc_status = 3,
            prc_time = '2021-06-05 11:12:13',
            filename = "MSC_MS_210525121500_100000001_09_raw",
            file_path = "/opt/temp/csst/MSC_MS_210525121500_100000001_09_raw.fits",
            pipeline_id = "P2",
            refs = {'dark': 1, 'bias': 2, 'flat': 3, 'sky': 33 })
        print('write:', rec)