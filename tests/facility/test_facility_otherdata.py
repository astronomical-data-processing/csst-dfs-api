import unittest

from csst_dfs_api.facility.otherdata import OtherDataApi

class OtherDataTestCase(unittest.TestCase):

    def setUp(self):
        self.api = OtherDataApi()

    def test_find(self):
        recs = self.api.find(
            module_id='MSC',
            create_time = ("2023-06-27 11:12:13","2023-06-27 23:12:13"))
        print('find:', recs)

    def test_get(self):
        rec = self.api.get(id = 1)
        print('get:', rec)

    def test_write(self):
        rec = self.api.write(
            obs_id='10000012001', 
            file_type = "sci",
            module_id = "MSC",
            detector_no = "01",
            filename = "CSST_MSC_MS_SCI_20270810142128_20270810142358_100000101_20_img_L1.fits",
            file_path = "/opt/temp/csst/CSST_MSC_MS_SCI_20270810142128_20270810142358_100000101_20_img_L1.fits",
            pipeline_id = "P1")
        print('write:', rec)