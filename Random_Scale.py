import cv2
import random
import numpy
from PIL import Image 

class randomScale(object):
  def __init__(self, dist):
    self.dist = dist
    

  def __call__(self, img):
    if random.randrange(0,2) == 0:
      return img
    self.d = random.randrange(0,2)
    img = numpy.array(img)
    img_dtype = img.dtype
    h, w, _ = img.shape
    x = w if self.d == 0 else h 

    n = int(x / self.dist) - 1 # number of lines
    lines = [i * self.dist for i in range(n + 2)] # initial idx of each line
    
    for i in range(1, len(lines) - 1):
        s, m, e = lines[i - 1], lines[i], lines[i + 1] # start, middle, end Lines
        plusminus = random.randrange(0,2) # 0 = plus, 1 = minus
        scale_range = random.randrange(int(self.dist / 4),int(self.dist / 2) + 1) # number of pixels for scaling
        scale_range *= 1 if plusminus == 0 else -1

        # scaling 
        firstB = cv2.resize(img[0:h, s:m], (m - s + scale_range, h)) if self.d == 0 else cv2.resize(img[s:m, 0:w], (w, m - s + scale_range))
        secondB = cv2.resize(img[0:h, m:e], (e - m - scale_range, h)) if self.d == 0 else cv2.resize(img[m:e, 0:w], (w, e - m - scale_range))

        # applying scaled part to original img
        if self.d == 0:
            temp = cv2.hconcat([firstB,secondB])
            img[0:h, s:e] = temp
        else:
            temp = cv2.vconcat([firstB,secondB])
            img[s:e, 0:w] = temp
    
    img = img.astype(img_dtype)
    return Image.fromarray(img)

  def __repr__(self):
    return self.__class__.__name__+'()'
    
    
