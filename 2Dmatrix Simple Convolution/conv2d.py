import kernel
import image
import numpy as np


class Conv2D(kernel.Kernel3x3, image.Img):
    def __init__(self, img_path):
        super(Conv2D, self).__init__()
        self.kernel = kernel.Kernel3x3().fill_matrix(mode='HORIZONTAL')
        self.image = image.Img(img_path).fill_image()
        print(self.image)

    def convolution2d(self):
        summed_array = []
        for i in range(len(self.image)):
            for j in range(len(self.image[0])):
                try:
                    img_line1 = self.image[i, j:(j + 3)]
                    img_line2 = self.image[i + 1, j:(j + 3)]
                    img_line3 = self.image[i + 2, j:(j + 3)]
                except IndexError:
                    break
                if len(img_line1) < 3 or len(img_line2) < 3 or len(img_line3) < 3:
                    break
                sum_ = 0
                sum_ += (img_line1.dot(self.kernel[0]) + img_line2.dot(self.kernel[1]) + img_line3.dot(self.kernel[2]))
                summed_array.append(sum_)
        summed_array = np.reshape(summed_array, (28, 28))

        for i in range(len(summed_array)):
            for j in range(len(summed_array[0])):
                summed_array[i][j] = 1 if summed_array[i][j] != 0 else 0

        return np.array(summed_array)


path = 'test1.png'
conv = Conv2D(path)
res = conv.convolution2d()
# >> res
