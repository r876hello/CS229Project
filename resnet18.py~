from fastai import *
from fastai.vision import *

data = ImageList.from_folder("../CleanedData").split_by_folder().label_from_folder().databunch(bs=128)
print("There are", len(data.train_ds), "training images and", len(data.valid_ds), "validation images.")
learner = cnn_learner(data, models.resnet18, metrics=[accuracy], pretrained=True,  model_dir = "/tmp/model")
#print(learner.loss_func)
#print(learner.opt_func)
learner.fit_one_cycle(4)
learner.save("TEST")
#LOAD
#learnLoad = cnn_learner...
#learnLoad.load("TEST")
