from calculateSboxOutput import calculateSboxOutput
from getInput import loadData, loadTrace
import numpy as np
import time


numberOfTraces  = 200
traceSize = 370 * 1000


plainText = loadData("plaintext.txt")
traces = loadTrace("traces.bin", numberOfTraces, traceSize)

print("Plain text and Traces loaded")

key = [0 for i in range (16)] # 16 byte

for i in range(len(key)):
    
    strartTime = time.time()
    meanDiffs = np.zeros(256)
    
    for guess in range(256):
        
        one_list = []
        zero_list = []
        
        for traceIndex in range(numberOfTraces):
            temp = calculateSboxOutput(plainText[traceIndex][i], guess)
    
            if temp & 0x01:        
                one_list.append(traces[traceIndex])
            else:
                zero_list.append(traces[traceIndex])
                
            
        one_avg = np.asarray(one_list).mean(axis=0)
        zero_avg = np.asarray(zero_list).mean(axis=0)
        meanDiffs[guess] = np.max(abs(one_avg - zero_avg))
        
        
    key[i] = np.where(meanDiffs == max(meanDiffs))[0][0]
    print("byte", i, ":", key[i])
    print(time.time() - strartTime)
   
print("Key =", *list(map(hex, key)))