# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 22:14:04 2016

@author: maik
"""

import argparse

parser = argparse.ArgumentParser(description='Abinoten')
parser.add_argument('file', metavar='file.csv', type=str, nargs=1, help='csv file with semester grades')
parser.add_argument('grades', metavar='grade', type=int, nargs='+', help='five exam grades', choices=range(0,16))

args = parser.parse_args()