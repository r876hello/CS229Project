from fastai import *
from fastai.vision import *
import matplotlib.pyplot as plt

data = ImageList.from_folder("../CleanedData").split_by_folder().label_from_folder().databunch(bs=64)
print("There are", len(data.train_ds), " training images and", len(data.valid_ds), "test images")

print(data.classes)





learner = cnn_learner(data, models.resnet34, metrics=[accuracy], pretrained=True, model_dir = "/tmp/model")


learner.load("rnet34flipped40")

preds, target, losses = learner.get_preds(data.train_ds, with_loss=True)
print(accuracy(preds, target))
interp = ClassificationInterpretation(learner, preds, target, losses)
print(interp.confusion_matrix())
interp.plot_top_losses(16, heatmap=False, figsize = (15, 11), heatmap_thresh = 4)
plt.savefig("TEMP2.png")
#preds, target = learner.get_preds(data.valid_ds)
#print(accuracy(preds, target))
