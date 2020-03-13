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
        path = os.path.join(res_dir, f"{file_name}{out_format}")

        imageio.imsave(path, img)

    @staticmethod
    def save_thumb(thumb, res_dir, out_format, file_name):
        path = os.path.join(res_dir, f"{file_name}{out_format}")

        with open(path, 'wb') as f:
            f.write(thumb.data)

    @staticmethod
    def load_thumb(file_name):
        try:
            raw = RawFiles.read_file(file_name)
            thumb = raw.extract_thumb()
        except rawpy.LibRawNoThumbnailError:
            exit_with_error(f"File {file_name} has no thumbnail")
        except rawpy.LibRawUnsupportedThumbnailError:
            exit_with_error(f"File {file_name} has no supported thumbnail")
        except rawpy.LibRawNonFatalError:
            exit_with_error(f"File {file_name} isn't raw file or damaged")

        return thumb

    @staticmethod
    def load(file_name):
        try:
            raw = RawFiles.read_file(file_name)
        except LibRawNonFatalError:
            exit_with_error(f"File {file_name} isn't raw file or damaged")

        img = raw.postprocess(gamma=(1, 1), output_bps=16,
                              use_camera_wb=True)
        return [img, raw]

    @staticmethod
    def close(img):
        img.close()
