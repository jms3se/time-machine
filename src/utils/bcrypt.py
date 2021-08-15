from flask_bcrypt import bcrypt

def generate_hash(data):
  hash = bcrypt.generate_password_hash(data)

  return hash

def check_hash(hash, data):
  isOk = bcrypt.check_password_hash(hash, data)

  return isOk
