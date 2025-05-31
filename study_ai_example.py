from simple_ai import SimpleAI

def create_study_ai():
    """Create and train an AI for study recommendations"""
    # Create a new AI instance
    ai = SimpleAI("StudyAdvisor")
    
    # Define study scenarios and recommendations
    study_patterns = [
        # Time-based patterns
        ({"time": "morning", "subject": "math", "energy": "high"}, "solve practice problems"),
        ({"time": "morning", "subject": "language", "energy": "high"}, "practice writing"),
        ({"time": "afternoon", "subject": "science", "energy": "medium"}, "read textbook"),
        ({"time": "evening", "subject": "history", "energy": "low"}, "watch educational videos"),
        
        # Subject-specific patterns
        ({"subject": "math", "topic": "algebra", "difficulty": "hard"}, "use step-by-step calculator"),
        ({"subject": "math", "topic": "geometry", "difficulty": "medium"}, "draw diagrams"),
        ({"subject": "science", "topic": "chemistry", "difficulty": "hard"}, "do lab experiments"),
        ({"subject": "language", "topic": "grammar", "difficulty": "medium"}, "complete exercises"),
        
        # Energy and focus based patterns
        ({"energy": "high", "focus": "good", "subject": "any"}, "tackle difficult topics"),
        ({"energy": "low", "focus": "poor", "subject": "any"}, "review notes"),
        ({"energy": "medium", "focus": "good", "subject": "any"}, "practice problems"),
        
        # Time management patterns
        ({"time_left": "long", "priority": "high"}, "deep study session"),
        ({"time_left": "short", "priority": "high"}, "quick review"),
        ({"time_left": "medium", "priority": "medium"}, "practice test")
    ]
    
    # Train the AI with all patterns
    print("Training StudyAdvisor AI...")
    for context, recommendation in study_patterns:
        ai.learn(str(context), recommendation)
        print(f"Learned: {context} -> {recommendation}")
    
    return ai

def get_study_recommendation(ai, context):
    """Get a study recommendation based on the current context"""
    return ai.predict(str(context))

def get_study_plan(ai, options, context):
    """Get a study plan from a list of options based on context"""
    return ai.make_decision(options, context)

def demonstrate_study_ai():
    """Demonstrate the StudyAdvisor AI in action"""
    print("\n=== StudyAdvisor AI Demonstration ===\n")
    
    # Create and train the AI
    ai = create_study_ai()
    
    # Example 1: Time-based recommendation
    print("\nExample 1: Time-based Study Recommendation")
    morning_context = {
        "time": "morning",
        "subject": "math",
        "energy": "high"
    }
    recommendation = get_study_recommendation(ai, morning_context)
    print(f"Context: {morning_context}")
    print(f"Recommendation: {recommendation}")
    
    # Example 2: Subject-specific recommendation
    print("\nExample 2: Subject-specific Study Recommendation")
    math_context = {
        "subject": "math",
        "topic": "algebra",
        "difficulty": "hard"
    }
    recommendation = get_study_recommendation(ai, math_context)
    print(f"Context: {math_context}")
    print(f"Recommendation: {recommendation}")
    
    # Example 3: Energy-based recommendation
    print("\nExample 3: Energy-based Study Recommendation")
    tired_context = {
        "energy": "low",
        "focus": "poor",
        "subject": "any"
    }
    recommendation = get_study_recommendation(ai, tired_context)
    print(f"Context: {tired_context}")
    print(f"Recommendation: {recommendation}")
    
    # Example 4: Study Plan Selection
    print("\nExample 4: Study Plan Selection")
    study_options = [
        "2-hour deep study session",
        "30-minute quick review",
        "1-hour practice test",
        "45-minute topic review"
    ]
    exam_context = {
        "time_left": "long",
        "priority": "high",
        "subject": "math"
    }
    plan = get_study_plan(ai, study_options, exam_context)
    print(f"Context: {exam_context}")
    print(f"Available options: {study_options}")
    print(f"Selected plan: {plan}")
    
    # Example 5: Similar but not exact context
    print("\nExample 5: Similar Context Handling")
    similar_context = {
        "time": "morning",
        "subject": "physics",  # Not exactly trained for physics
        "energy": "high"
    }
    recommendation = get_study_recommendation(ai, similar_context)
    print(f"Context: {similar_context}")
    print(f"Recommendation: {recommendation}")
    print("(Note: AI finds the closest matching pattern)")

if __name__ == "__main__":
    print("StudyAdvisor AI - Smart Study Recommendations")
    print("This example shows how the AI can help with study planning and recommendations.")
    print("It learns patterns for different study scenarios and provides personalized advice.\n")
    
    demonstrate_study_ai()
    
    print("\nKey Features Demonstrated:")
    print("1. Time-based study recommendations")
    print("2. Subject-specific learning strategies")
    print("3. Energy and focus-based advice")
    print("4. Study plan selection")
    print("5. Handling similar but not exact scenarios") 