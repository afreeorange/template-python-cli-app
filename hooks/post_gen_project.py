"""
Generate a project documentation scaffold depending on whether the user
picks MkDocs or Sphinx. The cookiecutter templates are separate repositories.

mail@nikhil.io
Wed Jul 13 11:23:20 CDT 2016
"""


from __future__ import print_function

import os
import shutil
import subprocess
import sys

import ast


# We do this since the JSON dumped by Jinja2/Cookiecutter has single
# quotes. Can use 'demjson' but sticking to the standard library is better.
project_data = ast.literal_eval(
    open('../{{cookiecutter.package_name}}/.project_data').read()
)

# Set up documentation depending on choice of generator
if project_data['documentation_markup'] == 'reStructuredText':
    shutil.rmtree(
        '../{{cookiecutter.package_name}}/docs_mkdocs',
        ignore_errors=True
    )
    os.rename(
        '../{{cookiecutter.package_name}}/docs_sphinx',
        '../{{cookiecutter.package_name}}/docs'
    )
elif project_data['documentation_markup'] == 'Markdown':
    shutil.rmtree(
        '../{{cookiecutter.package_name}}/docs_sphinx',
        ignore_errors=True
    )
    os.rename(
        '../{{cookiecutter.package_name}}/docs_mkdocs',
        '../{{cookiecutter.package_name}}/docs'
    )
else:
    print('Got an unexpected value for "documentation_markup"')
    sys.exit(1)

# Clean up
os.remove('../{{cookiecutter.package_name}}/.project_data')

# Attempt to initialize git repo with specified URI. This is not
# Windows-friendly. I don't care.
try:
    subprocess.call(
        'cd ../{{cookiecutter.package_name}} && \
        git init && \
        git remote add origin {{cookiecutter.project_repository}}',
        shell=True
    )
    print('{{cookiecutter.project_repository}} is remote called "origin"')
except Exception as e:
    print('! Could not initialize {{cookiecutter.package_name}} as git repo')
    print('! Error was "{}"'.format(str(e)))

print("""
All done! See README.md in {{cookiecutter.package_name}}/ for
some more information on how to start using your project.
""")

