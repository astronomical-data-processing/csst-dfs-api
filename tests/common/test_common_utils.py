import unittest
import time

from csst_dfs_api.common.utils import get_nextId_by_prefix

class CommonUtilsTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_nextId_by_prefix(self):
        t= time.time()
        result = get_nextId_by_prefix("MBI")
        print(result)
        assert type(result.data) == int
