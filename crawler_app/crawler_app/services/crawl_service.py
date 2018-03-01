from crawler_app.services.spider import Spider
from crawler_app.services.history_service import HistoryService
# from crawler_app.viewmodels.signin_viewmodel import SigninViewModel
# import crawler_app.infrastructure.cookie_auth as cookie_auth
import pandas as pd
import json
import os


def build_json_graph(df):
    '''build dictionary  to turn into JSON for D3 viz'''
    def make_graph(node_id, graph):
        '''recursively build a graph from nodes'''
        node = dict()
        if node_id in df['parent_node']:
            child_list = list()
            for idx,row in df.loc[df['parent_node'] == node_id].iterrows():
                if node_id != row['node_id']:
                    child_list.append(make_graph(row['node_id'],node))
            if len(child_list) > 0:
                node['children'] = child_list
            node['url'] = df.loc[df['node_id'] == node_id, 'url'].values[0]
            node['domain'] = df.loc[df['node_id'] == node_id, 'domain'].values[0]
            graph.update(node)
        return node

    graph = dict()
    make_graph(0,graph)
    start_node_children = [node for node in graph['children']]
    finalized_graph = dict(url=df.loc[df['node_id'] == 0, 'url'].values[0],
                            domain=df.loc[df['node_id'] == 0, 'domain'].values[0],
                            children=[node for node in graph['children']])
    return finalized_graph


def kick_off_crawl(userid, url, search_type, search_limit, keyword):
    '''start off a crawl'''
    if keyword:
        crawl_obj = Spider(url, search_type, search_limit, keyword)
    else:
        crawl_obj = Spider(url, search_type, search_limit)
    
    new_entry = HistoryService.add_history(userid, url, search_type, search_limit, keyword)
    build_frame = dict(node_id=[],node_depth=[],parent_node=[],domain=[],url=[])
    for i in crawl_obj.graph.nodes:
        build_frame['node_id'].append(i.id)
        build_frame['node_depth'].append(i.node_depth)
        build_frame['parent_node'].append(i.parent_node)
        build_frame['domain'].append(i.domain)
        build_frame['url'].append(i.url)
        
    df = pd.DataFrame(build_frame)
    df['lookup_id'] = new_entry

    print(HistoryService.add_data(df))
    
    # test = build_json_graph(df)
    # graph = json.dumps(test)
    return json.dumps(build_json_graph(df))