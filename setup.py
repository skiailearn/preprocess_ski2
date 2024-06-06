import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
	name = 'preprocess_ski2', #this should be unique
	version = '0.0.1',
	author = 'Santhosh I',
	author_email = 'skiailearn@gmail.com',
	description = 'This is preprocessing package',
	long_description = long_description,
	long_description_content_type = 'text/markdwon',
	packages = setuptools.find_packages(),
	classifiers = [
	'Programming Language :: Python :: 3', 
	'License :: OSI Approved :: MIT License'
	"Operating System :: OS Independent"],
	python_requires = '>=3.5'

	)
