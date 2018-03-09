import sqlalchemy
import sqlalchemy.orm
from crawler_app.data.modelbase import SqlAlchemyBase
import crawler_app.data.account
import os


class DbSessionFactory:
    factory = None
    db_file_path = None

    @staticmethod
    def global_init(db_file):
        if DbSessionFactory.factory:
            return

        if not db_file or not db_file.strip():
            raise Exception("You must specify a data file.")

        conn_str = 'sqlite:///' + db_file
        print("Connecting to db with conn string: {}".format(conn_str))
        DbSessionFactory.db_file_path = os.path.join(os.getcwd(),'db',db_file)
        engine = sqlalchemy.create_engine(conn_str, echo=False)
        SqlAlchemyBase.metadata.create_all(engine)
        DbSessionFactory.factory = sqlalchemy.orm.sessionmaker(bind=engine)


    @staticmethod
    def create_session():
        return DbSessionFactory.factory()


    @staticmethod
    def get_db_file_path():
        return DbSessionFactory.db_file_pathd