import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd

def get_data():
    '''
    Extracts the data of all the mat files in the data directory.
    Then extracts the second major column from all the schools into a 2D matrix
    with the row showing the data and each row is a different school
    :return: school_second_major
    :type: numpy array
    '''
    schools = scipy.io.loadmat('schools.mat') #load the mat file with the schools in order

    school_data = [] #initialize array
    for num,i in enumerate(schools['schools'],1): #iterate through the school names arrays
        fnamestring =  np.array_str(i[0]) #get the school name from the array
        fname = fnamestring[3:-2] #slice the string to just get the name of the school
        school_data.append(scipy.io.loadmat('data/'+ fname + str(num))['local_info']) #append the matfile to the array

    school_data = np.asarray((school_data)) #turn the array to a np.array
    school_student_flag = np.array([i[:,0] for i in school_data]) #the faculty_student flag is the first column
    school_second_major = np.array([i[:,3] for i in school_data]) #second major info is the fourth column
    gender = np.array([i[:,1] for i in school_data]) #gender info is on second column
    state = pd.read_excel('State-University.xlsx') #read the state location of each university

    return school_student_flag, school_second_major, gender, state #return all arrays as a tuple


def find_faculty_student_rate(flags):
    '''
    Gets the rate of faculty vs. student ratio for each school and then plots it
    A 2 represents a person is faculty and a 1 represents a person is a student
    Plots faculty-student ratio vs rank of the school and saves it as 'faculty_student_ratio_vs_rank.png'

    :param flags: 2D numpy array. Each row is a different school
    :return: None
    '''

    assert isinstance(flags,np.ndarray)
    value_counts = [dict(Counter(x).most_common()) for x in flags]
    rates = [float(y[2])/y[1] for y in value_counts]

    fig1 = plt.figure()
    plt.plot(range(1, 101), rates)
    plt.ylabel('Faculty/Student Ratio')
    plt.xlabel('Rank of School')
    plt.savefig('faculty_student_ratio_vs_rank.png')
    plt.show()

def universities_in_state(state):
    '''
    Creates a pie chart of how many top 100 universities each state has and then saves it as
    'top100_state.png'
    :param state: a pandas dataframe with university and state columns
    :return:None
    '''
    assert isinstance(state, pd.DataFrame)
    num_in_top100 = state['State'].value_counts()

    labels = np.array(num_in_top100.index)
    values = np.array(num_in_top100)

    fig2, ax2 = plt.subplots()
    ax2.pie(values,  labels=labels,
             startangle=90, rotatelabels=True, pctdistance=0.3)
    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig('top100_state.png', dpi=100)
    plt.show()

def second_major_gender(second_major, gender):
    males = []
    females = []
    for i in range(len(second_major)):
        males.append(np.array([second_major[i][idx] for idx in range(len(second_major[i])) if gender[i][idx]==1]))
        females.append(np.array([second_major[i][idx] for idx in range(len(second_major[i])) if gender[i][idx] == 2]))

        #male_rate[i] = len(np.nonzero(males)[0])/float(len(males))
        #female_rate[i] = len(np.nonzero(females)[0]) / float(len(females))
    males = np.asarray(males)
    females = np.asarray(females)

    males_10 = [dict(Counter(i)) for i in males]

    females_10 = [dict(Counter(i)) for i in females]

    males_zero = [float(x[0]) for x in males_10]
    females_zero = [float(x[0]) for x in females_10]
    print females_zero

    males_rate = [sum(males_zero[i:i+10])/sum]
def main():
    plt.close('all')
    student_faculty, second_major, gender, state = get_data()
    find_faculty_student_rate(student_faculty)
    universities_in_state(state)
    second_major_gender(second_major, gender)



main()