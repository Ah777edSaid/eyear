# setup.py

from setuptools import setup

setup(
    name="eyEar",  
    version="0.1",  
    py_modules=["my_script"],  
    install_requires=[], 
    entry_points={
        "console_scripts": [
            "my-python-project=my_script:hello_world",
        ],
    },
)
