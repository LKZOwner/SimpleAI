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

The repository includes several examples in the main file:
1. Learning numerical patterns
2. Learning text patterns
3. Making decisions
4. Learning preferences with context

Run the examples:
```bash
python simple_ai.py
```

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