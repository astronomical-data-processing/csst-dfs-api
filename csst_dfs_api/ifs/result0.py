
from ..common.delegate import Delegate

class Result0Api(object):
    """
    Level 0 Operation Class of IFS
    """
    def __init__(self, sub_system="ifs"):
        self.sub_system = sub_system
        self.module = Delegate().load(sub_module = "ifs")
        self.stub = getattr(self.module, "Result0Api")()
        self.file_prefix = self.stub.root_dir

    def find(self, **kwargs):
        '''
        parameter kwargs:
            raw_id = [int],
            file_name = [str],
            proc_type = [str]

        return list of level 0 record
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
        ''' copy a local level 0 file to file storage, and insert a record into database

        parameter kwargs:
            raw_id = [int],
            file_path = [str],
            proc_type = [str]
        '''  
        return self.stub.write(**kwargs)

