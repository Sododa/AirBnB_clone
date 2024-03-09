#!/usr/bin/python3
"""assign with an uuid when an instance is created
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
