# 🌿 MoodPrint: Carbon Footprint Calculator

A simple Python project that calculates your monthly carbon footprint based on your transport, diet, and energy usage.

---

## About

MoodPrint is an educational project for **Introduction to Problem Solving (Python)** course. It asks simple questions about your daily habits and calculates how much CO₂ you produce each month.

---

## Getting Started

### What You Need
- Python 3.x

### How to Run
1. Clone or download this repository
2. Make sure you have `main.py` and `factors.py` in the same folder
3. Run the program:
```bash
python main.py
```

---

## How It Works

The program has three parts:

### 1. Ask Questions
Asks you about:
- 🚗 **Transport**: How you commute (car, bus, train, bike, walk)
- 🍽️ **Diet**: What you eat (meat-heavy, average, vegetarian, vegan)
- ⚡ **Energy**: Electricity and heating usage

### 2. Do the Math
Calculates your emissions using these factors:

**Transport** (kg CO₂e per km):
- Car: 0.2
- Bus: 0.1
- Train: 0.05
- Bike/Walk: 0.0

**Diet** (kg CO₂e per month):
- Meat Heavy: 250
- Average: 150
- Vegetarian: 100
- Vegan: 75

**Energy**:
- Electricity: 0.5 kg CO₂e per kWh
- Gas Heating: 100 kg CO₂e per month
- Electric Heating: 80 kg CO₂e per month

### 3. Give Advice
Shows your total score and gives you tips to improve!

---

## Example Output

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

🚗 Transport:  60.00 kg CO2e/month
🍽️  Diet:       150.00 kg CO2e/month
⚡ Energy:     200.00 kg CO2e/month

🌍 TOTAL SCORE: 410.00 kg CO2e/month

⚠️  Your biggest impact area: Energy
💡 Tip: Switch to LED bulbs and unplug devices when not in use!
```

---

## Testing

### Crash Prevention Test
Try to break it! Type words instead of numbers, negative numbers, or wrong options. The program should handle it without crashing.

### Math Check
**Example**: Car, 1 km daily = 1 × 0.2 × 30 = 6 kg CO₂e ✓

---

## Files

- `main.py` - Main program
- `factors.py` - Emission factors data
- `README.md` - This file

---

## Python Skills Used

- Functions
- Dictionaries and Lists
- Error handling (try-except)
- Input validation
- File imports
- Calculations

---

## Future Ideas

- Add more transport options
- Save results to track progress over time
- Add graphs
- Compare with friends

---

**Made for Introduction to Problem Solving (Python) course** 🌍
