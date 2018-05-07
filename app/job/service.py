import logging
from app.database import Database
from app.model import Step, Job


class JobService:

    def __init__(self, db: Database):
        self.db = db

    def add_job(self, title, description=None, job=None):

        if title is None:
            logging.warning('Title field is mandatory to add a job')
            return False

        job = Job(
            id=job,
            title=title,
            description=description
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
