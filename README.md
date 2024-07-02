# Metode Numerik Sistem Persamaan Linier
```
Metode :
1. Gauss Jordan Method
2. Jacobi Method
3. Gauss Seidell Method
```
Example : 

$3x + y – z = 5$

$4x + 7y – 3z = 20$

$2x – 2y + 5z = 10$

For Gauss Jordan, the shape is changed to a matrix

$$
\left[\begin{array}{ccc|c}
3 & 1 & -1 & 5 \\
4 & 7 & -3 & 20 \\
2 & -2 & 5 & 10
\end{array}\right]
$$

For Jacobi and Gauss Seidel, The equation above changes its form to :

$x = (5 – y + z)/3$

$y = (20 – 4x + 3z)/7$

$z = (10 – 2x + 2y)/5$
