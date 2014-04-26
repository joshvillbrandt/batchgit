# batchgit

Runs git commands on multiple repositories.

## Installation

If you are have pip configured to use the SpaceX package index (see [pypi](https://code.spacex.corp/public/projects/avionics/pypi)), installation is as simple as:

```bash
sudo pip install batchgit
```

To manually install, you must first install the [LDAP JSON API Python](https://code.spacex.corp/public/projects/avionics/ldap-json-api-python) driver. Then you can run the following:

```bash
git clone https://code.spacex.corp/joshua.villbrandt/batchgit.git
cd batchgit/
sudo python setup.py install
```

## Usage

Right now, this command only support getting the status of a bunch of repositories that are in one directory. You can do this via Python or use the shortcut bash script that was installed:

```bash
cd ~repos/
python batchgit.py status
# or
status
```
