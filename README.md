# flask_for_data_scientist

### Introduction :  
This blog is coming from someone who has learnt data science through videos , tutorials, certification courses etc. Not having a computer science background, if there is any tool I have wanted to learn or understand , I have always done it from a data sciency way ; starts with understanding the purpose followed by putting all the build components together. And this is very much the approach that would be followed in our blogs.
I do use technical jargons  very much, rather get along the logic and purpose behind the solutions.

### Pre- Requisite :  
Basic Python  - Ah! Long time since you last used it ?? Don’t you worry, you can refer this <link - coming soon> to have a quick and short refresher's course.
### What are we trying to achieve ?  
I am going to demo/explain a very basic app and how can we connect different components of a flask app. In case we want to do some mind goggling and hit a more complicated app with complex features, please comment and I will definitely try to come up with another blog on this. So make sure you add in your reviews and comments, guys!

### Design:
#### We will have an app with:
  - One Input Text Box : User can input the data – here any number  
  - A Dropdown – having values : square root and cube root for selection  
  - One Output Box : Depending on the value selected in the above Dropdown, this displays the calculated output.  

This might not make sense but the idea here is to understand how we can input a data, transform or apply any functions on it and display the output on a web page. Instead of this use case of getting a square or cube root of a number, we can have any ML models depending on different types of use cases.


**Just a Thought** : I have created this example with bare minimum requirement. When I started learning about how one  can create an aesthetically appealing UI using Flask, I came across multiple hurdles , one of them was  JavaScript. I had never used JavaScript earlier but as I started digging deeper, I managed to  incorporate JavaScript as well in the code  which will serve small functionality. Probably will create a blog on that as well. Let's focus on this app without JavaScript for now.

### How does a flask app looks?
![Test Image 1](intro.PNG)

**STEP – 1** :  Keeping python script(routes.py) as my base ,  I will show simultaneously how is it connected with index.html  
  - Below code snippet is independent of html page, it is kind of a boiler plate code  
  - Similarly, in index.html we have <head> tag which includes path for style.css    
![Test Image 1](exp_1.PNG)  
  
**STEP – 2** :  Comparing Python to HTML Code – Here it shows how we are passing elements for our Dropdown. The UI shows our designed Dropdown
![Test Image 1](exp_2.PNG)
  
  
**STEP – 3** :  Comparing Python to HTML Code – Here it shows how we are passing elements for our Dropdown. The UI shows our designed Dropdown
![Test Image 1](exp_3.PNG)
  

**STEP – 4** :  Now, our final output looks like this -
![Test Image 1](exp_4.PNG)











