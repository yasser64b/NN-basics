import numpy as np 
class Cost(object):
    def __init__ (self,cost_func='Linear'):
        self.cost_func=cost_func
    def cost_fn(self,a,y):
        if (self.cost_func=='Linear'):
            return np.sum(a-y)/len(a)
        elif (self.cost_func=='quadratic'):
            return np.sum(0.5*((a-y)**2))/len(a)

        elif (self.cost_func == "cross_entropy"):
            return np.sum(np.nan_to_num(-y*np.log(a)-(1-y)*np.log(1-a)))/len(a)


    def cost_prime(self, a, y):
        if (self.cost_func=='Linear'):
            return 1
        elif (self.cost_func == 'quadratic'):
            return np.sum(a -y)/len(a)
        elif (self.cost_func == 'cross_entropy'):
            return np.sum(np.nan_to_num(-(y-a) / ((1 - a) * a)))/len(a)

a=np.array([0.5,0.1,0.2,0.34,0.1])
y=np.array([10,2,3,45,6])
# A=Cost('Linear')
# A=Cost('quadratic')
A=Cost('cross_entropy')
Cost_f=A.cost_fn(a,y)
print(Cost_f)

Cost_prime=A.cost_prime(a,y)
print(Cost_prime)

# See full Toturial at my Youtube Channel(YB TV): https://www.youtube.com/channel/UCvnhhDKv5takEN412dmVW8g
# GitHab Page:https://github.com/yasser64b/
#Email: big3del@gmail.com