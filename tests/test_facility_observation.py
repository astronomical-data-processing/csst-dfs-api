import os
import unittest
from astropy.io import fits

from csst_dfs_api.facility.observation import ObservationApi

class FacilityObservationTestCase(unittest.TestCase):

    def setUp(self):
        self.api = ObservationApi()

    def test_find(self):
        recs = self.api.find(module_id="MSC",limit = 0)
        print('find:', recs)

    def test_get(self):
        rec = self.api.get(id=17)
        print('get:', rec)
        rec = self.api.get(obs_id='0000017')
        print('get:', rec)        

    def test_update_proc_status(self):
        rec = self.api.update_proc_status(obs_id='0000017', status = 3, )
        print('update_proc_status:', rec)

    def test_update_qc0_status(self):
        rec = self.api.update_qc0_status(obs_id='0000017', status = 3, )
        print('update_qc0_status:', rec)        
