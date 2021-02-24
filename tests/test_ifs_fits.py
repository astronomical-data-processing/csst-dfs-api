import unittest

from csst_dfs_api.ifs import FitsApi

class IFSFitsTestCase(unittest.TestCase):

    def setUp(self):
        self.api = FitsApi()

    def test_find(self):
        files = self.api.find()
        print("find ", len(files))
    