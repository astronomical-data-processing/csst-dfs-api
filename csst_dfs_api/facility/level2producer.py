import random
from ..common.delegate import Delegate
from csst_dfs_commons.models.errors import CSSTGenericException

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
            name = [str]
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
            name = [str]
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

    def make_graph(self, start_producer_id, fig_path = None):
        start_node = self.get(id = start_producer_id)
        if not start_node.success:
            raise CSSTGenericException("start node not found")

        def get_next(pre_node, node_level_x, node_level_y):
            the_nodes = self.find_nexts(id = pre_node.id)
            graph_name_edges = [(pre_node.name, n.name) for n in the_nodes.data]
            graph_id_edges = [(pre_node.id, n.id) for n in the_nodes.data]
            pos = {pre_node.name: (node_level_x,node_level_y)}
            for idx, node in enumerate(the_nodes.data):
                sub_id_edges, sub_name_edges, sub_pos = get_next(node, node_level_x+1, random.randint(-3,3))

                graph_id_edges.extend(sub_id_edges)
                graph_name_edges.extend(sub_name_edges)
                pos.update(sub_pos)
            return graph_id_edges, graph_name_edges, pos

        graph_id_edges, graph_name_edges, pos = get_next(start_node.data, 0, 0)
        if fig_path:
            import networkx as nx
            from matplotlib import pyplot as plt
            g1 = nx.DiGraph()
            vertex_list = list(set([str(i) for e in graph_name_edges for i in e]))
            g1.add_nodes_from(vertex_list)
            g1.add_edges_from(graph_name_edges)
            plt.xlim(-1, 8)                     
            plt.ylim(-4, 4)             
            plt.tight_layout()
            nx.draw(
                    g1,
                    pos = pos,                    
                    node_color = 'orange',
                    edge_color = 'black',
                    font_size =12, 
                    node_size =360,
                    with_labels=True
                )

            plt.savefig(fig_path, format="PNG")
            plt.clf()
        return graph_id_edges
