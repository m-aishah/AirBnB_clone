#!/usr/bin/python3
'''Defines the AirBnB console.'''

import cmd
import re
import models
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
        Prints the string representation of an instance based on the class name.
        '''
        args = parse(line)
        objects = models.storage.all()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] != 'BaseModel':
            print('** class doesn\'t exist **')
        elif len(args) == 1:
            print('** instance id missing **')
        elif "{}.{}".format(args[0], args[1]) not in objects:
            print('** no instance found **')
        else:
            print(objects["{}.{}".format(args[0], args[1])])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
