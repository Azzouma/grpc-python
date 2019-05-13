from distutils.core import setup
from setuptools import find_packages

requires = [
    'six>=1.10.0',
]

if __name__ == "__main__":
    setup(
        name="email-grpc",
        version="0.0.1",
        packages=find_packages(),
        author='devops_team',
        author_email='devopsac@email.com',
        install_requires=requires,
        include_package_data=True,
    )

# python setup.py install