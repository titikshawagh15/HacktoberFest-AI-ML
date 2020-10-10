<h1> Titanic: Machine Learning from Disaster </h1>

<h2> Problem Statement </h2>

The sinking of the Titanic is one of the most infamous shipwrecks in history.

On April 15, 1912, during her maiden voyage, the widely considered “unsinkable” RMS Titanic sank after colliding with an iceberg. Unfortunately, there weren’t enough lifeboats for everyone onboard, resulting in the death of 1502 out of 2224 passengers and crew.

While there was some element of luck involved in surviving, it seems some groups of people were more likely to survive than others.

In this challenge, we ask you to build a predictive model that answers the question: “what sorts of people were more likely to survive?” using passenger data (ie name, age, gender, socio-economic class, etc).


<h2> Data </h2>

The data has been split into two groups:
<ul>
  <li>training set (train.csv)</li>
  <li>test set (test.csv)</li>
</ul>

The test set should be used to see how well your model performs on unseen data. For the test set, we do not provide the ground truth for each passenger. It is your job to predict these outcomes. For each passenger in the test set, use the model you trained to predict whether or not they survived the sinking of the Titanic.

We also include gender_submission.csv, a set of predictions that assume all and only female passengers survive, as an example of what a submission file should look like.

<a href="https://ibb.co/ykJQdFS"><img src="https://i.ibb.co/VC8qJYm/image.png" alt="Data" border="0"></a>


Variable Notes <br>
pclass: A proxy for socio-economic status (SES) <br>
1st = Upper <br>
2nd = Middle <br>
3rd = Lower <br>
<br><br>
age: Age is fractional if less than 1. If the age is estimated, is it in the form of xx.5 <br> 
<br>
sibsp: The dataset defines family relations in this way...<br>
Sibling = brother, sister, stepbrother, stepsister<br>
Spouse = husband, wife (mistresses and fiancés were ignored)<br>
<br>
parch: The dataset defines family relations in this way...<br>
Parent = mother, father<br>
Child = daughter, son, stepdaughter, stepson<br>
Some children travelled only with a nanny, therefore parch=0 for them.<br>

<h2> What can you contribute to the repository ?</h2>
This is a classification problem, you can use various Machine Learning classification Algorithms to improve the accuracy of the model. You can also add various data visualizations to understand the given data.

<h2> How to contribute to this repository ?</h2>
<ol>
  <li> Click on the fork button on the top right corner of this page. </li>
  <li> Now go to http://github.com/{your_username}/HacktoberFest-AI-ML where you can see your own fork of this repo. </li>
  <li> Clone your forked repository </li>
  
  ```
  git clone http://github.com/{your_username}/HacktoberFest-AI-ML
  ```
  <li> Go to the Titanic/Solution upload a .ipynb or .py file in the Solution for the given problem statement. </li>
  <li> Add the files you want to commit to the staging area. </li>
  
  ```
  git add {folder_name/file_name}
  ```
  
  <li> Commit the changes </li>
  
  ```
  git commit -m '{Your commit message}'
  ```
  <li> Push to GitHub </li>
  
  ```
  git push origin {branch_name}
  ```
  <li> Go to your repository and click on the Pull request button </li>
  <li> Add message and click on 'Create Pull request' </li>
</ol>
 
