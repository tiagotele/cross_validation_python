#!/usr/bin/env python
# encoding:utf8

import csv


def load_csv(file_name, training_data):
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        for r in reader:
            if len(r) == 0:
                continue
            training_data.append(r)
    f.close()


ratio = 10
data_set = []
load_csv("small_test.csv", data_set)

cont_ratio = 0
increase_rate = int(((ratio) / 100) * len(data_set))

start_index = cont_ratio
end_index = increase_rate

# while cont_ratio < len(data_set) - 1:
while cont_ratio < len(data_set) - 1:
    print("Start index = ", start_index, " end index = ", end_index)
    # print(data_set[cont_ratio:cont_ratio + increase_rate])

    training_data = []
    for element_index in range(len(data_set)):
        if element_index < start_index or end_index < element_index:
            training_data.append(data_set[element_index])


    test_data = data_set[start_index:end_index + 1]

    print(len(training_data))
    print(len(test_data))

    print(test_data)
    print(training_data)

    start_index += increase_rate
    end_index += increase_rate
    cont_ratio += increase_rate
