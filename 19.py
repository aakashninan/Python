""""Program to create a dictionary that stores an integer, float, string, list, tuple, set, and another dictionary as values, then print each key and its value. @AakashNinan IMCA Rollno:02"""
data = {"integer": 10,"float": 3.14,"string": "Hello","list": [1, 2, 3],"tuple": (4, 5, 6),"set": {7, 8, 9},"dictionary": {"a": 1, "b": 2}
}

for key, value in data.items():
    print(f"{key}: {value}")
