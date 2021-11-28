import os,DataImporter
from PIL import Image

class Importer:
  path = ""

  def __init__(self):
        self.path = DataImporter.getpath()
  
  def getpath(self):
      return self.path

  def getRealTrain(self):
    path = os.path.join(self.path, "train", "real")
    image_list = []
    for f in os.listdir(path):
      im=Image.open(os.path.join(path,f))
      image_list.append(im)
      #im.close()
    return image_list

  def getFakeTrain(self):
    path = os.path.join(self.path, "train", "fake")
    image_list = []
    for f in os.listdir(path):
      im=Image.open(os.path.join(path,f))
      image_list.append(im)
      #im.close()
    return image_list

  def getFakeTest(self):
    path = os.path.join(self.path, "test", "fake")
    image_list = []
    for f in os.listdir(path):
      im=Image.open(os.path.join(path,f))
      image_list.append(im)
      im.close()
    return image_list

  def getRealTrain(self):
    path = os.path.join(self.path, "test", "real")
    image_list = []
    for f in os.listdir(path):
      im=Image.open(os.path.join(path,f))
      image_list.append(im)
      im.close()
    return image_list