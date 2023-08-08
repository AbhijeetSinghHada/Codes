import bcrypt

# user = input("Enter Password: ")

salt = bcrypt.gensalt(12)
print(salt)