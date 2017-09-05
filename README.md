Cookiecutter Template for a A Command-line app in Python
========================================================

What it says on the tin. Should be compatible with both Pythons 2 and 3.

Usage
-----

You'll need an active virtualenv, [cookiecutter](https://github.com/audreyr/cookiecutter), and [GNU `make`](https://www.gnu.org/software/make)

```bash
# In a virtualenv
cookiecutter https://github.com/afreeorange/template-python-cli-app.git
```

Then answer some questions, get into the project folder and type `make` to see a list of project tasks.

What that does
--------------

* A basic `setuptools` configuration to package the project
* Documentation using either Markdown/MkDocs or reStructuredText/Sphinx with a server and live-reloader for easy edits and changes
* Tests using `py.test`
* Test coverage analysis using `coverage.py`
* Linting using Flake8
* Easy version-bumping using `semantic versioning` and [bumpversion](https://github.com/peritus/bumpversion)
* A comprehensive `.gitignore` (via [Github](https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore))
* A `Makefile` that allows me to do many other things :)

License
-------

Do whatever you want.
