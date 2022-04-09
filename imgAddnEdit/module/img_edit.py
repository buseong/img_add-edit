from PIL import Image
import os
import natsort


def overpx_edit(cut_img, basic_file, base_floader, n):

    back_img = Image.new('RGB', (0, int(cut_img.size[1]) / 2), (255, 255, 255))
    back_second_img = Image.new('RGB', (0, int(cut_img.size[1]) / 2), (255, 255, 255))
    back_img.paste(cut_img, 0, cut_img.size[1] / 2)
    back_second_img.paste(cut_img, 0, cut_img.size[1])
    back_img.save(f"{basic_file}/{base_floader}/{n - 1}.jpg")
    back_second_img.save(f"{basic_file}/{n}.jpg")

    return None


def img_add(img_pathe):
    img_path = natsort.natsorted(os.listdir(img_pathe))
    for i in range(len(img_path)):
        img_path[i] = img_pathe + "/" + img_path[i]
        print(img_path[i])
    new_img = None
    for i in range(len(img_path) - 1):
        if i == 0:
            first_img = Image.open(img_path[i])
        else:
            first_img = new_img
        second_img = Image.open(img_path[i + 1])
        first_img_size = first_img.size
        second_img_size = second_img.size
        new_img = Image.new('RGB', (first_img_size[0], first_img_size[1] + (second_img_size[1])), (255, 255, 255))
        new_img.paste(first_img, (0, 0))
        new_img.paste(second_img, (0, first_img_size[1]))

    return new_img
