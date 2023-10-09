#!/usr/bin/python3
import sys
sys.path.append("/root/AirBnB_clone")
from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance
storage = FileStorage()

# Call the reload() method to load data from the JSON file (if it exists)
storage.reload()

