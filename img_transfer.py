import os

import imageio
import rawpy
from rawpy._rawpy import LibRawNonFatalError

from log_utils import exit_with_error


class image_transfer:
    def __init__(self):
        pass

    @staticmethod
    def save(img, res_dir, out_format, file_name):
        path = os.path.join(res_dir, "{}{}".format(file_name, out_format))
        imageio.imsave(path, img)

    @staticmethod
    def load(file_name):
        try:
            raw = rawpy.imread(file_name)
        except LibRawNonFatalError as e:
            exit_with_error("{} isn't raw file or damaged".format(file_name))

        img = raw.postprocess(gamma=(1, 1), no_auto_bright=True, output_bps=16)
        return [img, raw]

    @staticmethod
    def close(img):
        img.close()
