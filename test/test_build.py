from unittest import TestCase
from app.database import Database
from app.build.service import BuildService
from app.job.service import JobService
import logging


class TestBuild(TestCase):

    def setUp(self):
        self.testdb = Database('sqlite:///test/data/database.db')
        logging.getLogger().setLevel(logging.DEBUG)

    def tearDown(self):
        self.testdb.dropAll()

    def test_queue_build(self):
        build_service = BuildService(self.testdb)
        job_service = JobService(self.testdb)

        job_service.add_job('Test job')
        job = job_service.get_jobs()[0]

        self.assertIsNotNone(job)

        build_service.queue_build(job.id)
        build_service.queue_build(job.id)

        builds = build_service.get_queue_builds(job.id)

        self.assertEqual(2, len(builds))
        self.assertFalse(builds[0].id == builds[1].id)
