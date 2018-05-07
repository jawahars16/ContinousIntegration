import logging
import os
from app.config import Config
from app._common.task_loader import TaskLoader
from app.database import Database

# Configure logging
logging.getLogger().setLevel(logging.DEBUG)

# Create database
db = Database(Config.DATABASE_PATH)

# Initiatlize task loader
taskloader = TaskLoader(os.path.join(os.path.dirname(__file__), Config.TASK_DIR))
