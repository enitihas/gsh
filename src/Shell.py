import os
import sys
import subprocess as sb
import getpass
import re
import shlex
# noinspection PyUnresolvedReferences
from Colors import Colors
__author__ = 'enitihas'
class Shell:
    """
    This class represents a shell object.
    An object of this class can be used to execute various shell functions.
    Initially, the interface is primitive, but it is expected that more functionality will be added soon.
    """

    def __init__(self):
        self.path = os.environ['PATH'].split(':')
        self.user = os.environ['LOGNAME']
        self.cwd = os.getcwd()
        self.prompt_function = input
        self.builtins = {
            'cd' : self.cd,
            'dir' : self.dir,
            'clr' : self.clr,
            'environ' : self.environ,
            'help' : self.help,
            'pause' : self.pause,
            'echo' : self.echo,
            'quit': self.quit,
        }
        self.executable_list = {}
        for dir in self.path:
            for file in os.listdir(dir):
                full_name = os.path.join(dir,file)
                if self.is_exe(full_name):
                    self.executable_list[file] = full_name

    @property
    def prompt(self):
        return self.user + '->' + re.sub(os.environ['HOME'],'~',self.cwd) + ':$'
        # + os.getcwd().replace('/home/'+self.user, '~') + '$:'

    @staticmethod
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    def clr(self,*args):
        sys.stderr.write("\x1b[2J\x1b[H")

    def cd(self, dest):
        if dest.strip()=='':
            print('The current directory is:', self.cwd)
            return
        try:
            os.chdir(dest)
        except FileNotFoundError:
            print('cd: no such file or directory:', dest)
            return
        if dest[0] == '/':
            self.cwd = dest
        else:
            self.cwd += '/' + dest
        os.environ['PWD'] = self.cwd

    def dir(self,dir):
        abs_path = False
        if dir == '':
            dir = '.'
        if dir[0] == '/':
            abs_path = True
        if dir == '':
            dir = self.cwd
        if not abs_path:
            dir = os.path.join(self.cwd,dir)
        for item in os.listdir(dir):
            fullName = os.path.join(dir,item)
            if os.path.isdir(fullName):
                Colors.print('BLUE',item)
            elif os.access(fullName, os.X_OK):
                Colors.print('RED',item)
            else:
                print(item)

    def environ(self,*args):
        for variable in os.environ:
            print(variable,'=',os.environ[variable],sep='')

    def echo(self,args):
        print(args)

    def pause(self,*args):
        print('In pause mode, press enter to resume.',end='')
        sys.stdout.flush()
        getpass.getpass(prompt='')

    def help(self,*args):
        help_text = '''Hello there.
        This is the help text for our primitive shell gsh.
        We will be happy if you do "chsh -s gsh".
        We are just kidding you.
        Don't do that at all.'''
        print(help_text)

    def quit(self, *args):
        sys.exit(0)

    def run(self):
        while True:
            user_input  = self.prompt_function(self.prompt).strip()
            if user_input == '':
                continue
            commands = user_input.split(';')
            for command in commands:
                arg_list = shlex.split(command)
                self.run_command(arg_list)

    def run_command(self, arg_list):
        if arg_list[0] in self.builtins:
            self.builtins[arg_list[0]](' '.join(arg_list[1:]))
        elif arg_list[0] in self.executable_list:
            sb.call([self.executable_list[arg_list[0]]] + arg_list[1:])
        else:
            print('Invalid command:', arg_list[0])

if __name__ == '__main__':
    sh = Shell()
    sh.run()
