import os
import unittest

from csst_dfs_api.facility.level2type import Level2TypeApi

class Level2TypeTestCase(unittest.TestCase):

    def setUp(self):
        self.api = Level2TypeApi()

    def test_find(self):
        recs = self.api.find(
            module_id='MSC',
            data_type='csst-msc-l1-phot'
        )
        print('find:', recs)

    def test_get(self):
        rec = self.api.get(data_type = 'csst-msc-l1-phot')
        print('get:', rec)

    def test_update_import_status(self):
        rec = self.api.update_import_status(data_type = 'csst-msc-l1-phot', status = 4)
        print('update_import_status:', rec)

    def test_write(self):
        rec = self.api.write(
            data_type = "csst-msc-l1-phot",
            module_id = "MSC",
            key_column = "ID",
            hdu_index = 1,
            demo_filename = "CSST_MSC_MS_SCIE_20240821005429_20240821005659_10160000004_12_L1_V01_CAT.fits",
            demo_file_path = "/Users/wsl/temp/csst/msc/L2/CSST_MSC_MS_SCIE_20240821005429_20240821005659_10160000004_12_L1_V01_CAT.fits",
            ra_column = "RA",
            dec_column = "DEC")
        rec = self.api.write(
            data_type = "csst-msc-xcat",
            module_id = "MSC",
            key_column = "PhotoObjID",
            hdu_index = 1,
            demo_filename = "MSC_MS_XCAT_BRICK_156958.fits",
            demo_file_path = "/Users/wsl/temp/csst/msc/L2/MSC_MS_XCAT_BRICK_156958.fits",
            ra_column = "RA_r",
            dec_column = "DEC_r")        
        print('write:', rec)