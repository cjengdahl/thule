from thule import Walker, Actions

class Tree(Actions):

    def print_directory(self, dir_path):
        print('dir_path: {}'.format(dir_path))

    def print_file(self, dir_path, file_name):
        print('  -- {}'.format(file_name))

if __name__ == "__main__":
    
    import os

    walker = Walker()
    walker.accept("/Users/coryengdahl/Documents", Tree())