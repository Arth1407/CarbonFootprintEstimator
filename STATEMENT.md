# 🌿 MoodPrint: CarbonFootprintEstimator

Simple Python thing that figure out your monthly carbon footprint from how you travel, what you eat, and the energy you use.

About: MoodPrint is just a  collage project for *Intro to Problem Solving (Python)* class. It ask easy question about your daily life and calculate how much $\text{CO}_2$ you make every month.

How to run it

We Need is Python 3

How to Run it

1.  Download this repo.
2.  get `main.py` and `factors.py` files.
3.  Run the code:

How It Is Working:

The program have three parts:

1. Ask Stuff
    
  - 🚗 Travel: How you commute (car, bus, train, bicycle, walk)
  - 🍽️ Grub: What you eat (lotta meat, normal, veggie, vegan)
  - ⚡ Power: Electricity and heating usage, which is important

2.  Do the Math
    Figure out your emissions using these factors :

Travel ($\text{kg CO}_2\text{e}$ per km):

  - Car: 0.2
  - Bus: 0.1
  - Train: 0.05
  - Bike/Walk: 0.0

Grub ($\text{kg CO}_2\text{e}$ per month):

  - Meat Heavy: 250
  - Average: 150
  - Vegetarian: 100
  - Vegan: 75

Power:

  - Electricity: 0.5 $\text{kg CO}_2\text{e}$ per kWh
  - Gas Heating: 100 $\text{kg CO}_2\text{e}$ per month
  - Electric Heating: 80 $\text{kg CO}_2\text{e}$ per month


3. Advice: Show your score and give quick tips for improvement.

Exaple:

```
🌿 Welcome to MoodPrint!

🚗 TRANSPORT QUESTIONS
What's your main transport? car
How many km do you travel by car daily? 10

🍽️ DIET QUESTIONS
What's your diet type? average

⚡ ENERGY QUESTIONS
How many kWh of electricity do you use monthly? 200
What heating do you use? gas

📊 YOUR CARBON FOOTPRINT RESULTS

🚗 Transport:  60.00 kg CO2e/month
🍽️  Diet:       150.00 kg CO2e/month
⚡ Energy:     200.00 kg CO2e/month

🌍 TOTAL SCORE: 410.00 kg CO2e/month

⚠️  Your biggest problem area: Energy
💡 Tip: Change to LED light bulbs and unplug things you not use!
```

Testing:

1.  Crash Test:
    Input words instead of number, -ve numbers or the wrong choices, it will not crash

2.  Math Check
    Like this: Car, 1 km daily = 1 $\times$ 0.2 $\times$ 30 = 6 $\text{kg CO}_2\text{e}$ 

Files and Stuff:

  - `main.py` - Main program
  - `factors.py` - The factors data
  - `README.md` - The intro file
  - `STATEMET.md` - This file

Python Skills Used:

  - Functios
  - Dictionaries and Lists
  - Error hadling 
  - Input validation
  - File imports
  - Calcultions

Thigs we can add:

  - More ways to travel
  - Save scores so we can track progress 
  - Put graphs

*Made for Introduction to Problem Solving (Python) course* 🌍
