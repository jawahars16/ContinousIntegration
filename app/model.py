from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship

Base = declarative_base()

class Build(Base):

    __tablename__ = 'build'

    id = Column(String(50), primary_key=True, autoincrement=False)
    job = Column(Integer, ForeignKey('job.id'), nullable=False)
    status = Column(Integer, nullable=False)
    initiated_on = Column(DateTime, nullable=False,
                          default=datetime.utcnow())
    initiated_by = Column(String(50))


class Job(Base):
    __tablename__ = 'job'

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(String(50))
    steps = relationship('Step', lazy='select')
    created_on = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_on = Column(DateTime, default=datetime.utcnow())

    
class Step(Base):
    __tablename__ = 'step'

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    job = Column(Integer, ForeignKey('job.id'), nullable=False)
    parameters = relationship('TaskParameter', lazy='select')

    def __init__(self, title, job_id):
        self.title = title
        self.job = job_id

        
class TaskParameter(Base):
    __tablename__ = 'task_parameter'

    id = Column(Integer, primary_key=True)
    step = Column(Integer, ForeignKey('step.id'), nullable=False)
    key = Column(String(50), nullable=False)
    value = Column(String(255))
    updated_on = Column(DateTime, default=datetime.utcnow())
