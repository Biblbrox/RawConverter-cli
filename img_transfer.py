import os

import imageio
import rawpy
from rawpy._rawpy import LibRawNonFatalError

from log_utils import exit_with_error, RawFiles


class image_transfer:
    def __init__(self):
        pass

    @staticmethod
    def save(img, res_dir, out_format, file_name):
        path = os.path.join(res_dir, "{}{}".format(file_name, out_format))

        imageio.imsave(path, img)

    @staticmethod
    def save_thumb(thumb, res_dir, out_format, file_name):
        path = os.path.join(res_dir, "{}{}".format(file_name, out_format))

        with open(path, 'wb') as f:
            f.write(thumb.data)

    @staticmethod
    def load_thumb(file_name):
        try:
            raw = RawFiles.read_file(file_name)
            thumb = raw.extract_thumb()
        except rawpy.LibRawNoThumbnailError:
            exit_with_error("File {} has no thumbnail".format(file_name))
        except rawpy.LibRawUnsupportedThumbnailError:
            exit_with_error("File {} has no supported thumbnail".format(file_name))
        except rawpy.LibRawNonFatalError:
            exit_with_error("File {} isn't raw file or damaged".format(file_name))

        return thumb

    @staticmethod
    def load(file_name):
        try:
            raw = RawFiles.read_file(file_name)
        except LibRawNonFatalError as e:
            exit_with_error("File {} isn't raw file or damaged".format(file_name))

        img = raw.postprocess(gamma=(1, 1), output_bps=16,
                              use_camera_wb=True)
        return [img, raw]

    @staticmethod
    def close(img):
        img.close()
