import math
import numpy as np

def code():
    PTS = 128 * 2
    PI = math.pi
    x = np.linspace(0, 2*math.pi, PTS)
    y = np.arange(0)
    for i in range(x.size):
        if(x[i] <= PI):
            y = np.append(y, x[i])
        else:
            y = np.append(y, 2*PI - x[i])

    print(y)
    y.tofile('saw_lut.csv', sep = ",")

    


def test():
    code()



def main():
    test()


if __name__ == "__main__":
    main()

