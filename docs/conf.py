from osscie_official import *

with open('../setup.py', 'r') as f:
    _setup = {}
    exec(f.read(), _setup)

project = _setup['cfg']['name']
rst_prolog = '.. |projectname| replace:: {}'.format(project)
