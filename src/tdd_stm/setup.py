from setuptools import setup, find_packages

setup(
    name='TDD_STM',
    extras_required=dict(tests=['pytest']),
    packages=find_packages(where='src'),
    package_dir={"": "src"},
)