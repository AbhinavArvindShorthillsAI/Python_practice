import os


class FileManager:
    def __init__(self, filename):
        """Initialize FileManager with a filename"""
        self.filename = filename

    def write_file(self, content):
        """Write content to a file (overwrite if exists)"""
        with open(self.filename, "w") as file:
            file.write(content)
        print(f"File '{self.filename}' written successfully.")

    def append_file(self, content):
        """Append content to a file"""
        with open(self.filename, "a") as file:
            file.write(content)
        print(f"Content appended to '{self.filename}'.")

    def read_file(self):
        """Read entire file content"""
        try:
            with open(self.filename, "r") as file:
                return file.read()
        except FileNotFoundError:
            return f"Error: File '{self.filename}' not found."

    def read_line(self):
        """Read a single line from the file"""
        try:
            with open(self.filename, "r") as file:
                return file.readline()
        except FileNotFoundError:
            return f"Error: File '{self.filename}' not found."

    def read_lines(self):
        """Read all lines as a list"""
        try:
            with open(self.filename, "r") as file:
                return file.readlines()
        except FileNotFoundError:
            return f"Error: File '{self.filename}' not found."

    def file_exists(self):
        """Check if the file exists"""
        return os.path.exists(self.filename)

    def delete_file(self):
        """Delete the file"""
        if self.file_exists():
            os.remove(self.filename)
            print(f"File '{self.filename}' deleted.")
        else:
            print(f"File '{self.filename}' does not exist.")


# Example Usage
file_manager = FileManager("example.txt")
file_manager.write_file("Hello, Python File Handling!\n")
file_manager.append_file("Appending a new line.\n")
print(file_manager.read_file())
file_manager.delete_file()