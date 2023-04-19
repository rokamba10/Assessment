import os
from datetime import datetime, timedelta

import pytz as pytz
import requests


def get_pull_requests():
    # Authenticate with GitHub API using an access token
    os.environ['GITHUB_ACCESS_TOKEN'] = "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"
    access_token = os.environ['GITHUB_ACCESS_TOKEN']
    owner, repo = "homebrew", "brew"
    manager = {"name": "John Doe", "email": "johndoe@company.xyz"}
    sender = {"name": "Rostin Okamba", "email": "rostinokamba@welcome.com", "role": "DevOps Engineer"}
    open_issues = f"https://api.github.com/repos/{owner}/{repo}/pulls"
    response = requests.get(open_issues.format(owner=owner, repo=repo),
                            headers={'Authorization': f'Token {access_token}'})
    opened_prs, closed_prs, in_progress_prs = [], [], []

    if response.status_code == 200:
        data = response.json()
        now = datetime.now(pytz.utc)
        last_week = now - timedelta(days=7)
        for pull_request in data:
            created_at = datetime.fromisoformat(pull_request['created_at'].replace('Z', '+00:00'))
            created_at = created_at.replace(tzinfo=pytz.utc)
            if created_at > last_week:
                # check for the pull request state
                if pull_request["state"] == "open":
                    opened_prs.append(pull_request)
                elif pull_request["state"] == "closed":
                    closed_prs.append(pull_request)
                elif pull_request["state"] and created_at > last_week:
                    in_progress_prs.append(pull_request)
    else:
        # Our API call to Github was not successful
        print(f'Error: {response.status_code}')
        exit()

    pr_summary(opened_prs, closed_prs, in_progress_prs, repo, manager, sender)


def pr_summary(opened, closed, in_progress, repository, receiver, sender):
    # format the output as an email-looking summary
    date_range = f'{datetime.now().date() - timedelta(days=7)} to {datetime.now().date()}'
    output = f'''
    From: {sender["email"]}
    To: {receiver["email"]}
    Subject: Summary of OPEN, CLOSED and IN PROGRESS Pull Requests from {date_range}
    
    Hello {receiver["name"]},

        Here is a summary of pull requests for the {repository} repository from {date_range}:

        Open Pull Requests:
        -------------------'''
    if len(opened) < 1:
        output += f'\n\t\tNo OPEN pull requests in the last week'
    else:
        for pr in opened:
            output += f'\n\t\t#{pr["number"]} - {pr["title"]}'

    output += f'''

        Closed Pull Requests:
        ---------------------'''
    if len(closed) < 1:
        output += f'\n\t\tNo CLOSED pull requests in the last week'
    else:
        for pr in closed:
            output += f'\n\t\t#{pr["number"]} - {pr["title"]} ({pr["state"]})'

    output += f'''

        In-Progress Pull Requests (last week):
        ---------------------------------------'''
    if len(in_progress) < 1:
        output += f'\n\t\tNo IN PROGRESS pull requests in the last week'
    else:
        for pr in in_progress:
            output += f'\n\t\t#{pr["number"]} - {pr["title"]} ({pr["state"]})'

    output += f'''\n\n\n
    Thanks
    {sender["name"]}
    {sender["role"]}
        '''

    return print(output)


get_pull_requests()
