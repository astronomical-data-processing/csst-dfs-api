import unittest

from csst_dfs_api.mbi import Level2CoApi

class MBILevel2CoDataTestCase(unittest.TestCase):

    def setUp(self):
        self.api = Level2CoApi()

    def test_find(self):
        recs = self.api.find(
            data_type='CAT',
            create_time = ("2022-06-15 11:12:13", "2024-06-16 11:12:13"))
        print('find:', recs)

    def test_get(self):
        rec = self.api.get(id = 4)
        print('get:', rec)

    def test_update_proc_status(self):
        rec = self.api.update_proc_status(id = 4, status = 9)
        print('update_proc_status:', rec)

    def test_update_qc2_status(self):
        rec = self.api.update_qc2_status(id = 4, status = 9)
        print('update_qc2_status:', rec)

    def test_write(self):
        rec = self.api.write(
            data_type = "CAT",
            prc_status = 3,
            prc_time = '2023-07-01 11:12:13',
            filename = "MSC_MS_210525120000_100000000_20_cat.fits",
            file_path = "/opt/temp/csst/msc_data/MSC_MS_210525120000_100000000_20_cat.fits",
            pipeline_id = "COMBI-2"
        )
        print('write:', rec)
