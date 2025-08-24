# Task Manager

A comprehensive command-line task management system with priorities, categories, deadlines, and persistent data storage.

## Features

### Core Task Management
- **Create Tasks**: Add tasks with titles, descriptions, categories, and deadlines
- **Update Tasks**: Modify task details, status, and properties
- **Delete Tasks**: Remove tasks with confirmation
- **Search Tasks**: Find tasks by keywords in title or description

### Task Organization
- **Categories**: Organize tasks into custom categories
- **Priorities**: Four priority levels (Low, Medium, High, Urgent)
- **Status Tracking**: Pending, In Progress, Completed, Cancelled
- **Deadlines**: Set and track task deadlines with overdue alerts

### Advanced Features
- **Data Persistence**: Tasks saved automatically to JSON file
- **Overdue Detection**: Automatic identification of overdue tasks
- **Upcoming Tasks**: View tasks due within specified timeframe
- **Statistics Dashboard**: Comprehensive task analytics
- **Smart Sorting**: Tasks sorted by urgency and priority

### Visual Indicators
- **Status Icons**: ⏳ Pending, 🔄 In Progress, ✅ Completed, ❌ Cancelled
- **Priority Colors**: 🔵 Low, 🟡 Medium, 🟠 High, 🔴 Urgent
- **Deadline Alerts**: 📅 Due dates, ⚠️ Overdue warnings

## Usage

### Running the Task Manager

```bash
python task_manager.py
```

### Menu Navigation

```
==================================================
                TASK MANAGER
==================================================
1.  Add New Task           9.  Mark Task as Completed
2.  View All Tasks         10. Mark Task as In Progress  
3.  View Tasks by Status   11. View Overdue Tasks
4.  View Tasks by Category 12. View Upcoming Tasks
5.  View Tasks by Priority 13. Task Statistics
6.  Search Tasks          14. Help
7.  Update Task           15. Exit
8.  Delete Task
==================================================
```

### Creating a Task

```
Task title: Complete project documentation
Description (optional): Write comprehensive README and API docs
Category (default: General): Work
Priority (1-4, default: 2): 3
Deadline (YYYY-MM-DD or 'today', 'tomorrow', '7d', optional): 2024-08-30

✅ Task created successfully!
Task ID: a1b2c3d4
```

### Viewing Tasks

Tasks are displayed with comprehensive information:

```
All Tasks (5):
--------------------------------------------------------------------------------
 1. ⏳ 🔴 [a1b2c3d4] Complete project documentation [Work] (📅 Due in 3 days)
    Description: Write comprehensive README and API docs
    Created: 2024-08-27 14:30

 2. 🔄 🟡 [e5f6g7h8] Review pull requests [Development]
    Created: 2024-08-26 09:15

 3. ✅ 🟠 [i9j0k1l2] Deploy to production [DevOps]
    Description: Deploy version 2.1.0 to production servers
    Created: 2024-08-25 16:45
    Completed: 2024-08-26 10:30
```

## Supported Date Formats

### Absolute Dates
- **YYYY-MM-DD**: 2024-12-25
- **MM/DD/YYYY**: 12/25/2024  
- **DD/MM/YYYY**: 25/12/2024
- **With Time**: 2024-12-25 15:30

### Relative Dates
- **today**: Today at 11:59 PM
- **tomorrow**: Tomorrow at 11:59 PM
- **7d**: 7 days from now
- **2w**: 2 weeks from now

## Task Priorities

| Priority | Icon | Description | Use Case |
|----------|------|-------------|----------|
| Low | 🔵 | Nice to have | Optional improvements |
| Medium | 🟡 | Normal priority | Regular tasks |
| High | 🟠 | Important | Critical for progress |
| Urgent | 🔴 | Immediate action | Blocking issues |

## Task Statistics

The statistics dashboard provides insights into your productivity:

```
📊 Task Statistics
========================================
Total Tasks: 25
Completed: 18
Pending: 5
In Progress: 2
Cancelled: 0
Overdue: 1
Completion Rate: 72.0%

Priority Breakdown:
  LOW: 3
  MEDIUM: 12
  HIGH: 8
  URGENT: 2

Category Breakdown:
  Work: 15
  Personal: 6
  Development: 4
```

## Data Storage

- **File**: `tasks.json` (automatically created)
- **Format**: JSON with full task details
- **Backup**: Manual backup recommended for important data
- **Portability**: JSON file can be moved between systems

## Example Usage Session

```bash
# Start the task manager
python task_manager.py

# Add a new urgent task
1. Add New Task
Task title: Fix critical bug in payment system
Description: Payment processing fails on mobile
Category: Development
Priority: 4 (Urgent)
Deadline: today

# View overdue tasks
11. View Overdue Tasks
⚠️ Overdue Tasks (1):
1. ⏳ 🔴 [abc123] Fix server memory leak [DevOps] (⚠️ OVERDUE by 2 days)

# Mark task as completed
9. Mark Task as Completed
Enter task ID: abc123
✅ Task marked as completed!

# View statistics
13. Task Statistics
Total Tasks: 10
Completion Rate: 90.0%
```

## Key Features Demonstrated

### Programming Concepts
- **Object-Oriented Design**: Task and TaskManager classes
- **Enums**: Type-safe priority and status definitions
- **JSON Serialization**: Data persistence with custom encoding
- **DateTime Handling**: Deadline tracking and date parsing
- **File I/O**: Automatic saving and loading
- **UUID Generation**: Unique task identifiers
- **Error Handling**: Comprehensive validation and user feedback

### User Experience
- **Interactive CLI**: Menu-driven navigation
- **Visual Feedback**: Icons and emojis for better UX
- **Smart Sorting**: Tasks ordered by urgency and priority
- **Flexible Input**: Multiple date formats and optional fields
- **Data Validation**: Input checking and error messages

### Advanced Features
- **Search Functionality**: Find tasks by keywords
- **Filtering Options**: View tasks by multiple criteria
- **Analytics**: Task completion rates and breakdowns
- **Data Persistence**: Automatic JSON storage
- **Relative Dates**: Natural language date input

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## File Structure

```
task_manager/
├── task_manager.py    # Main application
├── README.md         # Documentation
└── tasks.json       # Data file (auto-created)
```

The Task Manager demonstrates professional software development practices while maintaining simplicity and ease of use for daily productivity management.