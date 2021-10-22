from csst_dfs_api.facility.level1prc import Level1PrcApi

api = Level1PrcApi()

#find
recs = api.find(level1_id=3)
print('find:', recs)

#update_proc_status
rec = api.update_proc_status(id = 2, status = 4)
print('update_proc_status:', rec)

#write
rec = api.write(
    level1_id=3, 
    pipeline_id = "P1",
    prc_module = "QC0",
    params_file_path = "/opt/dddasd.params",
    prc_status = 3,
    prc_time = '2021-06-04 11:12:13',
    result_file_path = "/opt/dddasd.header")
print('write:', rec)