import os
import importlib
import logging

from csst_dfs_commons.models.errors import *
from .constants import *

log = logging.getLogger('csst')

API_MODULE_PREFIX = "csst_dfs_api_"

class Delegate(object):
    def __init__(self):
        self.mode = os.getenv("CSST_DFS_API_MODE", 'cluster')
        self.check_env()

    def check_env(self):
        if self.mode == MODE_LOCAL:
            self.local_path = os.getenv("CSST_LOCAL_FILE_ROOT")
            if not self.local_path:
                log.warn("enviroment variable CSST_DFS_API_MODE is not set, use default: /opt/temp/csst")
                self.local_path = "/opt/temp/csst"
            try:
                from csst_dfs_api_local._version import version  as local_version
            except ImportError:
                raise CSSTFatalException("please install csst_dfs_api_local firstly.")

        if self.mode == MODE_CLUSTER:
            self.gateway = os.getenv("CSST_DFS_GATEWAY")
            if not self.gateway:
                raise CSSTGenericException("enviroment variable CSST_DFS_GATEWAY is not set")
            try:
                from csst_dfs_api_cluster._version import version as cluster_version
            except ImportError:
                raise CSSTFatalException("please install csst_dfs_api_cluster firstly.")

            if not os.getenv("CSST_DFS_APP_ID"):
                raise CSSTGenericException("enviroment variable CSST_DFS_APP_ID is not set")

            if not os.getenv("CSST_DFS_APP_TOKEN"):
                raise CSSTGenericException("enviroment variable CSST_DFS_APP_TOKEN is not set")
    
    def load(self, sub_module):
        return importlib.import_module(f"{API_MODULE_PREFIX}{self.mode}.{sub_module}")
