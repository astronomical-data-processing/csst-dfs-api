import unittest

from csst_dfs_api.hstdm import Level2DataApi

class HSTDMLevel2TestCase(unittest.TestCase):

    def setUp(self):
        self.api = Level2DataApi()

    def test_find(self):
        recs = self.api.find(
                level1_id=1, 
                create_time = ("2021-06-01 11:12:13","2021-06-08 11:12:13")
            )
        print('find:', recs)

    def test_get(self):
        rec = self.api.get(id = 1)
        print('get:', rec)

    def test_update_proc_status(self):
        rec = self.api.update_proc_status(id = 1, status = 4)
        print('update_proc_status:', rec)

    def test_update_qc2_status(self):
        rec = self.api.update_qc2_status(id = 1, status = 7)
        print('update_qc1_status:', rec)

    def test_write(self):
        rec = self.api.write(
            level1_id=2, 
            project_id=2, 
            file_type = "SPC",
            prc_status = 3,
            prc_time = '2021-10-22 11:12:13',
            filename = "MSC_MS_210525120000_100000000_20_cat.fits",
            file_path = "/opt/temp/csst/msc_data/MSC_MS_210525120000_100000000_20_cat.fits",
            pipeline_id = "P2")
        print('write:', rec)