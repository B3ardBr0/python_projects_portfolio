#!/usr/bin/env python3
"""
Task Manager
A comprehensive command-line task management system with priorities, categories, 
deadlines, and data persistence.
"""

import json
import os
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Any
from enum import Enum
import uuid


class Priority(Enum):
    """Task priority levels."""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    URGENT = 4


class Status(Enum):
    """Task status options."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class Task:
    """Represents a single task with all its properties."""
    
    def __init__(self, title: str, description: str = "", category: str = "General", 
                 priority: Priority = Priority.MEDIUM, deadline: Optional[datetime] = None):
        self.id = str(uuid.uuid4())[:8]
        self.title = title
        self.description = description
        self.category = category
        self.priority = priority
        self.status = Status.PENDING
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.deadline = deadline
        self.completed_at = None
    
    def mark_completed(self):
        """Mark task as completed."""
        self.status = Status.COMPLETED
        self.completed_at = datetime.now()
        self.updated_at = datetime.now()
    
    def mark_in_progress(self):
        """Mark task as in progress."""
        self.status = Status.IN_PROGRESS
        self.updated_at = datetime.now()
    
    def mark_cancelled(self):
        """Mark task as cancelled."""
        self.status = Status.CANCELLED
        self.updated_at = datetime.now()
    
    def is_overdue(self) -> bool:
        """Check if task is overdue."""
        if self.deadline and self.status != Status.COMPLETED:
            return datetime.now() > self.deadline
        return False
    
    def days_until_deadline(self) -> Optional[int]:
        """Calculate days until deadline."""
        if self.deadline:
            delta = self.deadline - datetime.now()
            return delta.days
        return None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert task to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'priority': self.priority.value,
            'status': self.status.value,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'deadline': self.deadline.isoformat() if self.deadline else None,
            'completed_at': self.completed_at.isoformat() if self.completed_at else None
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Task':
        """Create task from dictionary."""
        task = cls(data['title'], data['description'], data['category'], 
                   Priority(data['priority']))
        task.id = data['id']
        task.status = Status(data['status'])
        task.created_at = datetime.fromisoformat(data['created_at'])
        task.updated_at = datetime.fromisoformat(data['updated_at'])
        
        if data['deadline']:
            task.deadline = datetime.fromisoformat(data['deadline'])
        if data['completed_at']:
            task.completed_at = datetime.fromisoformat(data['completed_at'])
            
        return task
    
    def __str__(self) -> str:
        """String representation of task."""
        status_icon = {
            Status.PENDING: "⏳",
            Status.IN_PROGRESS: "🔄",
            Status.COMPLETED: "✅",
            Status.CANCELLED: "❌"
        }
        
        priority_icon = {
            Priority.LOW: "🔵",
            Priority.MEDIUM: "🟡",
            Priority.HIGH: "🟠",
            Priority.URGENT: "🔴"
        }
        
        deadline_str = ""
        if self.deadline:
            days = self.days_until_deadline()
            if self.is_overdue():
                deadline_str = f" (⚠️ OVERDUE by {abs(days)} days)"
            elif days is not None:
                if days == 0:
                    deadline_str = " (📅 Due TODAY)"
                elif days > 0:
                    deadline_str = f" (📅 Due in {days} days)"
        
        return f"{status_icon[self.status]} {priority_icon[self.priority]} [{self.id}] {self.title} [{self.category}]{deadline_str}"


class TaskManager:
    """Main task management system."""
    
    def __init__(self, data_file: str = "tasks.json"):
        self.data_file = data_file
        self.tasks: List[Task] = []
        self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from JSON file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.tasks = [Task.from_dict(task_data) for task_data in data]
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error loading tasks: {e}")
                self.tasks = []
    
    def save_tasks(self):
        """Save tasks to JSON file."""
        try:
            with open(self.data_file, 'w') as f:
                json.dump([task.to_dict() for task in self.tasks], f, indent=2)
        except Exception as e:
            print(f"Error saving tasks: {e}")
    
    def add_task(self, title: str, description: str = "", category: str = "General", 
                 priority: Priority = Priority.MEDIUM, deadline: Optional[datetime] = None) -> Task:
        """Add a new task."""
        task = Task(title, description, category, priority, deadline)
        self.tasks.append(task)
        self.save_tasks()
        return task
    
    def get_task_by_id(self, task_id: str) -> Optional[Task]:
        """Find task by ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def update_task(self, task_id: str, **kwargs) -> bool:
        """Update task properties."""
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        
        for key, value in kwargs.items():
            if hasattr(task, key):
                setattr(task, key, value)
        
        task.updated_at = datetime.now()
        self.save_tasks()
        return True
    
    def delete_task(self, task_id: str) -> bool:
        """Delete a task."""
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
            return True
        return False
    
    def get_tasks_by_status(self, status: Status) -> List[Task]:
        """Get tasks filtered by status."""
        return [task for task in self.tasks if task.status == status]
    
    def get_tasks_by_category(self, category: str) -> List[Task]:
        """Get tasks filtered by category."""
        return [task for task in self.tasks if task.category.lower() == category.lower()]
    
    def get_tasks_by_priority(self, priority: Priority) -> List[Task]:
        """Get tasks filtered by priority."""
        return [task for task in self.tasks if task.priority == priority]
    
    def get_overdue_tasks(self) -> List[Task]:
        """Get all overdue tasks."""
        return [task for task in self.tasks if task.is_overdue()]
    
    def get_upcoming_tasks(self, days: int = 7) -> List[Task]:
        """Get tasks due within specified days."""
        upcoming = []
        cutoff_date = datetime.now() + timedelta(days=days)
        
        for task in self.tasks:
            if (task.deadline and task.status != Status.COMPLETED and 
                datetime.now() <= task.deadline <= cutoff_date):
                upcoming.append(task)
        
        return sorted(upcoming, key=lambda t: t.deadline)
    
    def search_tasks(self, query: str) -> List[Task]:
        """Search tasks by title or description."""
        query = query.lower()
        return [task for task in self.tasks 
                if query in task.title.lower() or query in task.description.lower()]
    
    def get_categories(self) -> List[str]:
        """Get all unique categories."""
        return list(set(task.category for task in self.tasks))
    
    def get_task_statistics(self) -> Dict[str, Any]:
        """Get comprehensive task statistics."""
        total = len(self.tasks)
        if total == 0:
            return {'total': 0}
        
        completed = len(self.get_tasks_by_status(Status.COMPLETED))
        pending = len(self.get_tasks_by_status(Status.PENDING))
        in_progress = len(self.get_tasks_by_status(Status.IN_PROGRESS))
        cancelled = len(self.get_tasks_by_status(Status.CANCELLED))
        overdue = len(self.get_overdue_tasks())
        
        # Priority breakdown
        priority_counts = {}
        for priority in Priority:
            priority_counts[priority.name] = len(self.get_tasks_by_priority(priority))
        
        # Category breakdown
        category_counts = {}
        for category in self.get_categories():
            category_counts[category] = len(self.get_tasks_by_category(category))
        
        return {
            'total': total,
            'completed': completed,
            'pending': pending,
            'in_progress': in_progress,
            'cancelled': cancelled,
            'overdue': overdue,
            'completion_rate': round((completed / total) * 100, 1) if total > 0 else 0,
            'priority_breakdown': priority_counts,
            'category_breakdown': category_counts
        }


