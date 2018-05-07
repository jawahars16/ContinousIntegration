from sqlalchemy import MetaData

from task.impl.input import Input
from task.impl.metadata import Metadata
from task.impl.task_base import TaskBase


class DeleteFiles(TaskBase):
    r"""Task to delete files in a folder"""

    def get_inputs(self):
        target_directory = Input('target', 'Target Directory', 'text', '', True)
        include_sub_directories = Input('include_sub', 'Include Sub directories', 'checkbox', )

    def run(self):
        print('running')