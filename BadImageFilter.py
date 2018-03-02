import os

train_directory = os.getcwd() + os.sep + "SmallDataSubset" + os.sep + "TrainImages"
test_directory = os.getcwd() + os.sep + "DataSubset" +  os.sep + "TestImages"
plane_list_train = os.listdir(train_directory)
plane_list_test = os.listdir(test_directory)

for plane in plane_list_train:
    file_path = train_directory + os.sep + plane
    file_list = os.listdir(file_path)
    for f in file_list:
        f_path = file_path + os.sep + f
        size = os.path.getsize(f_path)
        if size < 300:
            # Corrupt file, delete this
            os.remove(f_path)
            print(f_path)

for plane in plane_list_test:
    file_path = test_directory + os.sep + plane
    file_list = os.listdir(file_path)
    for f in file_list:
        f_path = file_path + os.sep + f
        size = os.path.getsize(f_path)
        if size < 300:
            # Corrupt file, delete this
            os.remove(f_path)
            print(f_path)