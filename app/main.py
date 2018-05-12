import logging
import os
from app.config import Config
from app._common.util import TaskLoader, Storage
from app.database import Database

class Application:
    def __init__(self):
    
        # Configure logging
        logging.getLogger().setLevel(logging.DEBUG)

        # Create database
        self.database = Database(Config.DATABASE_PATH)

        # Initiatlize task loader
        self.taskloader = TaskLoader(os.path.join(os.path.dirname(__file__), 'tasks'))

        # Initialize the storage
        self.storage = Storage('F:\Git\work')

    def reset():
        self.database.dropAll()

if __name__ == "__main__":
    app = Application()