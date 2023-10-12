#!/usr/bin/python3
import cmd
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
        """Create a new instance of BaseModel, save it (to the JSON file), and print the id."""
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
        """Print the string representation of an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name in ("BaseModel", "Place", "Amenity", "City", "Review", "State", "User"):
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    instance_id = args[1]
                    key = "{}.{}".format(class_name, instance_id)
                    if key in storage.all():
                        print(storage.all()[key])
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file)."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name in ("BaseModel", "Place", "Amenity", "City", "Review", "State", "User"):
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    instance_id = args[1]
                    key = "{}.{}".format(class_name, instance_id)
                    if key in storage.all():
                        del storage.all()[key]
                        storage.save()
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representations of all instances based on the class name."""
        args = arg.split()
        if len(args) == 0:
            print([str(value) for value in storage.all().values()])
        else:
            class_name = args[0]
            if class_name in ("BaseModel", "Place", "Amenity", "City", "Review", "State", "User"):
                print([str(value) for key, value in storage.all().items() if key.startswith(class_name)])
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name in ("BaseModel", "Place", "Amenity", "City", "Review", "State", "User"):
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    instance_id = args[1]
                    key = "{}.{}".format(class_name, instance_id)
                    if key in storage.all():
                        if len(args) < 3:
                            print("** attribute name missing **")
                        else:
                            attribute_name = args[2]
                            if len(args) < 4:
                                print("** value missing **")
                            else:
                                attribute_value = args[3]
                                instance = storage.all()[key]
                                setattr(instance, attribute_name, attribute_value)
                                instance.save()
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_EOF(self, arg):
        """Exit the program."""
        print("")
        return True

    def do_quit(self, arg):
        """Exit the program."""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
