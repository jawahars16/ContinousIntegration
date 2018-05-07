from abc import ABC, abstractmethod

class TaskBase(ABC):

    @abstractmethod
    def get_inputs(self):
        pass

    def validate_inputs(self):
        pass

    @abstractmethod
    def run(self):
        pass


class Input:

    def __init__(self,
                 key,
                 label,
                 inputType='string',
                 value=None,
                 required=False,
                 options=None,
                 info=None):
        self.key = key
        self.label = label
        self.type = inputType
        self.value = value
        self.required = required
        self.options = options
        self.info = info

class Metadata:

    def __init__(self, title, description):
        self.title = title
        self.description = description

class Task:

    def __init__(self, id, title, description = None):
        self.id = id
        self.title = title
        self.description = description
