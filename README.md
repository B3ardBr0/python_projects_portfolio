# Python Projects Portfolio

A collection of Python projects showcasing fundamental programming concepts, from basic exercises to complete applications. This portfolio demonstrates progression from simple scripts to complex, feature-rich programs.

## 📁 Project Structure

```
python-projects/
├── exercises/                    # Python fundamentals & exercises
│   └── Basics/                  # Core Python concepts
├── projects/                    # Complete applications
│   ├── basic_projects/          # Foundational projects
│   │   ├── password_generator/  # 🔐 Secure password generation
│   │   ├── simple_calculator/   # 🧮 Scientific calculator
│   │   ├── task_manager/        # 📝 Task management system
│   │   ├── number_guessing_game/ # 🎲 Interactive guessing game
│   │   ├── word_guessing_game/  # 🎯 Word puzzle game
│   │   └── python_data_analyzer/ # 📊 Data analysis toolkit
│   └── reflex_projects/         # Modern web applications
│       └── my_blog/            # 🌐 Reflex-based blog
└── README.md                   # This file
```

## 🚀 Featured Projects

### 🔐 Password Generator
**File**: `projects/basic_projects/password_generator/`

A cryptographically secure password generator with customizable options.

**Features**:
- Secure random generation using Python's `secrets` module
- Customizable length (4-128 characters)
- Character set selection (uppercase, lowercase, numbers, symbols)
- Ambiguous character exclusion option
- Built-in password strength analyzer
- Multiple password generation

**Skills Demonstrated**: Security best practices, cryptographic randomness, input validation, user interface design

**Usage**:
```bash
cd projects/basic_projects/password_generator/
python password_generator.py
```

### 🧮 Simple Calculator
**File**: `projects/basic_projects/simple_calculator/`

A feature-rich command-line calculator with basic arithmetic, scientific functions, and advanced features.

