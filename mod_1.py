print("This is mod_1's name ->", __name__)

if __name__ == '__main__':
    print("We are running this file directly")
else:
    print('This file was called/imported from somewhere')