# SimpleAI

A beginner-friendly AI class that demonstrates basic artificial intelligence concepts in Python. This project is perfect for learning about AI fundamentals and how to implement simple AI systems.

## Features

- Learning from examples
- Making predictions based on learned patterns
- Decision making with context awareness
- Knowledge base management
- Support for both numerical and text data

## Installation

1. Clone this repository:
```bash
git clone https://github.com/LKZOwner/SimpleAI.git
cd SimpleAI
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Here's a simple example of how to use SimpleAI:

```python
from simple_ai import SimpleAI

# Create a new AI instance
ai = SimpleAI("MyFirstAI")

# Teach the AI
ai.learn(1, 2)
ai.learn("hello", "greeting")

# Make predictions
result = ai.predict(1)  # Returns 2
greeting = ai.predict("hello")  # Returns "greeting"

# Make decisions
choice = ai.make_decision(["red", "blue", "green"])
```

## Examples

The repository includes two ways to learn about the AI:

1. **Basic Examples** in `simple_ai.py`:
   - Learning numerical patterns
   - Learning text patterns
   - Making decisions
   - Learning preferences with context

2. **Detailed Examples** in `examples.py`:
   - Example 1: Basic Learning and Prediction
     - Shows how the AI learns numerical patterns
     - Demonstrates prediction with known and unknown inputs
   - Example 2: Text Learning
     - Shows how the AI learns and processes text
     - Demonstrates text pattern matching
   - Example 3: Context-Aware Decision Making
     - Shows how the AI makes decisions based on context
     - Demonstrates weather and time-based decisions
   - Example 4: Advanced Learning
     - Shows how the AI handles multiple features
     - Demonstrates complex scenario learning

To run the detailed examples:
```bash
python examples.py
```

Each example includes:
- Step-by-step explanations
- Real-world use cases
- Interactive demonstrations
- Clear output formatting

## How It Works

The SimpleAI class implements several key AI concepts:

1. **Learning System**
   - Stores patterns in a knowledge base
   - Can learn from both numerical and text data
   - Maintains training data for reference

2. **Prediction System**
   - Makes predictions based on learned patterns
   - Handles unknown inputs by finding closest matches
   - Supports both exact and approximate matching

3. **Decision Making**
   - Makes context-aware decisions
   - Can learn preferences for different situations
   - Falls back to random choices for unknown contexts

4. **Knowledge Management**
   - Maintains a knowledge base of learned information
   - Can retrieve and clear learned knowledge
   - Supports multiple types of data

## Contributing

Feel free to contribute to this project by:
1. Forking the repository
2. Creating a new branch
3. Making your changes
4. Submitting a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

- LKZOwner (GitHub: [@LKZOwner](https://github.com/LKZOwner)) 