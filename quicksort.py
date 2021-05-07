def quicksort(A,l,r): #sortA[l:r]
  if r-l<=1: #base_Case
    return()
yellow =l+1 #partition_with_respect_to_pivot,a[l]
for green in range(l+1,r):
  if(A[green]<=A[l]):
    (A[yellow],A[green]) = (A[green],A[yellow])
    yellow=yellow+1
    
(A[l],A[yellow-1])=(A[yellow-1],A[l]) #move_pivot_into_place

Quicksort(A,l,yellow-1) #recursive_Calls
Quicksort(A,yellow,r)
