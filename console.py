#!/usr/bin/python3
'''Defines the AirBnB console.'''

import cmd
import re
import models
import json
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
    __classes = [
            'BaseModel',
            'User',
            'State',
            'City',
            'Amenity',
            'Place',
            'Review'
            ]

    def emptyline(self):
        '''Do nothing upon receiving an empty line.'''
        pass

    def default(self, line):
        '''This method runs when an invalid command is inputted.'''
        commands = {
            'all': self.do_all,
            'show': self.do_show,
            'destroy':self.do_destroy,
            'update': self.do_update
        }
        pattern = r'\.'
        match = re.search(pattern, line)
        if match is not None:
            args_list = [line[:match.span()[0]], line[match.span()[1]:]]
            pattern = r'\((.*?)\)'
            match = re.search(pattern, args_list[1])
            if match is not None:
                command = [args_list[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in commands.keys():
                    s = '{} {}'.format(args_list[0], command[1])
                    return commands[command[0]](s)
        return cmd.Cmd.default(self, line)

    def do_quit(self, line):
        '''Quit command to exit the program.'''
        return True

    def do_EOF(self, line):
        '''EOF signal to exit the program.'''
        return True

    def do_create(self, line):
        '''Usage: (hbnb) create <class_name>
        Creates a new instance of a class, saves it and prints the id.'''
        args = parse(line)
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.__classes:
            print('** class doesn\'t exist **')
        else:
            m = eval(args[0])()
            print(m.id)

    def do_show(self, line):
        '''Usage: (hbnb) show <class_name> <id>
        Prints the string representation of an instance of a class.
        '''
        args = parse(line)
        objects = models.storage.all()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.__classes:
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
        elif args[0] not in HBNBCommand.__classes:
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
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print('** class doesn\'t exist **')
        else:
            objects = models.storage.all()
            output = []
            for obj in objects.values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    output.append(obj.__str__())
                elif len(args) == 0:
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
        elif args[0] not in HBNBCommand.__classes:
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
