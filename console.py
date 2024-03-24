#!/usr/bin/python3
"""This shall represent the console module"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import shlex
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """This class shall represent the start of the command interpreter"""
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]


    def do_EOF(self, arg):
        """This shall represent the EOF command"""
        return True
    
    def do_quit(self, arg):
        """This shall represent the quit command"""
        return True
    
    def emptyline(self):
        """This shall represent the empty line"""
        pass

    def do_create(self, arg):
        """This shall represent the create command in basemodel"""
        try:
            if not arg:
                raise SyntaxError()
            split_args = arg.split()
            instance = eval(split_args[0])()

            for arg in split_args[1:]:
                parmater = arg.split("=")
                cle = parmater[0]
                valu = parmater[1].replace("_", " ")

                if hasattr(instance, cle):
                    try:
                        setattr(instance, cle, eval(valu))
                    except Exception:
                        pass
                instance.save()
                print("{}".format(instance.id))
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except:
            print("** instance doesn't exist **")

    def do_show(self, args):
        """This shall represent the show command"""
        try:
            if not args:
                raise SyntaxError()
            split_args = args.split(" ")
            if split_args[0] not in HBNBCommand.classes:
                raise NameError()
            if len(split_args) < 2:
                raise IndexError()
            objs = storage.all()
            key = split_args[0] + "." + split_args[1]
            if key in objs:
                print(objs[key])
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except:
            print("** no instance found **")

    def do_destroy(self, args):
        """This shall represent the destroy command"""
        try:
            if not args:
                raise SyntaxError()
            split_args = args.split()
            if split_args[0] not in HBNBCommand.classes:
                raise NameError()
            if len(split_args) < 2:
                raise IndexError()
            key = split_args[0] + "." + split_args[1]
            del storage.all()[key]
            storage.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except:
            print("** no instance found **")

    def do_all(self, args):
        """This shall represent the all command"""
        objs = storage.all()
        mi_lst = []
        if not args:
            for cle in objs:
                mi_lst.append(str(objs[cle]))
            print(mi_lst)
            return
        try:
            if args not in HBNBCommand.classes:
                raise NameError()
            for cle in objs:
                if args in cle:
                    mi_lst.append(str(objs[cle]))
            print(mi_lst)
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, args):
        """ THis shall represent the update command """
        try:
            if not args:
                raise SyntaxError()
            mi_lst = split(args, " ")
            if mi_lst[0] not in HBNBCommand.classes:
                raise NameError()
            if len(mi_lst) < 2:
                raise IndexError()
            objs = storage.all()
            cle = mi_lst[0] + "." + mi_lst[1]
            if cle not in objs:
                raise KeyError()
            if len(mi_lst) < 3:
                raise ValueError()
            if len(mi_lst) < 4:
                raise AttributeError()
            x = objs[cle]
            try:
                x.__dict__[mi_lst[2]] = eval(mi_lst[3])
            except Exception:
                x.__dict__[mi_lst[2]] = mi_lst[3]
            x.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except ValueError:
            print("** attribute name missing **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** value missing **")

    def default(self, line):
        """This shall represent the default command"""
        try:
            split_line = line.split(".")
            if len(split_line) < 2:
                raise SyntaxError()
            if split_line[1] == "all()":
                self.do_all(split_line[0])
            if split_line[1] == "count()":
                self.do_count(split_line[0])
            if split_line[1] == "show()":
                self.do_show(split_line[0])
            if split_line[1] == "destroy()":
                self.do_destroy(split_line[0])
            if split_line[1] == "update()":
                self.do_update(split_line[0])
        except SyntaxError:
            print("** command not found **")

    def do_count(self, args):
        """This shall represent the count command"""
        count = 0
        try:
            mi_lst = split(args, " ")
            if mi_lst[0] not in HBNBCommand.classes:
                raise NameError()
            objs = storage.all()
            for cle in objs:
                name = cle.split(".")
                if name[0] == mi_lst[0]:
                    count += 1
            print(count)
        except NameError:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
