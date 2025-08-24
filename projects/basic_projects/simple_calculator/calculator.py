#!/usr/bin/env python3
"""
Simple Calculator
A command-line calculator with basic arithmetic operations, scientific functions, 
memory operations, and calculation history.
"""

import math
import operator
from typing import List, Union, Callable
from enum import Enum


class Operation(Enum):
    """Enumeration of supported operations."""
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    POWER = "**"
    MODULO = "%"
    FLOOR_DIVIDE = "//"


class Calculator:
    """A feature-rich calculator with memory and history functions."""
    
    def __init__(self):
        self.memory: float = 0.0
        self.history: List[str] = []
        self.last_result: float = 0.0
        
        # Basic operations mapping
        self.operations = {
            Operation.ADD.value: operator.add,
            Operation.SUBTRACT.value: operator.sub,
            Operation.MULTIPLY.value: operator.mul,
            Operation.DIVIDE.value: operator.truediv,
            Operation.POWER.value: operator.pow,
            Operation.MODULO.value: operator.mod,
            Operation.FLOOR_DIVIDE.value: operator.floordiv,
        }
    
    def add_to_history(self, expression: str, result: float):
        """Add calculation to history."""
        self.history.append(f"{expression} = {result}")
        if len(self.history) > 50:  # Keep last 50 calculations
            self.history.pop(0)
    
    def basic_operation(self, num1: float, operator_str: str, num2: float) -> float:
        """Perform basic arithmetic operations."""
        if operator_str not in self.operations:
            raise ValueError(f"Unsupported operation: {operator_str}")
        
        if operator_str == "/" and num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        
        if operator_str == "//" and num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        
        if operator_str == "%" and num2 == 0:
            raise ZeroDivisionError("Cannot calculate modulo with zero")
        
        return self.operations[operator_str](num1, num2)
    
    def scientific_operation(self, function: str, num: float) -> float:
        """Perform scientific operations."""
        scientific_functions = {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'asin': math.asin,
            'acos': math.acos,
            'atan': math.atan,
            'sinh': math.sinh,
            'cosh': math.cosh,
            'tanh': math.tanh,
            'log': math.log10,
            'ln': math.log,
            'sqrt': math.sqrt,
            'ceil': math.ceil,
            'floor': math.floor,
            'abs': abs,
            'exp': math.exp,
            'factorial': math.factorial,
            'degrees': math.degrees,
            'radians': math.radians,
        }
        
        if function not in scientific_functions:
            raise ValueError(f"Unsupported function: {function}")
        
        # Special cases for domain restrictions
        if function in ['asin', 'acos'] and not -1 <= num <= 1:
            raise ValueError(f"{function} requires input between -1 and 1")
        
        if function in ['log', 'ln', 'sqrt'] and num <= 0:
            raise ValueError(f"{function} requires positive input")
        
        if function == 'factorial' and (num != int(num) or num < 0):
            raise ValueError("Factorial requires non-negative integer")
        
        if function == 'tan' and abs(num % math.pi - math.pi/2) < 1e-10:
            raise ValueError("Tangent is undefined at π/2 + nπ")
        
        return scientific_functions[function](num)
    
    def evaluate_expression(self, expression: str) -> float:
        """Evaluate a mathematical expression safely."""
        # Replace some common mathematical notations
        expression = expression.replace('^', '**')
        expression = expression.replace('π', str(math.pi))
        expression = expression.replace('e', str(math.e))
        
        # Allow only safe characters and functions
        allowed_chars = set('0123456789+-*/().% ')
        allowed_names = {
            'sin', 'cos', 'tan', 'asin', 'acos', 'atan',
            'sinh', 'cosh', 'tanh', 'log', 'ln', 'sqrt',
            'ceil', 'floor', 'abs', 'exp', 'factorial',
            'degrees', 'radians', 'pi', 'e'
        }
        
        # Create safe namespace for evaluation
        safe_dict = {
            "__builtins__": {},
            "sin": math.sin, "cos": math.cos, "tan": math.tan,
            "asin": math.asin, "acos": math.acos, "atan": math.atan,
            "sinh": math.sinh, "cosh": math.cosh, "tanh": math.tanh,
            "log": math.log10, "ln": math.log, "sqrt": math.sqrt,
            "ceil": math.ceil, "floor": math.floor, "abs": abs,
            "exp": math.exp, "factorial": math.factorial,
            "degrees": math.degrees, "radians": math.radians,
            "pi": math.pi, "e": math.e
        }
        
        try:
            result = eval(expression, safe_dict, {})
            return float(result)
        except Exception as e:
            raise ValueError(f"Invalid expression: {e}")
    
    def memory_store(self, value: float):
        """Store value in memory."""
        self.memory = value
    
    def memory_recall(self) -> float:
        """Recall value from memory."""
        return self.memory
    
    def memory_clear(self):
        """Clear memory."""
        self.memory = 0.0
    
    def memory_add(self, value: float):
        """Add value to memory."""
        self.memory += value
    
    def memory_subtract(self, value: float):
        """Subtract value from memory."""
        self.memory -= value
    
    def get_history(self, count: int = 10) -> List[str]:
        """Get recent calculation history."""
        return self.history[-count:] if self.history else []
    
    def clear_history(self):
        """Clear calculation history."""
        self.history.clear()


