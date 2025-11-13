""""Program to count the number of words lines and characters in a sentence provided by the user @Aakashninan IMCA Rollno:02"""

text = input("Enter your sentence or paragraph:\n")
char_count = len(text)
word_count = len(text.split())
line_count = text.count('\n') + 1
print("\n--- Counts ---")
print("Characters:", char_count)
print("Words:", word_count)
print("Lines:", line_count)
