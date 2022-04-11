import numpy as np
q1 = float(0.000002)
q2 = float(-0.00000350) 
r = float(0.250)

K_ = float(9000000000) 

def PotencialUb(a,b,r):
    return (K_*a*b)/r

# print ("valor de : "+np.format_float_scientific(K_,precision=1,exp_digits=1))

print(np.format_float_scientific(PotencialUb(q1,q2,r)),"J")
