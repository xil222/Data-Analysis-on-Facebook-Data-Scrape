# -*- coding: utf-8 -*-
"""
Created on Sun May 27 00:15:29 2018

@author: Joy Nwarueze

This code gathers information on .mat files that come paired with an adjacency matrix
Those matrices are then used to create a visual display of the information in the adjacency matrix


Notes:
    - Degree: The average number of connections of each node. Degree of nodes displayed by size
    - Q: Why shrink down the total rows and columns to be displayed by dividing by 5000?
        A: 1. Memory, my computer couldn't handle drawing that many connections and would freeze up.
                It couldn't even handle all 2 million+ connections of Univ of Illinois (as a tester)
           2. While there is still loading overhead, it is much faster to load each plot onto a figure 
                without my computer showing "not responding" while also showing I think a decent amount of connections
Helpful sites:
    - Colors: https://python-graph-gallery.com/python-colors/
    - Networkx: https://networkx.github.io/documentation/networkx-1.10/reference/drawing.html#module-networkx.drawing.layout
                https://python-graph-gallery.com/
    - Modeling in Networkx: https://programminghistorian.org/en/lessons/exploring-and-analyzing-network-data-with-python
Further Improvements:
    - Base the intensity of the color of a node by its degree
    - 3D model if possible
    - Ordering the radio buttons either by the number when University joined facebook
        or by number of connections
    - Maybe other ways to visualize an adjacency matrix?
    - Speed/Efficiency: This is pretty slow
"""
import scipy.io
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from scipy.sparse import find
from matplotlib.widgets import RadioButtons

global school_dict

def get_Data():
    '''
    TODO - change this docstring
    Extracts the data of all the mat files in the data directory.
    Then stores the adjacency matrix of each mat file into a dict of {University: matrix}
    key and value pairs
    @return school_data: dictionary - A dictionary with University+num as key and Adjacency matrix
    as the value
    '''
    schools = scipy.io.loadmat('schools.mat') #load the mat file with the schools in order
    school_data = {} #initialize dictionary to contain name with sparse matrix
    
    #parse each entry
    for num,i in enumerate(schools['schools'],1): #iterate through the school names arrays
        fnamestring =  np.array_str(i[0]) #get the school name from the array ex: [u'Penn'] brackets included
        fname = fnamestring[3:-2] #slice the string to just get the only the name of the school
        school_data[fname + str(num)]=(scipy.io.loadmat(fname + str(num))['A']) #append the matfile to the array
    return school_data


def store_School_With_Graph(school_data):
    '''
    Creates a small graph for each University then store it in a dictionary with University as key
    and Graph as the value
    
    @param school_data: dictionary - A dictionary with University+num as key and Adjacency matrix
    as the value
    @return school_dict: dictionary - A dictionary with University+num as key and Graph as the value
    '''
    global school_dict
    school_dict = {}
    for name in school_data:
        (rows,col,values) = find(school_data[name]) # find returns nonzero rows/columns/values
        short_Rows = rows[:len(rows)/5000]
        short_Cols = col[:len(col)/5000]
        df = pd.DataFrame({'from': short_Rows, 'to': short_Cols})
        G=nx.from_pandas_edgelist(df, 'from', 'to')
        degree_dict = dict(G.degree(G.nodes())) #See Modeling in Networkx for further info
        nx.set_node_attributes(G, degree_dict, 'degree')
        school_dict[name] = G 
    return school_dict


def main():
    '''
    Calls the method to extract the data from .mat files, as well as create University+AdjMatrix and University+Graph dictionaries
    Also draws the starting University
    '''
    global school_dict 
    school_data = get_Data()
    school_dict = store_School_With_Graph(school_data) #contains graph of each school by name
    return

plt.close('all')    
fig = plt.figure(figsize=(10,10))
fig.set_facecolor("#00000F")

