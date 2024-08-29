#!/usr/bin/python3
"""
create a console to streamline the process of
creating, updating, showing and deleting objects
"""

import cmd
from models.base_model import BaseModel
from models.category import Category
from models.project import Project
from models.tools import Tool
from models.users import User
import json
from models import storage

cls_names = {"BaseModel": BaseModel, "Category": Category,
             "Project": Project, "Tool": Tool, "User": User}



class SoftSCommand(cmd.Cmd):
    """creata a console for the softsphere"""
    prompt = "(SoS) "


    def do_quit(self, arg):
        """quit the console"""
        return True
    
    def do_EOF(slef, arg):
        """handle EOF situation"""
        print()
        return True
    
    def emptyline(self):
        pass

    def do_create(self, arg):
        """
        create new object and save it to the storage
        command => create Project {"category":"gaming"}
        """
        if not arg:
            print("** class name is missing **")
        else:
            args_list = arg.split(" ")
            cls_name = args_list[0]
            if cls_name in cls_names.keys():
                attrs_dict = {}
                if len(args_list) > 1:
                    attrs_dict = json.loads(' '.join(args_list[1:]))
                # get the class name
                # and concatenate all other text together
                # to avoid teh space split issue
                new_obj = cls_names[cls_name](**attrs_dict)
                new_obj.save()
                print(new_obj.to_dict())
            else:
                print("**class doesn't exist**")

    def do_all(self, arg):
        """
        command => all Project
        the arg after all is optional
        if arg is not existed, print all of the objects from all classes
        """
        print(storage.all(arg))

    def do_update(self, arg):
        """
        command => update Project 12x3-34r5-24f4-234d {"name":"Softsphere"}
        print the current object after updating and after changind update date
        if class name not existing:
        print "class does not exist"
        """
        args_list = arg.split(" ")
        if not arg:
            print("** class name is missing **")
        elif args_list[0] not in cls_names.keys():
            print("**class does not exist**")
        elif len(args_list) < 2:
            print("** id is missing **")
        elif len(args_list) < 3:
            print("**attribute are missing**")
        else: # the 3 input fields was passed successfully
            id = args_list[1]
            obj = storage.find(id)
            if not obj:
                print(f"** no object by id {id} was found **")
            try:
                attrs_dict = json.loads(" ".join(args_list[2:]))
                for attr, val in attrs_dict.items():
                    obj.__dict__[attr] = val
                obj.save()
            except:
                print("**not valid atributes dictionary**")
    
    def do_show(self, arg):
        """
        command => show Project 123-44d-553
        show all attributes of an object
        """
        args_list = arg.split(" ")
        if not arg:
            print("** class name is missing **")
        elif args_list[0] not in cls_names.keys():
            print("**class does not exist**")
        elif len(args_list) < 2:
            print("** id is missing **")
        else: # the 2 input fields was passed successfully
            id = args_list[1]
            obj = storage.find(id)
            if not obj:
                print(f"** no object by id {id} was found **")
            else:
                print(obj.to_dict())
        
    def do_delete(self, arg):
        """
        command => delete project 12x3-34r5-24f4-234d
        if class name not existing:
        print "class does not exist"
        """
        args_list = arg.split(" ")
        if not arg:
            print("** class name is missing **")
        elif args_list[0] not in cls_names.keys():
            print("**class does not exist**")
        elif len(args_list) < 2:
            print("** id is missing **")
        else: # the 2 input fields was passed successfully
            id = args_list[1]
            obj = storage.find(id)
            if not obj:
                print(f"** no object by id {id} was found **")
            else:
                storage.delete(obj)


if __name__ == "__main__":
    SoftSCommand().cmdloop()
