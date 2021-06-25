
from csst_dfs_api.facility.observation import ObservationApi

api = ObservationApi()

#find 
recs = api.find(module_id="MSC",limit = 0)
print('find:', recs)

# get
rec = api.get(obs_id=17)
print('get:', rec)

# update_proc_status
rec = api.update_proc_status(obs_id = 17, status = 3,)
print('update_proc_status:', rec)

# update_qc0_status
rec = api.update_qc0_status(obs_id = 17, status = 3,)
print('update_qc0_status:', rec)        
   