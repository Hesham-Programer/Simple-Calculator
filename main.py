from flask import Flask, render_template, request
import time

app = Flask(__name__, template_folder="templates")

numbers = [str(i) for i in range(0, 10)]
all_signs = ["plus", "minus", "multiply", "divide", "close_bracket", "open_bracket"]

signs = {
    all_signs[0]:"+",
    all_signs[1]:"-",
    all_signs[2]:"*",
    all_signs[3]:"/",
    all_signs[4]:")",
    all_signs[5]:"("
}

@app.route("/", methods=['GET', 'POST'])
def home_page():
    input_value = ''
    if request.method == 'POST':
        input_value = request.form.get('calculator_input', '')
        # the operators' functionality.
        for sign in all_signs:
            if sign in request.form:
                input_value += signs[sign]
        # for loop for numbers only.
        for number in numbers:
            if number in request.form:
                input_value += number
        # for loop for signs
        if "equals" in request.form:
            try:
                solution = str(eval(input_value))
            except:
                input_value = ""
                input_value += "ERROR"
                time.sleep(0.5)
                input_value = ""
            else:
                input_value = ""
                input_value += solution
        elif "dot" in request.form:
            input_value += "."
        elif "clear" in request.form:
            input_value = ""
        elif "delete" in request.form:
            input_value = input_value[:-1]
        
    return render_template("index.html", input_value=input_value)


if __name__ == '__main__':
    app.run(debug=True)
