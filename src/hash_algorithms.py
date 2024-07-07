import hashlib
import bcrypt
import os

hash_algorithms = {
    "MD5": hashlib.md5,
    "SHA-256": hashlib.sha256,
    "SHA-384": hashlib.sha384,
    "SHA-512": hashlib.sha512,
    "bcrypt": bcrypt.hashpw,
    "PBKDF2": hashlib.pbkdf2_hmac,
}

def hash_password(password, algorithm, salt=None):
    if algorithm == 'bcrypt':
        salt = salt or bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt), salt
    elif algorithm == 'PBKDF2':
        salt = salt or os.urandom(16)
        return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000), salt
    else:
        hash_object = hash_algorithms[algorithm](password.encode('utf-8'))
        return hash_object.digest(), None
