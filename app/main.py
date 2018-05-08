import logging
import os
from app.config import Config
from app._common.util import TaskLoader
from app.database import Database

class Application:
    def __init__(self):
    
        # Configure logging
        logging.getLogger().setLevel(logging.DEBUG)

        # Create database
        self.database = Database(Config.DATABASE_PATH)

        # Initiatlize task loader
        self.taskloader = TaskLoader(os.path.join(os.path.dirname(__file__), Config.TASK_DIR))

        if not os.path.exists(Config.WORK_DIR):
            os.makedirs(Config.WORK_DIR)

if __name__ == "__main__":
    app = Application()