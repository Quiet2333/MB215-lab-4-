import traceback

def write_to_file(filename, data):
    try:
        with open(filename, 'w') as file:
            file.write(data)  # This line should be indented
    except Exception as e:
        print(f"An error occurred while writing to the file: {filename}")
        traceback.print_exc()
