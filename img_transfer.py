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
    def load(file_name, load_thumb=False):
        try:
            raw = rawpy.imread(file_name)
            # if load_thumb:
            #     try:
            #         thumb = raw.extract_thumb()
            #     except rawpy.LibRawNoThumbnailError:
            #         exit_with_error('{} file has no thumbnail'.format(file_name))
            #     except rawpy.LibRawUnsupportedThumbnailError:
            #         exit_with_error("{} file has unsupported thumbnail".format(file_name))
            #     else:
            #         pass

        except LibRawNonFatalError as e:
            exit_with_error("{} isn't raw file or damaged".format(file_name))

        img = raw.postprocess(gamma=(1, 1), no_auto_bright=True, output_bps=16)
        return [img, raw]

    @staticmethod
    def close(img):
        img.close()
