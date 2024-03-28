[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/FJiO-WNb)
# EA1
# Sample Program Using Toolz Library

**1. Which package/library does the sample program demonstrate?**

This sample program demonstrates the usage of the Toolz library, a Python library for functional programming utilities.

**2. How does someone run your program?**

To run the program, follow these steps:

- Ensure you have Python installed on your system.
- Install the Toolz library using pip:
- Copy the provided Python script (sample_program.py) to your local machine.
- Open a terminal or command prompt.
- Navigate to the directory containing the sample_program.py file.
- Run the program by executing the following command:
  python sample_program.py
  
**3. What purpose does your program serve?**

This program serves the purpose of demonstrating various functionalities of the Toolz library in Python. It performs operations on a set of student grades, including calculating average grades, finding the highest and lowest grades, and filtering out failing grades. By showcasing these functionalities, the program highlights the utility of the Toolz library in functional programming tasks.

**4. What would be some sample input/output?**

**Sample Input:**
The program uses a dictionary containing student names as keys and their corresponding grades in different subjects as values. Here's an example of the input data:
```python
grades = {
  'Alice': {'math': 85, 'science': 90, 'history': 75},
  'Bob': {'math': 70, 'science': 80, 'history': 65},
  'Charlie': {'math': 60, 'science': 75, 'history': 80},
  'David': {'math': 80, 'science': 85, 'history': 90},
  'Eve': {'math': 55, 'science': 60, 'history': 70}
}

Sample Output:
Average grades: [83.33, 71.67, 71.67, 78.33, 61.67]
Highest grade: 90
Lowest grade: 55
Students with passing grades: [('Alice', {'math': 85, 'science': 90, 'history': 75}), ('Bob', {'math': 70, 'science': 80, 'history': 65}), ('Charlie', {'math': 60, 'science': 75, 'history': 80}), ('David', {'math': 80, 'science': 85, 'history': 90})]



