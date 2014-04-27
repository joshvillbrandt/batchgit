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

def print_repo_status(name, branch, msg, color):
    print('{:30}  {}{:10}{}  {}{}{}'.format(
        name,
        Fore.CYAN, branch, Fore.RESET,
        color, msg, Fore.RESET))

# run the command
if args.cmd == 'status':
    fetch_fail = False

    # list all directories
    dirnames = os.walk('.').next()[1]
    for dirname in dirnames:
        # link to the git repo
        try:
            repo = Repo(dirname)
        except Exception:
            print_repo_status(dirname, "n/a", "not a git repo", Fore.WHITE)
            continue

        # get active branch
        br = repo.active_branch.__str__()

        # find uncommitted files
        if repo.is_dirty():
            print_repo_status(
                dirname, br,
                str(len(repo.index.diff(None))) + " files modified", Fore.RED)
            continue

        # find un-pushed commits
        unpushed_commits = list(repo.iter_commits('%s@{u}..%s' % (br, br)))
        if len(unpushed_commits) > 0:
            print_repo_status(
                dirname, br,
                "ahead " + str(len(unpushed_commits)) + " commits", Fore.RED)
            continue

        # # find out-of-date repos
        try:
            repo.remotes.origin.fetch()
        except Exception:
            # not connected to the network
            fetch_fail = True
            br = '*' + br
            pass
        unpulled_commits = list(repo.iter_commits('%s..%s@{u}' % (br, br)))
        if len(unpulled_commits) > 0:
            print_repo_status(
                dirname, br,
                "behind " + str(len(unpulled_commits)) + " commits",
                Fore.YELLOW)
            continue

        # else "ok"
        print_repo_status(dirname, br, "ok", Fore.GREEN)

    # let the client know if things didn't go well
    if fetch_fail is True:
        print("\n*unable to fetch remote repositories...")
else:
    print('Command "%s%s%s" not supported.' % (
        Fore.CYAN, args.cmd, Fore.RESET))
