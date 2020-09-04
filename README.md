# Najara - Serverless 5e Item Management
[![Python Version](https://img.shields.io/github/pipenv/locked/python-version/greynewell/najara)](https://www.python.org/downloads/release/python-370/) 
[![Chalice](https://img.shields.io/github/pipenv/locked/dependency-version/greynewell/najara/chalice/development)](https://github.com/aws/chalice)
[![GitHub License](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/greynewell/najara/blob/master/LICENSE) 
[![Build Status](https://travis-ci.com/greynewell/najara.svg?branch=development)](https://travis-ci.com/github/greynewell/najara) 
[![codecov](https://codecov.io/gh/greynewell/najara/branch/development/graph/badge.svg)](https://codecov.io/gh/greynewell/najara)




### Introduction
Najara is a serverless Python REST API for managing Dungeons & Dragons fifth edition items. Najara was created using the Chalice framework and primarily depends on the Lambda and DynamoDB AWS services.

## Getting Started
1. Clone this repository & get [pipenv](https://pipenv-fork.readthedocs.io/en/latest/install.html)
1. Install dependencies `pipenv install`
1. Enter the virtualenv `pipenv shell`
1. Run the tests `pipenv run test`
1. Run the API locally `pipenv run start`

Now you can call the API locally with [curl](https://curl.haxx.se/), [postman](https://www.postman.com/), or similar.

## Useful Links
- Information on routes, http methods, and formatting: [API Docs on GitHub Pages](https://greynewell.github.io/najara/)

## Development
Najara was initially written as an [OpenAPI Spec](https://swagger.io/specification/). The Chalice micro-framework was selected due to its testability and devleopment experience. Najara is built using [Test Driven Development](https://www.agilealliance.org/glossary/tdd/) and is designed to be inexpensive to develop, operate and maintain.

### Goals
- Najara preserves 100% test coverage
- Najara has never had a "broken build"
- Najara is quick and easy to setup
- Najara is scalable and highly performant

### Installing Packages
In order to add a package to the environment:
- Install the package with pipenv `pipenv install packagename`
- Update the lock `pipenv lock`

