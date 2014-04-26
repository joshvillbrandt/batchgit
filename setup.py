from setuptools import setup

setup(
    name='batchgit',
    version='0.1.0',
    description='Runs git commands on multiple repositories.',
    url='https://code.spacex.corp/public/projects/joshua.villbrandt/batchgit',
    author='Josh Villbrandt',
    author_email='Joshua.Villbrandt@spacex.com',
    license='SpaceX',
    packages=['batchgit'],
    install_requires=[
        "colorama",
        "gitpython"
    ],
    # dependency_links=['http://github.com/user/repo/tarball/master#egg=package-1.0'],
    zip_safe=False)
