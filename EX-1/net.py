import numpy as np

def sig(x):
    return 1/(1+np.exp(-x))

def sig_der(x):
    return x*(1-x)
    
t_ip = np.array([[0,0,1],[1,1,0],[1,0,1],[0,0,1]])
t_op = np.array([[0,1,1,0]]).T

np.random seed(1)

wei = 2*np.random.random((3,1)) - 1

print('Random Wights:')
print(wei)

for itr in range(1000):
    ipl = t_ip
    op = sig(np.dot(ipl,wei))
    er = t_op - op
    adj = er * sig_der(op)
    wei += np.dot(ip.T,adj)

print('Weights After update:')
print(wei)

print('output')
print(op)    
    
