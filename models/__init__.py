from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance
storage = FileStorage()

# Call the reload() method to deserialize existing data (if the JSON file exists)
storage.reload()
