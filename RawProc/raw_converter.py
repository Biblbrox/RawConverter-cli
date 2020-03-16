import argparse
import os

from RawProc.log_utils import RawFiles, exit_with_error
from RawProc.str_utils import *
import ntpath

from RawProc.img_transfer import ImageTransfer

"""
Supported arguments
Default image extension is jpeg
"""

class Image:
    """
    Image class.
    Keeps original raw file and postprocessed image
    or thumbnail only.
    """
    def __init__(self, file_name, thumb=False):
        self.file_path = file_name
        self.file_name = os.path.splitext(ntpath.basename(self.file_path))[0]
        self.is_thumb = thumb
        if thumb:
            self.img = ImageTransfer.load_thumb(file_name)
        else:
            self.img, self.raw = ImageTransfer.load(file_name)
        self.dir_name = ntpath.dirname(self.file_path)

    def save(self, file_name="", res_dir="", out_format=".jpeg"):
        if self.is_thumb:
            ImageTransfer.save_thumb(self.img,
                                     res_dir if res_dir else self.dir_name,
                                     out_format,
                                     file_name if file_name
                                     else self.file_name)
        else:
            ImageTransfer.save(self.img,
                               res_dir if res_dir else self.dir_name,
                               out_format,
                               file_name if file_name else self.file_name)

    def close(self):
        RawFiles.close_file(self.file_path)


def run():
    args = {
        "files": {
            "help": 'List of files you want to convert',
            "type": str,
            "nargs": '*'
        },
        "--out-type": {
            "help": 'Output type of image',
            "default": '.jpeg',
            "type": str
        },
        "--res-dir": {
            "default": None,
            "help": 'Output directory',
            "type": str
        },
        "--get-thumb": {
            "default": False,
            "action": "store_true",
            "help": "Get thumbnails only"
        }
    }

    parser = argparse.ArgumentParser()
    for k, v in args.items():
        parser.add_argument(k, **v)
    args = parser.parse_args()

    # Command line arguments
    args = vars(args)
    # Check if result directory is exists
    if args['res_dir'] and not os.path.exists(args['res_dir']):
        exit_with_error(f"Directory {args['res_dir']} does't exists "
                        f"or unable to write")

    # Parse Unix style filenames(like *)
    res_files = []
    for file in args['files']:
        if os.path.isdir(file):
            res_files.append(get_files(file))
            continue
        res_files.append(parse_path(file))

    res_files = [file for sublist in res_files for file in sublist]
    for file in res_files:
        im = Image(file, True) if args['get_thumb'] else Image(file)

        im.save(out_format=args['out_type'], res_dir=args['res_dir'])
        im.close()
