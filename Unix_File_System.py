
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 15:49:20 2024

@author: dinesht
"""

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
        return "{"+self.name+"}"

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

# Class to implement 'find' command in Linux

class LinuxFind():
    def __init__(self):
        self.filters: List[Filter] = []  # List to hold filters

    # Method to add filters
    def add_filter(self, given_filter):
        # Validate given_filter is a filter
        if isinstance(given_filter, Filter):
            self.filters.append(given_filter)

    # Method to apply OR filtering based on filters added
    def apply_OR_filtering(self, root):
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
                for filter in self.filters:
                    if filter.apply(curr_root):
                        found_files.append(curr_root)
                        break
        return found_files

    # Method to apply AND filtering based on filters added
    def apply_AND_filtering(self, root):
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
                is_valid = True
                for filter in self.filters:
                    if not filter.apply(curr_root):
                        is_valid = False
                        break
                if is_valid:
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
txt_filter = ExtensionFilter("txt")  # File extension filter

# Initialize LinuxFind object
my_linux_find = LinuxFind()

# Add filters
my_linux_find.add_filter(greater5_filter)
my_linux_find.add_filter(txt_filter)

# Apply OR filtering and print results
print(my_linux_find.apply_OR_filtering(f1))

# Apply AND filtering and print results
print(my_linux_find.apply_AND_filtering(f1))
