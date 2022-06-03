# -*- coding: utf-8 -*-
"""
Pitch estimation from gyro and accelero measurements
using Kalman FIlter (small angles assumption)

(c) S. Bertrand
"""


import math
import KalmanFilter as kf
import numpy as np
import matplotlib.pyplot as plt
import ImuData as imud



if __name__=='__main__':

    # sampling period (s)
    '''
    # !!!!!!!!!!! A COMPLETER EN TD !!!!!!!!!!!!!!!!
    Te = 
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    '''
       
    # read data file
    #fileName = 'donneesIMUAuRepos.txt'
    fileName = 'donneesIMUPetitsAngles.txt'
    delimiter = '\t'
    imuMes = imud.ImuData(fileName, delimiter, Te)

    # system definition
    # state : pitch angle (rad), gyro's bias (rad/s)
    # input: pitch rate (rad/s) from gyro measurement
    # measurement : pitch angle (rad) computed from accelero measurements
    
    '''
    # !!!!!!!!!!! A COMPLETER EN TD !!!!!!!!!!!!!!!!
    nx = 
    nu = 
    ny =     
    Ak = 
    Bk = 
    Ck = 
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    '''
    
    # noises std dev
    
    '''
    # !!!!!!!!!!! A COMPLETER EN TD !!!!!!!!!!!!!!!!
    gyroPitchRateStdDev =             # (rad/s)
    gyroPitchRateBiasStdDev = 0.00005  # (rad/s)
    acceleroPitchStdDev =             # (rad)
    biasRateGyro =              # (rad)
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    '''
    
    # covariance matrices
    Qk = Te * np.array( [ [math.pow(gyroPitchRateStdDev,2), 0.0], [0.0, math.pow(gyroPitchRateBiasStdDev,2)] ] )
    Rk = np.array([math.pow(acceleroPitchStdDev,2)])

    # initial state estimate and covariance matrix
    x0 = np.array([ [0.0],[-biasRateGyro] ])
    P0 = np.array( [ [0.5,0.0],[0.0,0.1] ] )  
    
    # filter instantiation
    pitchKF = kf.KalmanFilter(nx, nu, ny)
    pitchKF.setStateEquation(Ak, Bk)
    pitchKF.setCk(Ck)
    pitchKF.setQk(Qk)
    pitchKF.setRk(Rk)
    pitchKF.initFilter( x0 , P0 )
    

    # init data structures for simulation
    estimatedPitch = []
    estimatedPitch.append(x0[0,0])
    estimatedBias = []
    estimatedBias.append(x0[1,0])
    indicesK = [0]
    
    pitchImu = []
     
    computedPitchFromAcc = []    
    computedPitchFromGyro = [0.0] # initial angle assumed to be zero


   
    # main loop to parse data from IMU
    for i in range(0, len(imuMes.time)):
    
    
        '''
        # !!!!!!!!!!! A COMPLETER EN TD !!!!!!!!!!!!!!!!
        
        # read pitch rate measurement from gyro         
        uk = 

        # prediction step of KF
        pitchKF.   ....
    
        
        # compute pitch from acc measurements
        yk = 

        # update step of KF
        pitchKF.   ...

        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        '''

        # save to data structures used for simulation
        estimatedPitch.append( pitchKF.xk[0,0])
        estimatedBias.append(pitchKF.xk[1,0])
        indicesK.append(i+1)       
        pitchImu.append( math.radians(  imuMes.pitchDeg[i] ) )
        


    # plots
    fig2, graph = plt.subplots(1)
    graph.plot(indicesK, estimatedPitch, color='r')
    graph.plot(indicesK[1:len(indicesK)], pitchImu, color='b')
    graph.set_title('Red: from Kalman Filter, Blue: from IMU filter')
    graph.set_ylabel('Pitch angle (rad)')
    graph.set_xlabel('Iteration')
    graph.grid(True)    

    
    
    fig3, graph = plt.subplots(1)
    graph.plot(indicesK, estimatedBias, color = 'r')
    graph.grid(True)
    graph.set_ylabel('gyro bias estimate (rad/s)')
    graph.set_xlabel('iteration')