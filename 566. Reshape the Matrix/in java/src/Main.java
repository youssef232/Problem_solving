public class Main {

    public static void main(String[] args) {


    }

    public static int[][] matrixReshape(int[][] mat, int r, int c) {
        int m = mat.length;
        int n = mat[0].length;
        int [][] output = new int[r][c];
        int pointer = 0;
        if ((m * n) != (r * c))
            return mat;
        int [] oneDim = new int[m * n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                oneDim[pointer] = mat[i][j];
                pointer++;
            }
        }
        pointer = 0;
        for (int i = 0; i < r ; i++) {
            for (int j = 0; j < c; j++) {
                output[i][j] =oneDim[pointer];
                pointer++;
            }
        }
        return output;
    }
}
