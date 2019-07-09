# requirements.txt in python

## what is the purpose of the requirements.txt's exists?

“Requirements files” are files containing a list of items to be installed using pip install like so:


```
pip install -r requirements.txt
```

Requirements files are used to force pip to properly resolve dependencies. 

## how to generate requirements.txt?

Requirements files are used to hold the result from [pip freeze][pip freeze] for the purpose of achieving repeatable installations. In this case, your requirement file contains a pinned version of everything that was installed when pip freeze was run.

[pip freeze]: https://pip.pypa.io/en/stable/reference/pip_freeze/#pip-freeze

```
pip freeze > requirements.txt
```


### pip freeze

Output installed packages in requirements format.
packages are listed in a case-insensitive sorted order.

```
Usage:   
  pip3.6 freeze [options]
Description:
  Output installed packages in requirements format.
  packages are listed in a case-insensitive sorted order.

Freeze Options:
  -r, --requirement <file>    Use the order in the given requirements file and
                              its comments when generating output. This option
                              can be used multiple times.
  -f, --find-links <url>      URL for finding packages, which will be added to
                              the output.
  -l, --local                 If in a virtualenv that has global access, do
                              not output globally-installed packages.
  --user                      Only output packages installed in user-site.
  --all                       Do not skip these packages in the output: pip,
                              setuptools, wheel, distribute
  --exclude-editable          Exclude editable package from output.

General Options:
  --isolated                  Run pip in an isolated mode, ignoring
                              environment variables and user configuration.
  -v, --verbose               Give more output. Option is additive, and can be
                              used up to 3 times.
  -q, --quiet                 Give less output. Option is additive, and can be
                              used up to 3 times (corresponding to WARNING,
                              ERROR, and CRITICAL logging levels).
  --log <path>                Path to a verbose appending log.
  --proxy <proxy>             Specify a proxy in the form
                              [user:passwd@]proxy.server:port.
  --retries <retries>         Maximum number of retries each connection should
                              attempt (default 5 times).
  --timeout <sec>             Set the socket timeout (default 15 seconds).
  --exists-action <action>    Default action when a path already exists:
                              (s)witch, (i)gnore, (w)ipe, (b)ackup, (a)bort.
  --trusted-host <hostname>   Mark this host as trusted, even though it does
                              not have valid or any HTTPS.
  --cert <path>               Path to alternate CA bundle.
  --client-cert <path>        Path to SSL client certificate, a single file
                              containing the private key and the certificate
                              in PEM format.
  --cache-dir <dir>           Store the cache data in <dir>.
  --no-cache-dir              Disable the cache.
  --disable-pip-version-check
                              Don't periodically check PyPI to determine
                              whether a new version of pip is available for
                              download. Implied with --no-index.
  --no-color                  Suppress colored output

```

## how to use requirementst.txt?

```
pip install -r requirements.txt
```

## other: pyvenv 

The venv module provides support for creating lightweight “virtual environments” with their own site directories, optionally isolated from system site directories. Each virtual environment has its own Python binary (which matches the version of the binary that was used to create this environment) and can have its own independent set of installed Python packages in its site directories.

```
pyvenv ENV_DIR
```