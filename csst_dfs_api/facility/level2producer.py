
from ..common.delegate import Delegate

class Level2ProducerApi(object):
    """
    Level 0 Data Operation API
    """
    def __init__(self):
        self.pymodule = Delegate().load(sub_module = "facility")
        self.stub = getattr(self.pymodule, "Level2ProducerApi")()

    def register(self, **kwargs):
        ''' register a Level2Producer data record into database
 
        :param kwargs: Parameter dictionary, key items support:
            name = [str]\n
            gitlink = [str]\n
            paramfiles = [str]\n
            priority = [int]\n
            pre_producers = list[int]
        
        :returns: csst_dfs_common.models.Result
        '''  
        return self.stub.register(**kwargs)

    def find(self, **kwargs):
        ''' retrieve Level2Producer records from database

        :param kwargs: Parameter dictionary, key items support:
            key: [str]
            limit: limits returns the number of records,default 0:no-limit
        
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.find(**kwargs)

    def get(self, **kwargs):
        '''  fetch a record from database

        :param kwargs: Parameter dictionary, key items support:
            id : [int]
        
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.get(**kwargs)

    def find_nexts(self, **kwargs):
        ''' retrieve Level2Producer records from database

        :param kwargs: Parameter dictionary, key items support:
            id : [int]
        
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.find_nexts(**kwargs)

    def find_start(self, **kwargs):
        ''' retrieve Level2Producer records from database

        :param kwargs: Parameter dictionary, key items support:
            key : [str]
        
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.find_start(**kwargs)

    def update(self, **kwargs):
        ''' update a Level2Producer
        
        :param kwargs: Parameter dictionary, key items support:
            id : [int]\n
            name = [str]\n
            gitlink = [str]\n
            paramfiles = [str]\n
            priority = [int]\n
            pre_producers = list[int]
        
        :returns: csst_dfs_common.models.Result            
        '''        
        return self.stub.update(**kwargs)    

    def delete(self, **kwargs):
        ''' delete a Level2Producer data
 
        :param kwargs: Parameter dictionary, key items support:
            id = [int]
        
        :returns: csst_dfs_common.models.Result
        '''  
        return self.stub.delete(**kwargs)

    def new_job(self, **kwargs):
        ''' new a Level2Producer Job
 
        :param kwargs: Parameter dictionary, key items support:
            dag = [str]
        
        :returns: csst_dfs_common.models.Result
        '''  
        return self.stub.new_job(**kwargs)

    def get_job(self, **kwargs):
        '''  fetch a record from database

        :param kwargs: Parameter dictionary, key items support:
            id : [int]
        
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.get_job(**kwargs)

    def update_job(self, **kwargs):
        ''' update a Level2Producer Job
 
        :param kwargs: Parameter dictionary, key items support:
            id = [int]
            dag = [str]
            status = [int]
        
        :returns: csst_dfs_common.models.Result
        '''  
        return self.stub.update_job(**kwargs)

    def new_running(self, **kwargs):
        ''' insert a Level2ProducerRuningRecord data
 
        :param kwargs: Parameter dictionary, key items support:
            job_id = [int]\n
            producer_id = [int]\n
            brick_id = [int]\n
            start_time = [str]\n
            end_time = [str]\n
            prc_status = [int]\n
            prc_result = [str]
        
        :returns: csst_dfs_common.models.Result
        '''  
        return self.stub.new_running(**kwargs)   

    def get_running(self, **kwargs):
        '''  fetch a record from database

        :param kwargs: Parameter dictionary, key items support:
            id : [int]
        
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.get_running(**kwargs)

    def update_running(self, **kwargs):
        ''' udpate a Level2ProducerRuningRecord data
 
        :param kwargs: Parameter dictionary, key items support:
            id = [int]\n
            job_id = [int]\n
            producer_id = [int]\n
            brick_id = [int]\n
            start_time = [str]\n
            end_time = [str]\n
            prc_status = [int]\n
            prc_result = [str]
        
        :returns: csst_dfs_common.models.Result
        '''  
        return self.stub.update_running(**kwargs)

    def find_running(self, **kwargs):
        ''' find Level2ProducerRuningRecord data
 
        :param kwargs: Parameter dictionary, key items support:
            job_id = [int]\n
            producer_id = [int]\n
            brick_id = [int]\n
            prc_status = [int]\n
            create_time : (start, end)\n
            limit = [int]
        
        :returns: csst_dfs_common.models.Result
        '''  
        return self.stub.find_running(**kwargs)
