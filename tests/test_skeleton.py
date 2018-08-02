#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from showtime.skeleton import fib

__author__ = "Donovan T. Le"
__copyright__ = "Donovan T. Le"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)


def test_why_dont_you_do_more_work():
    assert False