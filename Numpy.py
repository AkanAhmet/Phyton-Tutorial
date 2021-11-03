import numpy as np

x = np.array([1,2,3,4])
print(x[0])
x = np.append(x,0)
print(x)
x = np.delete(x,2)
print(x)
x =  np.sort(x)
print(x)
print(x[x> np.mean(x)])

z = np.arange(50,100,5)
z =  z.reshape(5,2)
print(z)
z = z.reshape(10)
print(z[z%10 == 0])
print(z.sum())
z = z*2
print(z)

y = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(y.ndim)
print(y.size)
print(y.shape)

print(f"Mean: {np.mean(y)}")
print(f"Median: {np.median(y)}")
print(f"Variance: {np.var(y)}")
print(f"Standart Deviation: {np.std(y)}")

vac_nums = [0,0,0,0,0,
            1,1,1,1,1,1,1,1,
            2,2,2,2,
            3,3,3
            ]
            
sum_squares = 0
mean = sum (vac_nums ) / len ( vac_nums )
for num in vac_nums:
    dif = (num - mean)
    sum_squares = sum_squares + dif * dif
variance = sum_squares / len ( vac_nums )
print (f"Covid 19 Vaccinations Variance : {variance}" )