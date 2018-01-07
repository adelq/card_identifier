from setuptools import setup, find_packages

setup(
    name='card_identifier',
    description='Python library for credit/debit card identification and'
                'utilities',
    long_description='Card Identifier takes out the busy work from simple card'
    'operations. This includes validation, formatting, and identification.',
    url='https://github.com/adelq/card_identifier',
    version='1.0',
    author='Adel Qalieh',
    author_email='aqalieh95@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['tests*']),
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='credit card cc bin creditcard'
)
