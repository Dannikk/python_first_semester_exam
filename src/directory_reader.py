import os
import functools


class Var:
    format_position_in_split = -1
    format_req = 'txt'


def print_iter(reader):  # a function decorator
    @functools.wraps(reader)
    def dir_reader_decorator(*args, **kwargs):  # The class that will contain the wrapped class
        inner_reader = reader(*args, **kwargs)
        for result in inner_reader:
            print(result)
            yield result

    return dir_reader_decorator


@print_iter
def DirReader(dir):  # To read files in a directory
    walk = os.walk(dir)
    for root, dirs, files in walk:
        if files:
            for file in files:
                if file.split('.')[
                    Var.format_position_in_split] == Var.format_req:  # If the file matches the format we need
                    yield root + "\\" + file  # giving the canonical path
