
from ..common.delegate import Delegate
from astropy.table import Table

class Level2DataApi(object):
    """
    Level2 Data Operation Class
    """
    def __init__(self):
        self.pymodule = Delegate().load(sub_module = "msc")
        self.stub = getattr(self.pymodule, "Level2DataApi")()
        
    def find(self, **kwargs):
        ''' retrieve level2 records from database

        :param kwargs: Parameter dictionary, key items support:
            level1_id: [int]
            data_type: [str]
            create_time : (start, end),
            qc2_status : [int],
            prc_status : [int],
            filename: [str]
            limit: limits returns the number of records,default 0:no-limit
        
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.find(**kwargs)

    def catalog_query(self, **kwargs):
        ''' retrieve level2 catalog

        :param kwargs: Parameter dictionary, key items support:
            obs_id: [str]
            detector_no: [str]
            min_mag: [float]
            max_mag: [float]
            obs_time: (start, end),
            limit: limits returns the number of records,default 0:no-limit
        
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.catalog_query(**kwargs)        

    def _fields_dtypes(self, rec):
        fields = tuple(rec.__dataclass_fields__.keys())
        dtypes = []
        for _, f in rec.__dataclass_fields__.items():
            if f.type == int:
                dtypes.append('i8')
            elif f.type == float:
                dtypes.append('f8')        
            elif f.type == str:
                dtypes.append('S2')
            elif f.type == list:
                dtypes.append('(12,)f8')       
            else:
                dtypes.append('S2')                
        dtypes = tuple(dtypes)
        return fields, dtypes

    def to_table(self, query_result):
        if not query_result.success or not query_result.data:
            return Table()
        fields, dtypes = self._fields_dtypes(query_result.data[0])
        t = Table(names = fields, dtype = dtypes)
        t.meta['comments'] = [str(query_result.data[0].__class__)]
        t.meta['total'] = query_result['totalCount']

        for rec in query_result.data:
            t.add_row(tuple([rec.__getattribute__(k) for k in fields]))
        return t

    def get(self, **kwargs):
        '''  fetch a record from database

        :param kwargs: Parameter dictionary, key items support:
            id : [int] 
        
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.get(**kwargs)


    def update_proc_status(self, **kwargs):
        ''' update the status of reduction

        :param kwargs: Parameter dictionary, key items support:
            id = [int],
            status = [int]
        
        :returns: csst_dfs_common.models.Result
        '''
        return self.stub.update_proc_status(**kwargs)

    def update_qc2_status(self, **kwargs):
        ''' update the status of QC0
        
        :param kwargs: Parameter dictionary, key items support:
            id = [int],
            status = [int]
        
        :returns: csst_dfs_common.models.Result
        '''        
        return self.stub.update_qc2_status(**kwargs)    

    def write(self, **kwargs):
        ''' insert a level2 record into database
 
        :param kwargs: Parameter dictionary, key items support:
            level1_id: [int]
            data_type : [str]
            filename : [str]
            file_path : [str]            
            prc_status : [int]
            prc_time : [str]
        
        :returns: csst_dfs_common.models.Result
        '''          
        return self.stub.write(**kwargs)

