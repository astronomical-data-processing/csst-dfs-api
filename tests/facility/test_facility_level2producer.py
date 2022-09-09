import unittest

from csst_dfs_api.facility.level2producer import Level2ProducerApi

class FacilityLevel2ProducerTestCase(unittest.TestCase):

    def setUp(self):
        self.api = Level2ProducerApi()

    def test_register(self):
        rec = self.api.register(name='Test2', 
            gitlink='http://github.com/xxx/xxx',
            paramfiles='/opt/csst/param1.ini',
            image='centos:7',
            priority = 3,
            pre_producers=[1,2] )
        print('register:', rec)

    def test_find(self):
        recs = self.api.find(key="Te")
        print('find:', recs)

    def test_get(self):
        rec = self.api.get(id=10)
        print('get:', rec)

    def test_find_nexts(self):
        recs = self.api.find_nexts(id=1)
        print('find_nexts:', recs)

    def test_find_start(self):
        recs = self.api.find_start(key="Te")
        print('find_start:', recs)

    def test_update(self):
        recs = self.api.update(
            id=2,
            name = "start2",
            gitlink = "http://github.com/xxx/xxx",
            image = "centos:8",
            paramfiles='/opt/csst/param1.ini',
            priority = 3,
            pre_producers=[1,3]
        )
        print('test_update:', recs)

    def test_delete(self):
        recs = self.api.delete(
            id=11
        )
        print('test_delete:', recs)

    def test_new_job(self):
        recs = self.api.new_job(
            name = "start2-1-1-",
            dag = "{'start':'1'}"
        )
        print('new_job:', recs)

    def test_get_job(self):
        recs = self.api.get_job(
            id = 2
        )
        print('get_job:', recs)     

    def test_update_job(self):
        recs = self.api.update_job(
            id = 2,
            dag = "222",
            status = 2
        )
        print('update_job:', recs) 

    def test_new_running(self):
        recs = self.api.new_running(
            job_id = 2,
            producer_id = 2,
            brick_id = 2,
            start_time = '2022-04-22 13:13:13'
        )
        print('new_running:', recs)

    def test_get_running(self):
        recs = self.api.get_running(
            id = 2
        )
        print('get_running:', recs)

    def test_update_running(self):
        recs = self.api.update_running(
            id = 3,
            job_id = 2,
            producer_id = 2,
            brick_id = 2,
            start_time = '2022-04-22 13:13:13',
            end_time = '2022-04-22 15:13:13',
            prc_status = 1,
            prc_result = 'OK'
        )
        print('update_running:', recs)

    def test_find_running(self):
        recs = self.api.find_running(
            job_id = 2,
            producer_id = 2,
            brick_id = 2,
            create_time = ('2022-04-22 10:13:13','2022-04-22 23:13:13')
        )
        print('find_running:', recs)

    def test_make_graph(self):
        graph_id_edges = self.api.make_graph(
            start_producer_id = 2,
            fig_path = 'graph11.png'
        )
        print('graph_id_edges:', graph_id_edges)