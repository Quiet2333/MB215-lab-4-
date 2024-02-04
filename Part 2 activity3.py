def append_to_file(filename, data):
    try:
        with open(filename, 'a') as file:  # 'a' mode opens the file for appending
            file.write(data)
    except Exception as e:
        print(f"An error occurred while appending to the file: {filename}")
        traceback.print_exc()
import traceback

def write_to_file(filename, data):
    try:
        with open(filename, 'w') as file:
            file.write(data)
    except Exception as e:
        print(f"An error occurred while writing to the file: {filename}")
        traceback.print_exc()

def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"An error occurred while reading from the file: {filename}")
        traceback.print_exc()
        return None

def append_to_file(filename, data):
    try:
        with open(filename, 'a') as file:
            file.write(data)
    except Exception as e:
        print(f"An error occurred while appending to the file: {filename}")
        traceback.print_exc()

if __name__ == "__main__":
    # Writing to a file
    write_to_file('sample.txt', 'Hello, World!\n')
    
    # Reading from a file
    content = read_from_file('sample.txt')
    if content is not None:
        print("Content of the file after writing:")
        print(content)
    
    # Appending to a file
    append_to_file('sample.txt', 'This is a new line appended.\n')
    
    # Reading from the file again to show the appended content
    content_after_appending = read_from_file('sample.txt')
    if content_after_appending is not None:
        print("Content of the file after appending:")
        print(content_after_appending)

    # Trying to read from a non-existent file to demonstrate exception handling
    non_existent_content = read_from_file('non_existent_file.txt')
    if non_existent_content is None:
        print("Could not read the non-existent file.")
