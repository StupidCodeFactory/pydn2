import io
import os
import subprocess

from setuptools import setup, Extension, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

def get_pkg_config_flags(package, flag):
    try:
        output = subprocess.check_output(
            ["pkg-config", flag, package], universal_newlines=True
        )
        return output.strip().split()
    except subprocess.CalledProcessError:
        return []


cflags = get_pkg_config_flags("libidn2", "--cflags")
include_dirs = [flag[2:] for flag in cflags if flag.startswith("-I")]

libs = get_pkg_config_flags("libidn2", "--libs")
library_dirs = [flag[2:] for flag in libs if flag.startswith("-L")]
libraries = [flag[2:] for flag in libs if flag.startswith("-l")]

module = Extension(
    "pydn2._pydn2",
    sources=["src/pydn2/pydn2.c"],
    include_dirs=include_dirs,
    library_dirs=library_dirs,
    libraries=[
        "idn2"
    ],
)

setup(
    name="pydn2",
    version="0.0.6",
    description="Python binding for libidn2",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    ext_modules=[module],
)
