# -*- coding: utf-8 -*-
"""
Pitch estimation from rate gyros' measurements

(c) S. Bertrand
"""


import math
import numpy as np
import matplotlib.pyplot as plt
import ImuData as imud


if __name__ == '__main__':

    # sampling period (s)
    # !!!!!!!!!!! A COMPLETER EN TD !!!!!!!!!!!!!!!!
    Te = 0.01
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # read data file
    #fileName = 'donneesIMUAuRepos.txt'
    fileName = 'donneesIMUPetitsAngles.txt'
    delimiter = '\t'
    imuMes = imud.ImuData(fileName, delimiter, Te)

    # init data structures for simulation
    computedPitchFromGyro = [0.0]   # initial angle assumed to be zero
    indicesK = [0]
    pitchImu = []
    pitchGyr = 0

    # main loop to parse data from IMU
    for i in range(0, len(imuMes.time)):

        # !!!!!!!!!!! A COMPLETER EN TD !!!!!!!!!!!!!!!!
        pitchGyr += imuMes.gyrY[i] * Te
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        # save to data structures used for simulation
        indicesK.append(i+1)
        pitchImu.append(math.radians(imuMes.pitchDeg[i]))
        computedPitchFromGyro.append(pitchGyr)

    # plots
    plt.figure(2)
    plt.plot(indicesK, computedPitchFromGyro, color='k')
    plt.plot(indicesK[1:len(indicesK)], pitchImu, color='b')
    plt.title('Black: computed from rate gyros, Blue: from IMU filter')
    plt.ylabel('Estimated pitch (rad)')
    plt.xlabel('Iteration')
    plt.grid(True)
    plt.show()