def display_main_menu():
    """Display the main menu."""
    print("\n" + "="*60)
    print("                    TASK MANAGER")
    print("="*60)
    print("1.  Add New Task")
    print("2.  View All Tasks")
    print("3.  View Tasks by Status")
    print("4.  View Tasks by Category")
    print("5.  View Tasks by Priority")
    print("6.  Search Tasks")
    print("7.  Update Task")
    print("8.  Delete Task")
    print("9.  Mark Task as Completed")
    print("10. Mark Task as In Progress")
    print("11. View Overdue Tasks")
    print("12. View Upcoming Tasks")
    print("13. Task Statistics")
    print("14. Help")
    print("15. Exit")
    print("="*60)


def parse_date(date_str: str) -> Optional[datetime]:
    """Parse date string into datetime object."""
    if not date_str or date_str.lower() == 'none':
        return None
    
    try:
        # Try different date formats
        formats = [
            "%Y-%m-%d",
            "%Y-%m-%d %H:%M",
            "%m/%d/%Y",
            "%m/%d/%Y %H:%M",
            "%d/%m/%Y",
            "%d/%m/%Y %H:%M"
        ]
        
        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        
        # Try relative dates
        if date_str.lower() == 'today':
            return datetime.now().replace(hour=23, minute=59, second=59)
        elif date_str.lower() == 'tomorrow':
            return (datetime.now() + timedelta(days=1)).replace(hour=23, minute=59, second=59)
        elif date_str.endswith('d'):
            days = int(date_str[:-1])
            return datetime.now() + timedelta(days=days)
        elif date_str.endswith('w'):
            weeks = int(date_str[:-1])
            return datetime.now() + timedelta(weeks=weeks)
        
        raise ValueError("Invalid date format")
        
    except ValueError:
        print(f"Invalid date format: {date_str}")
        print("Supported formats: YYYY-MM-DD, MM/DD/YYYY, 'today', 'tomorrow', '7d', '2w'")
        return None


