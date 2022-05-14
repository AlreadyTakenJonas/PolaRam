#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 14 13:36:23 2022

@author: jonas
"""

# Run all tests in this directory
def main():
    import unittest
    loader = unittest.TestLoader()
    tests = loader.discover('.')
    testRunner = unittest.runner.TextTestRunner()
    testRunner.run(tests)
    
if __name__ == "__main__":
    main()