# Najara.py - Serverless 5e Item Management
[![Python Version](https://img.shields.io/github/pipenv/locked/python-version/greynewell/Najara.py)](https://www.python.org/downloads/release/python-370/)
[![Chalice Version](https://img.shields.io/github/pipenv/locked/dependency-version/greynewell/Najara.py/chalice)](https://github.com/aws/chalice)
[![GitHub License](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/greynewell/Najara.py/blob/master/LICENSE)
[![Build Status](https://travis-ci.com/greynewell/Najara.py.svg?branch=master)](https://travis-ci.com/github/greynewell/Najara.py)
[![Codecov Test Coverage](https://codecov.io/gh/greynewell/Najara.py/branch/master/graphs/badge.svg?style=flat)](https://codecov.io/gh/greynewell/Najara.py)
[![Last Commit](https://img.shields.io/github/last-commit/greynewell/Najara.py/master)](https://github.com/greynewell/Najara.py/commits/master)




### Introduction
Najara is a serverless Python REST API for managing Dungeons & Dragons fifth edition items. Najara was created using the Chalice framework and primarily depends on the Lambda and DynamoDB AWS services.

## Getting Started
1. Clone this repository
1. Install [pipenv](https://pipenv-fork.readthedocs.io/en/latest/install.html)
1. Install dependencies `pipenv install`
1. Enter the virtualenv `pipenv shell`
1. Run the tests `pipenv run test`
1. Run the API locally `chalice local`

Now you can call the API locally with [curl](https://curl.haxx.se/), [postman](https://www.postman.com/), or similar.

## Useful Links
- Information on routes, http methods, and formatting: [API Docs on GitHub Pages](https://greynewell.github.io/Najara.py/)

## Development Goals
- Najara conforms to an [OpenAPI Spec](https://swagger.io/specification/)
- Najara preserves 100% test coverage
- Najara has never had a "broken build"
- Najara is easy to setup and use with helpful instructions
- Najara is highly performant and scalable proven by repeatable benchmarks

### Installing Packages
In order to add a package to the environment:
- Install the package with pipenv `pipenv install packagename`
- Update the lock `pipenv lock`
- Update the requirements.txt `pipenv lock -r > requirements.txt`

