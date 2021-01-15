import os
def print_iter(reader):  # a function decorator
    class false_class:  # The class that will contain the wrapped class
        def __init__(self, *args, **kwargs):
            self._obj = reader(*args, **kwargs)  # proxying the entire class creation

        def __iter__(self):
            return self

        def __next__(self):  # Get the file name from the wrapped class and output it
            res = next(self._obj)
            print(res)
            return res

    return false_class


@print_iter
class DirReader:  # To read files in a directory
    def __init__(self, dir):  # Getting the path to the directory
        self.dir = dir
        self.walk = os.walk(dir)
        self.files_remaining = []  # To write unread files

    def __next__(self):
        if len(self.files_remaining) == 0:  # If there are no unread messages left, take the next step
            root, dirs, files = next(self.walk)
        else:
            files = self.files_remaining
        if len(files) > 0:  #
            for file in files:
                if file.split('.')[-1] == 'txt':  # If the file matches the format we need
                    self.files_remaining = files[files.index(file) + 1:]  # We remember the remaining files
                    return root + "\\" + file  # giving the canonical path
        return next(self)

    def __iter__(self):  # So that you can run through the for loop
        return self
