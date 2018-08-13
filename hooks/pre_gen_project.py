from __future__ import print_function

from string import ascii_letters
import sys
import subprocess

# Check for a valid package name
cleaned_package_name = ''.join(
    filter(
        lambda x: x in ascii_letters + '_', '{{cookiecutter.package_name}}'
    )
)

invalid_message = """
Invalid package name!
Can only contain upper or lowercase letters and underscores
"""

if cleaned_package_name != '{{cookiecutter.package_name}}':
    print(invalid_message)
    sys.exit(1)

# Upgrade setuptools to avoid version issues when running
# coverage or linting tests
try:
    subprocess.call(
        'pip install --upgrade setuptools',
        shell=True,
    )
except Exception as e:
    print('! Could not upgrade setuptools')
    print('! Error was "{}"'.format(str(e)))
    sys.exit(1)

