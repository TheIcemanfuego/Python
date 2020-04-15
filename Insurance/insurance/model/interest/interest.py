from matplotlib import pyplot as plt
import math


class Interest():
    
    def __init__(self):
        pass

    #(I^{(q)}ae)^{(m)}_{inf}
    #
    # i - nominal interest rate
    # m - the number of interest conversion periods per year
    # q - the number of increments per year
    def increasing_perpetuity_due(self, i, m, q):
        """increasing_perpetuity_due(i, m, q)"""
        
        return 1/(self.perpetuity_due(i, m) * self.perpetuity_due(i, m))
    
    
    #ae^{(m)}_{inf}
    # 
    # i - nominal interest rate    
    # m - the number of interest conversion periods per year
    def perpetuity_due(self, i, m):
        """
        perpetuity_due(i, m)
        Parameters
        ----------
        i : float
            `i` is the nominal interest rate.
        m : int
            `m` is the number of interest conversion periods per year.
            
        Returns
        -------
        float
            Returns the perpetuity due.
        """
        
        dm = self.interest_in_advance(i, m)
        
        return 1/dm
        
        
    #a^{(m)}_{inf}
    # 
    # i - nominal interest rate
    # m - the number of interest conversion periods per year
    def immediate_perpetuity(self, i, m):
        """immediate_perpetuity(i, m)"""
        
        return 1/self.interest_in_arrears(i, m)
    
    
    
    #d^{(m)}
    #
    # i - nominal interest rate 
    # m - the number of interest conversion periods per year    
    def interest_in_advance(i, m):
        """interest_in_advance(i, m)"""
        
        return m * (1 - math.exp(-(1/m) * math.log(1 + i)))
    
    
    #i^{(m)}
    # 
    # i - nominal interest rate
    # m - the number of interest conversion periods per year
    def interest_in_arrears(i, m):
        """interest_in_arrears(i, m)"""
    
        return m * (math.exp(1/m * math.log((1 + i))) - 1)
    
    
    # d^{(m*)} where m* is a list
    # i - nominal interest rate
    # 
    def graph_interest_in_advance(i):
        """graph_interest_in_advance(i)"""
        
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
    
    
    # i^{(m*)} where m* is a list
    def graph_interest_in_arrears(i):
        """graph_interest_in_arrears(i)"""
        
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
    print(Interest.interest_in_arrears(0.06, 1))
    print(Interest.interest_in_advance(0.06, 1))