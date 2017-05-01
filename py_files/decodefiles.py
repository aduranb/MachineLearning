computer_path = "C:\Users\Usuario\PycharmProjects\\"

# 'https://pythonprogramming.net/image-recognition-python/'

# Import PIL to identify images in .png, numpy to treat statistics, and matplotlib to represent in graph

from numpy import asarray, array
from matplotlib.pyplot import subplot2grid, figure, show
from PIL import Image


# this function takes an array and creates another array that includes the average tone in the row,
# which will help us to differentiate black from white in fuzzy grey pixels.
def threshold(image_array):
    """
    :type image_array: object
    """
    balance_ar = []
    new_ar = image_array
    for eachRow in image_array:
        for eachPix in eachRow:
            avg_num = reduce(lambda x, y: x + y, eachPix[:3]) / len(eachPix[:3])
            balance_ar.append(avg_num)
    balance = reduce(lambda x, y: x + y, balance_ar) / len(balance_ar)
    for eachRow in new_ar:
        for eachPix in eachRow:
            if balance < reduce(lambda x, y: x + y, eachPix[:3]) / len(eachPix[:3]):
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
                eachPix[3] = 255
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
                eachPix[3] = 255
    return new_ar


# This facilitates the access to the files using the computers path of the file and the Image class from PIL
def open_image(f):
    return asarray(Image.open(computer_path + "MachineLearning\\numbers\\" + f + '.png'))


# Append the images array to the numArEx file
def create_examples():
    # open the array examples file in both read and write mode.
    number_array_examples = open(computer_path + 'MachineLearning\\numArEx.txt', 'a')
    numbers_we_have = xrange(1, 10)
    for num in numbers_we_have:
        for furtherNum in numbers_we_have:
            print str(num) + '.' + str(furtherNum)
            img_file_path = "{0}MachineLearning\\numbers\\{1}.{2}.png".format(computer_path, str(num), str(furtherNum))
            ei = Image.open(img_file_path)  # open the file image
            eiar = array(ei)  # create the array
            eiarl = str(eiar.tolist())  # convert into a string list
            lineToWrite = str(num) + '::' + eiarl + '\n'
            number_array_examples.write(lineToWrite)
    number_array_examples.close()


# Call this function to execute the display of several images as test
def test():
    i = open_image("0.1")
    # Iars are a 3 dimensional array of the data;
    # each matrix block is a row of data, and each element within that is the pixel values in RGB-A.
    # Apply threshold to filter black-white the data
    iar = threshold(array(i))
    i2 = open_image("y0.4")
    iar2 = threshold(array(i2))
    i3 = open_image("y0.5")
    iar3 = threshold(array(i3))
    i4 = Image.open('{0}MachineLearning\\sentdex.png'.format(computer_path))
    iar4 = threshold(array(i4))

    fig = figure()
    ax1 = subplot2grid((8, 6), (0, 0), rowspan=4, colspan=3)
    ax2 = subplot2grid((8, 6), (4, 0), rowspan=4, colspan=3)
    ax3 = subplot2grid((8, 6), (0, 3), rowspan=4, colspan=3)
    ax4 = subplot2grid((8, 6), (4, 3), rowspan=4, colspan=3)

    ax1.imshow(iar)
    ax2.imshow(iar2)
    ax3.imshow(iar3)
    ax4.imshow(iar4)

    show()

# create_examples() running the create_examples function, but only needed once.
