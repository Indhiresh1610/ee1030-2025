#include <math.h> // For fabs()

// Define matrix dimensions
#define ROWS 3
#define COLS 3

/*
* A generic function to calculate the rank of any 3x3 matrix.
* @param mat The input 3x3 matrix (array of doubles).
* @return The rank of the matrix as an integer.
*/
int calculate_rank(double mat[ROWS][COLS]) {
    // Create a local copy to avoid modifying the original matrix passed from Python
    double local_mat[ROWS][COLS];
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            local_mat[i][j] = mat[i][j];
        }
    }

    int rank = 0;
    int pivot_row = 0;

    // Use Gaussian elimination on the local copy to find the rank
    for (int j = 0; j < COLS && pivot_row < ROWS; j++) {
        int i = pivot_row;
        while (i < ROWS && fabs(local_mat[i][j]) < 1e-9) {
            i++;
        }

        if (i < ROWS) { // Pivot found
            // Swap the pivot row with the current row if necessary
            if (i != pivot_row) {
                for (int k = 0; k < COLS; k++) {
                    double temp = local_mat[pivot_row][k];
                    local_mat[pivot_row][k] = local_mat[i][k];
                    local_mat[i][k] = temp;
                }
            }

            // Eliminate all other non-zero entries in this column
            for (int row_iter = 0; row_iter < ROWS; row_iter++) {
                if (row_iter != pivot_row) {
                    double factor = local_mat[row_iter][j] / local_mat[pivot_row][j];
                    for (int k = j; k < COLS; k++) {
                        local_mat[row_iter][k] -= factor * local_mat[pivot_row][k];
                    }
                }
            }
            pivot_row++;
            rank++;
        }
    }
    return rank;
}
