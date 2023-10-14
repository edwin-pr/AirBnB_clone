#!/usr/bin/python3
import cmd
import datetime
from models import storage
from models.base_model import BaseModel
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.state import State
from models.user import User

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, arg):
        """This create a new instance of BaseModel, saves it (to the JSON file), and prints the id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name in ("BaseModel", "Place", "Amenity", "City", "Review", "State", "User"):
                new_instance = globals()[class_name]()
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """This retrieves an instance based on its ID."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ("BaseModel", "Place", "Amenity", "City", "Review", "State", "User"):
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        instances = storage.all()

        if key in instances:
            print(instances[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """For destroying an instance based on its ID."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ("BaseModel", "Place", "Amenity", "City", "Review", "State", "User"):
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        instances = storage.all()

        if key in instances:
            del instances[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """This is responsible for prints all string representations of
        all instances based on the class name."""
        args = arg.split()
        if len(args) == 0:
            print([str(value) for value in storage.all().values()])
        else:
            class_name = args[0]
            if class_name in ("BaseModel", "Place", "Amenity", "City", "Review", "State", "User"):
                print([str(value) for key, value in storage.all().items() if key.startswith(class_name)])
            else:
                print("** class doesn't exist **")

    def do_count(self, arg):
        """Retrieve the number of instances of a class."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name in ("BaseModel", "Place", "Amenity", "City", "Review", "State", "User"):
            instances = [value for key, value in storage.all().items() if key.startswith(class_name)]
            count = len(instances)
            print(count)
        else:
            print("** class doesn't exist **")

    def do_EOF(self, arg):
        """Exit the program."""
        print("")
        return True

    def do_quit(self, arg):
        """Exit the program."""
        return True

    def do_update(self, arg):
        """Now, this updates an instance based on its ID with
        a new attribute and value."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ("BaseModel", "Place", "Amenity", "City", "Review", "State", "User"):
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        instances = storage.all()

        if key not in instances:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attr_name = args[2]
        attr_value = args[3]
        instance = instances[key]

        if hasattr(instance, attr_name):
            attr_type = type(getattr(instance, attr_name))
            setattr(instance, attr_name, attr_type(attr_value))
            instance.updated_at = datetime.now()
            storage.save()
        else:
            print("** attribute doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
