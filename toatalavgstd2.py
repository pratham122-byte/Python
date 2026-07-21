import numpy as np
marks=np.array([[78,85,90],
               [92,88,95],  
                [65,70,72],
                [80,82,79]])
total_per_student=np.sum(marks,axis=1)
avg_per_student=np.mean(marks,axis=1)
print("Total marks per student:",total_per_student)
print("Average marks per student:",avg_per_student)
best_shift=np.argmax(total_per_student)
print("most proudtive shift student:",best_shift+1)