from setuptools import setup

setup(
    name='dikicli',
    version='0.0.1',
    packages=['dikicli'],
    zip_safe=False,
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    extras_require={
        'dev': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'diki=dikicli.cli:main',
        ],
    },
)
