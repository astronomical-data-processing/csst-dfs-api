import os
import unittest
from astropy.io import fits
from csst_dfs_api.common.utils import to_table as to_fits_table
from csst_dfs_api.facility.level2 import Level2DataApi

class Level2DataTestCase(unittest.TestCase):

    def setUp(self):
        self.api = Level2DataApi()

    def test_find(self):
        recs = self.api.find(
            level1_id=1)
        print('find:', recs)

    def test_find_existed_brick_ids(self):
        recs = self.api.find_existed_brick_ids(data_type = "csst-msc-l1-phot")
        print('find_existed_brick_ids:', recs)        

    def test_catalog_query(self):
        result = self.api.catalog_query(
            sql = 'select x,y,A,B,PA,AB,E from csst_msc_l1_phot',
            limit = 2)
        print(result)
        if result.success and result['totalCount'] > 0:
            dt = to_fits_table(result)
            dt.pprint()

    # def test_get(self):
    #     rec = self.api.get(id = 1)
    #     print('get:', rec)

    # def test_update_proc_status(self):
    #     rec = self.api.update_proc_status(id = 1, status = 4)
    #     print('update_proc_status:', rec)

    # def test_update_qc2_status(self):
    #     rec = self.api.update_qc2_status(id = 1, status = 7)
    #     print('update_qc2_status:', rec)

    # def test_write(self):
    #     rec = self.api.write(
    #         level1_id= 1, 
    #         module_id = 'MSC',
    #         data_type = "csst-msc-l1-phot",
    #         prc_status = 3,
    #         prc_time = '2021-10-22 11:12:13',
    #         filename = "CSST_MSC_MS_SCIE_20240821005429_20240821005659_10160000004_12_L1_V01_CAT.fits",
    #         file_path = "/opt/temp/csst/msc/L2/CSST_MSC_MS_SCIE_20240821005429_20240821005659_10160000004_12_L1_V01_CAT.fits",
    #         pipeline_id = "P1"
    #         )
    #     print('write:', rec)
        # rec = self.api.write(
        #     level1_id= 1, 
        #     module_id = 'MSC',
        #     data_type = "csst-msc-xcat",
        #     prc_status = 3,
        #     prc_time = '2021-10-22 11:12:13',
        #     filename = "MSC_MS_XCAT_BRICK_156958.fits",
        #     file_path = "/opt/temp/csst/fits_file/L2/L2_DEMO/MSC_MS_XCAT_BRICK_156958.fits",
        #     pipeline_id = "P1"
        #     )
        # print('write:', rec)        