#!/bin/bash
cd enigma_sim/test
nosetests *_test.py --with-coverage --cover-erase
