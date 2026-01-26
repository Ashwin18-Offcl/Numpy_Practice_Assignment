import numpy as np
# 1D array: marks of students (Maths, Science)
marks_1D = np.array([85, 90, 78, 88, 92, 80])

print("originaL 1d Array:")
print(marks_1D)

# Reshape into 2D array(3 students * 2 Subjects)
marks_2d = marks_1D.reshape(3, 2)

print("\nReshaped 2D Array (3 studednts * 2 Subjects):")
print(marks_2d)

# Accessing marks

print("\nStudent 1 Maths Marks:", marks_2d[0][0])
print("Student 2 Sciences Marks:", marks_2d[1][1])

# Average marks per each student 
average = marks_2d.mean(axis=1)
print("\nAverage marks of each student:", average)
