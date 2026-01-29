from statistics import mode, multimode, variance, stdev
data=[4,6,8,8,9,10,10,11,12,12,13,14,15,18,30]
print("dataset=",data)
mean_value=sum(data)/len(data)
print("mean=",mean_value)
sorted_data=sorted(data)
n=len(sorted_data)
if n%2==1:
    median_value=sorted_data[n//2]
else:
    median_value=sorted_data[(n//2)-1]+sorted_data[n//2]/2
print("median=",median_value)
print("mode=",multimode(data))
print("variance_lib=",round(variance(data),2))
squared_diffs=[]
for x in data:
    squared_diffs.append((x-mean_value)**2)
sum_squared_diff=sum(squared_diffs)
variance_man=round(sum_squared_diff/(len(data)-1),2)
std_dev_manual=round(variance_man**0.5,2)
print("variance_man=",variance_man)
print("standard_dev_Man=",std_dev_manual)
print("standard_deviation_lib=",round(stdev(data),2))
Q2=median_value
lower_half=sorted(data[:n//2])
Upper_half=sorted(data[n//2:])
Q1=lower_half[len(lower_half)//2]
Q3=Upper_half[len(Upper_half)//2]
IQR=Q3-Q1
print("Q1=",Q1)
print("Q2(median)=",Q2)
print("Q3=",Q3)
print("IQR=",IQR)
Lower_bound=Q1-1.5*IQR
Upper_bound=Q3+1.5*IQR
print("Lower_bound=",Lower_bound)
print("upper_bound=",Upper_bound)


-----------numpy---------


import numpy as np
data=np.array([4,6,8,8,9,10,10,11,12,12,13,14,15,18,30])
print("dataset=",data)
mean_val=np.mean(data)
print("mean=",mean_val)
median_val=np.median(data)
print("median=",median_val)
values,counts=np.unique(data,return_counts=True)
modes=values[counts==counts.max()]
print("mode=",modes.tolist())
variance_val=np.var(data,ddof=1)
std_dev_val=np.std(data,ddof=1)
print("variance=",round(variance_val,2))
print("stadard deviation=",round(std_dev_val,2))
Q1=np.percentile(data,25)
Q2=np.percentile(data,50)
Q3=np.percentile(data,75)
print("Q1=",Q1)
print("Q2=",Q2)
print("Q3=",Q3)
IQR=Q3-Q1
print("IQR=",IQR)
lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR
print("Upper Bound=",upper_bound)
print("Lower Bound=",lower_bound)
