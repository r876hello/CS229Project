from fastai import *
from fastai.vision import *


tfms=get_transforms(flip_vert=True)
data = ImageList.from_folder("../CleanedData").split_by_folder().label_from_folder().transform(tfms).databunch(bs=128)
print("There are", len(data.train_ds), "training images and", len(data.valid_ds), "validation images.")
learner = cnn_learner(data, models.resnet18, metrics=[accuracy], pretrained=True,  model_dir = "/tmp/model")
learner.fit_one_cycle(40)
learner.save("rnet18flipped40")
