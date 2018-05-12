from datetime import datetime
from app.model import Job, Build
from app._common.enumeration import BuildStatus
from app._common.error import JobNotFoundError


class BuildService:

    def __init__(self, db):
        self.db = db

    def queue_build(self, job_id):

        job = None

        with self.db.new_query_session() as session:
            job = session.query(Job).filter(Job.id == job_id).one()

        if job is None:
            raise JobNotFoundError(f'Job with {job_id} not found')

        build = Build(
            id=datetime.utcnow().strftime("%Y%m%d.%f"),
            job=job_id,
            status=BuildStatus.QUEUED.value
        )

        with self.db.new_session() as session:
            session.add(build)

    def get_queue_builds(self, job_id):

        builds = []

        with self.db.new_query_session() as session:
            builds = session.query(Build).filter(Build.job == job_id).all()

        return builds
