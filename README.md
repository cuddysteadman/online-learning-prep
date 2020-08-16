# Evaluating Student Preparation for Online Schooling with a Machine Learning Algorithm

This project attempts to make an algorithm to determine whether a student is prepared for online schooling based on three factors: procrastination, time online, and times asked for help. The final output is a gui that asks three questions and then outputs the final predicted grade.

## Getting Started

To replicate this experiment:<br />
First, download every single file in the repository. This project used google colab as the way to run all the code, but it can be done using any IDE such as PyCharm. It does require Python 3.7.<br />
Secondly, run all the scripts following the steps below and then the final script will be gui.py.
### Prerequisites
This requires the following packages:<br />
-numpy<br />
-matplotlib<br />
-sklearn<br />
-six<br />
These are all pre-installed in google colab, and will need to be installed on the machine if you are using a local IDE.  
### Installing
To load in each dataset in google colab, we use the line:
```
files.upload()
```
and then upload the dataset we need (it is commented in-line). No uploading of datasets is required for the gui. If you are using a local IDE, such as PyCharm, you have to reference the file path, like this:
```
dataset = pd.read_csv('path')
```
and there is no need for the files.upload() line.
## Each File Explained

formatting_data.py: this is for making the data from both of the datasets useable for our model. (it turns studentAssesment_original.csv and online_posts_data_original.csv into studentAssesment_formatted.csv and online_posts_data_formatted.csv)<br />
<br />
gui.py: this is the script that would be used for the gui. It takes three user inputs and then outputs the final score.<br />
<br />
making_graphs.py: this is the script that makes all the graphs used in the paper.<br />
<br />
model_procrastination.py: this is the script that makes the model for the procrastination input.<br />
<br />
model_timeonline.py: this is the script that makes the model for the time online input.<br />
<br />
model_total_posts.py: this is the script that makes the model for the times asked for help input.<br />
<br />
online_classroom_data_formatted.csv: this is the final .csv dataset that is used for the model_total_posts.py script and the model_timeonline.py script.<br />
<br />
online_classroom_data_original.csv: this is the original .csv dataset that is formatted in formatting_data.py<br />
<br />
studentAssesment_formatted.csv:this is the final .csv dataset that is used for the model_procrastination.py script.<br />
<br />
studentAssesment_original.csv: this is the original .csv dataset that is formatted in formatting_data.py<br />
<br />
testing_algorithm.csv: these are all the students I surveyed's inputs for the three questions and their actual final score.<br />
<br />
testing_algorithm.py: this is a script that adds a column to testing_algorithm.py of predicted_score that the algorithm predicts. it also outputs a table that can be downloaded as a .png file.<br />
## Deployment

A tkinter GUI could be implemented to make this more user friendly, but that was beyond the scope of this project. Right now, it is solely print statements, so it would be harder to implement for school systems.

## Authors

* **Cuthbert Steadman** - *Initial work* - [theCudster](https://github.com/theCudster)

## Acknowledgments

* David Marx on StackOverflow for the abline code (graphing lines)
* volodymyr on StackOverflow for the render_mpl_table code 
* Everyone at the Summer STEM Institute 2020 course
* Mr. Siddharth Reddy for his guidance
