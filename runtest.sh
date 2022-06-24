#!/bin/bash
python -m pytest -v --cov --cov-config=cov.conf --cov-branch --cov-report term-missing
