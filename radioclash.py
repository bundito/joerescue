#!/usr/bin/python3

import multiprocessing

bind = "0.0.0.0:6543"
workers = multiprocessing.cpu_count() * 2 + 1

import my_app