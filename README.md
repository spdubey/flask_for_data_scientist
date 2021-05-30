# flask_for_data_scientist
Quick Intro about blog :
I am writing this blog as I am someone who learnt data science through certifications/videos etc. And I do not have computer science back ground due to which if there is any tool then I have to learn it or understand it in data sciency way and what I mean by that is if there is a task I try to understand the purpose of it and then piece all the component together. I am going to follow the same approach in this blog.

PS: As I told I am not from CS background I do not use very technical terms, rather try to understand the logic and purpose behind it. I am also assuming that people reading this blog is aware of basic python syntax. I am going to demo/explain a very basic app and how you can connect different component of a flask app. If you want me to do a more complicated app with multiple page and functionality let me know.

What we will try to achieve :
An app which will have an input text box, a drop down(with two function square root and cube root) selection and an output box.
Output will contain the text you entered in input box all converted into lower case and along with square root or cube root of the 5. I know it might not make sense but the idea here is to understand how you can take input, process them and apply a function to it and show them on your web page. Instead of number converting to square or cube can be replaced with any ML model depending on use case.




















How does a Flask app look in its structure :

I have created this with bare minimum requirement, when I started learning about how you can create an aesthetically appealing UI using Flask. Came across multiple components and one of them was  JavaScript. Now I had never used JavaScript but as I started digging deeper, I was able to manage incorporate JavaScript as well in the code  which will serve small functionality. Probably will create a blog on that as well. Let's focus on this app without JavaScript.

Unravelling the code :

I will keep the python script(routes.py) as my base and will show simultaneously how is it connected with index.html. Below code snippet is independent of html page, it is kind of a boiler plate code.
Similarly, in index.html we have <head> tag which includes path for style.css







