from decodefiles import computer_path, open_image
from PIL import Image
import numpy as np
from collections import Counter
import operator
import matplotlib.pyplot as plt


def what_num_is_this(file_path):
    matched_ar = []
    load_examps = open(computer_path + 'MachineLearning\\numArEx.txt', 'r').read().split('\n')
    i = Image.open(file_path)
    plt.figure()
    plt.imshow(np.asarray(Image.open(file_path)))
    plt.show()
    iar = np.array(i)
    iarl = iar.tolist()
    in_question = str(iarl)

    for eachExample in load_examps:
        try:
            split_ex = eachExample.split('::')
            current_num = split_ex[0]
            current_ar = split_ex[1]

            each_pix_ex = current_ar.split('],')
            each_pix_in_q = in_question.split('],')

            x = 0

            while x < len(each_pix_ex):
                if each_pix_ex[x] == each_pix_in_q[x]:
                    matched_ar.append(int(current_num))
                x += 1
        except Exception:
            pass
    x = Counter(matched_ar)
    print "The number is", max(x.iteritems(), key=operator.itemgetter(1))[0]


what_num_is_this(computer_path + 'MachineLearning\\numbers\\6.5.png')
