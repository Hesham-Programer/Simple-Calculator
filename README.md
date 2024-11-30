# Simple Calculator

This simple calculator is a web-based application built using Flask. It allows users to perform basic arithmetic operations directly from their web browser.

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, and division.
- Input handling for numbers, operators, and parentheses.
- Responsive and user-friendly interface.
- Error handling for incorrect operations.
- Interactive buttons with smooth transitions.

## Installation

### Prerequisites

- Python 3.7 or higher.
- Flask installed (you can install it via `pip`).

### Setup

1. Clone the repository (or download the source files) to your local machine.

2. Navigate to the project directory.

3. If not already installed, you can create a virtual environment and install Flask:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install Flask
   ```

4. Ensure that your `requirements.txt` file is configured and install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. With your virtual environment activated, run the Flask app:

   ```bash
   python main.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000/` to access the calculator.

## Usage

- Input the numbers and use the operator buttons to perform calculations.
- Use the `=` button to see the results.
- Use the `C` button to clear the input or the `Delete` button to remove the last character.
- Parentheses can be used to structure calculations as required.

## Styles and UI

- The user interface is styled using CSS for a modern and clean look.
- Button shades and transitions make the calculator interactive and visually appealing.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to fork the repository and submit a pull request.

---

This project is a simple demonstration of using Flask for web applications, aimed at beginners or those interested in web development with Python.
