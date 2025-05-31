import random
import numpy as np
from typing import List, Dict, Any

class SimpleAI:
    """
    A simple AI class that demonstrates basic AI concepts including:
    - Learning from data
    - Making predictions
    - Storing knowledge
    - Making decisions
    """
    
    def __init__(self, name: str = "SimpleAI"):
        """
        Initialize the AI with a name and empty knowledge base
        """
        self.name = name
        self.knowledge_base = {}  # Stores learned information
        self.training_data = []   # Stores training examples
        self.learning_rate = 0.1  # How quickly the AI learns
        
    def learn(self, input_data: Any, expected_output: Any) -> None:
        """
        Learn from a single example
        Args:
            input_data: The input to learn from
            expected_output: The correct output for this input
        """
        self.training_data.append((input_data, expected_output))
        # Store the pattern in knowledge base
        if isinstance(input_data, (int, float)):
            # For numerical data, store the relationship
            self.knowledge_base[input_data] = expected_output
        else:
            # For other types of data, store as a pattern
            self.knowledge_base[str(input_data)] = expected_output
            
    def predict(self, input_data: Any) -> Any:
        """
        Make a prediction based on learned knowledge
        Args:
            input_data: The input to make a prediction for
        Returns:
            The predicted output
        """
        if isinstance(input_data, (int, float)):
            # For numerical data, find closest known value
            if input_data in self.knowledge_base:
                return self.knowledge_base[input_data]
            else:
                # Find closest known value
                known_values = list(self.knowledge_base.keys())
                if known_values:
                    closest = min(known_values, key=lambda x: abs(x - input_data))
                    return self.knowledge_base[closest]
        else:
            # For other types of data, look for exact match
            return self.knowledge_base.get(str(input_data), "Unknown")
            
    def make_decision(self, options: List[Any], context: Dict[str, Any] = None) -> Any:
        """
        Make a decision from a list of options
        Args:
            options: List of possible choices
            context: Additional information to consider
        Returns:
            The chosen option
        """
        if not options:
            return None
            
        # If we have learned preferences, use them
        if context and str(context) in self.knowledge_base:
            preferred_option = self.knowledge_base[str(context)]
            if preferred_option in options:
                return preferred_option
                
        # Otherwise, make a random choice
        return random.choice(options)
        
    def get_knowledge(self) -> Dict[str, Any]:
        """
        Get the current knowledge base
        Returns:
            Dictionary containing all learned information
        """
        return self.knowledge_base
        
    def clear_knowledge(self) -> None:
        """
        Clear all learned knowledge
        """
        self.knowledge_base = {}
        self.training_data = []

# Example usage
if __name__ == "__main__":
    # Create an instance of the AI
    ai = SimpleAI("MyFirstAI")
    
    # Example 1: Learning numerical patterns
    print("Example 1: Learning numerical patterns")
    ai.learn(1, 2)
    ai.learn(2, 4)
    ai.learn(3, 6)
    print(f"Prediction for input 4: {ai.predict(4)}")  # Should predict something close to 8
    
    # Example 2: Learning text patterns
    print("\nExample 2: Learning text patterns")
    ai.learn("hello", "greeting")
    ai.learn("goodbye", "farewell")
    print(f"Prediction for 'hello': {ai.predict('hello')}")
    
    # Example 3: Making decisions
    print("\nExample 3: Making decisions")
    options = ["red", "blue", "green"]
    print(f"AI chose: {ai.make_decision(options)}")
    
    # Example 4: Learning preferences
    print("\nExample 4: Learning preferences")
    context = {"weather": "sunny", "mood": "happy"}
    ai.learn(str(context), "blue")
    print(f"AI chose with context: {ai.make_decision(options, context)}")
    
    # Show all learned knowledge
    print("\nAll learned knowledge:")
    print(ai.get_knowledge()) 