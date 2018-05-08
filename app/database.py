from sqlalchemy import create_engine
from builtins import Exception
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from contextlib import contextmanager
from app.model import *
import logging


class Database:
    def __init__(self, path, echo=False):
        try:
            self.engine = create_engine(path, poolclass=NullPool)
            self.engine.echo = echo
            self.session = sessionmaker(bind=self.engine)
            Base.metadata.create_all(self.engine)
        except Exception as e:
            logging.error('Database creation failed')
            logging.error(e)

    def newsession(self):
        return self.session()

    def dropAll(self):
        try:
            Base.metadata.drop_all(self.engine)
        except Exception as error:
            logging.error(error)


    @contextmanager
    def new_session(self):
        """
        Provide a transactional scope around a series of operations.
        Useful in case of DML operations
        """
        session = self.session()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    @contextmanager
    def new_query_session(self):
        """
        Provide a transactional scope around a series of operations.
        Useful in case of query operations
        """
        session = self.session()
        try:
            yield session
        except:
            session.rollback()
            raise
        finally:
            session.close()
