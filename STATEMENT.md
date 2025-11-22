Hey, Check Out My Project: MoodPrint - The Carbon Footprint Estimator!

Problem Statement

Honestly, it's tough to know how much our daily choices—like driving, eating meat, or using the AC—contribute to carbon emissions. Most existing tools are super complicated, and they don't clearly explain why your score is what it is, which makes it hard to know where to start changing! This project is all about fixing that.

Scope of the Project

MoodPrint is a simple, rule-based Python tool you run right from the command line (CLI).

Here's what it includes:

It asks you for three key things: transport info, diet habits, and home energy use.

It has a cool modular system that calculates your estimated monthly $\text{CO}_2\text{e}$ score.

It uses smart input validation and error handling so it won't crash when you type something wrong!

It figures out your biggest problem area and gives you personalized advice.

And here's what it doesn't include (keeping it simple!):

No fancy Graphical User Interface (GUI).

No need for external web APIs or live internet data.

It uses fixed, static emission numbers for its calculations.

Target Users

This tool is totally perfect for students and home users! It's meant for anyone who wants a straightforward, free way to get basic info on their environmental impact and get some clear, actionable suggestions for cutting down emissions.

High-level Features (The Three Main Jobs)

The project gets the job done with three main functional modules:

Input Profile Generator: This handles all the questions and makes sure all your lifestyle data is valid before moving on.

Emission Factor Calculator: This is the math brain! It runs your profile against a data map (the $\text{EMISSION\_FACTORS}$) to crunch the numbers and give you a $\text{CO}_2\text{e}$ total for each category.

Impact Report & Suggestions: It prints a clear report with your final scores and gives you a prioritized tip based on the category where you scored highest. Boom!
