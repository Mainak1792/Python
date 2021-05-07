def merge(A,B): #mergeA[0:m],B[0:n]
  (c,m,n)=([],len(A),len(B))
  (i,j)=(0,0)#current_position_of_A,B
  while i+j<m+n: #i+j_is_number_of_elements_merged_so_far
    if i==m: #case1:A_is_empty
      C.append(B[j])
      j=j+1
    elif j ==n: #case2:B_is_empty
      C.append(A[i])
      i=i+1
    elif (A[i]<=B[j]): #case3:Head_of_A_is_smaller
      C.append(A[i])
      i=i+1
     elif A[i]>B[j]: #case4:Head_of_B_is_smaller
      C.append(B[j])
      j=j+1
    return(C)
