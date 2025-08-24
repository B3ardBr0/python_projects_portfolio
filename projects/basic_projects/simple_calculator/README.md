# Simple Calculator

A feature-rich command-line calculator with basic arithmetic operations, scientific functions, memory operations, and calculation history.

## Features

### Basic Operations
- Addition (+), Subtraction (-), Multiplication (*)
- Division (/), Floor Division (//), Modulo (%)
- Exponentiation (**)
- Error handling for division by zero

### Scientific Functions
- **Trigonometric**: sin, cos, tan, asin, acos, atan
- **Hyperbolic**: sinh, cosh, tanh
- **Logarithmic**: log (base 10), ln (natural logarithm)
- **Other Functions**: sqrt, abs, exp, ceil, floor, factorial
- **Angle Conversion**: degrees, radians

### Expression Evaluation
- Evaluate complete mathematical expressions
- Support for mathematical constants (π, e)
- Safe evaluation with restricted namespace

### Memory Operations
- **MS** - Memory Store
- **MR** - Memory Recall
- **MC** - Memory Clear
- **M+** - Add to Memory
- **M-** - Subtract from Memory

### Additional Features
- **History**: Track last 50 calculations
- **Constants**: Built-in mathematical constants
- **Help System**: Comprehensive usage instructions

## Usage

### Running the Calculator

```bash
python calculator.py
```

### Menu Navigation

The calculator provides an interactive menu system:

```
==================================================
                SIMPLE CALCULATOR
==================================================
1.  Basic Operations (+, -, *, /, %, //, **)
2.  Scientific Functions
3.  Expression Evaluation
4.  Memory Operations
5.  View History
6.  Constants (π, e)
7.  Help
8.  Exit
==================================================
```

### Example Usage

#### Basic Operations
```
Enter first number: 15
Enter operator (+, -, *, /, %, //, **): *
Enter second number: 3.5

Result: 52.5
```

#### Scientific Functions
```
Enter function name: sin
Enter number: 1.5708  # π/2

Result: 1.0
```

#### Expression Evaluation
```
Enter expression: 2 + 3 * sin(pi/2) - sqrt(16)

Result: 1.0
```

#### Memory Operations
```
Memory Operation: MS
Enter value to store: 42.5
Stored 42.5 in memory

Memory Operation: M+
Enter value to add to memory: 7.5
Added 7.5 to memory. New value: 50.0
```

## Supported Functions

### Basic Operators
| Operator | Description | Example |
|----------|-------------|---------|
| + | Addition | 5 + 3 = 8 |
| - | Subtraction | 5 - 3 = 2 |
| * | Multiplication | 5 * 3 = 15 |
| / | Division | 5 / 3 = 1.667 |
| // | Floor Division | 5 // 3 = 1 |
| % | Modulo | 5 % 3 = 2 |
| ** | Exponentiation | 5 ** 3 = 125 |

### Scientific Functions
| Function | Description | Domain |
|----------|-------------|--------|
| sin(x) | Sine | All real numbers |
| cos(x) | Cosine | All real numbers |
| tan(x) | Tangent | x ≠ π/2 + nπ |
| asin(x) | Arcsine | -1 ≤ x ≤ 1 |
| acos(x) | Arccosine | -1 ≤ x ≤ 1 |
| atan(x) | Arctangent | All real numbers |
| log(x) | Log base 10 | x > 0 |
| ln(x) | Natural log | x > 0 |
| sqrt(x) | Square root | x ≥ 0 |
| factorial(x) | Factorial | x ≥ 0, integer |
| abs(x) | Absolute value | All real numbers |
| exp(x) | Exponential (e^x) | All real numbers |

### Constants
- **π** (pi): 3.14159...
- **e**: 2.71828... (Euler's number)
- **τ** (tau): 6.28318... (2π)
- **φ** (phi): 1.61803... (Golden ratio)

## Error Handling

The calculator includes comprehensive error handling:
- Division by zero protection
- Domain validation for scientific functions
- Invalid expression detection
- Input validation for all operations

## Example Session

```
Welcome to the Simple Calculator!

Basic Operations
Enter first number: 10
Enter operator: **
Enter second number: 2
Result: 100.0

Scientific Functions
Enter function name: sqrt
Enter number: 100
Result: 10.0

Expression Evaluation  
Enter expression: log(100) + sin(pi/2)
Result: 3.0

Memory Operations
MS: Stored 3.0 in memory
M+: Added 7 to memory. New value: 10.0
MR: Memory: 10.0
```

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## Features Demonstrated

- Object-oriented programming with classes
- Error handling and input validation
- Mathematical operations and functions
- Data persistence (history and memory)
- Interactive command-line interface
- Safe expression evaluation