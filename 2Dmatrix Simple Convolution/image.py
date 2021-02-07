from PIL import Image
import numpy as np


class Img:
    def __init__(self, img_link):
        self.image = Image.open(img_link)

    def fill_image(self):
        height, width = self.image.size
        data = [[None for _ in range(width)] for _ in range(height)]
        px = self.image.load()
        for i in range(height):
            for j in range(width):
                data[i][j] = 0 if px[j, i][0] > 120 else 1
        return np.array(data)


# img = Img('firstTest.jpg')
# img_ = img.fill_image()
# print(img_)
# img_ = img.mirror_array(img_)
# print(img_)

# path = '/Users/ruslanakhtariev/PycharmProjects/convo_from_scratch/firstTest.jpg'
# # image = Image.open(path)
# #
# # x, y = image.size
# # px = image.load()
# # for i in range(x):
# #     for j in range(y):
# #         print(px[i, j][0], sep='-')
# #     print('\n')
# #
# # print(px[1, 0])
# # print(x, y)
# # print(px)
# image = Img(path)
# matrix = image.fill_image()
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         print(matrix[i][j], end='\t')
#     print('\n')

