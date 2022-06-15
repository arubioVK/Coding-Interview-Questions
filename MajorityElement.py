
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        len_A = len(A)
        mayority_limit = round(len_A/2)
        dict_freq = {}
        for i in range(len_A):
            freq_A = dict_freq.get(A[i],0)+1
            if (freq_A>=mayority_limit):
                return A[i]
            dict_freq[A[i]] = freq_A
        raise Exception("Error")
