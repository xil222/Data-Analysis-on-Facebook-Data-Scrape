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
from matplotlib.widgets import RadioButtons

global school_dict

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

def store_School_With_Graph(school_data):
    global school_dict
    school_dict = {}
    for name in school_data:
        (rows,col,values) = find(school_data['UIllinois20']) # find returns nonzero rows/columns/values
        short_Rows = rows[:len(rows)/1000]
        short_Cols = col[:len(col)/1000]
        df = pd.DataFrame({'from': short_Rows, 'to': short_Cols})
        G=nx.from_pandas_edgelist(df, 'from', 'to')
        degree_dict = dict(G.degree(G.nodes()))
        nx.set_node_attributes(G, degree_dict, 'degree')
        school_dict[name] = G 
    return school_dict




def main():
    global school_dict 
    school_data = get_Data()
    school_dict = store_School_With_Graph(school_data) #contains graph of each school by name

    assert school_dict.has_key('UIllinois20')
    G = school_dict['UIllinois20']
    degree_dict = nx.get_node_attributes(G, 'degree')   
    nx.draw(G,ax = ax2 ,with_labels=False, node_color='darkviolet', node_size=[size*10 for size in degree_dict.values()], edge_color='red', alpha = 0.5, linewidths=2, font_size=5,pos=nx.fruchterman_reingold_layout(G))
    return

plt.close('all')    
fig = plt.figure(figsize=(8,8))
fig.set_facecolor("#00000F")
axis = plt.axis(facecolor='springgreen')
fig.add_axes(axis)
axes_list = fig.get_axes()
ax2= axes_list[0]
main()


axcolor = 'skyblue'
rax = plt.axes([0.05, 0.7, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ('UIllinois20', 'Penn94'))
#radio = RadioButtons(rax, tuple(school_dict.keys()))
plt.sca(ax2)
plt.show()

def network(label):
    global school_dict
    plt.cla()
    plt.sca(ax2)
    #axes_list = fig.get_axes()
    #print axes_list
    #print fig.axes
    G = school_dict[label]
    degree_dict = nx.get_node_attributes(G, 'degree')
    #Notes : fruchterman_reingold_layout(G) - layout based on larger hubs near center 
    nx.draw(G, ax=ax2, with_labels=False, node_color='darkviolet', node_size=[size*10 for size in degree_dict.values()], edge_color='red', alpha = 0.5, linewidths=2, font_size=5,pos=nx.fruchterman_reingold_layout(G))
    fig.set_facecolor("#00000F")
    plt.show()
radio.on_clicked(network)
