import numpy as np

A = np.array([
    [3, 1, -1, 5],
    [4, 7, -3, 20],
    [2, -2, 5, 10]
], dtype=float)

print("Soal:")
print(A)
print("Penyelesaian:")

def gauss_jordan(A):
    rows, cols = A.shape

    langkah = 1  # Initialize step counter

    for i in range(rows):
        # Normalize row i
        print(f"Langkah {langkah}: Mengubah baris {i+1} dengan cara = B{i+1} / {A[i, i]:.2f}")
        A[i] = A[i] / A[i, i]
        print(A, "\n")
        langkah += 1
        
        for j in range(rows):
            if i != j:
                factor = A[j, i]
                print(f"Langkah {langkah}: Mengubah baris {j+1} dengan cara = B{j+1} - ({factor:.2f} * B{i+1})")
                A[j] = A[j] - factor * A[i]
                print(A, "\n")
                langkah += 1
                
    return A

# Perform Gauss-Jordan elimination
result = gauss_jordan(A)

# Print final result
print("Hasil Matrix:")
print(result)

# Display the final result
print(f"\nX = {A[0, 3]}")
print(f"Y = {A[1, 3]}")
print(f"Z = {A[2, 3]}")
