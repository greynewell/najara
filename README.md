# Najara.py - Serverless 5e Item Management API
[![Python Version](https://img.shields.io/github/pipenv/locked/python-version/greynewell/Najara.py)](https://www.python.org/downloads/release/python-370/)
[![GitHub License](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/greynewell/Najara.py/blob/master/LICENSE)
[![Build Status](https://travis-ci.com/greynewell/Najara.py.svg?branch=master)](https://travis-ci.com/github/greynewell/Najara.py)
[![Codecov Test Coverage](https://codecov.io/gh/greynewell/Najara.py/branch/master/graphs/badge.svg?style=flat)](https://codecov.io/gh/greynewell/Najara.py)
[![Last Commit](https://img.shields.io/github/last-commit/greynewell/Najara.py/master)](https://github.com/greynewell/Najara.py/commits/master)




### Introduction
Najara is a serverless Python/Flask REST API for managing Dungeons & Dragons fifth edition items. Najara was created using the AWS Serverless Application Model framework and primarily depends on the Lambda and DynamoDB AWS services.

## Getting Started
1. Clone this repository & [install pipenv](https://pipenv-fork.readthedocs.io/en/latest/install.html)
1. Install packages & run virtualenv `pipenv install && pipenv shell`
1. Test Najara `pipenv run test`
1. Run the Najara locally `chalice local`

## Useful Links
- Information on routes, http methods, and formatting: [API Docs on GitHub Pages](https://greynewell.github.io/Najara.py/)

## Development Goals
Najara was initially created by writing an [OpenAPI Spec](https://swagger.io/specification/). This design spec was used to generate initial documentation and to structure the project. Development progresses from this point in a test-driven and iterative manner. The biggest goal of this project is to maintain 100% test coverage.

### Installing Packages
In order to add a package to the environment:
- Install the package with pipenv `pipenv install packagename`
- Update the lock `pipenv lock`
- Update the requirements.txt `pipenv lock -r > requirements.txt`

