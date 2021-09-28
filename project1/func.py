data = [[2, 4], [0,1], [5, -2], [2,-2]]
alpha = [3, 2, 4, 5]
y = [1, 1, 1, -1]
def dot(x,y):
    dot = 0
    for i in range(0,len(x)):
        dot += x[i] * y[i]
    return dot

def kernel_linear(data, x):
    result = []
    for i in data:
        result.append(dot(i,x))
    return result 

