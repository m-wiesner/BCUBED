import bcubed
import b3
import numpy as np
import pdb

num_cases = 10

num_clusters = np.random.randint(1,10,(num_cases,))
num_labels = np.random.randint(1,10,(num_cases,))
num_elements = np.random.randint(1000,2000,(num_cases,))

for i in xrange(num_cases):
  L = np.random.randint(1,num_clusters[i]+1,(num_elements[i],))
  K = np.random.randint(1,num_labels[i]+1,(num_elements[i],))
  
  [my_f,my_p,my_r] = b3.calc_b3(L,K)
  
  Ldict = { i:set([L[i]])  for i in xrange(num_elements[i])}
  Cdict = { i:set([K[i]])  for i in xrange(num_elements[i])}
  
  p = bcubed.precision(Cdict,Ldict)
  r = bcubed.recall(Cdict,Ldict)
  f = bcubed.fscore(p,r)
 
  # Check 
  if(abs(p - my_p) > 0.0001 or abs(r - my_r) > 0.001 or abs(f - my_f) > 0.0001):
    print("ERROR") 

