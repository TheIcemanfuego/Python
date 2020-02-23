from matplotlib import pyplot as plt
import math



def nominal_interest_graph(i):
    x = [1, 2, 3, 4, 6, 12]
    y = []
    p = 0.01
    
    for j in range(0, len(x)):
        y.append(x[j] * (math.exp(1/x[j] * math.log((1 + i))) - 1))
        
    for j in range(0, len(x)):
        print("({0}, {1})".format(x[j], y[j]))
    
    plt.ylim((1-p) * min(y), (1+p) * max(y))
    plt.title('Nominal interest rate')
    plt.xlabel('conversion period m')
    plt.ylabel('interest rate')
    plt.plot(x, y, '-o')
    




if __name__ == "__main__":
    nominal_interest_graph(0.06)