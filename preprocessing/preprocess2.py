import numpy as np
import os

filenames = np.load("QINGBMImagePaths.npy")
protocol_names = np.load("QINGBMProtocolName.npy")


unique, index= np.unique(protocol_names, return_inverse = True)


filenames_flair = filenames[index == 4]
Y = np.array(["flair"] * np.size(filenames_flair))

filenames_t1_post = filenames[index==7]
to_append = ["t1ce"] * np.size(filenames_t1_post)
Y = np.append(Y, to_append)

filenames_t1_pre = filenames[index == 9]
to_append = ["t1"]*np.size(filenames_t1_pre)
Y = np.append(Y, to_append)

filenames_t2 = filenames[index == 26]
to_append = ["t2"]*np.size(filenames_t2)
Y = np.append(Y, to_append)

X = filenames_flair
X = np.append(X, filenames_t1_post)
X = np.append(X, filenames_t1_pre)
X = np.append(X, filenames_t2)

print(X.shape)
print(Y.shape)
#exit()
counter = 0
for (x, y) in zip(X, Y):
    print(counter)
    counter += 1
    curr_path = "./" + x
    dest_path = "../../test/" + y
    command = "cp " + curr_path + " " + dest_path
    os.system(command)

