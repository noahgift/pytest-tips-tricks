[![Python application test with Github Actions](https://github.com/noahgift/pytest-tips-tricks/actions/workflows/testing-ci.yml/badge.svg)](https://github.com/noahgift/pytest-tips-tricks/actions/workflows/testing-ci.yml)
[![AWS](https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoibm1YdHFvMzVaQ0hrQS9oRlFGUVhoVy9wWmNHNmQyMGRkTWwwaE9ocEU5TFRRYXJmQWtwaVc1NkxSbGcrOTBLM0RJN0VFS09jSWFoQWxIQUpGUHdYbFkwPSIsIml2UGFyYW1ldGVyU3BlYyI6IlFXcDJNdWhqV3VYL3M1d2oiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)

# pytest-tips-tricks
A primer on pytest

## Introduction to Testing with pytest

* Why Test?
  * Does anything work?
  * Why PyTest?   
* Setup Cloud Development Environments with Local CI and Compare:  
  * Github Codespaces
  * AWS Cloud9
  * AWS Cloudshell 
* CI Systems with PyTest
  * Github Actions:  https://docs.github.com/actions/automating-builds-and-tests/building-and-testing-nodejs-or-python?langId=py      
  * AWS Code Build
 
##  Invoking pytest

* [Overview of pytest invocation](https://docs.pytest.org/en/6.2.x/usage.html?highlight=pdb)
* Simple version:  `make test` via `python -m pytest -vv test_hello.py`
* Adding Code Coverage:  `pytest-cov` `python -m pytest -vv --cov=hello test_hello.py`
  * [Coverage Invoke Snippit](https://github.com/noahgift/devops-from-zero/blob/main/Makefile#L7)   
* Adding Jupyter Notebook testing: 
  * nbval:  https://github.com/computationalmodelling/nbval
  * [nbval](https://github.com/noahgift/myrepo/blob/master/Makefile#L8-L10)
* Debugging Code with PDB
  * What is PDB and how does it work?
  * Alternative IPDB[https://pypi.org/project/ipdb/]
  * Invoke pytest with `--pdb`:  https://github.com/paiml/testing-in-python/blob/master/chapter6/Makefile#L2
* Stop on fail:
  * `pytest -x`
  * `pytest --maxfail=2`
* Specify Tests:  https://docs.pytest.org/en/6.2.x/usage.html?highlight=pdb#specifying-tests-selecting-tests
  * dir
  * keyword
* Build a report:  https://docs.pytest.org/en/6.2.x/usage.html?highlight=pdb#detailed-summary-report
  
##  Advanced pytest

* Setup and Teardown
* Testing Click CLI
* Testing Flask API
* Testing FastAPI

### References

* To use caching use this option:  https://github.com/actions/cache/blob/main/examples.md#python---pip

### Watch the pytest master class

* [Watch on YouTube](https://youtu.be/IN4qt-9bMiE)
* [Watch on O'Reilly](https://learning.oreilly.com/videos/pytest-master-class/10132021VIDEOPAIML/10132021VIDEOPAIML-c1_s0/)



