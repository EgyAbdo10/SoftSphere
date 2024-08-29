#!/usr/bin/python3
"""reload storage every time models are imported"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
