import rawpy


def exit_with_error(msg):
    RawFiles.close_files()
    exit(msg)


def exit_suc(msg):
    print(msg)
    RawFiles.close_files()
    exit(1)


class RawFiles:
    files = {}

    @classmethod
    def read_file(cls, file_name):
        raw = rawpy.imread(file_name)
        RawFiles.files.update({file_name: raw})

        return raw

    @classmethod
    def close_files(cls):
        for file in RawFiles.files:
            file.close()
        RawFiles.files.clear()

    @classmethod
    def close_file(cls, file_name):
        if RawFiles.files[file_name]:
            RawFiles.files[file_name].close()
            del RawFiles.files[file_name]
            return True

        return False
