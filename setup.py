# setup.py
from setuptools import setup, Extension

module = Extension(
    "pydn2",                  # Module name
    sources=["pydn2.c"],  # Source file(s)
    libraries=["idn2"],         # Link against libidn2 (make sure it's installed on your system)
)

setup(
    name="pydn2",
    version="0.1.0",
    description="Python binding for libidn2",
    ext_modules=[module],
)
