#!/usr/bin/emv python3
import io
import json
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import pep8
import unittest
"""
Test for the file storage engine database
"""


class TestFileStorage(unittest.TestCase):
    """
    Test for the file engine
    """
    def setUp(self):
        self.user_model = BaseModel()

    def Pep8StyleGuide(self):
        """
        Test pep8 style guide
        """
        pep8_style = pep8.StyleGuide(quite=True)
        result = pep8_style.check_files(["models/engine/file_storage.py"])
        self.seertEqual(result, 0)

    def test_module_doc(self):
        self.assertTrue(len(FileStorage.__doc__) > 1)

    def test_attribute(self):
        self.assertIsInstance(models.storage._FileStorage__objects, dict)
        self.assertIsInstance(models.storage._FileStorage__file_path, str)

    def test_new_method(self):
       """ New object is correctly added to __objects """
        new = BaseModel()
        for obj in models.storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_all_method(self):
        """unnittest for object returned"""
        objects = storage.all()
        self.assertIsInstance(objects, dict)
        self.assertEqual(models.storage._FileStorage__objects,
                         objects)
        for key, value in models.storage._FileStorage__objects.items():
            self.assertIsInstance(value, BaseModel)

    def test_save_method(self):
        models.storage.save()
        with open(models.storage._FileStorage__file_path,
                  mode="r", encoding="utf-8") as file:
            json_string = json.load(file)
        new_dict = {}
        for key, value in models.storage._FileStorage__objects.items():
            new_dict[key] = value.to_dict()
        self.assertTrue(new_dict == json_string)
