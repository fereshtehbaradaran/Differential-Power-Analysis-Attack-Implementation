from calculateSboxOutput import calculateSboxOutput
from getInput import loadData, loadTrace
import numpy as np
import time


numberOfTraces  = 200
traceSize = 370 * 1000
offset = 40 * 1000
segmentLength = 50 * 1000


plainText = loadData("plaintext.txt")
traces = loadTrace("traces.bin", traceSize, offset, segmentLength, numberOfTraces)

print("Plain text and Traces loaded")

start = [0, 0, 0, 0, 0, 0, 0, 0, 20 * 1000, 0, 0, 0, 25 * 1000, 35 * 1000 , 0, 0]
end = [segmentLength, segmentLength, segmentLength, segmentLength, segmentLength, segmentLength, segmentLength, segmentLength, 25 * 1000, segmentLength, segmentLength, segmentLength, 30 * 1000, 40 * 1000 , segmentLength, segmentLength]
bitNum = [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7 , 1, 0]

key = [0 for i in range (16)] # 16 byte

for i in range(len(key)):
    
    strartTime = time.time()
    meanDiffs = np.zeros(256)
    
    for guess in range(256):
        
        one_list = []
        zero_list = []
        
        for traceIndex in range(numberOfTraces):
            temp = calculateSboxOutput(plainText[traceIndex][i], guess)
    
            if temp & (1 << bitNum[i]):        
                one_list.append(traces[traceIndex])
            else:
                zero_list.append(traces[traceIndex])
                
            
        one_avg = np.asarray(one_list).mean(axis=0)
        zero_avg = np.asarray(zero_list).mean(axis=0)
        temp = abs(one_avg - zero_avg)
        meanDiffs[guess] = np.max(temp[start[i]:end[i]])
        
          
    key[i] = np.where(meanDiffs == max(meanDiffs))[0][0]
    print("byte", i, ":", key[i])
    print(time.time() - strartTime)
 
print("Key =", *list(map(hex, key)))