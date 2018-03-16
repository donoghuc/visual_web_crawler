# from passlib.handlers.sha2_crypt import sha512_crypt
from crawler_app.data.history import History
from crawler_app.data.dbsession import DbSessionFactory
from crawler_app.services.helpers import build_json_graph
import pandas as pd
import sqlite3 as lite
import json


class HistoryService:
    @staticmethod
    def add_history(user_id, url, search_type, search_limit, keyword):
        session = DbSessionFactory.create_session()

        history = History()
        history.user_id = user_id
        history.url = url
        history.search_type = search_type
        history.search_limit = search_limit
        history.keyword = keyword

        session.add(history)
        session.commit()

        return history.auto_id


    @staticmethod
    def get_history(user_id):
        query = "SELECT auto_id, url, search_type, search_limit, keyword, created FROM History WHERE user_id=?"
        conn = lite.connect(DbSessionFactory.get_db_file_path())
        df = pd.read_sql_query(query,conn,params=(user_id,))
        conn.close()
        history_dict_list = list()
        for i,r in df.iterrows():
            history_dict_list.append(dict(auto_id=r['auto_id'],
                                              url=r['url'],
                                              search_type=r['search_type'],
                                              search_limit=r['search_limit'],
                                              keyword=r['keyword'],
                                              created=r['created']))
        return history_dict_list


    @staticmethod
    def get_params_by_history_id(lookup_id):
        ''' return parameters from an old search'''

        session = DbSessionFactory.create_session()

        history = session.query(History) \
            .filter(History.auto_id == lookup_id) \
            .first()

        return dict(url=history.url, search_type=history.search_type, search_limit=history.search_limit, keyword=history.keyword)


    @staticmethod
    def get_archived_graph_data(lookup_id):
        '''get json repr of old graph'''
        query = "SELECT domain, node_depth, node_id, parent_node, url, found FROM Graph_Data WHERE lookup_id=?"
        conn = lite.connect(DbSessionFactory.get_db_file_path())
        df = pd.read_sql_query(query,conn,params=(lookup_id,))
        conn.close()
        if len(df) > 1:
            graph = build_json_graph(df)
            return json.dumps(graph)
        # if graph only had one node, build with seed url 
        else:
            graph = json.dumps(dict(url = df['url'].values[0], domain=df['domain'].values[0]))
            return graph 


    @staticmethod
    def add_data(dataframe):
        conn = lite.connect(DbSessionFactory.get_db_file_path())
        dataframe.to_sql('Graph_Data',conn,if_exists='append',index=False)
        conn.close()
