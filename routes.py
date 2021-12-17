import math
from flask import Flask, request, render_template
app = Flask(__name__)
func_list = ['square', 'cube']


@app.route('/')
def home():
    """Activate the index.html and display it as soon as the program run"""
    return render_template('index.html', func_list=func_list)


@app.route('/run', methods=['GET', 'POST'])
def run():
    """Creating an endpoint (fancy name for page /run)"""
    func = request.form['function_list']
    input_text = request.form['input_box']
    # This is where calculation happens
    output = calc_fun(func, input_text)
    return render_template('index.html', selected_func=func,
                           input_text=input_text, output_text=output,
                           func_list=func_list)


def calc_fun(func, input_text):
    """Helper function to execute functionality on the UI"""
    if 'square' in func.lower():
        return f"The square of the number {input_text} is  : {math.pow(eval(input_text), 2)}"
    elif 'cube' in func.lower():
        return f"The cube of the number {input_text} is  : {math.pow(eval(input_text), 3)}"


if __name__ == "__main__":
    app.run(debug=True, port=5050)
