"""
Unit test for testing fix for markdown message
"""
import unittest
from unittest.mock import patch
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from pto_detector.pto_detector import clean_message


def test_cleaned_message():

    cleaned_message = clean_message("<I am on PTO today>take care")
    assert cleaned_message == ''