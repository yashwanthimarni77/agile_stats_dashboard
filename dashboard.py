from flask import Flask, jsonify
from flask_restful import Api, Resource
import stat_dashboard  # Import the entire module

# Initialize Flask app
app = Flask(__name__)
api = Api(app)

class ProjectStatsAPI(Resource):
    def get(self):
        """Retrieve both project statistics and detailed project information"""
        projects = stat_dashboard.projects  # Access projects from imported module

        total_projects = len(projects)
        ongoing_projects = sum(1 for p in projects if p["status"] == "Active")
        completed_projects = sum(1 for p in projects if p["status"] == "Completed")
        pending_tasks = sum(p["pending_tasks"] for p in projects if "pending_tasks" in p)

        sprint_velocity = sum(p["tasks_completed"] for p in projects if "tasks_completed" in p) // total_projects if total_projects else 0
        total_issues = sum(p["total_issues"] for p in projects if "total_issues" in p)
        resolved_issues = sum(p["resolved_issues"] for p in projects if "resolved_issues" in p)
        issue_resolution_percentage = (resolved_issues / total_issues) * 100 if total_issues > 0 else 0

        # Retrieve detailed project list
        project_details = [
            {
                "name": p["name"],
                "manager": p["manager"],
                "team": p["team"],
                "status": p["status"],
                "progress": p["progress"],
                "pending_tasks": p["pending_tasks"],
                "tasks_completed": p["tasks_completed"],
                "total_issues": p["total_issues"],
                "resolved_issues": p["resolved_issues"]
            }
            for p in projects
        ]

        return jsonify({
            "overview": {
                "total_projects": total_projects,
                "ongoing_projects": ongoing_projects,
                "completed_projects": completed_projects,
                "pending_tasks": pending_tasks,
                "sprint_velocity": sprint_velocity,
                "issue_resolution_percentage": round(issue_resolution_percentage, 2)
            },
            "projects": project_details  # Includes full project details
        })
    
class TeamPerformanceAPI(Resource):
    def get(self):
        """Retrieve team performance metrics"""
        return jsonify(stat_dashboard.team_performance)

class ProgressTrackingAPI(Resource):
    def get(self):
        """Retrieve progress tracking details"""
        return jsonify(stat_dashboard.progress_data)


# ---- API ROUTES ----
api.add_resource(ProjectStatsAPI, '/api/projects/stats')
api.add_resource(TeamPerformanceAPI, '/api/projects/team-performance')
api.add_resource(ProgressTrackingAPI, '/api/projects/progress')

# ---- RUN APP ----
if __name__ == '__main__':
    app.run(debug=True)