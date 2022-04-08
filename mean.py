from operator import le


m = 0
def mean(x:list):
        for i in range(len(x)):
                m = m + x[i]
        m = m/len(x)
        return m