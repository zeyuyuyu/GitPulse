import os
import git
import datetime
import json

class GitPulseCollaborator:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.commits = []

class GitPulseProject:
    def __init__(self, repo_path):
        self.repo_path = repo_path
        self.repo = git.Repo(repo_path)
        self.collaborators = {}

    def add_collaborator(self, name, email):
        collaborator = GitPulseCollaborator(name, email)
        self.collaborators[email] = collaborator

    def commit_change(self, file_path, message, author):
        commit = self.repo.index.commit(message, author=git.Actor(author.name, author.email))
        author.commits.append(commit)

    def get_commit_history(self):
        commit_history = []
        for commit in self.repo.iter_commits():
            author = self.collaborators.get(commit.author.email, None)
            if author:
                commit_history.append({
                    'hash': commit.hexsha,
                    'message': commit.message,
                    'author': author.name,
                    'date': commit.committed_datetime.isoformat()
                })
        return commit_history

    def save_state(self):
        state = {
            'collaborators': [{
                'name': collaborator.name,
                'email': collaborator.email,
                'commits': [commit.hexsha for commit in collaborator.commits]
            } for collaborator in self.collaborators.values()]
        }
        with open(os.path.join(self.repo_path, '.gitpulse'), 'w') as f:
            json.dump(state, f)

    def load_state(self):
        state_file = os.path.join(self.repo_path, '.gitpulse')
        if os.path.exists(state_file):
            with open(state_file, 'r') as f:
                state = json.load(f)
                for collaborator_data in state['collaborators']:
                    collaborator = GitPulseCollaborator(collaborator_data['name'], collaborator_data['email'])
                    self.collaborators[collaborator_data['email']] = collaborator
                    for commit_hash in collaborator_data['commits']:
                        commit = self.repo.commit(commit_hash)
                        collaborator.commits.append(commit)

if __name__ == '__main__':
    project = GitPulseProject('/path/to/repo')
    project.add_collaborator('John Doe', 'john@example.com')
    project.add_collaborator('Jane Smith', 'jane@example.com')
    project.commit_change('src/main.py', 'feat: Added real-time collaboration', project.collaborators['john@example.com'])
    project.commit_change('README.md', 'docs: Updated readme', project.collaborators['jane@example.com'])
    print(project.get_commit_history())
    project.save_state()
