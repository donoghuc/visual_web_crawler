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
    def add_data(dataframe):
        conn = lite.connect(DbSessionFactory.get_db_file_path())
        dataframe.to_sql('Graph_Data',conn,if_exists='append',index=False)
        conn.close()
        return "OK"