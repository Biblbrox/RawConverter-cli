import argparse
import os

from str_utils import *
import ntpath

from img_transfer import image_transfer

"""
Supported optional arguments is [out_type, res_dir]
"""


class raw_converter:
    def __init__(self):
        pass

    def convert(self, file):
        pass

    def convert_many(self, files):
        pass


class image:
    def __init__(self, file_name):
        self.file_path = file_name
        self.file_name = os.path.splitext(ntpath.basename(self.file_path))[0]
        self.img, self.raw = image_transfer.load(file_name)
        self.dir_name = ntpath.dirname(self.file_path)
        pass

    def save(self, file_name="", res_dir="", out_format=".jpeg"):
        image_transfer.save(self.img,
                            res_dir if res_dir else self.dir_name,
                            out_format,
                            file_name if file_name else self.file_name)

    def close(self):
        image_transfer.close(self.raw)


parser = argparse.ArgumentParser()
parser.add_argument('files', help='List of files you want to convert', type=str, nargs='*')
parser.add_argument('--out_type', help='Output type of image', type=str)
parser.add_argument('--res_dir', help='Output directory', type=str)
args = parser.parse_args()

# Command line arguments
list_files = args.files
res_dir = args.res_dir if args.res_dir else None
out_type = ".{}".format(args.out_type) if args.out_type else None

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
    im = image(file)
    im.save(out_format=out_type if out_type else ".jpeg")
    im.close()
