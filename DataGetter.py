import os,DataImporter
import matplotlib.pyplot as plt

class Importer:
  path = ""

  def __init__(self):
        self.path = DataImporter.getpath()
  
  def getpath(self):
      return self.path

  def getRealTrain(self):
    path = os.path.join(self.path, "train", "real")
    return self.loadImagesFromPath(path)

  def getFakeTrain(self):
    path = os.path.join(self.path, "train", "fake")
    return self.loadImagesFromPath(path)

  def getFakeTest(self):
    path = os.path.join(self.path, "test", "fake")
    return self.loadImagesFromPath(path)

  def getRealTest(self):
    path = os.path.join(self.path, "test", "real")
    return self.loadImagesFromPath(path)

  def loadImagesFromPath(self, path):
    image_list = []
    i = 0
    for f in os.listdir(path):
      if(i < 5000):
        im=plt.imread(os.path.join(path,f))
        pixels = im.reshape( im.shape[0], im.shape[1], im.shape[2] )
        image_list.append(pixels)
      i = i + 1
    return image_list