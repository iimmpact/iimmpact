# coding: utf-8

"""
    IIMMPACT API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2020-09-14T13:01:14Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "iimmpact"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]
    

setup(
    name="iimmpact",
    version="1.0.0",
    description="IIMMPACT API",
    author_email="alex@iimmpact.com",
    author="Alex Tan",
    url="https://github.com/iimmpact/iimmpact",
    keywords=["Swagger", "IIMMPACT API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    long_description="""\
    """,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