def display_menu():
    """Display the main menu."""
    print("\n" + "="*60)
    print("                    SIMPLE CALCULATOR")
    print("="*60)
    print("1.  Basic Operations (+, -, *, /, %, //, **)")
    print("2.  Scientific Functions")
    print("3.  Expression Evaluation")
    print("4.  Memory Operations")
    print("5.  View History")
    print("6.  Constants (π, e)")
    print("7.  Help")
    print("8.  Exit")
    print("="*60)


def display_scientific_menu():
    """Display scientific functions menu."""
    print("\nScientific Functions:")
    print("Trigonometric: sin, cos, tan, asin, acos, atan")
    print("Hyperbolic: sinh, cosh, tanh")
    print("Logarithmic: log (base 10), ln (natural log)")
    print("Other: sqrt, abs, exp, ceil, floor, factorial")
    print("Angle conversion: degrees, radians")


def display_memory_menu():
    """Display memory operations menu."""
    print("\nMemory Operations:")
    print("MS - Memory Store")
    print("MR - Memory Recall") 
    print("MC - Memory Clear")
    print("M+ - Add to Memory")
    print("M- - Subtract from Memory")


def main():
    """Main program loop."""
    calc = Calculator()
    
    print("Welcome to the Simple Calculator!")
    print("Type 'menu' at any time to return to the main menu")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-8) or 'menu': ").strip()
        
        if choice == '1':
            print("\nBasic Operations")
            print("Supported operators: +, -, *, /, %, //, **")
            
            try:
                num1 = float(input("Enter first number: "))
                op = input("Enter operator (+, -, *, /, %, //, **): ").strip()
                num2 = float(input("Enter second number: "))
                
                result = calc.basic_operation(num1, op, num2)
                expression = f"{num1} {op} {num2}"
                
                print(f"\nResult: {result}")
                calc.add_to_history(expression, result)
                calc.last_result = result
                
            except ValueError as e:
                print(f"Error: {e}")
            except ZeroDivisionError as e:
                print(f"Error: {e}")
                
        elif choice == '2':
            display_scientific_menu()
            
            try:
                function = input("\nEnter function name: ").strip().lower()
                num = float(input("Enter number: "))
                
                result = calc.scientific_operation(function, num)
                expression = f"{function}({num})"
                
                print(f"\nResult: {result}")
                calc.add_to_history(expression, result)
                calc.last_result = result
                
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == '3':
            print("\nExpression Evaluation")
            print("Examples: 2+3*4, sin(pi/2), sqrt(16), 2**3")
            print("Use 'pi' for π and 'e' for Euler's number")
            
            try:
                expression = input("Enter expression: ").strip()
                if expression:
                    result = calc.evaluate_expression(expression)
                    print(f"\nResult: {result}")
                    calc.add_to_history(expression, result)
                    calc.last_result = result
                    
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == '4':
            display_memory_menu()
            
            while True:
                mem_choice = input("\nEnter memory operation (MS/MR/MC/M+/M-) or 'back': ").strip().upper()
                
                if mem_choice == 'BACK':
                    break
                elif mem_choice == 'MS':
                    try:
                        value = float(input("Enter value to store: "))
                        calc.memory_store(value)
                        print(f"Stored {value} in memory")
                    except ValueError:
                        print("Invalid number")
                        
                elif mem_choice == 'MR':
                    print(f"Memory: {calc.memory_recall()}")
                    
                elif mem_choice == 'MC':
                    calc.memory_clear()
                    print("Memory cleared")
                    
                elif mem_choice == 'M+':
                    try:
                        value = float(input("Enter value to add to memory: "))
                        calc.memory_add(value)
                        print(f"Added {value} to memory. New value: {calc.memory_recall()}")
                    except ValueError:
                        print("Invalid number")
                        
                elif mem_choice == 'M-':
                    try:
                        value = float(input("Enter value to subtract from memory: "))
                        calc.memory_subtract(value)
                        print(f"Subtracted {value} from memory. New value: {calc.memory_recall()}")
                    except ValueError:
                        print("Invalid number")
                        
                else:
                    print("Invalid memory operation")
                    
        elif choice == '5':
            history = calc.get_history()
            if history:
                print("\nCalculation History:")
                for i, calculation in enumerate(history, 1):
                    print(f"{i:2d}. {calculation}")
                    
                clear = input("\nClear history? (y/n): ").strip().lower()
                if clear == 'y':
                    calc.clear_history()
                    print("History cleared")
            else:
                print("\nNo calculations in history")
                
        elif choice == '6':
            print("\nMathematical Constants:")
            print(f"π (pi) = {math.pi}")
            print(f"e (Euler's number) = {math.e}")
            print(f"τ (tau) = {2 * math.pi}")
            print(f"φ (golden ratio) = {(1 + math.sqrt(5)) / 2}")
            
        elif choice == '7':
            print("\nCalculator Help:")
            print("• Use the menu to navigate between different modes")
            print("• Basic operations: +, -, *, /, % (modulo), // (floor division), ** (power)")
            print("• Scientific functions: sin, cos, tan, log, sqrt, etc.")
            print("• Expression evaluation: Enter complete expressions like '2+3*sin(pi/4)'")
            print("• Memory operations: Store, recall, and manipulate values in memory")
            print("• History: View and clear your calculation history")
            print("• Constants: Use 'pi' and 'e' in expressions")
            
        elif choice == '8':
            print("\nThank you for using the Simple Calculator!")
            print("Keep calculating! 🧮")
            break
            
        else:
            print("Invalid choice. Please select 1-8.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()