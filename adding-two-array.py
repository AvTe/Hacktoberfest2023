# Define two arrays
array1 = [1, 2, 3, 4, 5]
array2 = [10, 20, 30, 40, 50]

# Create an empty result array
result_array = []

# Check if the arrays are of the same length
if len(array1) == len(array2):
    # Add the values from both arrays element by element
    for i in range(len(array1)):
        result_array.append(array1[i] + array2[i])
    print("Resulting array:", result_array)
else:
    print("Arrays are of different lengths. Cannot add values.")

