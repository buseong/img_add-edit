import argparse
import numpy as np
from module.img_edit import overpx_edit, img_add
import os


def editer(img_patch, base_folder):
    basic_path = os.getcwd().replace("\\", "/")
    img = img_add(img_patch)
    n = 1
    cut_img_y = 0
    pix = np.array(img)
    counter = 0
    for pixel_y in range(img.size[1]):
        judge = pix[pixel_y][np.arange(0, img.size[0])]
        if np.max(judge) == np.min(judge) == 255 or \
                np.max(judge) == np.min(judge) == 0:
            counter += 1
        if counter == 300:
            cut_img = img.crop((0, cut_img_y, img.size[0], pixel_y))
            if int(cut_img.size[1]) <= 300:
                n = n - 1
            else:
                if cut_img.size[1] >= 50000:
                    print('image overflow')
                    n += 1
                    overpx_edit(cut_img, basic_path, base_folder, n)
                else:
                    cut_img.save(f"{basic_path}/{base_folder}//{n}.jpg")
            cut_img_y = pixel_y
            counter = 0
            n += 1


if __name__ == '__main__':

    preser = argparse.ArgumentParser(description='imgAddnedit')
    preser.add_argument('-f', '--folder', help='folder to imgFile, warning:do not typing end of the path "\\"',
                        required=True, type=str, )
    preser.add_argument('-l', '--local_folder', help='save img folder, default_fold = img_folder',
                        type=str, required=False, default='folder')
    args = preser.parse_args()

    try:
        os.makedirs(os.getcwd().replace("\\", "/") + "/" + args.local_folder)
    except (Exception,):
        print('already exist folder')
    editer(args.folder, args.local_folder)
