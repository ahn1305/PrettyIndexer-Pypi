from setuptools import setup

with open("README.md","r") as fh:
	long_description = fh.read()

setup (

	name="PrettyIndexer",
	version='0.0.1',
	description="Get positive and negative index values of a string displayed in a beautiful manner.",
	py_modules=["stringindexer"],
	package_dir={'':'src'},
	long_description=long_description,
	long_description_content_type = "text/markdown",

	classifiers=[
    'Programming Language :: Python :: 3.6',      
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'License :: OSI Approved :: MIT License',  
    'Opera ting System :: OS Independent',
  ],

)

install_requires = [
	'prettytable==2.1.0',
	'printtools==1.2',
]
