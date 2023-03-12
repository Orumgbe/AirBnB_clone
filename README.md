AirBnB clone - The Console

This project is the first step of a multi-stage project to develop a
clone of the AirBnB site.

This stage focuses on the console.

The console is a command interpreter that allows the manipulation of
data without a visual interface.

The console was implemented using the cmd module, and uses a file
storage method to save data (serializatiion and deserialization with
JSON file).

Files and Directories

* models - directory will contain all classes used for the entire project.
* tests - directory will contain all unit tests.
* console.py - file is the entry point of our command interpreter.
* models/base_model.py - file is the base class of all our models.
                       It contains common elements:
                       attributes: id, created_at and updated_at
                       methods: save() and to_json()
* models/engine - directory will contain all storage classes (using the same prototype).

Commands

* create - Creates an instance based on given class

* destroy - Destroys an object based on class and UUID

* show - Shows an object based on class and UUID

* all - Shows all objects the program has access to, or all objects of a given class

* update - Updates existing attributes an object based on class name and UUID

* quit - Exits the program (EOF will as well)
