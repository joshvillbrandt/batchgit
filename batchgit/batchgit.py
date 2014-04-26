# batchgit
# Josh Villbrandt, 2014/04/26
# Usage: python batchgit.py -h

import os
import argparse
from colorama import Fore
from git import Repo

# get input
parser = argparse.ArgumentParser(
    description='Runs git commands on multiple repositories.')
parser.add_argument(
    'cmd', action='store', help='the command to run on all repos')
args = parser.parse_args()

# run the command
if args.cmd == 'status':
    print('Running "%s%s%s" on all repos...\n' % (
        Fore.CYAN, args.cmd, Fore.RESET))

    # list all directories
    dirnames = os.walk('.').next()[1]
    for dirname in dirnames:
        # link to the git repo
        repo = Repo(dirname)
        print dir(repo)
        print('{:30}  {}{}{}'.format(
            dirname, Fore.GREEN, repo.is_dirty, Fore.RESET))
else:
    print('Command "%s%s%s" not supported.' % (
        Fore.CYAN, args.cmd, Fore.RESET))
