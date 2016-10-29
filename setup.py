
from setuptools import setup, find_packages

from pynverse import __version__ as version

setup(
    name='pynverse',
    packages=find_packages(),
    version=version,
    description='A library for calculating the numerical inverse of a function',
    author='Alvaro Sanchez-Gonzalez',
    author_email='sanchezgnzlz.alvaro@gmail.com',
    url='https://github.com/alvarosg/pynverse',
    download_url='https://github.com/alvarosg/pynverse/tarball/' + version,
    keywords=['inverse', 'function', 'numerical'],
    license='MIT',
    classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Build Tools',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
    ],
    test_suite='nose.collector',
    install_requires=['scipy>=0.11', 'numpy>=1.6'],
    setup_requires=['nose>=1.0'],
    tests_require=['nose>=1.0'],
)