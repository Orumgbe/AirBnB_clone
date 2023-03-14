#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Defines the command interpreter method and attribute"""
    prompt = '(hbnb) '
    class_list = ['BaseModel', 'User', 'Place', 'State', 'City',
                  'Amenity', 'Review']

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exits the program"""
        return True

    def emptyline(self):
        """Empty line builtin update"""
        pass

    def do_create(self, line):
        """Creates instance of a class, saves to JSON file and prints id
           Usage: create <class name>
        """
        if not line:
            print("** class name missing **")
        elif line not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        else:
            temp = eval(line)()
            temp.save()
            print(temp.id)

    def do_show(self, line):
        """Print string representation of as instance based on name and id
           Usage: show <class name> <id>
        """
        if not line:
            print("** class name missing **")
        else:
            try:
                name, id = line.split(' ')
            except ValueError:
                print("** instance id missing **")
                return

            key = "{}.{}".format(name, id)
            if name not in HBNBCommand.class_list:
                print("** class doesn't exist **")
                return
            elif key not in storage.all().keys():
                print("** no instance found **")
                return
            else:
                print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on class name and id
           Usage: delete <class name> <id>
        """
        if not line:
            print("** class name missing **")
        else:
            try:
                name, id = line.split(' ')
            except ValueError:
                print("** instance id missing **")
                return

            key = "{}.{}".format(name, id)
            if name not in HBNBCommand.class_list:
                print("** class doesn't exist **")
                return
            elif key not in storage.all().keys():
                print("** no instance found **")
                return
            else:
                del(storage.all()[key])
                storage.save()

    def do_all(self, line):
        """Prints string representation of all instance (specified or not)
           Usage: all <class name>

           If class name is missing, command prints all classes in storage
        """
        instances = []
        if not line:
            for key, value in storage.all().items():
                cls_name = key.split('.')[0]
                instance = eval(cls_name)(**value.to_dict())
                instances.append(str(instance))
            print(instances)
        elif line in HBNBCommand.class_list:
            for key, value in storage.all().items():
                if line == key.split('.')[0]:
                    instance = eval(line)(**value.to_dict())
                    instances.append(str(instance))
            print(instances)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates instance by adding or updating attribute
           Usage:
               update <class name> <id> <attribute name> '<attribute value>'"""
        if not line:
            print("** class name missing **")
        else:
            try:
                args = line.split(' ')
            except ValueError:
                print("** instance id missing **")
                return
            try:
                if args[2]:
                    pass
            except IndexError:
                print("** attribute name missing **")
                return
            try:
                if args[3]:
                    pass
            except IndexError:
                print("** value missing **")
                return

           key = "{}.{}".format(args[0], args[1])
            if args[0] not in HBNBCommand.class_list:
                print("** class doesn't exist **")
            elif key not in storage.all().keys():
                print("** no instance found **")
            else:
                args[3] = args[3].strip("'")
                args[3] = args[3].strip('"')
                setattr(storage.all()[key], args[2], args[3])
                storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
