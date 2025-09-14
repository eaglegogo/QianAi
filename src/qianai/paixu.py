import os

def sort_files_by_modification_time(directory):
    """Sort files in the given directory by their last modification time."""
    files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    print("Sorted files by modification time:")
    return files    

if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath(__file__))
    sorted_files = sort_files_by_modification_time(directory)
    for file in sorted_files:
        print(file)