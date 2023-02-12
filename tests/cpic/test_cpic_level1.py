import unittest

from csst_dfs_api.cpic import Level1DataApi

class CPICLevel1TestCase(unittest.TestCase):

    def setUp(self):
        self.api = Level1DataApi()

    def test_find(self):
        recs = self.api.find(
                level0_id='400001223', 
                create_time = ("2021-06-01 11:12:13","2021-06-08 11:12:13")
            )
        print('find:', recs)

    def test_get(self):
        rec = self.api.get(id = 1)
        print('get:', rec)

    def test_update_proc_status(self):
        rec = self.api.update_proc_status(id = 1, status = 4)
        print('update_proc_status:', rec)

    def test_update_qc1_status(self):
        rec = self.api.update_qc1_status(id = 1, status = 7)
        print('update_qc1_status:', rec)

    def test_write(self):
        rec = self.api.write(
            level0_id='400001223', 
            data_type = "sci",
            prc_params = "/opt/dddasd.params",
            prc_status = 3,
            prc_time = '2021-10-22 11:12:13',
            filename = "CSST_MSC_MS_SCI_20270810142128_20270810142358_100000101_20_img_L1.fits",
            file_path = "/opt/temp/csst/CSST_MSC_MS_SCI_20270810142128_20270810142358_100000101_20_img_L1.fits",
            pipeline_id = "P2",
            refs = {'dark': 1, 'bias': 2, 'flat': 3 })
        print('write:', rec)