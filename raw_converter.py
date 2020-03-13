import argparse
import os

from log_utils import RawFiles, exit_with_error
from str_utils import *
import ntpath

from img_transfer import image_transfer

"""
Supported optional arguments is [out_type, res_dir, get_thumb]
Default format to saving images is jpeg
"""


class raw_converter:
    def __init__(self):
        pass

    def convert(self, file):
        pass

    def convert_many(self, files):
        pass


class image:
    def __init__(self, file_name, thumb=False):
        self.file_path = file_name
        self.file_name = os.path.splitext(ntpath.basename(self.file_path))[0]
        self.is_thumb = thumb
        if thumb:
            self.img = image_transfer.load_thumb(file_name)
        else:
            self.img, self.raw = image_transfer.load(file_name)
        self.dir_name = ntpath.dirname(self.file_path)
        pass

    def save(self, file_name="", res_dir="", out_format=".jpeg"):
        if self.is_thumb:
            image_transfer.save_thumb(self.img,
                                      res_dir if res_dir else self.dir_name,
                                      out_format,
                                      file_name if file_name else self.file_name)
        else:
            image_transfer.save(self.img,
                                res_dir if res_dir else self.dir_name,
                                out_format,
                                file_name if file_name else self.file_name)

    def close(self):
        RawFiles.close_file(self.file_path)


parser = argparse.ArgumentParser()
parser.add_argument('files', help='List of files you want to convert',
                    type=str, nargs='*')
parser.add_argument('--out_type', help='Output type of image', default='jpeg',
                    type=str)
parser.add_argument('--res_dir', default=None, help='Output directory',
                    type=str)
parser.add_argument('--get_thumb', default=False, action='store_true',
                    help='Get only thumbnails of photos.')
args = parser.parse_args()

# Command line arguments
list_files = args.files
res_dir = args.res_dir
out_type = ".{}".format(args.out_type)
load_thumb = args.get_thumb

# Check if result directory is exists
if res_dir and not os.path.exists(res_dir):
    exit_with_error("Directory {} doesn't exists or unable to write"
                    .format(res_dir))

# Parse Unix style filenames(like *)
res_files = []
for file in list_files:
    if os.path.isdir(file):
        res_files.append(get_files(file))
        continue
    f = parse_path(file)
    res_files.append(f)

res_files = [file for sublist in res_files for file in sublist]
converter = raw_converter()
for file in res_files:
    if load_thumb:
        im = image(file, True)
    else:
        im = image(file)
    if res_dir:
        im.save(out_format=out_type, res_dir=res_dir)
    else:
        im.save(out_format=out_type)
    im.close()
