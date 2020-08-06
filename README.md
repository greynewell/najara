# Najara.py
[![Python Version](https://img.shields.io/github/pipenv/locked/python-version/greynewell/Najara.py)](https://www.python.org/downloads/release/python-370/)
[![GitHub License](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/greynewell/Najara.py/blob/master/LICENSE)
[![Build Status](https://travis-ci.com/greynewell/Najara.py.svg?branch=master)](https://travis-ci.com/github/greynewell/Najara.py)
[![Last Commit](https://img.shields.io/github/last-commit/greynewell/Najara.py/master)](https://github.com/greynewell/Najara.py/commits/master)




### Introduction
Najara is a serverless Python/Flask REST API for managing Dungeons & Dragons fifth edition items. Najara was created using the AWS Serverless Application Model framework and primarily depends on the Lambda and DynamoDB AWS services.

## Getting Started
1. Install Python 3.7 (or just use [pyenv](https://realpython.com/intro-to-pyenv/)) and clone this repo.
1. Install dependencies `pip3 install pytest pytest-mock --user`
1. Run the tests `python3 -m pytest tests/ -v`
1. Run the API locally `sam local start-api`

Refer to the API Docs for more information on routes, http methods, inputs and outputs.

## Useful Links
- [API Docs on GitHub Pages](https://greynewell.github.io/Najara.py/)

## Development
Najara was initially created by writing an [OpenAPI Spec](https://swagger.io/specification/). This spec was used to generate initial documentation as well as the scaffolding and structure of the code. Development progresses from this point in a test-driven and iterative manner.
