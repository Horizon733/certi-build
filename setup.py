import pathlib
from io import open
from os import path

from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# automatically captured required modules for install_requires in requirements.txt and as well as configure
# dependency links
with open(path.join(HERE, 'requirements.txt'), encoding='utf-8') as file:
    all_reqs = file.read().split('\n')

install_requires = [package.strip() for package in all_reqs
                    if ('git+' not in package) and
                    not package.startswith("#") and
                    (not package.startswith('-'))]
dependency_links = [package.strip().replace('git+', '') for package in all_reqs if 'git+' not in package]

setup(
    name='certi_builder',
    description='A simple commandline app for generating bulk of certificates',
    version='1.0.0',
    packages=find_packages(),  # list of all packages
    install_requires=install_requires,
    python_requires='>=3.7',  # any python greater than 3.0
    entry_points='''
        [console_scripts]
        certi-builder=certi_builder.__main__:main
    ''',
    author="Dishant Gandhi",
    keyword="certificate generator, certificates, python certificates, certi builder",
    long_description=README,
    long_description_content_type="text/markdown",
    license='MIT',
    url='https://github.com/Horizon733/certi-build',
    download_url='https://github.com/Horizon733/certi-build/archive/refs/tags/v1.0.tar.gz',
    dependency_links=dependency_links,
    author_email='dishantgandhi733@gmail.com',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ]
)
