from setuptools import Extension
from setuptools import setup

from Cython.Build import cythonize

extensions = [
    Extension(
        'encoder',
        sources=[
            't9.pyx'
        ],
        language='c++',
        include_dirs=['.'],
        extra_compile_args=['-std=c++11'],
    ),
]

setup(
    ext_modules=cythonize(extensions),
)
