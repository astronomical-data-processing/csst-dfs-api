import os
import unittest
from astropy.io import fits

from csst_dfs_api.ifs.level1 import Level1DataApi

class IFSLevel1DataTestCase(unittest.TestCase):

    def setUp(self):
        self.api = Level1DataApi()

    def test_find(self):
        recs = self.api.find(raw_id=1,
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
        rec = self.api.write(raw_id=12, 
            data_type = "sci",
            cor_sci_id = 2,
            prc_params = "/opt/dddasd.params",
            flat_id = 1,
            dark_id = 2,
            bias_id = 3,
            lamp_id = 4,
            arc_id = 5,
            sky_id = 6,            
            prc_status = 3,
            prc_time = '2021-06-05 11:12:13',
            filename = "dddasd",
            file_path = "/opt/dddasd.fits",
            pipeline_id = "P2")
        print('write:', rec)