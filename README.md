# Test Automation

[![UI Tests](https://github.com/woofiwaffle/Test-Automation/actions/workflows/config.yml/badge.svg)](https://github.com/woofiwaffle/Test-Automation/actions/workflows/config.yml)
[![codecov](https://codecov.io/github/woofiwaffle/Test-Automation/graph/badge.svg?token=W0GNHDRI0D)](https://codecov.io/github/woofiwaffle/Test-Automation)

<p align="center">
   <img alt="Pytest" src="https://img.shields.io/badge/PyTest-8.3.1-a?style=plastic&logo=pytest&labelColor=black&color=grey">
   <img alt="Selenium" src="https://img.shields.io/badge/Selenium-3.23.1-a?style=plastic&logo=selenium&labelColor=black&color=grey">
   <img alt="DevTools" src="https://img.shields.io/badge/DevTools-2024-a?style=plastic&labelColor=black&color=grey">
   <img alt="Static Badge" src="https://img.shields.io/badge/Docker-4.32-a?style=plastic&logo=docker&labelColor=black&color=gray">
</p>

## Description

The project is designed to automate testing of the OrangeHRM web application. Also allows you to manage tests, run them and create test reports (for pytest)

## Project structure

- `base/` - base classes and common functions for testing
- `config/` - project configuration files
- `features/` - files with descriptions of BDD tests
- `js_tests_for_browser` - js tests for the console in the browser
- `pages/` - Page Objects for web applications
- `received_data/` - data obtained during testing
- `tests/` - test scripts
- `conftest.py` - configuration file for pytest
