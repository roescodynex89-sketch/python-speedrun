# Dictionary
student = {"name": "Estiak", "age": 20, "skills": ["JS", "Python"]}
student.get("age")            # safe access, even if the key doesn't exist.
student.get("email", "N/A")   # default value With
student.keys()                 # all keys
student.values()                # all values
student.pop("age")              # remove + return value
"name" in student                 # key check → True

# nested dict
users = {
    "u1": {"name": "Estiak", "role": "dev"},
    "u2": {"name": "Rahim", "role": "admin"}
}
print(users["u1"]["name"])

