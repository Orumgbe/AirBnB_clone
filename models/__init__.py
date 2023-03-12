#!/usr/bin/python3
"""This module creates an instance of class FileStorage"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
