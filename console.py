#!/usr/bin/python3
'''Defines the AirBnB console.'''

import cmd
import re
import models
import json
from models.base_model import BaseModel


def parse(args):
    '''Split the arguments into a list of words.'''
    args_list = args.split()
    return args_list


class HBNBCommand(cmd.Cmd):
    '''The AirBnB command interpreter.

    Attributes:
        prompt(str): The command prompt.
    '''

    prompt = '(hbnb) '

    def emptyline(self):
        '''Do nothing upon receiving an empty line.'''
        pass

    def do_quit(self, line):
        '''Quit command to exit the program.'''
        return True

    def do_EOF(self, line):
        '''EOF signal to exit the program.'''
        return True

    def do_create(self, line):
        '''Usage: (hbnb) create <class_name>
        Creates a new instance of a class, saves it and prints the id.'''
        if line:
            if line == 'BaseModel':
                bm = BaseModel()
                bm.save()
                print(bm.id)
            else:
                print('** class doesn\'t exist **')
        else:
            print('** class name missing **')

    def do_show(self, line):
        '''Usage: (hbnb) show <class_name> <id>
        Prints the string representation of an instance of a class.
        '''
        args = parse(line)
        objects = models.storage.all()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] != 'BaseModel':
            print('** class doesn\'t exist **')
        elif len(args) == 1:
            print('** instance id missing **')
        elif '{}.{}'.format(args[0], args[1]) not in objects:
            print('** no instance found **')
        else:
            print(objects["{}.{}".format(args[0], args[1])])

    def do_destroy(self, line):
        '''Usage: (hbnb) destroy <class_name> <id>
        Deletes an instance of the given class.
        '''
        args = parse(line)
        objects = models.storage.all()

        if len(args) == 0:
            print('** class name missing **')
        elif args[0] != 'BaseModel':
            print('** class doesn\'t exist **')
        elif len(args) == 1:
            print('** instance id missing **')
        elif '{}.{}'.format(args[0], args[1]) not in objects:
            print('** no instance found **')
        else:
            del(objects['{}.{}'.format(args[0], args[1])])
            models.storage.save()

    def do_all(self, line):
        '''Usage: (hbnb) all <class_name> OR (hbnb) all
        Prints all string representation of instance of a specified class.
        If no class is given, all instances are printed.
        '''
        args = parse(line)
        if len(args) > 0 and args[0] != 'BaseModel':
            print('** class doesn\'t exist **')
        else:
            objects = models.storage.all()
            output = []
            for obj in objects.values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    output.append(obj.__str__())
                else:
                    output.append(obj.__str__())
            print(output)

    def do_update(self, line):
        '''Usage: update <class name> <id> <attribute name> "<attribute value>"
        Adds/updates an attribute to an instance of a given class.
        '''
        args = parse(line)
        objects = models.storage.all()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] != 'BaseModel':
            print('** class doesn\'t exist **')
        elif len(args) == 1:
            print('** instance id missing **')
        elif '{}.{}'.format(args[0], args[1]) not in objects:
            print('** no instance found **')
        elif len(args) == 2:
            print('** attribute name missing **')
        elif len(args) == 3:
            print('** value missing **')
        elif len(args) > 3:
            obj = objects['{}.{}'.format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                v_type = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = v_type(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
