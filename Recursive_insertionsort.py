def insertionsor(seq):
  isort(seq,len(seq))
def isort(seq,k): #sort_slice_seq[0:k]
  if k>1:
    isort(seq,k-1) #recursion
    insert(seq,k-1)

def insert(seq,k): #sorting_algo
  pos=k
  while pos>0 and seq[pos]<seq[pos-1]:
    (seq[pos],seq[pos-1]) = (seq[pos-1],seq[pos])
    pos=pos-1
