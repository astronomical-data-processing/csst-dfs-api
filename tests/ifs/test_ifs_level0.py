import os
import unittest
from astropy.io import fits

from csst_dfs_api.ifs.level0 import Level0DataApi

class IFSLevel0DataTestCase(unittest.TestCase):

    def setUp(self):
        self.api = Level0DataApi()

    # def test_find(self):
    #     result = self.api.find(ra = 248, dec = 87, radius = 2, limit = 0, obs_type = "sky")
    #     print('find:', result)

    # def test_get(self):
    #     result = self.api.get(id = 1)
    #     print('get:', result.data)

    #     rec = self.api.get(level0_id = '300000145CCD231-c4')
    #     print('get:', rec)        

    # def test_update_proc_status(self):
    #     rec = self.api.update_proc_status(level0_id = '000001102', status = 6)
    #     print('update_proc_status:', rec)

    # def test_update_qc0_status(self):
    #     rec = self.api.update_qc0_status(level0_id = '000001102', status = 7)
    #     print('update_qc0_status:', rec)

    def test_write(self):
        rec = self.api.write(file_path = "/Users/wsl/temp/csst/ifs_data/sky_Data/CSST_IFS_B_sky_20211225001425_20211225001925_300000013_X_L0_VER_I4203.fits")
        print('write:', rec)  