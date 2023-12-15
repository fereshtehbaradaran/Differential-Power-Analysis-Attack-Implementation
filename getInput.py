import struct
import matplotlib.pyplot as plt
import numpy as np


# def loadTrace(fileName, numberOfTraces, traceSize):
    
#     with open(fileName, mode='rb') as file:
#         fileContent = file.read()

#     return [[struct.unpack("B" , fileContent[i:i + 1])[0] for i in range(j * traceSize, (j + 1) * traceSize)] for j in range(numberOfTraces)]

# with open("traces.bin", mode='rb') as file:
#     fileContent = file.read()
    
# y = [struct.unpack("B" , fileContent[i - 1:i])[0] for i in range(1, traceSize + 1)]
# x = [i for i in range(traceSize)]


# xpoints = np.array(x)
# ypoints = np.array(y)

# plt.plot(xpoints, ypoints)
# plt.show()


def loadData(fileName):
    
    result = []
    
    with open(fileName, mode='r') as file:
        result = [[int('0x' + item, 16) for item in line.split()] for line in file]
    
    return result



def loadTrace(fname, trlen, start, length, n):
    
    with open(fname, 'rb') as myfile:
        
        traces = np.zeros((n, length), dtype=np.uint8)
        
        for i in range(n):
            myfile.seek(start, 1)  # Seek from current position
            
            if length + start > trlen:
                t = np.fromfile(myfile, dtype = np.uint8, count = length - start)
            else:
                t = np.fromfile(myfile, dtype = np.uint8, count = length)
                
            myfile.seek(trlen - length - start, 1)  # Seek from current position
            traces[i, :len(t)] = t  # In case t is shorter than length
            
    return traces