import random

projects = []

with open("PythonProjects.txt") as projectFile:
    projects = projectFile.read().split("\n")

project = random.choice(projects)
projectTitle = project.split(" - ")[0]
projectDescription = project.split(" - ")[1]

print("Your suggested project is: " + projectTitle)
print()
print(projectDescription)
