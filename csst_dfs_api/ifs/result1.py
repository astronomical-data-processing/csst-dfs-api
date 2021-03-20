
from ..common.delegate import Delegate

class Result1Api(object):
    """
    Level 1 Operation Class of IFS
    """
    def __init__(self, sub_system="ifs"):
        self.sub_system = sub_system
        self.module = Delegate().load(sub_module = "ifs")
        self.stub = getattr(self.module, "Result1Api")()
        self.file_prefix = self.stub.root_dir

    def find(self, **kwargs):
        '''
        parameter kwargs:
            file_name = [str],
            proc_type = [str]

        return list of level 1 record
        '''
        return self.stub.find(**kwargs)

    def get(self, **kwargs):
        '''  query database, return a record as dict

        parameter kwargs:
            fits_id = [int] 

        return dict or None
        '''
        return self.stub.get(**kwargs)

    def read(self, **kwargs):
        ''' yield bytes of fits file

        parameter kwargs:
            fits_id = [int],
            file_path = [str], 
            chunk_size = [int] default 20480

        yield bytes of fits file
        '''
        return self.stub.read(**kwargs)

    def write(self, **kwargs):
        ''' copy a local level 1 file to file storage, and insert a record into database

        parameter kwargs:
            file_path = [str],
            proc_type = [str],
            result0_ids = [list]
        '''  
        yield self.stub.write(**kwargs)

