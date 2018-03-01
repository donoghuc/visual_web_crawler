# from passlib.handlers.sha2_crypt import sha512_crypt
from crawler_app.data.history import History
from crawler_app.data.dbsession import DbSessionFactory
import pandas as pd
import sqlite3 as lite


class HistoryService:
    @staticmethod
    def add_history(user_id, url, search_type):
        session = DbSessionFactory.create_session()

        history = History()
        history.user_id = user_id
        history.url = url
        history.search_type = search_type

        session.add(history)
        session.commit()

        return history.auto_id

    @staticmethod
    def get_history(user_id):
        query = "SELECT auto_id, url, search_type, created FROM History WHERE user_id=?"
        conn = lite.connect(DbSessionFactory.get_db_file_path())
        df = pd.read_sql_query(query,conn,params=(user_id,))
        conn.close()
        if len(df) > 0:
            history_dict_list = list()
            for i,r in df.iterrows():
                history_dict_list.append(dict(auto_id=r['auto_id'],
                                              url=r['url'],
                                              search_type=r['search_type'],
                                              created=r['created']))
            return history_dict_list

        else:
            return None


    @staticmethod
    def add_data(dataframe):
        conn = lite.connect(DbSessionFactory.get_db_file_path())
        dataframe.to_sql('Graph_Data',conn,if_exists='append',index=False)
        conn.close()
        return "OK"