Project Proposal:  An Analysis on Students’ Categories in Top 100 US Universities
ECE 143 Team 9
Team Members:
			Xin Li, Daniel Truong, Ruhan Fan, Joy Nwarueze

Overview:             
The project aims to analyze the student categories and social structures in Top 100 US Universities and get conclusions that help show the culture and lifestyles at these schools. We can display what we find to students or undergraduates who need to decide which universities to apply to and would fit their lifestyle the best.

We decided to look at a Facebook dataset from 2005 disclosing info about the network within 100 American universities. Facebook used this dataset to analyze students relationship within a college which is intra-class(deal with information in the same university) analysis. We will do intra-class analysis and plan to do inter-class analysis too(deal with information in different universities).

Source of Data:
Facebook 2005 dataset:
https://archive.org/download/oxford-2005-facebook-matrix

The dataset includes 100 universities in .mat file. Each file includes a matrix N*N indicating if each person was a friend on Facebook to eachother and a N*7 representing 7 features of for each student in people’s student/faculty status,  gender, class, major, second major or minor, dorm/residence, and high school. There is also unknown data due to users not fully uploading all of their information.

Core python packages:
Numpy 
A basic package dealing with basic data types and computations
Scipy
A useful tool in helping with loading data
Pandas
Read from multiple sources
Create dataframes
Compute aggregate analytics
Built in visualizations
concurrent.futures + executor.map
Useful for parallel processing
Matplotlib
Visualization that pairs well with IPython notebook
Bokeh (+Blaze optional)
Great for visualizing completed datasets
Map-Reduce 
Useful for categorizing large amounts of data
Sklearn
A supplementary tool in helping with data visualization in Machine Learning (might not be used)

Project Plan
In general, by working on these datasets, we aim to help visualize these data to help incoming college students or graduate students have a better understanding of students’ composition in different majors, groups, college culture and even a trend of a change of student number in different realms. We can combine datasets of universities of close ranks, or universities in same state to gain more useful insights. This way, young people will have a better understanding of which university fits them well and what groups of people they are more likely to engage with once they get into universities. 

Some Sample Specific Topics from the dataset we can analyze/visualize:
Do people with the same major tend to live together?
Do people tend to drop their second major the further they get into college?
Gender disparities in different majors
Average number of people in dorm/house (tells if the apartments/houses can hold more/less than other universities)
Most popular major
How many people take a second major
Dropout rate (we can if there is a decrease in number of people from freshman to senior)


Here are some ideas and insights to preprocess data, and do data analysis:


Schedule:


Xin
Daniel 
Ruhan
Joy
Week 6:
pre-process some  non-semantic data with meaningless number (e.g. 20105 in high school category) using strategies like (data, normalization, one hot encoding)
Figure out different insights to analyze in the data
Pre-process dataset by classifying Universities based on states 
Data preprocessing based around Major density and at which Universities
Week 7:
Working on Python to make Data visualization on combined datasets generate plots for non-semantic categories/features. Mostly plot years vs other features
Work on preparing data for visualization based on living situation (Avg. number of people for dorm, amount of housemates vs. gender)


Working on Python to make Data analysis on combined datasets of Universities in a state. Generate plots for major, ratio of male vs female
Work on data visualization based on Majors. Generate Interactive plots.
Week 8:
Compare previous  analysis with some resources like USnews to interpret relationship some trends over years  
Help write the report on data analysis and how the data can tell us more about present situation
Do data analysis and help to write report 
Analyze data based around Majors - percentage of double Majors, Male-to- Female ratio in each Major, etc 
Week 9:
Prepare for final Presentation by creating powerpoint, rehearsing
Rehearse and help make powerpoint
Prepare the final presentation and make powerpoint
Help prepare Final presentation






Resources:
https://archive.org/details/oxford-2005-facebook-matrix

https://www.usnews.com/rankings

http://humannaturelab.net/wp-content/uploads/2015/01/Tastes-Ties-and-Time-A-New-Cultural-Multiplex-and-Longitudinal-Social-Network-Dataset-Using-Facebook.com_.pdf

https://escience.rpi.edu/data/DA/fb100/facelong14.pdf

Github repository:
https://github.com/xil222/Data-Analysis-on-Facebook-Data-Scrape

