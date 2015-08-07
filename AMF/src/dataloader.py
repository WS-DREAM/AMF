########################################################
# dataloader.py
# Author: Jamie Zhu <jimzhu@GitHub>
# Created: 2014/2/6
# Last updated: 2014/7/20
########################################################

import numpy as np 
from utilities import *
import cPickle as pickle


########################################################
# Function to load the dataset
#
def load(para):
    datafile = para['dataPath'] + para['dataType'] + 'data.txt'
    logger.info('Loading data: %s'%datafile)
    dataTensor = -1 * np.ones((142, 4500, 64))
    fid = open(datafile, 'r')
    for line in fid:
        data = line.split(' ')
        rt = float(data[3])
        if rt > 0:
            dataTensor[int(data[0]), int(data[1]), int(data[2])] = rt
    fid.close()
    dataTensor = preprocess(dataTensor, para)
    logger.info('Loading data done.')
    logger.info('Data size: %d users * %d services * %d timeslices'\
        %(dataTensor.shape[0], dataTensor.shape[1], dataTensor.shape[2]))
    return dataTensor
########################################################


########################################################
# Function to preprocess the dataset
# delete the invalid values
# 
def preprocess(matrix, para):
    if para['dataType'] == 'rt':
        matrix = np.where(matrix == 0, -1, matrix)
        matrix = np.where(matrix >= 19.9, -1, matrix)
    elif para['dataType'] == 'tp':
        matrix = np.where(matrix == 0, -1, matrix)
    return matrix
########################################################
