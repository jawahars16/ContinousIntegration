from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from app.model import Base
# from model import job
# from model import step
# from model import step
# from model import step

from contextlib import contextmanager
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
            raise

    def newsession(self):
        return self.session()

    def dropAll(self):
        Base.metadata.drop_all(self.engine)

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
