import math

v=[390,390,390,385,380,380,380]
i=[3.8,3.8,3.9,4.5,5.6,6.5,7.5]
N=[1350,1422,1486,1438,1404,1372,1348]
k1=1
k2=1
w1=[0,0,0,400,900,1000,1700]
w2=[0,0,0,800,1000,1100,1900]
s1=[0,0,0,1,2,5,4]
s2=[0,0,0,5,9,11,15]

inputwatts=[]
Torque=[]
outputwatts=[]
efficiency=[]
slip=[]

def ipwatts(x,y):
    return x+y

def Tor(s1,s2):
    return math.fabs((s1-s2)*0.15*9.81)

def opwatts(n,t):
    return (2*3.1415926*n*t)/60

def eff(o,i):
    if(i==0):
        return 0
    else:
        return (o/i)*100

def sl(n):
    return ((1500-n)/1500)*100

for i in range(len(w1)):
    a=ipwatts(w1[i],w2[i])
    inputwatts.append(a)
    b=Tor(s1[i],s2[i])
    Torque.append(b)

for i in range(len(N)):
    a=opwatts(N[i],Torque[i])
    outputwatts.append(a)
    b=sl(N[i])
    slip.append(str(b)+"%, ")

for i in range(len(outputwatts)):
    a=eff(outputwatts[i],inputwatts[i])
    efficiency.append(str(a)+"%, ")

print("Input Watts = ",inputwatts)
print("Output Watts = ",outputwatts)
print("Torque = ",Torque)
print("Efficiency = ",efficiency,"%")
print("Slip = ",slip,"%")


f = open("EM Ex.3","w")
f.write("\nInput Watts = ")
f.writelines(str(inputwatts))
f.write("\nOutput Watts = ")
f.writelines(str(outputwatts))
f.write("\nTorque = ")
f.writelines(str(Torque))
f.write("\nEfficency = ")
f.writelines(efficiency)
f.write("\nslip = ")
f.writelines(slip)

f.close