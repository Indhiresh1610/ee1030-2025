#include <math.h>

#define N 3
#define TOLERANCE 1e-9

int check_vectors(double v1[], double v2[], double v3[]) {
    double mat[N][N];
    
    // Create a matrix from the input vectors (as columns)
    for (int i = 0; i < N; i++) {
        mat[i][0] = v1[i];
        mat[i][1] = v2[i];
        mat[i][2] = v3[i];
    }
    
    // --- Gaussian Elimination to find rank ---
    for (int col = 0; col < N; col++) {
        int pivot_row = col;
        for (int i = col + 1; i < N; i++) {
            if (fabs(mat[i][col]) > fabs(mat[pivot_row][col])) {
                pivot_row = i;
            }
        }
        
        if (pivot_row != col) {
            for (int i = 0; i < N; i++) {
                double temp = mat[col][i];
                mat[col][i] = mat[pivot_row][i];
                mat[pivot_row][i] = temp;
            }
        }

        if (fabs(mat[col][col]) < TOLERANCE) continue;

        for (int i = 0; i < N; i++) {
            if (i != col) {
                double factor = mat[i][col] / mat[col][col];
                for (int j = col; j < N; j++) {
                    mat[i][j] -= factor * mat[col][j];
                }
            }
        }
    }

    int zero_rows = 0;
    for (int i = 0; i < N; i++) {
        int all_zeros = 1;
        for (int j = 0; j < N; j++) {
            if (fabs(mat[i][j]) > TOLERANCE) {
                all_zeros = 0;
                break;
            }
        }
        if (all_zeros) zero_rows++;
    }
    
    int rank = N - zero_rows;
    
    return (rank < 3) ? 2 : 3;
}
