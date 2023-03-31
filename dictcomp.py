from string import ascii_lowercase
def my_dict():
    return {k:v for v, k in enumerate(ascii_lowercase, 1)}
print(my_dict())