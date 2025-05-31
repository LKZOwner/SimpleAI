from simple_ai import SimpleAI
import time

def print_section(title):
    """Helper function to print section titles"""
    print("\n" + "="*50)
    print(f" {title} ".center(50, "="))
    print("="*50 + "\n")

def example_1_basic_learning():
    """Example 1: Basic Learning and Prediction"""
    print_section("Example 1: Basic Learning and Prediction")
    
    # Create a new AI instance
    ai = SimpleAI("LearningAI")
    print("Created new AI instance:", ai.name)
    
    # Teach the AI some basic patterns
    print("\nTeaching the AI some patterns...")
    ai.learn(1, 2)
    ai.learn(2, 4)
    ai.learn(3, 6)
    ai.learn(4, 8)
    
    # Show what the AI learned
    print("\nKnowledge base after learning:")
    print(ai.get_knowledge())
    
    # Make some predictions
    print("\nMaking predictions:")
    test_numbers = [1, 2, 3, 4, 5, 6]
    for num in test_numbers:
        prediction = ai.predict(num)
        print(f"Input: {num} -> Prediction: {prediction}")
    
    # Explain what happened
    print("\nExplanation:")
    print("1. The AI learned a pattern where each number is doubled")
    print("2. For known numbers (1-4), it returns the exact learned value")
    print("3. For unknown numbers (5-6), it finds the closest known value")
    print("4. The AI uses the closest known pattern to make predictions")

def example_2_text_learning():
    """Example 2: Learning and Predicting with Text"""
    print_section("Example 2: Learning and Predicting with Text")
    
    # Create a new AI instance
    ai = SimpleAI("TextAI")
    
    # Teach the AI some text patterns
    print("Teaching the AI some text patterns...")
    patterns = {
        "hello": "greeting",
        "goodbye": "farewell",
        "thank you": "gratitude",
        "sorry": "apology",
        "yes": "affirmation",
        "no": "negation"
    }
    
    for input_text, output_text in patterns.items():
        ai.learn(input_text, output_text)
        print(f"Learned: '{input_text}' -> '{output_text}'")
    
    # Test the AI with known and unknown inputs
    print("\nTesting the AI with different inputs:")
    test_inputs = ["hello", "goodbye", "maybe", "thank you", "unknown"]
    for text in test_inputs:
        prediction = ai.predict(text)
        print(f"Input: '{text}' -> Prediction: '{prediction}'")
    
    # Explain what happened
    print("\nExplanation:")
    print("1. The AI learned specific text-to-text mappings")
    print("2. For known words, it returns the exact learned response")
    print("3. For unknown words, it returns 'Unknown'")
    print("4. Text matching is case-sensitive and exact")

def example_3_decision_making():
    """Example 3: Context-Aware Decision Making"""
    print_section("Example 3: Context-Aware Decision Making")
    
    # Create a new AI instance
    ai = SimpleAI("DecisionAI")
    
    # Define some decision contexts and options
    print("Teaching the AI to make decisions based on context...")
    
    # Weather-based decisions
    weather_context = {"weather": "sunny", "temperature": "hot"}
    ai.learn(str(weather_context), "wear sunscreen")
    
    weather_context = {"weather": "rainy", "temperature": "cold"}
    ai.learn(str(weather_context), "wear raincoat")
    
    # Time-based decisions
    time_context = {"time": "morning", "day": "weekday"}
    ai.learn(str(time_context), "go to work")
    
    time_context = {"time": "evening", "day": "weekend"}
    ai.learn(str(time_context), "watch movie")
    
    # Test different scenarios
    print("\nTesting decision making with different contexts:")
    
    # Scenario 1: Weather decision
    weather_options = ["wear sunscreen", "wear raincoat", "wear jacket"]
    context1 = {"weather": "sunny", "temperature": "hot"}
    decision1 = ai.make_decision(weather_options, context1)
    print(f"\nContext: {context1}")
    print(f"Options: {weather_options}")
    print(f"Decision: {decision1}")
    
    # Scenario 2: Time decision
    time_options = ["go to work", "watch movie", "go shopping"]
    context2 = {"time": "evening", "day": "weekend"}
    decision2 = ai.make_decision(time_options, context2)
    print(f"\nContext: {context2}")
    print(f"Options: {time_options}")
    print(f"Decision: {decision2}")
    
    # Scenario 3: Unknown context
    context3 = {"weather": "cloudy", "temperature": "mild"}
    decision3 = ai.make_decision(weather_options, context3)
    print(f"\nContext: {context3}")
    print(f"Options: {weather_options}")
    print(f"Decision: {decision3} (random choice for unknown context)")
    
    # Explain what happened
    print("\nExplanation:")
    print("1. The AI learned specific context-to-decision mappings")
    print("2. For known contexts, it makes decisions based on learned preferences")
    print("3. For unknown contexts, it makes random choices")
    print("4. The AI considers the entire context when making decisions")

def example_4_advanced_learning():
    """Example 4: Advanced Learning with Multiple Features"""
    print_section("Example 4: Advanced Learning with Multiple Features")
    
    # Create a new AI instance
    ai = SimpleAI("AdvancedAI")
    
    # Teach the AI to recommend activities based on multiple factors
    print("Teaching the AI to recommend activities...")
    
    # Define some complex scenarios
    scenarios = [
        ({"weather": "sunny", "time": "morning", "mood": "energetic"}, "go jogging"),
        ({"weather": "sunny", "time": "afternoon", "mood": "relaxed"}, "have picnic"),
        ({"weather": "rainy", "time": "morning", "mood": "energetic"}, "go to gym"),
        ({"weather": "rainy", "time": "evening", "mood": "tired"}, "watch movie"),
        ({"weather": "cloudy", "time": "afternoon", "mood": "creative"}, "paint"),
    ]
    
    # Learn each scenario
    for context, activity in scenarios:
        ai.learn(str(context), activity)
        print(f"Learned: {context} -> {activity}")
    
    # Test with similar but not exact scenarios
    print("\nTesting with similar scenarios:")
    test_scenarios = [
        {"weather": "sunny", "time": "morning", "mood": "happy"},
        {"weather": "rainy", "time": "night", "mood": "sleepy"},
        {"weather": "cloudy", "time": "afternoon", "mood": "artistic"}
    ]
    
    for scenario in test_scenarios:
        prediction = ai.predict(str(scenario))
        print(f"\nContext: {scenario}")
        print(f"Prediction: {prediction}")
    
    # Explain what happened
    print("\nExplanation:")
    print("1. The AI learned complex patterns involving multiple factors")
    print("2. It can handle multiple features in the context")
    print("3. For similar but not exact matches, it finds the closest known pattern")
    print("4. The AI can make recommendations based on multiple conditions")

def run_all_examples():
    """Run all examples with a pause between each"""
    examples = [
        example_1_basic_learning,
        example_2_text_learning,
        example_3_decision_making,
        example_4_advanced_learning
    ]
    
    for example in examples:
        example()
        print("\nPress Enter to continue to the next example...")
        input()

if __name__ == "__main__":
    print("SimpleAI Examples and Explanations")
    print("This program demonstrates various capabilities of the SimpleAI class.")
    print("Each example will show how the AI learns and makes decisions.\n")
    
    run_all_examples() 