import pydicom as dicom
from pathlib import Path
import matplotlib.pylab as plt
import numpy as np


result = list(Path(".").rglob("*.dcm"))
protocolName = []
imagePaths = []
for (index, i) in enumerate(result):
    counter = (index/len(result))
    print(counter)
    ds = dicom.read_file(i)
    protocolName.append(ds.ProtocolName) ##SAVE THIS
    filename = "QINGBM_" + str(index) + ".png"
    plt.imshow(ds.pixel_array, cmap=plt.cm.binary_r)
    plt.axis('off')
    plt.savefig(filename, bbox_inches='tight')
    plt.close()
    imagePaths.append(filename)
np.save("QINGBMImagePaths", np.array(imagePaths))
np.save("QINGBMProtocolName", np.array(protocolName))
