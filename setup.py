from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='btree_test',
    ext_modules=cythonize("benchmark_try1_c.pyx"),
)
