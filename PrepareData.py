import os
import numpy as np
import shutil

## need to replace file path for your own

# data from scraping
directory = os.getcwd() + os.sep + "Images"
plane_list = os.listdir(directory)

# created directory for test data
test_directory = '/path/to/TestImages'
os.chdir(test_directory)
for plane in plane_list:
    os.mkdir(plane)

# split data into 80 train 20 test
os.chdir(directory)


# go through each plane file list and put about 20 percent into test directory
for plane in plane_list:
    file_path = os.getcwd() + '/' + plane
    file_list = os.listdir(file_path)

    for f in file_list:
        if np.random.rand(1) < 0.2:
            shutil.move(directory + '/' + plane + '/' + f,
                    test_directory + '/' + plane + '/' + f)

