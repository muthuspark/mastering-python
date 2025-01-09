from setuptools import setup, Extension

module = Extension('mymodule', sources=['add.c'])

setup(
    name='mymodule',
    version='1.0',
    description='A simple C extension',
    ext_modules=[module]
)