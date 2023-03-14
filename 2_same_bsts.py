# Check if 2 arrays represent the same Binary Search Trees. You are not allowed to construct Binary Search Trees.

def sameBsts(arrayOne, arrayTwo):
  return rechelper(arr1, arr2)
 
def rechelper(arr1, arr2):
  if len(arr1) != len(arr2):
    return False
  
  if len(arr1) == 0:
    return True
  
  if arr1[0] != arr2[0]:
    return False
  
  rootval = arr1[0]
  
  smaller1 = []
  larger1 = []
  for idx in range(1, len(arr1)):
    ele = arr1[idx]
    if ele >= rootval:
      larger1.append(ele)
    else:
      smaller1.append(ele)
  
  smaller2 = []
  larger2 = []
  for idx in range(1, len(arr2)):
    ele = arr2[idx]
    if ele >= rootval:
      larger2.append(ele)
    else:
      smaller2.append(ele)
  
  
  return True and rechelper(smaller1, smaller2) and rechelper(larger1, larger2)
