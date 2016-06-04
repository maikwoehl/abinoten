#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 02:14:10 2016

@author: maik
"""

import sys

import csv
import argparse

ALEVEL_FACTOR = 2
EXAM_FACTOR = 4
POINTS_MULTIPLIER = 40
POINTS_DIVIDER = 48

def read_semester_grades(grades):
    """ Reads the semester grades from the given file """
    reader = csv.reader(grades, delimiter=';')
    if sum(1 for line in grades) is not 4:
        raise IndexError("The *.csv-file doesn't have the expected "
                         "four lines of semester grades.")
    grades.seek(0)
    
    points = 0
    for semester in reader:
        if len(semester) is not 9:
            raise IndexError("One of the semesters doesn't have the "
                             "expected nine grades.\nLength: {} => {}"
                             .format(len(semester), semester))
        
        for index, grade in enumerate(semester):
            try:
                int(grade)
            except ValueError as error:
                raise ValueError("One of the grades isn't a number. "
                                 "Please correct that.") from error
            
            if not 0 <= int(grade) <= 15:
                raise ValueError("Your grades should be between 0 and 15.")
            
            if index <= 2:
                # First three are the a-level courses
                points += int(grade) * ALEVEL_FACTOR
            else:
                points += int(grade)
                    
    return points

def read_exam_grades(grades):
    """ Reads the exam grades from the argument list """
    for grade in grades:
        if not 0 <= int(grade) <= 15:
            raise ValueError("Your grades should be between 0 and 15.")
        
    return sum(map(int, grades))
    
def calculate_average_grade(points):
    """ Calculates the average grade """
    return 17/3 - points/180

def main():
    parser = argparse.ArgumentParser(description='Calculates the average grade'
                                                 ' of your A-levels.')
    parser.add_argument('file', metavar='grades.csv', 
                        type=argparse.FileType('r'), nargs=1,
                        help='csv file with semester grades')
    parser.add_argument('grades', metavar='grade', type=int, nargs=5, 
                        help='five exam grades', choices=range(0,16))
    if len(sys.argv) is 1:
        parser.print_help()
        sys.exit(0)
    args = parser.parse_args()

    points_block1 = read_semester_grades(args.file)
    points_block1 *= POINTS_MULTIPLIER
    points_block1 = round(points_block1 / POINTS_DIVIDER, 0)
    
    points_block2 = read_exam_grades(args.grades) * EXAM_FACTOR
    points_sum = points_block1 + points_block2
    average_grade = calculate_average_grade(points_sum)

    print(30 * '=')
    print('Points in Block 1: {}'.format(int(points_block1)))
    print('Points in Block 2: {}'.format(points_block2))
    print('Sum (Block1 + Block2): {}'.format(int(points_sum)))
    print(30 * '=')
    print('Average grade: {}'.format(round(average_grade, 2)))

if __name__ == "__main__":
    try:
        main()
    except (ValueError, IndexError) as error:
        print(error)
        sys.exit(0)
        