      +-------------------+              +----------------+
      |      Directory    |              |      File      |
      +-------------------+              +----------------+
      | - name: String    |              | - name: String |
      | - children: Map<String, Object> |              |
      +-------------------+              +----------------+
      | + createFile()    |              | + rename()     |
      | + createDirectory()|              +----------------+
      | + delete()        |              
      | + move()          |              
      +-------------------+              


class File:
    def __init__(self, name):
        self.name = name

    def rename(self, new_name):
        self.name = new_name

class Directory:
    def __init__(self, name):
        self.name = name
        self.children = {}

    def create_file(self, file_name):
        file = File(file_name)
        self.children[file_name] = file

    def create_directory(self, dir_name):
        directory = Directory(dir_name)
        self.children[dir_name] = directory

    def delete(self, name):
        del self.children[name]

    def move(self, name, new_directory):
        item = self.children.pop(name)
        new_directory.children[name] = item

# Example usage:
root = Directory('/')
root.create_file('example.txt')
root.create_directory('folder1')
folder1 = root.children['folder1']
folder1.create_file('test.txt')

# Renaming a file
root.children['example.txt'].rename('new_example.txt')

# Deleting a file
folder1.delete('test.txt')

# Moving a file to another directory
root.move('new_example.txt', folder1)
