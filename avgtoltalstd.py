#marks of 5 students in 3 subjects
import numpy as np
marks=np.array([[78,85,90],
               [92,88,95],
               [65,70,72],
               [80,82,79],
               [55,60,58]])
avg_per_student=np.mean(marks,axis=1)
print("Average marks per student:",avg_per_student)
avg_per_subject=np.mean(marks,axis=0)
print("Average marks per subject:",avg_per_subject)
topper=np.argmax(np.sum(avg_per_student))
print("Topper  student", topper+1)