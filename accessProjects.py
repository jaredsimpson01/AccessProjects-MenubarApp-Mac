import rumps
import os
import subprocess

class AccessProjects(rumps.App):
    def __init__(self, search_dirs, max_projects=3):
        """
        search_dirs: List of directories to search for projects
        max_projects: How many recent projects to show
        """
        super(AccessProjects, self).__init__(name="Access Projects App", title="Access")
        self.search_dirs = search_dirs
        self.max_projects = max_projects
        self.project_paths = {}  # Map project name -> full path
        self.create_menu()

    def create_menu(self):
        self.menu.clear()
        projects_and_times = []

        for directory in self.search_dirs:
            if not os.path.exists(directory):
                continue  # skip invalid paths
            for project in os.listdir(directory):
                project_path = os.path.join(directory, project)
                if os.path.isdir(project_path):
                    projects_and_times.append((os.path.getmtime(project_path), project, project_path))

        # Sort by most recently modified
        projects_and_times.sort(reverse=True)

        # Add top projects to the menu
        for mtime, project_name, project_path in projects_and_times[:self.max_projects]:
            self.project_paths[project_name] = project_path
            item = rumps.MenuItem(project_name, callback=self.open_project)
            self.menu.add(item)

        self.menu.add(rumps.separator)
        self.menu.add(rumps.MenuItem("Add Folder", callback=self.add_folder))

    def open_project(self, sender):
        project_name = sender.title
        project_path = self.project_paths.get(project_name)
        if project_path:
            subprocess.Popen(["code", project_path])  # MacOS "code" command to open in VS Code

    def add_folder(self, sender):
        response = rumps.Window("Enter full path of folder to add:", "Add New Folder").run()
        if response.clicked and response.text:
            new_folder = response.text.strip()
            if os.path.exists(new_folder) and os.path.isdir(new_folder):
                self.search_dirs.append(new_folder)
                self.create_menu()
            else:
                rumps.alert("Invalid folder path!")

if __name__ == '__main__':
    # Example usage
    search_directories = [
        "/Users/yourusername/PycharmProjects",
        "/Users/yourusername/Java_Projects"
    ]

    app = AccessProjects(search_dirs=search_directories)
    app.run()