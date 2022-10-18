import numpy as np #Importing numpy module
vector_1 = np.random.randint(1,20,15)
print("Printing vector 1 ",vector_1)

vector_2=np.reshape(vector_1,(3,5))
print("Printing vector 1 after reshaping as vector 2 ",vector_2)

print(vector_2.shape)

max_elements = np.amax(vector_2, axis = 1)
max_elements = max_elements[: , None]
new_arr = np.where(vector_2 == max_elements, 1, vector_2)
print(new_arr)
