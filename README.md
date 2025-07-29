# GPA Tracker

A Python program to manage student grades, calculate GPA, and display academic performance using statistical grading.

## Overview

This project allows users to:

- Add and delete students
- Input marks for 5 subjects: CS 101, MT 101, PHY 101, CH 101, and HM 101
- Automatically compute letter grades and GPA using z-score based normalization
- Display all student records or only students meeting a GPA threshold (Dean's Honor List)
- Generate dummy data for testing purposes

## Features

- **Robust input validation** for roll numbers and marks
- **Statistical grading system** using mean and standard deviation (z-scores)
- Grades range from A (highest) to F (fail) based on relative performance
- Supports up to 50 students and 5 subjects
- Interactive command-line menu interface

## Usage

1. Clone or download the repository.
2. Run the program using Python 3:

   ```bash
   python gradebook.py
