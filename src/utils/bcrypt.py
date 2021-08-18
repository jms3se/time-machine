from . import bcrypt

def generate_hash(data):
    return bcrypt.generate_password_hash(data).decode("utf-8")

def check_hash(hash, data):
    return bcrypt.check_password_hash(hash, data)
