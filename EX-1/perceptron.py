import numpy as np
x1 = np.array([0,1,1,0])
x2 = np.array([0,1,0,1])
y = np.array([0,1,1,1])
ep = int(input("Enter epoch: "))
b = 1
l = 0.4
a=[]
a.append(float(input("Enter weight Bias: ")))
a.append(float(input("Enter weight X1: ")))
a.append(float(input("Enter weight X2: ")))
w = np.array(a)
n = x1.shape[0]
for k in range(ep):
    for i in range(n):
        f=x1[i]*w[1]+x2[i]*w[2]+b*w[0]
        yt = (f>0).astype("int")
        er = y[i]-yt
        if(er!=0):
            w[1] = w[1]+l*er*x1[i]
            w[2] = w[2]+l*er*x2[i]
            w[0] = w[0]+l*er*b
        print("-------------------")
        print("updated weight ",i+1,"instance")
        print("X1 weight ",round(w[1],2))
        print("X2 weight ",round(w[2],2))
        print("bias weight ",round(w[0],2))

print("---------------")
print("Final weight after",ep,"epochs(s)")
print("updated weight for x1: ",round(w[1],2))
print("updated weight for x2: ",round(w[2],2))
print("updated weight for Bias: ",round(w[0],2))
