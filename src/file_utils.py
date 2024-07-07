from .hash_algorithms import hash_algorithms

def hash_file(file_path, algorithm):
    hash_object = hash_algorithms[algorithm]()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_object.update(chunk)
    return hash_object.digest()
