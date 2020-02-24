from matplotlib import pyplot as plt
import math





def perpetuity_due(i, m):
    
    dm = interest_in_advance(i, m)
    
    return 1/dm
    
    

def immediate_perpetuity(i, m):
    
    im = interest_in_arrears(i, m)
    
    return 1/im




def interest_in_advance(i, m):
    
    return m * (1 - math.exp(-(1/m) * math.log(1 + i)))



def interest_in_arrears(i, m):

    return m * (math.exp(1/m * math.log((1 + i))) - 1)


def graph_interest_in_advance(i):
    m = [1, 2, 3, 4, 6, 12]
    y = []
    p = 0.01
    
    for j in range(0, len(m)):
        y.append(m[j] * (1 - math.exp(-(1/m[j]) * math.log(1 + i))))

    for j in range(0, len(m)):
        print("({0}, {1})".format(m[j], y[j]))
        
    plt.ylim((1-p) * min(y), (1+p) * max(y))
    plt.title('Interest rate in advance')
    plt.xlabel('conversion period m')
    plt.ylabel('equivalent nominal interest rate in advance')
    plt.plot(m, y, '-o')        

def graph_interest_in_arrears(i):
    m = [1, 2, 3, 4, 6, 12]
    y = []
    p = 0.01
    
    for j in range(0, len(m)):
        y.append(m[j] * (math.exp(1/m[j] * math.log((1 + i))) - 1))
        
    for j in range(0, len(m)):
        print("({0}, {1})".format(m[j], y[j]))
    
    plt.ylim((1-p) * min(y), (1+p) * max(y))
    plt.title('Interest rate in arrears')
    plt.xlabel('conversion period m')
    plt.ylabel('equivalent nominal interest rate in arrears')
    plt.plot(m, y, '-o')
    




if __name__ == "__main__":
    print(interest_in_arrears(0.06, 1))
    print(interest_in_advance(0.06, 1))