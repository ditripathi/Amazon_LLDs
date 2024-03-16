


from abc import ABC, abstractmethod
from collections import deque
from typing import List

# File Class representing files and directories in the UNIX file system
class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.children = []  # Children files or directories
        self.is_directory = False if '.' in name else True  # Check if it's a directory or file
        self.extension = name.split(".")[1] if '.' in name else ""  # Extract file extension

    def __repr__(self):
        return "{" + self.name + "}"

# Abstract Base Class for Filters
class Filter(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def apply(self, file):
        pass

# Filter to select files based on minimum size
class MinSizeFilter(Filter):
    def __init__(self, size):
        self.size = size

    def apply(self, file):
        return file.size > self.size

# Filter to select files based on file extension
class ExtensionFilter(Filter):
    def __init__(self, extension):
        self.extension = extension

    def apply(self, file):
        return file.extension == self.extension

# Class to implement 'find' command in Unix
class UnixFind():
    def __init__(self):
        self.filter: Filter = None  # Only one filter

    # Method to set filter
    def set_filter(self, given_filter):
        # Validate given_filter is a filter
        if isinstance(given_filter, Filter):
            self.filter = given_filter

    # Method to apply filter to the file system
    def apply_filter(self, root):
        found_files = []  # List to store found files

        # Breadth-first search (BFS) traversal
        queue = deque()
        queue.append(root)
        while queue:
            curr_root = queue.popleft()
            if curr_root.is_directory:
                for child in curr_root.children:
                    queue.append(child)
            else:
                if self.filter.apply(curr_root):
                    found_files.append(curr_root)

        return found_files

# Sample files and directories
f1 = File("root_300", 300)
f2 = File("fiction_100", 100)
f3 = File("action_100", 100)
f4 = File("comedy_100", 100)
f1.children = [f2, f3, f4]
f5 = File("StarTrek_4.txt", 4)
f6 = File("StarWars_10.xml", 10)
f7 = File("JusticeLeague_15.txt", 15)
f8 = File("Spock_1.jpg", 1)
f2.children = [f5, f6, f7, f8]
f9 = File("IronMan_9.txt", 9)
f10 = File("MissionImpossible_10.rar", 10)
f11 = File("TheLordOfRings_3.zip", 3)
f3.children = [f9, f10, f11]
f11 = File("BigBangTheory_4.txt", 4)
f12 = File("AmericanPie_6.mp3", 6)
f4.children = [f11, f12]

# Define filters
greater5_filter = MinSizeFilter(5)  # Minimum size filter
txt_filter = ExtensionFilter("txt")  # File extension

# Initialize UnixFind object
my_unix_find = UnixFind()

# Set filter
my_unix_find.set_filter(greater5_filter)

# Apply filter and print results
print(my_unix_find.apply_filter(f1))

'''

Class: File
    Methods:
        - __init__(self, name, size)
        - __repr__(self)
        
Class: Filter (ABC)
    Methods:
        - __init__(self)
        - apply(self, file)
        
Class: MinSizeFilter (Filter)
    Methods:
        - __init__(self, size)
        - apply(self, file)
        
Class: ExtensionFilter (Filter)
    Methods:
        - __init__(self, extension)
        - apply(self, file)
        
Class: LinuxFind
    Methods:
        - __init__(self)
        - add_filter(self, given_filter)
        - apply_filtering(self, root)
'''
