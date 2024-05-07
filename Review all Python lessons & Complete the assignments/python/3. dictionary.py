# Advanced Python: Dictionaries

"""
Author: Haseen Nurayin
Email: c193268@ugrad.iiuc.ac.bd

This Python script is designed to provide a comprehensive understanding of Python dictionaries.
We will explore:
1. Dictionary basics - Creation, accessing, and updating.
2. All dictionary methods and their uses.
3. Integrating dictionaries with lists and tuples for complex data structures.

Each section includes detailed explanations, examples, and challenging assignments.
"""

# Section 1: Dictionary Basics
# ----------------------------
# Dictionaries in Python are unordered collections that store data in key-value pairs.

# Example 1: Creating and Using Dictionaries
#simple_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
# print(simple_dict['name'])  # Accessing value by key
# print(simple_dict.get('address', "Dhaka"))  # Accessing value by key


# Updating dictionary
#simple_dict['age'] = 31  # Updates the age
#simple_dict['country'] = 'USA'  # Adds a new key-value pair
# print("Updated Dictionary: ", simple_dict)

# Dictionary Methods
# keys(), values(), items()
# print(simple_dict.keys())  # Prints all keys
# print(simple_dict.values())  # Prints all values
# print(simple_dict.items())  # Prints all key-value pairs as tuples

# get()
#print(simple_dict.get('name'))  # Returns 'John'

# pop()
#removed_value = simple_dict.pop('country')  # Removes 'country' key and returns its value
#print("Removed Value:", removed_value)
#print("Dictionary after pop(): ", simple_dict)

# popitem()
#last_item = simple_dict.popitem()  # Removes and returns the last inserted key-value pair
#print("Last Item:", last_item)
#print("Dictionary after popitem(): ", simple_dict)

# update()
#simple_dict.update({'age': 32, 'email': 'john@example.com'})  # Updates the dictionary
#print("Dictionary after update(): ", simple_dict)

# clear()
# simple_dict.clear()  # Empties the dictionary
# print("Dictionary after clear(): ", simple_dict)

# copy()
#dict_copy = simple_dict.copy()  # Creates a shallow copy of the dictionary
#print("Dictionary Copy: ", dict_copy)

# Assignment 1: Create a dictionary representing a student with keys like 'name', 'roll_number', 'grades' (a list of subjects and marks).
# Perform various operations like adding, removing, and modifying elements.
# Write your code below:

# Creating a dictionary for a student
student_info = {
    'name': 'Haseen Nurayin',
    'roll_number': 193268,
    'grades': {
        'Math': 97,
        'Science': 99,
        'English': 100
    }
}

print("Original Student Info:", student_info)

student_info['grades']['History'] = 92
print("After adding a subject:", student_info)

student_info['grades']['Math'] = 88
print("After modifying a grade:", student_info)

del student_info['grades']['Science']
print("After removing a subject:", student_info)

student_info['address'] = '123 Elm Street'
print("After adding address:", student_info)

student_copy = student_info.copy()
print("Copy of Student Info:", student_copy)

# Section 2: Integrating Dictionaries with Lists and Tuples
# ---------------------------------------------------------
# Dictionaries can be used with lists and tuples to create complex data structures.

# Example 2: List of Dictionaries
#students = [
#    {'name': 'Alice', 'grade': 85},
#    {'name': 'Bob', 'grade': 90},
#    {'name': 'Charlie', 'grade': 78}
#]

# Sorting list of dictionaries by grade
#students_sorted_by_grade = sorted(students, key=lambda x: x['grade'], reverse=True)
#print("Students sorted by grade: ", students_sorted_by_grade)

# Example 3: Dictionary of Tuples
# Using tuples as keys
#coordinates_info = {(35.6895, 139.6917): "Tokyo", (40.7128, -74.0060): "New York"}

# Assignment 2: Create a dictionary where keys are student names and values are lists of grades. Calculate the average grade for each student.
# Write your code below:

students_grades = {
    'Noumi': [85, 78, 92],
    'Urmi': [75, 88, 82],
    'Lubna': [90, 92, 85]
}

print("Students and their grades:", students_grades)

students_averages = {name: sum(grades) / len(grades) for name, grades in students_grades.items()}

print("Average grade for each student:")
for student, average in students_averages.items():
    print(f"{student}: {average:.2f}")

# Congratulations on completing the advanced section on Python dictionaries!
# Review the assignments, try to solve them, and check your understanding of this powerful data structure.
