import unittest

from csst_dfs_api import functional as F

class CommonUtilsTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_find_observation(self):
        result = F.find_observation(module_id='MSC')
        print(result)
        assert result.success, result.message

    def test_find_level0(self):
        result = F.find_level0()
        print(result)
        assert result.success, result.message