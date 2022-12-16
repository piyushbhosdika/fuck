import random
import matplotlib.pyplot as plt
def histogram(list):
    plt.hist(list, bins=5, color='red', edgecolor='black') 
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.show()

n=0
l = []
n = int(input('Enter Number of Elements: ')) 
for i in range(0, n, 1):
    x=int(input("Enter number {}:").format(i+1))
    l.append(x) 
histogram(l)