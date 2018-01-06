from setuptools import setup, find_packages

setup(
    name='card_identifier',
    version='1.0',
    author='Adel Qalieh',
    author_email='aqalieh95@gmail.com',
    license='MIT',
    packages=find_packages(exclude=["tests", "tests.*"])
)
