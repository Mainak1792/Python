def bsearch(seq,v,l,r):
  #search for v in seq[l:r], seq is sorted
  if(r-l)==0:
    return(false) #The_element_is_not_found
   mid = (l+r)//2 #integer_division_to_find_mid_point
   if(v == seq[mid]):
    return(True) #the_element_is_in_mid_point
   if(v < seq[mid]):
      return (bsearch(seq,v,l,mid)) #iterate_Till_mid-1
   else:
      return(bsearch(seq,v,mid+l,r)) #iterate_till_mid+1
   
def binary_search(lst,target):
    """"
    Returns index of the element present in the list
    """
    first= 0
    last= len(lst)-1
    while first<=last:
        midpoint = (first+last)//2
        if lst[midpoint]==target:
            return midpoint
        elif lst[midpoint]<target:
            first=midpoint+1
        else:
            last=midpoint-1
    return None

def bsearc(lst,v):
    if len(lst)==0:
        return False
    m= len(lst)//2
    if lst[m]==v:
        return True
    else:
        if lst[m]<v:
            return bsearc(lst[m+1:],v)
        else:
            return bsearc(lst[:m+1],v)



numbers=[1,2,3,7,4,56,778]
print(bsearc(numbers,7))
