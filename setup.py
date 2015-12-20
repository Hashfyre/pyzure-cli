from setuptools import setup

setup(
    name='pyzure-cli',
    version='0.0',
    description=(
        'A CLI tool for Microsoft Azure Storage',
        'and Service Bus operations, built on Azure'
    )
    url='http://github.com/hashfyre/pyzure-cli',
    author='Joy Bhattacherjee',
    author_email='joy.bhattacherjee@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: System Administrators',
        'Topic :: System :: Systems Administration',
        'License :: OSI Approved :: MIT License'
    ],
    packages=['pyzure-cli'],
    keywords='cli azure',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'pyzure=pyzure:main',
        ],
    }
)
