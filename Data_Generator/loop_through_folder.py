import cv2
import os
from helmet import create_helmet


folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'without_helmet')
#dist_path = "/home/preeth/Downloads"

#c = 0
images = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
for i in range(len(images)):
    #print("the path of the image is", images[i])
    #image = cv2.imread(images[i])
    #c = c + 1
    create_helmet(images[i])



