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
from scipy.sparse import find

global school_names

def get_Data():
    '''
    TODO - change this docstring
    Extracts the data of all the mat files in the data directory.
    Then extracts the second major column from all the schools into a 2D matrix
    with the row showing the data and each row is a different school
    :return: school_second_major
    :type: numpy array
    '''
    global school_names
    schools = scipy.io.loadmat('schools.mat') #load the mat file with the schools in order
    school_data = {} #initialize dictionary to contain name with sparse matrix
    school_names= {} #dictionary of name? --- TODO - Remove if not needed ----
    #parse each entry
    for num,i in enumerate(schools['schools'],1): #iterate through the school names arrays
        fnamestring =  np.array_str(i[0]) #get the school name from the array ex: [u'Penn'] brackets included
        fname = fnamestring[3:-2] #slice the string to just get the only the name of the school
        school_data[fname + str(num)]=(scipy.io.loadmat(fname + str(num))['A']) #append the matfile to the array
        #school_names[fname] = num
    #print school_data
    #school_data = np.asarray((school_data))
    #print np.shape(school_data[99])
    #(rows, col) = np.shape(school_data[99])
    #print rows
    #print school_data[99].todense()
    #print school_data[99][1,:]
    #print school_data[99][1,:].toarray()
    #print school_data[99][1,2]
    return school_data

def get_School_Adj_Matrix(school_data, name):
    '''
    Adjacency lists are in compressed sparse column format
    '''
    return school_data[name]#order of 1-100 but index of 1-99

def create_Network(school_Mat):
    return


def main():
    plt.close('all')
    school_data = get_Data()
    (rows,col,values) = find(school_data['UIllinois20']) # find returns nonzero rows/columns/values
    #print (school_data['UIllinois20'])
    #print rows
    short_Rows = rows[:len(rows)/1000]
    short_Cols = col[:len(col)/1000]
    #print len(rows)
    #print len(short_Rows)
    
    #df_Large = pd.DataFrame({'from': rows, 'to':col})
    df = pd.DataFrame({'from': short_Rows, 'to': short_Cols})
    #print df
    G=nx.from_pandas_edgelist(df, 'from', 'to')
    degree_dict = dict(G.degree(G.nodes()))
    nx.set_node_attributes(G, degree_dict, 'degree')
 
    # Plot the network:
    fig = plt.figure()
    #Notes : fruchterman_reingold_layout(G) - layout based on larger hubs near center 
    nx.draw(G, with_labels=False, node_color='darkviolet', node_size=[size*10 for size in degree_dict.values()], edge_color='white', alpha = 0.5, linewidths=2, font_size=5,pos=nx.fruchterman_reingold_layout(G))
    #nx.draw(G, with_labels=False, node_size=1500, node_color="skyblue", pos=nx.circular_layout(G))
    fig.set_facecolor("#00000F")

    #for University in school_data: #for each university (key) in school_data
      #  school_Adj = school_data[University]
    

main()