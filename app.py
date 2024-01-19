# Import necessary classes and functions from 5he Flask module

from flask import Flask,request,render_template

# Create a Flask web application instance
app=Flask(__name__)

# Define a route for the root URL ('/')


app.route('/')
def welcome():
    return "Welcome to Flask"

@object.route('/cal',methods=["GET"])
def math_operator()
    operation=request.form()
    number1=request.json[number1]
    number2=request.json[number2]

    if operation=="add":
       result=number1+number2
    elif operation=="multiply":
       result=number1*number2 
    elif operation=="division":
       result=number1/number2  
    else 
       result=number1-number2   

       return result 





# Start the Flask development server if the script is executed directly

if __name__ == '__main__':
    
  app.run
