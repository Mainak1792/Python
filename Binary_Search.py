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
   
