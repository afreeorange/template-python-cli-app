from __future__ import print_function

from string import ascii_letters
import pip
import sys

# Check for a valid package name
cleaned_package_name = ''.join(
    filter(
        lambda x: x in ascii_letters + '_', '{{cookiecutter.package_name}}'
    )
)

invalid_message = """
Invalid package name!
Can only contain alphabets (upper or lowercase) and underscores
"""

if cleaned_package_name != '{{cookiecutter.package_name}}':
    print(invalid_message)
    sys.exit(1)

# Upgrade setuptools to avoid version issues when running
# coverage or linting tests
pip.main(['install', '--upgrade', 'setuptools'])

