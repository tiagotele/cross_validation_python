#!/usr/bin/env python
# encoding:utf8

# GENERIC WAY TO SPLIT A DATABASE TO DO CROSS VALIDATION

import csv


# Loads a csv file
def load_csv(file_name, database):
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        for r in reader:
            if len(r) == 0:
                continue
            database.append(r)
    f.close()


# Ratio percentage of how do you want split your dataset
ratio_percentage = 10

# Data set with your CSV file
data_set = []

# Load data set using load_csv function
load_csv("small_test.csv", data_set)

# Calculates the sub array size for split the full dataset.
increase_rate = int(((ratio_percentage) / 100) * len(data_set))

# Internal variable to increat
cont_ratio = 0

# start_index for each test_data sub array
start_index = cont_ratio

# end index for each test data sub array
end_index = increase_rate

# Increases cont_ratio with increase_rate variable until data_set size
while cont_ratio < len(data_set) - 1:
    # Debug information
    print("Start index = ", start_index, " end index = ", end_index)

    training_data = []
    for element_index in range(len(data_set)):
        if element_index < start_index or end_index < element_index:
            training_data.append(data_set[element_index])

    test_data = data_set[start_index:end_index + 1]

    start_index += increase_rate
    end_index += increase_rate
    cont_ratio += increase_rate

    print(test_data)
    print(training_data)

    '''DO WHATEVER YOU WANT WITH YOUR TEST DATA AND TRAINING SET AND BE HAPPY!!!'''
