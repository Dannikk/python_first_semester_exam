import os
import functools


class Var:
    format_position_in_split = -1
    format_req = 'txt'


def print_iter(reader):  # a function decorator
    @functools.wraps(reader)
    def dir_reader_decorator(*args, **kwargs):  # The class that will contain the wrapped class
        # print("init")
        inner_reader = reader(*args, **kwargs)
        # print(type(inner_reader))
        for result in inner_reader:
            print(result)
            yield result

    return dir_reader_decorator


@print_iter
def DirReader(dir):  # To read files in a directory
    walk = os.walk(dir)
    for root, dirs, files in walk:
        # root, dirs, files = next(walk)
        if files:
            for file in files:
                if file.split('.')[
                    Var.format_position_in_split] == Var.format_req:  # If the file matches the format we need
                    # self.files_remaining = files[files.index(file) + 1:]  # We remember the remaining files
                    yield root + "\\" + file  # giving the canonical path

# @print_iter
# class DirReader:  # To read files in a directory
#     def __init__(self, dir):  # Getting the path to the directory
#         self.dir = dir
#         self.walk = os.walk(dir)
#         print("init")
#         # self.files_remaining = []  # To write unread files
#
#     def work(self):
#         while True:
#             root, dirs, files = next(self.walk)
#             if files:
#                 for file in files:
#                     if file.split('.')[
#                         Var.format_position_in_split] == Var.format_req:  # If the file matches the format we need
#                         # self.files_remaining = files[files.index(file) + 1:]  # We remember the remaining files
#                         yield root + "\\" + file  # giving the canonical path
# if len(self.files_remaining) == 0:  # If there are no unread messages left, take the next step
#     root, dirs, files = next(self.walk)
# else:
#     files = self.files_remaining
# if files:
#     for file in files:
#         if file.split('.')[Var.format_position_in_split] == Var.format_req:  # If the file matches the format we need
#             self.files_remaining = files[files.index(file) + 1:]  # We remember the remaining files
#             return root + "\\" + file  # giving the canonical path
# return next(self)

# def __iter__(self):  # So that you can run through the for loop
#     return self
