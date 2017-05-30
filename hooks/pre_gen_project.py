from __future__ import print_function

from string import ascii_letters
import sys


cleaned_package_name = ''.join(
    filter(
        lambda x: x in ascii_letters + '_', '{{cookiecutter.package_name}}'
    )
)

if cleaned_package_name != '{{cookiecutter.package_name}}':
    print("""
Invalid package name!
Can only contain alphabets (upper or lowercase) and underscores
""")
    sys.exit(1)
