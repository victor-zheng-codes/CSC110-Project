"""CSC110 Fall 2021 Final Project Main Program

Instructions (READ THIS FIRST!)
===============================
Run this file to run the program


Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students, TA, and professors
within the CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited.

This file is Copyright (c) 2021 Daniel Xu, Nicole Leung, Kirsten Sutantyo, and Victor Zheng.
"""

if __name__ == '__main__':
    import filter
    from visual import Visual
    # filter.filter_covid()
    filter.filter_employment_data()
    program = Visual()
    program.start_menu()
