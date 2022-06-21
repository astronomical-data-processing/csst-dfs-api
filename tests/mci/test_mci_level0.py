import os
import unittest
from astropy.io import fits

from csst_dfs_api.mci.level0 import Level0DataApi

class MCILevel0DataTestCase(unittest.TestCase):

    def setUp(self):
        self.api = Level0DataApi()

    def test_find(self):
        recs = self.api.find(obs_id = '000009', obs_type = 'sci', limit = 0)
        print('find:', recs)

    def test_get(self):
        rec = self.api.get(id = 100)
        print('get:', rec)

        rec = self.api.get(level0_id = '1000000102')
        print('get:', rec)        

    def test_update_proc_status(self):
        rec = self.api.update_proc_status(level0_id = '000001102', status = 6)
        print('update_proc_status:', rec)

    def test_update_qc0_status(self):
        rec = self.api.update_qc0_status(level0_id = '000001102', status = 7)
        print('update_qc0_status:', rec)

    def test_write(self):
        rec = self.api.write(
            file_path = "/opt/MSC_00001234.fits")
        print('write:', rec)  