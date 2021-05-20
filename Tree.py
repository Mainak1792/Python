def delete(self,v):
  if self.isempty(): #
    return
  if v<self.value():
    self.left.delete(v)
    return
  if v>self.value:
    self.right.delete(v)
    return
  if v==self.value:
    if self.isleaf():
      self.makeempty()
     elif self.left.isempty():
      self.copyright()
     else:
      self.value = self.left.maxval()
      self.left.delete(self.left.maxval())\
      return
def makeempty(self):
  self.value=None
  self.left=None
  self.right=None
  return
def copyright(self):
  self.value= self.right.value
  self.left=self.right.left
  self.right=self.right.right
  return
