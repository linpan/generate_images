#!/user/bin/env python
# -*- coding:utf-8 -*-
# create_thumb.py
# multiprocessing
# 2018/2/7 today Falcon Heavy lauched by spacex
# WebP format 适合网页显示及传输
# 3036 images cup=4 run_time=4.7;cup=2 run_time=7.3;cup=1,run_time=11.5
"""
将遍历传入的文件夹中的图片文件，生成缩略图，并将这些缩略图保存到特定文件夹中。
"""

import os
import time
import glob
from PIL import Image


from multiprocessing import Pool
import multiprocessing

SIZE = (32, 32)
SAVE_DIRECTON = 'thumbs'

def get_image_paths(folder):
    """

    :param path:
    :return: generator object
    """
    obj_image_path = glob.iglob(folder+'/*.jpg')
    return obj_image_path


def create_thumbmail(filename):
    im = Image.open(filename)
    im.thumbnail(SIZE, Image.ANTIALIAS)
    base, fname = os.path.split(filename)
    save_path = os.path.join(base, SAVE_DIRECTON, fname)
    im.save(save_path)


if __name__ == '__main__':
    folder = os.path.abspath(r'/Users/py2018/flower_photos/sunflowers')
    os.mkdir(os.path.join(folder, SAVE_DIRECTON))

    images = [image for image in get_image_paths(folder)]
    print len(images)
    start = time.time()
    pool = Pool(multiprocessing.cpu_count())  # based cup cores set pools
    pool.map(create_thumbmail, images)
    pool.close()
    pool.join()
    print (time.time()-start)





