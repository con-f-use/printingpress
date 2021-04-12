# Contributing

Code Contributions should be made on on their own Git branches.
When the code is ready for review, open a pull request to the `dev`
branch. The pull request will first be reviewed and, if accepted, be
merged to `dev`.
After a evaluation period, it can propagated to the `main` and included
into a release, if all goes well.

## Development Environment

You can setup a development Environment like so:

```
git clone https://github.com/con-f-use/printingpress.git
cd printingpress
python -m venv ppress && source ppress/bin/activate
git checkout -b "$USER-branch"
pip install -r requirements-dev.txt
pre-commit install
```

Which should clone this repository and install the necessary tools and
dependencies into a Python virtual environment named `ppress`.
You can enter this environment by via `source ppress/bin/activate`
(on windows: `ppress\Scripts\activate.bat`) and exit it by calling
`deactivate`.

## Workflows

The repository on Github has number of workflows (Github Actions) for
automatic checking, packaging and releasing of our Code.

 * Any commit to the repository will be subjected to code quality checks
   using [pre-commit](https://pre-commit.com/). This helps mitigate
   formatting disputes and common mistakes.
 * Any commit will be packages and uploaded to the test index as
   https://test.pypi.org/project/printingpress/ for development convenience.
   From there it can be installed with:
   ```
   pip install --pre -i https://test.pypi.org/simple/ printingpress
   ```
 * Any pull request will cause the unit tests in `./tests/` to be
   executed.
 * A push to the `main` branch will trigger the same checks as a pull
   request.
 * A push of a new version tag to `main` will trigger the same checks
   as a pull request would and cause the new version to be uploaded to the
   main Python Package Index at https://pypi.org/project/printingpress/

If you have set up your development environment as described above,
the code quality checks should run at every local commit.
You can run them manually with:

```
pre-commit run --all-files
```

Skip individual checks with:

```
env SKIP=black,check-ast git commit -m 'some message'
```

Or skip the local checks alltogether:

```
git commit --no-verify -m 'some message'
```

## Tests

We strongly encourage you to write tests and run them locally prior to
any push to the Github repository.
Tests are located in the `./tests/` directory and we use
pytest](https://docs.pytest.org/en/stable/)
as our testrunner.

The most common way to invoke pytest is by running:

```
pytest --log-level=DEBUG --log-cli-level=DEBUG --show-capture=all --maxfail 1 -k "equivalence or noisy"
```

in your development environment.

Some of the frequently used pytest options are:

 * `-maxfail <number>` stop after a number of failed tests
 * `--pdb` start a pdb debugger session where a test case failed
 * `-k <erpressions>` to run only cases with matching names or classes (partial matches are fine)
 * `-m <markers>` to run only marked tests (`pytest --markers` to show possible markers to mark cases with)

Logical operators like `not`, `and` and `or` can be used with markers
and expressions.
You can run exclusively those tests in individual files by passing
their paths as arguments:

```
pytest ./tests/printingpress_test.py
```

But pytest is very good at auto-discovery.

## Documentation

The Documentation is hosted on [readthedocs](https://readthedocs.org/)
and build with
[Sphinx](https://www.sphinx-doc.org).

[http://printingpress.readthedocs.io](http://printingpress.readthedocs.io)

To get started:

 - [Getting Started with Sphinx](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html)
 - [Re-Structured Text Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)

The development environment described above, should have everything
you need to build the documentation locally.
Just run:

```
cd docs/
make html
```

And open ./docs/_build/html/index.html in your browser.

**Note:** The readthedocs webinterface options are ignored, because we
have a `./.readthedocs.yaml` present.

## Packaging

Packages can be manually build and uploaded with:

```
rm -rf ./dist/
python setup.py bdist_wheel
twine upload ./dist/raphepp-*.whl \
    --username __token__ --password "$(pass printingpress-pypi-token)" \
    --repository-url https://test.pypi.org/legacy/
```

Where the `--repository-url` can be omitted for the main Python Package
Index. We strongly recommend using a password manager like `pass` in
the example or twine's configuration file to manage the authentication token.
