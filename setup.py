from setuptools import Extension
from setuptools import setup

extensions = [
    Extension(
        'encoder',
        sources=[
            't9.py'
        ],
        language='Python',
        include_dirs=['.'],
        extra_compile_args=[],
    ),
]

setup(
    ext_modules=extensions
)
