# -*- coding: utf-8 -*-
"""
Created on Sun May 27 00:15:29 2018

@author: Super
"""
import scipy.io
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd


def get_Adjacency_Matrices():
    '''
    TODO - change this docstring
    Extracts the data of all the mat files in the data directory.
    Then extracts the second major column from all the schools into a 2D matrix
    with the row showing the data and each row is a different school
    :return: school_second_major
    :type: numpy array
    '''
    schools = scipy.io.loadmat('schools.mat') #load the mat file with the schools in order
    school_data = [] #initialize array
    for num,i in enumerate(schools['schools'],1): #iterate through the school names arrays
        fnamestring =  np.array_str(i[0]) #get the school name from the array ex: [u'Penn'] brackets included
        fname = fnamestring[3:-2] #slice the string to just get the only the name of the school
        if fname == 'UIllinios':
            fname = 'UIllinois'
        school_data.append(scipy.io.loadmat(fname + str(num))['A']) #append the matfile to the array

    school_data = np.asarray((school_data))
    print np.shape(school_data[0])
    return



def main():
    plt.close('all')
    get_Adjacency_Matrices()


main()