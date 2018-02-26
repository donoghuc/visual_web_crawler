# from passlib.handlers.sha2_crypt import sha512_crypt
from crawler_app.data.history import History
from crawler_app.data.dbsession import DbSessionFactory


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

    # @classmethod
    # def find_account_by_username(cls, username):

    #     if not username or not username.strip():
    #         return None

    #     username = username.lower().strip()

    #     session = DbSessionFactory.create_session()

    #     account = session.query(Account) \
    #         .filter(Account.username == username) \
    #         .first()

    #     return account

    # @staticmethod
    # def hash_text(plain_text_password):
    #     hashed_text = sha512_crypt.encrypt(plain_text_password, rounds=150000)
    #     return hashed_text

    # @classmethod
    # def get_authenticated_account(cls, username, plain_text_password):
    #     account = AccountService.find_account_by_username(username)
    #     if not account:
    #         return None

    #     if not sha512_crypt.verify(plain_text_password, account.password_hash):
    #         return None

    #     return account

    # @classmethod
    # def find_account_by_id(cls, user_id):
    #     if not user_id:
    #         return None

    #     session = DbSessionFactory.create_session()

    #     account = session.query(Account) \
    #         .filter(Account.id == user_id) \
    #         .first()

    #     return account