
""""Program to read a file a display the number of words in it @Aakashninan IMCA Rollni:02"""
with open("sample.txt", "r") as file:
    content = file.read()
    words = content.split()
    print(len(words))
