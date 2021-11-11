
#global Constants
WIDTH, HEIGHT, LAYERS =  1280, 720, 3
SIZE = (WIDTH, HEIGHT)
FPS = 25
DTYPE = 'uint8'

IMAGE_FRAMES = 15
BLACK_FRAME = 7
BLACK_FRAME_FOR_SAME_LETTERS = 1

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
 
# img = np.zeros((WIDTH, HEIGHT, LAYERS),dtype=np.uint8)
# # for i in range(img.shape[1]):
# #     for j in range(img.shape[0]):
# #         img[j,i]=0

# cv2.imwrite('black.jpg', img)
# # cv2.imshow('a',img)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()