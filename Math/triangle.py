import math
import numpy as np

PTS = 64
PI = math.pi

Fclk = 

def lut():
    x = np.linspace(0, 2*math.pi, PTS)
    y = np.arange(0)
    ## generate the raw points
    for i in range(x.size):
        if(x[i] <= PI):
            y = np.append(y, x[i])
        else:
            y = np.append(y, 2*PI - x[i])

    print(y)

    ## generate
    y.tofile('saw_lut.csv', sep = ",")



def param():
    F_trig 
    


def test():
    lut()



def main():
    test()


if __name__ == "__main__":
    main()

