import os
import inspect
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    setupdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    return open(os.path.join(setupdir, fname)).read()

install_requires = [
        "numpy",
        "scipy",
        "coveralls",
        "pyNastran",
        "setuptools-git-version",
        ]

if os.environ.get('TRAVIS') == 'true':
    install_requires.pop(install_requires.index("pyNastran"))

CLASSIFIERS = """\

Development Status :: 3 - Alpha
Intended Audience :: Science/Research
Intended Audience :: Developers
Intended Audience :: Education
Topic :: Scientific/Engineering :: Mathematics
License :: OSI Approved :: BSD License
Operating System :: Microsoft :: Windows
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3.5
Operating System :: Unix

"""

is_release = False
if is_release:
    version_format = '{tag}'
else:
    version_format = '{tag}.dev{commitcount}+{gitsha}'

data_files = [('', [
        'README.md',
        'LICENSE',
        ])]

s = setup(
    name = "meshless",
    version_format = version_format,
    author = "Saullo G. P. Castro",
    author_email = "castrosaullo@gmail.com",
    description = ("Meshless Methods for Computational Mechanics"),
    license = "BSD",
    keywords = "es-pim finite element partial diferential equations",
    url = "https://github.com/compmech/meshless",
    packages=find_packages(),
    data_files=data_files,
    long_description=read('README.md'),
    classifiers=[_f for _f in CLASSIFIERS.split('\n') if _f],
    install_requires=install_requires,
)

with open("./meshless/version.py", "wb") as f:
    f.write(b"__version__ = %s\n" % s.get_version().encode())