def display_tasks(tasks: List[Task], title: str = "Tasks"):
    """Display a list of tasks."""
    if not tasks:
        print(f"\nNo {title.lower()} found.")
        return
    
    print(f"\n{title} ({len(tasks)}):")
    print("-" * 80)
    
    # Sort tasks: overdue first, then by priority, then by deadline
    def sort_key(task):
        overdue = task.is_overdue()
        priority = task.priority.value
        deadline = task.deadline if task.deadline else datetime.max
        return (not overdue, -priority, deadline)
    
    sorted_tasks = sorted(tasks, key=sort_key)
    
    for i, task in enumerate(sorted_tasks, 1):
        print(f"{i:2d}. {task}")
        if task.description:
            print(f"    Description: {task.description}")
        print(f"    Created: {task.created_at.strftime('%Y-%m-%d %H:%M')}")
        if task.completed_at:
            print(f"    Completed: {task.completed_at.strftime('%Y-%m-%d %H:%M')}")
        print()


def main():
    """Main program loop."""
    manager = TaskManager()
    
    print("Welcome to the Task Manager!")
    print("Your personal productivity companion 📝")
    
    while True:
        display_main_menu()
        choice = input("Enter your choice (1-15): ").strip()
        
        if choice == '1':
            print("\n--- Add New Task ---")
            title = input("Task title: ").strip()
            if not title:
                print("Task title is required!")
                continue
            
            description = input("Description (optional): ").strip()
            category = input("Category (default: General): ").strip() or "General"
            
            print("Priority levels: 1=Low, 2=Medium, 3=High, 4=Urgent")
            try:
                priority_num = int(input("Priority (1-4, default: 2): ") or "2")
                priority = Priority(priority_num)
            except ValueError:
                priority = Priority.MEDIUM
            
            deadline_str = input("Deadline (YYYY-MM-DD or 'today', 'tomorrow', '7d', optional): ").strip()
            deadline = parse_date(deadline_str)
            
            task = manager.add_task(title, description, category, priority, deadline)
            print(f"\n✅ Task created successfully!")
            print(f"Task ID: {task.id}")
            
        elif choice == '2':
            display_tasks(manager.tasks, "All Tasks")
            
        elif choice == '3':
            print("\nTask Status Options:")
            print("1. Pending")
            print("2. In Progress") 
            print("3. Completed")
            print("4. Cancelled")
            
            try:
                status_choice = int(input("Select status (1-4): "))
                status_map = {1: Status.PENDING, 2: Status.IN_PROGRESS, 3: Status.COMPLETED, 4: Status.CANCELLED}
                status = status_map[status_choice]
                tasks = manager.get_tasks_by_status(status)
                display_tasks(tasks, f"{status.value.replace('_', ' ').title()} Tasks")
            except (ValueError, KeyError):
                print("Invalid status selection")
                
        elif choice == '4':
            categories = manager.get_categories()
            if not categories:
                print("No categories found")
                continue
                
            print("\nAvailable Categories:")
            for i, category in enumerate(categories, 1):
                print(f"{i}. {category}")
            
            try:
                cat_choice = int(input(f"Select category (1-{len(categories)}): "))
                category = categories[cat_choice - 1]
                tasks = manager.get_tasks_by_category(category)
                display_tasks(tasks, f"{category} Tasks")
            except (ValueError, IndexError):
                print("Invalid category selection")
                
        elif choice == '5':
            print("\nPriority Levels:")
            print("1. Low 🔵")
            print("2. Medium 🟡")
            print("3. High 🟠")
            print("4. Urgent 🔴")
            
            try:
                priority_choice = int(input("Select priority (1-4): "))
                priority = Priority(priority_choice)
                tasks = manager.get_tasks_by_priority(priority)
                display_tasks(tasks, f"{priority.name.title()} Priority Tasks")
            except ValueError:
                print("Invalid priority selection")
                
        elif choice == '6':
            query = input("Enter search query: ").strip()
            if query:
                tasks = manager.search_tasks(query)
                display_tasks(tasks, f"Search Results for '{query}'")
                
        elif choice == '7':
            task_id = input("Enter task ID to update: ").strip()
            task = manager.get_task_by_id(task_id)
            if not task:
                print("Task not found!")
                continue
                
            print(f"\nUpdating task: {task.title}")
            print("Leave blank to keep current value")
            
            new_title = input(f"Title ({task.title}): ").strip()
            if new_title:
                task.title = new_title
                
            new_desc = input(f"Description ({task.description}): ").strip()
            if new_desc:
                task.description = new_desc
                
            new_category = input(f"Category ({task.category}): ").strip()
            if new_category:
                task.category = new_category
                
            manager.save_tasks()
            print("✅ Task updated successfully!")
            
        elif choice == '8':
            task_id = input("Enter task ID to delete: ").strip()
            task = manager.get_task_by_id(task_id)
            if not task:
                print("Task not found!")
                continue
                
            confirm = input(f"Delete task '{task.title}'? (y/n): ").lower()
            if confirm == 'y':
                manager.delete_task(task_id)
                print("✅ Task deleted successfully!")
                
        elif choice == '9':
            task_id = input("Enter task ID to mark as completed: ").strip()
            task = manager.get_task_by_id(task_id)
            if task:
                task.mark_completed()
                manager.save_tasks()
                print("✅ Task marked as completed!")
            else:
                print("Task not found!")
                
        elif choice == '10':
            task_id = input("Enter task ID to mark as in progress: ").strip()
            task = manager.get_task_by_id(task_id)
            if task:
                task.mark_in_progress()
                manager.save_tasks()
                print("✅ Task marked as in progress!")
            else:
                print("Task not found!")
                
        elif choice == '11':
            overdue_tasks = manager.get_overdue_tasks()
            display_tasks(overdue_tasks, "⚠️ Overdue Tasks")
            
        elif choice == '12':
            try:
                days = int(input("Show tasks due within how many days? (default: 7): ") or "7")
                upcoming_tasks = manager.get_upcoming_tasks(days)
                display_tasks(upcoming_tasks, f"📅 Upcoming Tasks (Next {days} Days)")
            except ValueError:
                print("Invalid number of days")
                
        elif choice == '13':
            stats = manager.get_task_statistics()
            print("\n📊 Task Statistics")
            print("="*40)
            print(f"Total Tasks: {stats['total']}")
            if stats['total'] > 0:
                print(f"Completed: {stats['completed']}")
                print(f"Pending: {stats['pending']}")
                print(f"In Progress: {stats['in_progress']}")
                print(f"Cancelled: {stats['cancelled']}")
                print(f"Overdue: {stats['overdue']}")
                print(f"Completion Rate: {stats['completion_rate']}%")
                
                print("\nPriority Breakdown:")
                for priority, count in stats['priority_breakdown'].items():
                    print(f"  {priority}: {count}")
                
                print("\nCategory Breakdown:")
                for category, count in stats['category_breakdown'].items():
                    print(f"  {category}: {count}")
                    
        elif choice == '14':
            print("\n📖 Task Manager Help")
            print("="*50)
            print("• Add tasks with titles, descriptions, categories, priorities, and deadlines")
            print("• View tasks filtered by status, category, or priority")
            print("• Search tasks by keywords in title or description")
            print("• Update task details and mark progress")
            print("• Track overdue and upcoming tasks")
            print("• View comprehensive statistics")
            print("\nDate Formats:")
            print("• YYYY-MM-DD (2024-12-25)")
            print("• MM/DD/YYYY (12/25/2024)")
            print("• 'today', 'tomorrow'")
            print("• '7d' (7 days from now)")
            print("• '2w' (2 weeks from now)")
            print("\nTask Priorities:")
            print("• 🔵 Low - Nice to have")
            print("• 🟡 Medium - Normal priority")
            print("• 🟠 High - Important")
            print("• 🔴 Urgent - Critical")
            
        elif choice == '15':
            print("\nThank you for using Task Manager!")
            print("Stay productive! ✨")
            break
            
        else:
            print("Invalid choice. Please select 1-15.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()