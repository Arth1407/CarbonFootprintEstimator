"""
MoodPrint: Carbon Footprint Estimator
Introduction to Problem Solving & Programming (Python) Project
"""

from factors import TRANSPORT_FACTORS, DIET_FACTORS, ENERGY_FACTORS, DAYS_PER_MONTH


def get_valid_number(prompt, min_val=0, max_val=None):
    """
    Ask a question and make sure the answer is a valid number.
    This stops the program from crashing if a  user types wrong type of input.
    """
    while True:
        try:
            value = float(input(prompt))
            if value < min_val:
                print(f"Please enter a number greater than or equal to {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"Please enter a number less than or equal to {max_val}.")
                continue
            return value
        except ValueError:
            print("Oops! That's not a valid number. Please try again.")


def get_valid_choice(prompt, options):
    """
    Ask a question with specific choices (like 'car', 'bus', 'bike').
    This makes sure the user picks a valid option.
    """
    while True:
        choice = input(prompt).lower().strip()
        if choice in options:
            return choice
        print(f"Please choose from: {', '.join(options)}")


def ask_transport_questions():
    """
    Part 1: Ask Questions - Transport Section
    Returns a dictionary with transport answers.
    """
    print("\n🚗 TRANSPORT QUESTIONS")
    print("-" * 40)
    
    transport_type = get_valid_choice(
        "What's your main transport? (car/bus/train/bike/walk): ",
        list(TRANSPORT_FACTORS.keys())
    )
    
    if transport_type in ['bike', 'walk']:
        daily_km = 0  # Zero emissions for bike/walk
    else:
        daily_km = get_valid_number(
            f"How many km do you travel by {transport_type} daily? ",
            min_val=0
        )
    
    return {
        'type': transport_type,
        'daily_km': daily_km
    }


def ask_diet_questions():
    """
    Part 1: Ask Questions - Diet Section
    Returns a dictionary with diet answers.
    """
    print("\n🍽️ DIET QUESTIONS")
    print("-" * 40)
    
    diet_type = get_valid_choice(
        "What's your diet type? (meat_heavy/average/vegetarian/vegan): ",
        list(DIET_FACTORS.keys())
    )
    
    return {
        'type': diet_type
    }


def ask_energy_questions():
    """
    Part 1: Ask Questions - Energy Section
    Returns a dictionary with energy answers.
    """
    print("\n⚡ ENERGY QUESTIONS")
    print("-" * 40)
    
    electricity_kwh = get_valid_number(
        "How many kWh of electricity do you use monthly? ",
        min_val=0
    )
    
    heating_type = get_valid_choice(
        "What heating do you use? (gas/electric/none): ",
        list(ENERGY_FACTORS['heating'].keys())
    )
    
    return {
        'electricity_kwh': electricity_kwh,
        'heating_type': heating_type
    }


def calculate_transport_score(transport_data):
    """
    Part 2: Do the Math - Transport Calculation
    Returns CO2 kg per month for transport.
    """
    transport_type = transport_data['type']
    daily_km = transport_data['daily_km']
    factor = TRANSPORT_FACTORS[transport_type]
    
    monthly_score = daily_km * factor * DAYS_PER_MONTH
    return monthly_score


def calculate_diet_score(diet_data):
    """
    Part 2: Do the Math - Diet Calculation
    Returns CO2 kg per month for diet.
    """
    diet_type = diet_data['type']
    monthly_score = DIET_FACTORS[diet_type]
    return monthly_score


def calculate_energy_score(energy_data):
    """
    Part 2: Do the Math - Energy Calculation
    Returns CO2 kg per month for energy.
    """
    electricity_kwh = energy_data['electricity_kwh']
    heating_type = energy_data['heating_type']
    
    electricity_score = electricity_kwh * ENERGY_FACTORS['electricity']
    heating_score = ENERGY_FACTORS['heating'][heating_type]
    
    monthly_score = electricity_score + heating_score
    return monthly_score


def get_biggest_problem(scores):
    """
    Find which category has the highest score.
    Returns the category name.
    """
    max_category = max(scores, key=scores.get)
    return max_category


def give_advice(biggest_problem):
    """
    Part 3: Give Advice - Provide tips based on biggest problem area
    """
    tips = {
        'Transport': "🚴 Try using public transport, biking, or carpooling to reduce emissions!",
        'Diet': "🥗 Consider eating less meat and more plant-based meals!",
        'Energy': "💡 Switch to LED bulbs and unplug devices when not in use!"
    }
    
    return tips.get(biggest_problem, "Keep up the good work! 🌍")


def display_results(scores, total_score):
    """
    Part 3: Display final results with scores and advice
    """
    print("\n" + "=" * 50)
    print("📊 YOUR CARBON FOOTPRINT RESULT")
    print("=" * 50)
    
    print(f"\n🚗 Transport:  {scores['Transport']:.2f} kg CO2e/month")
    print(f"🍽️  Diet:       {scores['Diet']:.2f} kg CO2e/month")
    print(f"⚡ Energy:     {scores['Energy']:.2f} kg CO2e/month")
    print(f"\n{'─' * 50}")
    print(f"🌍 TOTAL SCORE: {total_score:.2f} kg CO2e/month")
    print(f"{'─' * 50}")
    
    # Find and display biggest problem
    biggest_problem = get_biggest_problem(scores)
    print(f"\n⚠️  Your biggest impact area: {biggest_problem}")
    print(f"💡 Tip: {give_advice(biggest_problem)}")
    
    # Add context
    print(f"\n📌 Context: Average person emits ~400-600 kg CO2e/month")
    if total_score < 400:
        print("✅ Great! You're below average!")
    elif total_score < 600:
        print("👍 You're around average. Small changes can help!")
    else:
        print("⚠️  Above average. Consider making some changes!")
    
    print("=" * 50 + "\n")


def main():
    """
    Main program - runs all three parts:
    1. Questions
    2. Math
    3. Advice
    """
    print("=" * 50)
    print("🌿 Welcome to MoodPrint!")
    print("Let's calculate your monthly carbon footprint!")
    print("=" * 50)
    
    # Part 1:Questions
    transport_data = ask_transport_questions()
    diet_data = ask_diet_questions()
    energy_data = ask_energy_questions()
    
    # Part 2:Math
    transport_score = calculate_transport_score(transport_data)
    diet_score = calculate_diet_score(diet_data)
    energy_score = calculate_energy_score(energy_data)
    
    scores = {
        'Transport': transport_score,
        'Diet': diet_score,
        'Energy': energy_score
    }
    
    total_score = sum(scores.values())
    
    # Part 3: Give Advice
    display_results(scores, total_score)


if __name__ == "__main__":
    main()