**Features**:
- Basic operations (+, -, *, /, %, //, **)
- Scientific functions (trigonometric, logarithmic, exponential)
- Expression evaluation with safe parsing
- Memory operations (store, recall, clear, add, subtract)
- Calculation history (last 50 calculations)
- Mathematical constants (π, e)
- Comprehensive error handling

**Skills Demonstrated**: Mathematical computation, safe expression evaluation, memory management, interactive CLI design

**Usage**:
```bash
cd projects/basic_projects/simple_calculator/
python calculator.py
```

### 📝 Task Manager
**File**: `projects/basic_projects/task_manager/`

A comprehensive task management system with priorities, categories, deadlines, and persistent storage.

**Features**:
- Complete CRUD operations for tasks
- Priority levels (Low, Medium, High, Urgent)
- Category organization and filtering
- Deadline tracking with overdue alerts
- Task status management (Pending, In Progress, Completed, Cancelled)
- JSON data persistence
- Search and filtering capabilities
- Comprehensive statistics dashboard
- Multiple date format support

**Skills Demonstrated**: Object-oriented programming, data persistence, datetime handling, JSON serialization, UUID generation, enumeration types

**Usage**:
```bash
cd projects/basic_projects/task_manager/
python task_manager.py
```

### 📊 Python Data Analyzer
**File**: `projects/basic_projects/python_data_analyzer/`

A comprehensive data analysis tool for CSV files with statistical calculations and visualizations.

**Features**:
- CSV file import and cleaning
- Statistical analysis (mean, median, standard deviation, etc.)
- Data grouping and aggregation
- Multiple visualization types (bar charts, histograms, scatter plots, etc.)
- Correlation analysis and heatmaps
- Time series analysis
- Export capabilities

**Skills Demonstrated**: Data analysis, pandas/numpy usage, matplotlib visualization, modular programming, statistical concepts

**Usage**:
```bash
cd projects/basic_projects/python_data_analyzer/
pip install -r requirements.txt
python data_analyzer.py example_data/sample_sales.csv
```

### 🎲 Interactive Games
**Files**: `projects/basic_projects/number_guessing_game/`, `projects/basic_projects/word_guessing_game/`

Classic guessing games demonstrating fundamental programming concepts.

**Features**:
- Random number/word selection
- Input validation and error handling
- Score tracking and difficulty levels
- Interactive gameplay with hints

**Skills Demonstrated**: Random module usage, control structures, input validation, game logic

### 🌐 Reflex Blog
**File**: `projects/reflex_projects/my_blog/`

A modern web application built with the Reflex framework (Python-based web development).

**Features**:
- Modern Python web framework
- Automatic Next.js frontend generation
- Component-based architecture
- Markdown post support

**Skills Demonstrated**: Modern web development, component architecture, full-stack Python development

**Usage**:
```bash
cd projects/reflex_projects/my_blog/
pip install -r requirements.txt
reflex run
```

## 🎓 Learning Progression

This portfolio demonstrates progression through key Python concepts:

### Beginner Level
1. **Basic Syntax** (`exercises/Basics/`) - Variables, loops, functions, operators
2. **Simple Games** - Control structures, random module, input handling

### Intermediate Level
3. **Calculator** - Mathematical operations, error handling, modular design
4. **Password Generator** - Security concepts, randomness, validation

### Advanced Level
5. **Task Manager** - OOP, data persistence, complex data structures
6. **Data Analyzer** - External libraries, data manipulation, visualization
7. **Web Development** - Modern frameworks, full-stack development

## 🛠 Technical Skills Demonstrated

### Core Python
- Variables, data types, and operators
- Control structures (if/else, loops)
- Functions and scope
- Error handling and exceptions
- Object-oriented programming
- File I/O operations

### Libraries and Modules
- **Standard Library**: `json`, `datetime`, `uuid`, `secrets`, `math`, `operator`, `enum`
- **Data Analysis**: `pandas`, `numpy`, `matplotlib`
- **Web Development**: `reflex`, `flask`
- **Testing**: `unittest`

### Programming Concepts
- **Security**: Cryptographic randomness, password strength analysis
- **Data Structures**: Lists, dictionaries, classes, enums
- **Algorithms**: Search, sort, statistical calculations
- **Design Patterns**: Object-oriented design, modular programming
- **User Experience**: Interactive CLIs, input validation, error messages
- **Data Persistence**: JSON serialization, file handling

### Software Engineering
- **Code Organization**: Modular design, separation of concerns
- **Documentation**: Comprehensive READMEs, inline comments
- **Error Handling**: Comprehensive validation and user feedback
- **Testing**: Unit tests for critical functions
- **Version Control**: Git repository with clear commit history

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd python-projects
   ```

2. For projects with dependencies:
   ```bash
   cd projects/basic_projects/python_data_analyzer/
   pip install -r requirements.txt
   ```

3. Run any project:
   ```bash
   python project_name.py
   ```

## 📈 Future Enhancements

Planned additions to the portfolio:
- **Database Integration**: PostgreSQL/SQLite projects
- **API Development**: REST APIs with Flask/FastAPI
- **Machine Learning**: Data science and ML projects
- **GUI Applications**: tkinter or PyQt projects
- **Web Scraping**: BeautifulSoup and requests projects
- **Automation**: System administration and automation scripts

## 📝 Project Status

- ✅ **Password Generator** - Complete with comprehensive features
- ✅ **Simple Calculator** - Complete with scientific functions
- ✅ **Task Manager** - Complete with full CRUD operations
- ✅ **Data Analyzer** - Complete with visualizations
- ✅ **Guessing Games** - Complete basic implementations
- 🔄 **Reflex Blog** - In development
- 📅 **Future Projects** - Planned enhancements

## 🤝 Contributing

This is a personal learning portfolio, but suggestions and feedback are welcome! Feel free to:
- Report issues or bugs
- Suggest improvements
- Propose new project ideas
- Share learning resources

## 📧 Contact

Created and maintained by **B3ardBr0**
- GitHub: [@B3ardBr0](https://github.com/B3ardBr0)
- Email: wjmaritz@protonmail.com

---

*This portfolio represents my journey learning Python programming, from basic concepts to advanced applications. Each project builds upon previous knowledge while introducing new concepts and challenges.*