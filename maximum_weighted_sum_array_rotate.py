# Given an array, return the maximum weighted sum that can be obtained by rotating the array 

def maxweighedsumarrshift(array):
  arrsum = 0
  weightedsum = 0
  
  for idx in range(len(array)):
    arrsum += array[idx]
    weightedsum += array[idx]*idx
  
  maxval = float("-inf")
  for j in range(len(array)-1,0,-1):
    weightedsum = weightedsum + arrsum - (len(array)*array[j])
    maxval = max(maxval, weightedsum)
  return maxval
