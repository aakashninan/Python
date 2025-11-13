"""Program to create a tuple with subkect names and display them using loops @author Aakashninan IMCA Rollno:02"""
a=tuple(map(str,input("Enter the subjects").split(" ")))
for i in a:
    print(i)
