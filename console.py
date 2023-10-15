#!/usr/bin/env python3
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
        """Create a new instance of BaseModel, save it (to the JSON file),
        and print the id."""
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
        """Retrieve an instance based on its ID."""
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
        """Destroy an instance based on its ID."""
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

    def do_count(self, arg):
        """Count instances of a class."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name in ("BaseModel", "Place", "Amenity", "City", "Review", "State", "User"):
            instances = storage.all()
            count = sum(1 for key in instances if key.startswith(class_name + '.'))
            print(count)
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """Prints all string representations of all instances based on the class name."""
        arguments = args.split()
        if not arguments:
            print("** class name missing **")
            return

        class_name = arguments[0]
        if class_name in ("BaseModel", "Place", "Amenity", "City", "Review", "State", "User"):
            if len(arguments) == 2 and arguments[1] == "count()":

                self.do_count(class_name)
            else:
                all_instances = storage.all().values()
                instances_of_class = [str(instance) for instance in all_instances if type(instance).__name__ == class_name]
                if instances_of_class:
                    print(instances_of_class)
                else:
                    print("[]")
        else:
            print("** class doesn't exist **")

    def do_User(self, arg):
        """List every instance or count instances of User class."""
        if arg == "count()":
            self.do_count("User")
        else:
            self.do_all("User " + arg)

    def do_EOF(self, arg):
        """Exit the program."""
        print("")
        return True

    def do_quit(self, arg):
        """Exit the program."""
        return True

    def do_update(self, arg):
        """Update an instance based on its ID with a
        dictionary representation."""
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

        """Check if the attribute name exists in the instance"""
        if hasattr(instance, attr_name):
            """Cast the attribute value to the type of the attribute"""
            attr_type = type(getattr(instance, attr_name))
            setattr(instance, attr_name, attr_type(attr_value))
            instance.updated_at = datetime.datetime.now()
            storage.save()
        else:
            print("** attribute doesn't exist **")

    def do_EOF(self, arg):
        """Exit the program."""
        print("")
        return True

    def do_quit(self, arg):
        """Exit the program."""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
