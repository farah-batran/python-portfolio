# conditional_tests.py
# Adapted from p.77 - Boolean tests

user = "analyst"
role = "viewer"
failed = 5
port = 22

print("Is failed == 5? I predict True.")
print(failed == 5)

print("\nIs user == 'admin'? I predict False.")
print(user == "admin")

print("\nIs failed != 3? I predict True.")
print(failed != 3)

print("\nIs port > 100? I predict False.")
print(port > 100)

print("\nIs port < 100? I predict True.")
print(port < 100)

print("\nIs failed >= 5? I predict True.")
print(failed >= 5)

print("\nIs failed <= 4? I predict False.")
print(failed <= 4)

print("\nIs user == 'analyst' and role == 'viewer'? I predict True.")
print(user == "analyst" and role == "viewer")

print("\nIs role == 'admin' or port == 80? I predict False.")
print(role == "admin" or port == 80)

print("\nIs not (port == 22)? I predict False.")
print(not (port == 22))