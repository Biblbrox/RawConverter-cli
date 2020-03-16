## Raw converter
It's the tool for postprocess camera RAW files to several formats.
Raw converter uses [RawPy](https://github.com/letmaik/rawpy) library
## Sample code
```bash
python3 raw_converter.py /home/user/photo/* --res-dir /home/user/final_photo --out-type .jpeg
```

You can get thumbnail for more speed rendering. But on some cameras it don't work 
and may return different thumbnails for different cameras.
```bash
python3 raw_converter.py /home/user/photo/some_img.CR2 --res-dir /home/user/final_photo --get-thumb
```

By default --out-type is .jpeg and --res-dir is same dir with input file