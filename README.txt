Project Proposal:  An Analysis on Students’ Categories in Top 100 US Universities
ECE 143 Team 9
Team Members:
                        Xin Li, Daniel Truong, Ruhan Fan, Joy Nwarueze


Overview:             
The project aims to analyze the student categories and social structures in Top 100 US Universities and get conclusions that help show the culture and lifestyles at these school. We can possibly display what we find to students or undergraduates who need to decide which universities to apply to and would fit their lifestyle the best.


We decided to look at a Facebook dataset from 2005 disclosing info about the network within 100 American universities. It was used to find social connections in the Facebook network  of students and faculties within the university. Facebook used some statistical and data analysis strategy in dealing with this dataset. 


Facebook makes use of this dataset analyze students relationship within a college which is intra-class(deal with information in the same group) analysis. We also plan to do Data Analysis and Visualization on students from different universities which is inter-class(deal with information in different groups).




Source of Data:
Facebook 2005 dataset:
https://archive.org/download/oxford-2005-facebook-matrix


The dataset includes 100 universities in .mat file. Each file includes a matrix N*N representing students’ relationship to each other and a N*7 representing 7 features of for each student in people’s student/faculty flag,  gender, class, major, second major or minor, dorm/residence, and high school. 


Core python packages:
* Numpy 
   * A basic package help with dealing with basic data types, computations
* Scipy 
   * A useful tool in helping with loading data
* Pandas
   * Read from multiple sources
   * Create dataframes
   * Compute aggregate analytics
   * Some built in visualizations
* concurrent.futures + executor.map
   * Useful for parallel processing
* Matplotlib
   * Visualization that pairs well with IPython notebook
* Bokeh (+Blaze optional)
   * Great for visualizing completed datasets
* Map-Reduce 
   * Useful for categorizing large amounts of data
* Sklearn
   * A supplementary tool in helping with data visualization in Machine Learning(might not be used)


Project Plan
In general, by working on these datasets, we aim to help visualize these data to help incoming college students or graduate students have a better understanding of students’ composition in different majors, groups, the college’s culture and even a trend of a change of student number in different realms. We can combine datasets of universities of close ranks, or universities in same State to gain more useful insights. In this way, young people can have a better understanding of which University fits them well, what groups of people they will more likely to engage with once they get into Universities. 


Some Sample Specific Topics from the dataset we can analyze/visualize:
* Do people with the same major tend to live together?
* Do people tend to drop their second major the further they get into college?
* Gender disparities in different majors
* Average number of people in dorm/house (tells if the apartments/houses can hold more/less than other universities)
* Most popular major
* How many people take a second major
* Dropout rate (we can if there is a decrease in number of people from freshman to senior)




Schedule:
Week 6
	Data preprocessing, figure out different insights to analyze data
	Week 7
	Working on Python to make Data visualization, Generate plots 
	Week 8
	Do data analysis on figures we create, write report 
	Week 9
	Prepare for final Presentation by creating powerpoint, rehearsing
	



Resources:
https://archive.org/details/oxford-2005-facebook-matrix
http://humannaturelab.net/wp-content/uploads/2015/01/Tastes-Ties-and-Time-A-New-Cultural-Multiplex-and-Longitudinal-Social-Network-Dataset-Using-Facebook.com_.pdf
https://escience.rpi.edu/data/DA/fb100/facelong14.pdf