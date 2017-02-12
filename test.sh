#!/bin/bash
cd enigma_sim/test
nosetests *_test.py --with-coverage --cover-erase
CODECLIMATE_REPO_TOKEN=a45b642c34e1e12ec2f160b55c7f7dff8ca0affe3406c1ea4b856a6c97f71fc3 codeclimate-test-reporter --file .coverage
