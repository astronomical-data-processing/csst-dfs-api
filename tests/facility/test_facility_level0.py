import unittest

from csst_dfs_api.facility.level0 import Level0DataApi

class Level0DataTestCase(unittest.TestCase):

    def setUp(self):
        self.api = Level0DataApi()

    def test_find(self):
        recs = self.api.find(obs_id = '0000011', obs_type = 'sci', limit = 0)
        print('find:', recs)

    def test_find_by_brick_ids(self):
        recs = self.api.find_by_brick_ids(brick_ids = [1,2,3,4])
        print('find:', recs)

    def test_get(self):
        rec = self.api.get(id = 3)
        print('get:', rec)

        rec = self.api.get(level0_id = '000001101',obs_type='sci')
        print('get:', rec)        

    def test_update_proc_status(self):
        rec = self.api.update_proc_status(level0_id = '000001101', status = 6)
        print('update_proc_status:', rec)

    def test_update_qc0_status(self):
        rec = self.api.update_qc0_status(level0_id = '000001101', status = 7)
        print('update_qc0_status:', rec)

    def test_write(self):
        rec = self.api.write(
            level0_id = '000001101',
            obs_id = '0000011',
            detector_no = "01",
            obs_type = "sci",            
            obs_time = "2021-06-06 11:12:13",
            exp_time = 150,
            detector_status_id = 3,
            filename = "MSC_00001234",
            file_path = "/opt/MSC_00001234.fits")
        print('write:', rec)  