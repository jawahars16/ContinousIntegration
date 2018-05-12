import logging
from app.database import Database
from app._common.util import Storage
from app.model import Step, Job
import datetime


class JobService:

    def __init__(self, db: Database, storage: Storage):
        self.db = db
        self.storage = storage

    def create_job(self, title, description=None):

        if title is None:
            logging.warning('Title field is mandatory to add a job')
            return False

        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        job_directory = self.storage.create_directory(f'title_{timestamp}')

        job = Job(
            id=None,
            title=title,
            description=description,
            directory = job_directory
        )

        with self.db.new_session() as session:
            session.add(job)

        return True

    def get_jobs(self):
        jobs = []

        with self.db.new_query_session() as session:
            jobs = session.query(Job).all()

        return jobs

    def add_steps(self, job_id, steps):
        job = None

        with self.db.new_session() as session:
            job = session.query(Job).get(job_id)
            if job is None:
                logging.error(f'Job with id {job_id} not found')
                return
            job.steps = steps

    def get_steps(self, job_id):
        with self.db.new_query_session() as session:
            steps = session.query(Step).filter_by(job=job_id).all()

        return steps
