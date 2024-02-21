#!/usr/bin/python3
""" This code shall represent the console code"""
import cmd
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """This is the HBNBCommand class"""
    prompt = "(hbnb) "
    clsses = ["BaseModel", "User", "State", "City",
              "Amenity", "Place", "Review"]

    def do_EOF(self, arg):
        """This shall exit the program"""
        return True

    def do_quit(self, arg):
        """This shall exit the program"""
        return True

    def emptyline(self):
        """This shall do nothing"""
        pass

    def do_create(self, arg):
        """This shall create a new instance of BaseModel"""
        try:
            if not arg:
                raise SyntaxError("** class name missing **")
            args = split(arg)
            if args[0] not in self.clsses:
                raise NameError("** class doesn't exist **")
            new = eval("{}()".format(args[0]))
            new.save()
            print(new.id)
        except SyntaxError as e:
            print(e)
        except NameError as e:
            print(e)
        except Exception as e:
            print(e)

    def do_show(self, arg):
        """This shall print the string representation of an instance"""
        try:
            if not arg:
                raise SyntaxError("** class name missing **")
            args = split(arg)
            if args[0] not in self.clsses:
                raise NameError("** class doesn't exist **")
            if len(args) < 2:
                raise SyntaxError("** instance id missing **")
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all().keys():
                raise NameError("** no instance found **")
            print(storage.all()[key])
        except SyntaxError as e:
            print(e)
        except NameError as e:
            print(e)
        except Exception as e:
            print(e)

    def do_destroy(self, arg):
        """This shall delete an instance"""
        try:
            if not arg:
                raise SyntaxError("** class name missing **")
            args = split(arg)
            if args[0] not in self.clsses:
                raise NameError("** class doesn't exist **")
            if len(args) < 2:
                raise SyntaxError("** instance id missing **")
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all().keys():
                raise NameError("** no instance found **")
            del storage.all()[key]
            storage.save()
        except SyntaxError as e:
            print(e)
        except NameError as e:
            print(e)
        except Exception as e:
            print(e)

    def do_all(self, arg):
        """This shall print all instances"""
        try:
            if not arg:
                raise SyntaxError("** class name missing **")
            args = split(arg)
            if args[0] not in self.clsses:
                raise NameError("** class doesn't exist **")
            lst = []
            for key, value in storage.all().items():
                if args[0] in key:
                    lst.append(str(value))
            print(lst)
        except SyntaxError as e:
            print(e)
        except NameError as e:
            print(e)
        except Exception as e:
            print(e)

    def do_update(self, arg):
        """This shall update an instance"""
        try:
            if not arg:
                raise SyntaxError("** class name missing **")
            args = split(arg)
            if args[0] not in self.clsses:
                raise NameError("** class doesn't exist **")
            if len(args) < 2:
                raise SyntaxError("** instance id missing **")
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all().keys():
                raise NameError("** no instance found **")
            if len(args) < 3:
                raise SyntaxError("** attribute name missing **")
            if len(args) < 4:
                raise SyntaxError("** value missing **")
            if len(args) < 5:
                setattr(storage.all()[key], args[2], args[3])
            else:
                setattr(storage.all()[key], args[2], " ".join(args[3:]))
            storage.all()[key].save()
        except SyntaxError as e:
            print(e)
        except NameError as e:
            print(e)
        except Exception as e:
            print(e)

    def default(self, arg):
        """This shall handle the default case"""
        try:
            args = arg.split(".")
            if len(args) > 1:
                if args[1] == "all()":
                    self.do_all(args[0])
                elif args[1] == "count()":
                    count = 0
                    for key, value in storage.all().items():
                        if args[0] in key:
                            count += 1
                    print(count)
                elif args[1][:5] == "show(" and args[1][-1] == ")":
                    self.do_show(args[0] + " " + args[1][5:-1])
                elif args[1][:8] == "destroy(" and args[1][-1] == ")":
                    self.do_destroy(args[0] + " " + args[1][8:-1])
                elif args[1][:7] == "update(" and args[1][-1] == ")":
                    if "{" in args[1] and "}" in args[1]:
                        new = args[1].split("{")
                        new = new[1].split("}")
                        new = new[0].split(", ")
                        for i in new:
                            self.do_update(args[0] + " " + i)
                    else:
                        self.do_update(args[0] + " " + args[1][7:-1])
                else:
                    raise AttributeError
            else:
                raise AttributeError
        except AttributeError as e:
            print("*** Unknown syntax: {}".format(arg))
        except Exception as e:
            print(e)

    def do_count(self, arg):
        """This shall count the instances of a class"""
        try:
            if not arg:
                raise SyntaxError("** class name missing **")
            args = split(arg)
            if args[0] not in self.clsses:
                raise NameError("** class doesn't exist **")
            count = 0
            for key, value in storage.all().items():
                if args[0] in key:
                    count += 1
            print(count)
        except SyntaxError as e:
            print(e)
        except NameError as e:
            print(e)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
