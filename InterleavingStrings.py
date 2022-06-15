
class Solution:
	# @param A : string
	# @param B : string
	# @param C : string
	# @return an integer
	def isInterleave(self, A, B, C):
        index_A = 0
        index_B = 0
        len_A = len(A)
        len_B = len(B)
        for i in range(len(C)):
            #Tour A completed
            if ((len_A)<=index_A):
                if (C[i]==B[index_B]):
                    index_B+=1
                else:
                    return 0
            #Tour B completed
            elif ((len_B)<=index_B):
                if  C[i]==A[index_A]:
                    index_A+=1
                else:
                    return 0
            #Same next character in A B
            elif ((C[i]==A[index_A]) and (C[i]==B[index_B])):
                route_A = Solution().isInterleave(A[index_A+1:],B[index_B:],C[(i+1):])
                if route_A==1:
                   return 1
                route_B = Solution().isInterleave(A[index_A:],B[index_B+1:],C[(i+1):])
                return route_B  
            #Next A 
            elif (C[i]==A[index_A]):
                index_A+=1
            #Next B
            elif (C[i]==B[index_B]):
                index_B+=1
            else:
                return 0
        return 1
