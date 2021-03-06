from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='limitpages',
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    license='Apache 2.0 License',
    url='https://papermerge.com/',
    description=("Papermerge App to limit number of uploaded documents"),
    long_description=long_description,
    author='Eugen Ciur',
    author_email='eugen@papermerge.com',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
