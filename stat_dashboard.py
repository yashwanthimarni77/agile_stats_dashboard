from datetime import datetime

# Simulated project data
# Sample project data stored separately
projects = [
    {
        "name": "Agile Dashboard",
        "manager": "Alice",
        "team": "Development",
        "status": "Active",
        "progress": 40,
        "pending_tasks": 5,
        "tasks_completed": 30,
        "total_issues": 10,
        "resolved_issues": 9
    },
    {
        "name": "E-Commerce App",
        "manager": "Bob",
        "team": "Design",
        "status": "On Hold",
        "progress": 25,
        "pending_tasks": 10,
        "tasks_completed": 25,
        "total_issues": 15,
        "resolved_issues": 14
    },
    {
        "name": "Healthcare System",
        "manager": "Charlie",
        "team": "Backend",
        "status": "Completed",
        "progress": 100,
        "pending_tasks": 0,
        "tasks_completed": 50,
        "total_issues": 20,
        "resolved_issues": 20
    }
]

# Simulated team performance data
team_performance = [
    {"name": "Yashwanthi", "tasks_completed": 30, "efficiency": "90%"},
    {"name": "Aditya", "tasks_completed": 25, "efficiency": "85%"},
    {"name": "Harish", "tasks_completed": 20, "efficiency": "80%"}
]

# Simulated progress tracking data
progress_data = {
    "completion_percentage": 70,
    "current_sprint": "Sprint 1",
    "deadline": "2025-03-15"
}