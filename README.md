# Pytest / Selenium / Gherkin Boilerplate

## About

This is a very simplistic boilerplate to get you started with this framework. It has three technologies implemented:

- Selenium Webdriver - Drives the interactions with the browser

- Pytest - Testing framework that allows us to pick and choose which tests to run with ease

- Pytest-bdd - A pytest plugin that allows us to write our tests using gherkin syntax

## Structure

This file structure has several important components:

- Pipfile - pulls in all of our chosen technologies. Essentially a package.json

- pytest.ini - A configuration file for pytest. It currently only contains tracked markers for use in our tests

- pages folder - A package containing all of our page objects. Each page object extends from a base page class with a handful of simple pre-built functions. Each page object is then imported into the **init** file for ease of access.

- elements folder - A package containing a class that corresponds with each page object. Each class contains a series of functions that return webelements that are used in each page object. This separates concerns and makes it easier to update tests when breaking changes occur to the codebase.

- Tests folder - contains a test steps folder and features folder

  - Features - Each feature/page/function test is stored within a file in this folder. Here we can use gherkin to it's full power. It's incredibly readable, iterable, and a great file to hand off to clients with less testing knowledge.

  - Steps - Each steps file contains the functions associated with the given, when, then statements in the feature files. Functions that are used in more than one feature file can be added in conftest.py

## Terminal Commands

- Before doing anything else, run `pipenv shell` to enter the virtual python environment for this package. Also `pipenv install` will install all required dependencies.

- `python -m pytest` will run all tests contained in the features file.

- `python -m pytest -m {marker}` will run tests that correspond with the given marker. Try running it with the 'sample' marker to see how it works.

- `python -m pytest -n {x}` will run the tests x at a time. You will need more tests in the suite for it to be of any use.

## Getting Started

1. I usually start by creating a new page object that extends the BasePage. Look at the SamplePage object to see how to set it up. I then define every page interaction I feel will be necessary for the tests we plan to implement.

2. After that, build an element object for that page and move all of your webelement selectors to this class. Look at the SamplePageElements class for examples.

3. With fully functional page and element classes, we need to write our first test in gherkin. Create a new feature file and follow the example in sample.feature for some basic gherkin syntax. Should you decide to add a marker, just type `@{marker}` before a chosen scenario or feature. Then go into the _pytest.ini_ file and add it on the next line underneath `markers =`

4. Create a new file in the 'steps' folder. This file needs to begin with 'test\_'. Make sure to add `scenarios({path to feature file})` before doing anything else. Now you can copy and paste your gherkin statements into `@given`, `@when`, and `@then` functions. The given statement will require a target_fixture attribute that directs it to the function below. Assertions can be placed in any function, but are of most use in the then function.

5. Continue building on this boilerplate. This is a very powerful setup, and I've only covered the bare basics in this repo.
