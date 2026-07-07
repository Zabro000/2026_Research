import math
import numpy as np

PTS = 128
PI = math.pi

VREF = 3.3
DACRES_12B = 4096

LINK = "https://deepbluembedded.com/stm32-dac-tutorial-example-hal-code-analog-signal-genreation/"

Fclk = 0

def lut():
    x = np.linspace(0, 2*math.pi, PTS)
    y = np.arange(0)
    dor = np.arange(0)
    ## generate the raw points
    for i in range(x.size):
        if(x[i] <= PI):
            y = np.append(y, x[i])
        else:
            y = np.append(y, 2*PI - x[i])
    
    for i in range(y.size):
        temp = y[i] / (VREF / 4096)
        dor = np.append(dor, int(temp))


    print(dor)

    ## generate file with the numbers
    dor.tofile('saw_lut.csv', sep = ",")



def test():
    lut()



def main():
    test()


if __name__ == "__main__":
    main()

