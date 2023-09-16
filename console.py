#!/usr/bin/python3
'''Defines the AirBnB console.'''

import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
