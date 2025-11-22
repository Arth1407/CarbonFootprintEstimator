# CarbonFootprintEstimator
🌿 MoodPrint: My Carbon Footprint Estimator Project

🧑‍💻 Overview & Goal

Hey! This is my project for the Introduction to Problem Solving (Python) course.

The main idea is simple: it's hard to track how much CO₂ we actually produce every month. So, this tool helps you figure out your approximate monthly carbon footprint (in kg CO₂e) by asking you a few quick questions about your daily life.

The project mainly uses Python's core features like dictionaries, functions, and loops to calculate the score and give you practical advice.

✨ Project Features (The 3 Modules)

The whole thing is broken down into three main parts:

Input Profile Builder: This is where the program asks you all the questions (commute, diet, etc.). I added some error handling so it doesn't crash if you accidentally type a letter instead of a number!

Emission Factor Calculator: This module takes your answers and uses the data in factors.py to do the actual math. It figures out your score for Transport, Diet, and Energy separately.

Impact Report: It prints your final score and, more importantly, tells you which area (Transport, Diet, or Energy) is contributing the most, and gives you a simple tip on how to reduce it.

🛠️ Tech Used

Language: Python 3.x

Key Skills Used: Functions, Dictionaries (lots of them!), Lists, File Handling (implied via data storage), and try/except blocks.

Version Control: Git (of course).

🚀 How to Run It

This is a basic command-line tool, so it's super easy to get running.

Prerequisites

Just make sure you have Python 3 installed on your machine.

1. Grab the Code

git clone [https://github.com/YourUsername/MoodPrint-Carbon-Estimator.git](https://github.com/Arth1407/MoodPrint-Carbon-Estimator.git)
cd MoodPrint-Carbon-Estimator


2. Launch!

Run this command from your terminal:

python3 main.py


✅ Quick Testing Guide

You can easily check two important things:

1. Crash Test (Error Handling)

Goal: Try to break the program.

How: When it asks for a distance (e.g., "commute distance in km"), type something like oops or ten.

What should happen: It should yell at you with an "Error" message and ask the question again, not crash.

2. Logic Test (Calculation)

Goal: Make sure the numbers are right.

How: Look at the factors in factors.py and run a quick score in your head. For example, choose "CAR" and "1 km" daily. The final monthly transport score should be close to $0.20 \text{ kg} \times 1 \text{ km} \times 30 \text{ days} = 6 \text{ kg} \text{ CO}_{2}\text{e}$.

What should happen: The final output should match your manual calculation.

For the Evaluator: Please see statement.md for the formal academic write-up.
