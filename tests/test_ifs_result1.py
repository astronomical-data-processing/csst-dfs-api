import os
import unittest
from astropy.io import fits

from csst_dfs_api.ifs import Result1Api

class IFSResult1TestCase(unittest.TestCase):

    def setUp(self):
        self.api = Result1Api()

    def test_find(self):
        recs = self.api.find(file_name='CCD2_ObsTime_1200_ObsNum_40.fits')
        print('find:', recs)

        recs = self.api.find()
        print('find:', recs)

    def test_read(self):
        recs = self.api.find(file_name='CCD2_ObsTime_1200_ObsNum_40.fits')
        print("The full path: ", os.path.join(self.api.file_prefix, recs[0]['file_path']))

        rec, result0s = self.api.get(fits_id=recs[0]['id'])
        print(result0s)
        file_segments = self.api.read(file_path=rec['file_path'])
        file_bytes = b''.join(file_segments)
        hdul = fits.HDUList.fromstring(file_bytes)
        print(hdul.info())
        hdr = hdul[0].header
        print(repr(hdr))

    def test_write(self):
        self.api.write(result0_ids = [1,2,3,4], 
                file_path='/opt/temp/csst_ifs/CCD2_ObsTime_1200_ObsNum_40.fits',
                proc_type = 'default')

        recs = self.api.find(raw_id=1)
        print()
        print(recs)
        print("="*80)
        recs = self.api.find(file_name='CCD2_ObsTime_1200_ObsNum_40.fits')
        print(recs)