main()
#Building the radio buttons
axcolor = 'cyan'
first33pairs = {k: school_dict[k] for k in school_dict.keys()[:33]}
next33pairs = {k: school_dict[k] for k in school_dict.keys()[33:67]}
last33pairs = {k: school_dict[k] for k in school_dict.keys()[67:]}
#[0.05, 0.7, 0.15, 0.15] -> [left, bottom, width, height]
#left
rax = plt.axes([0.01, 0.1, 0.15, 0.85], facecolor=axcolor)
radio = RadioButtons(rax, tuple(first33pairs.keys()))

#right
rax = plt.axes([0.8, 0.1, 0.15, 0.85], facecolor=axcolor)
radio2 = RadioButtons(rax, tuple(next33pairs.keys()))

#middle
rax = plt.axes([0.4, 0.1, 0.15, 0.85], facecolor=axcolor)
radio3 = RadioButtons(rax, tuple(last33pairs.keys()))

font = {'family': 'serif',
        'color':  'lime',
        'weight': 'normal',
        'size': 16,
        }

# 3 radio callback functions that open a figure window for manipulation
def network(label):
    '''
    Draws the network of the selected University
    
    @param label: string - The name of the radio button for the University selected
    '''
    global school_dict   
    fig2 = plt.figure(2,figsize=(10,10)) #work on a specific figure
    fig2.clear() #clear previous display (if it had one)
    G = school_dict[label]
    degree_dict = nx.get_node_attributes(G, 'degree')
    nx.draw(G, with_labels=False, node_color='darkviolet', node_size=[size*10 for size in degree_dict.values()], edge_color='red', alpha = 0.5, linewidths=2, font_size=5,pos=nx.fruchterman_reingold_layout(G))
    string = label + "\n" + "Connections shown: " + str(G.number_of_edges())
    fig2.suptitle(string, fontsize = 14, fontweight = 'bold', fontdict=font)
    fig2.set_facecolor("#00000F")
    plt.draw()
radio.on_clicked(network)


def network2(label):
    '''
    Draws the network of the selected University
    
    @param label: string - The name of the radio button for the University selected
    '''
    global school_dict  
    fig3 = plt.figure(3, figsize= (10,10))
    fig3.clear() 
    G = school_dict[label]
    degree_dict = nx.get_node_attributes(G, 'degree')
    nx.draw(G, with_labels=False, node_color='darkviolet', node_size=[size*10 for size in degree_dict.values()], edge_color='red', alpha = 0.5, linewidths=2, font_size=5,pos=nx.fruchterman_reingold_layout(G))    
    string = label + "\n" + "Connections shown: " + str(G.number_of_edges())
    fig3.suptitle(string, fontsize = 14, fontweight = 'bold', fontdict=font)
    fig3.set_facecolor("#00000F")
    plt.draw()
radio2.on_clicked(network2)


def network3(label):
    '''
    Draws the network of the selected University
    
    @param label: string - The name of the radio button for the University selected
    '''
    global school_dict
    fig4 = plt.figure(4, figsize= (10,10))
    fig4.clear()  
    G = school_dict[label]
    degree_dict = nx.get_node_attributes(G, 'degree')
    nx.draw(G, with_labels=False, node_color='darkviolet', node_size=[size*10 for size in degree_dict.values()], edge_color='red', alpha = 0.5, linewidths=2, font_size=5,pos=nx.fruchterman_reingold_layout(G))  
    string = label + "\n" + "Connections shown: " + str(G.number_of_edges())
    fig4.suptitle(string, fontsize = 14, fontweight = 'bold', fontdict=font)
    fig4.set_facecolor("#00000F")
    plt.draw()
radio3.on_clicked(network3)




'''
list of layouts to play around with at the end of those long nx.draw lines that help with visualization
Notes : fruchterman_reingold_layout/spring_layout - Force directed Graphs

pos=nx.fruchterman_reingold_layout(G) - default layout based on force graph
pos=nx.circular_layout(G) - pretty good showing of density UCSD is like 10 lines lol though its right side oriented... +
pos=nx.spring_layout(G) - looks exactly the same as the F_R layout tbh so its fine
'''



plt.show() #just in case