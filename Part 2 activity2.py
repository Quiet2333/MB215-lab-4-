import traceback

def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            return data
    except Exception as e:
        print(f"An error occurred while reading from the file: {filename}")
        traceback.print_exc()
        return None
