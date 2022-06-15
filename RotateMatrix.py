
class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        len_A = len(A[0])
        for i in range(len_A // 2):
            for n in range(i, len_A - i - 1):
                temp = A[i][n]
                A[i][n] = A[len_A - 1 - n][i]
                A[len_A - 1 - n][i] = A[len_A - 1 - i][len_A - 1 - n]
                A[len_A - 1 - i][len_A - 1 - n] = A[n][len_A - 1 - i]
                A[n][len_A - 1 - i] = temp
        return A
