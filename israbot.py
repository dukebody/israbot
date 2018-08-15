import datetime
from datetime import datetime as dt

import requests
import github3 as gh

utc_tz = datetime.timezone.utc


def message_open_pull_requests(repo_organization, repo_name, token=None):
    pull_requests = get_open_pull_requests(repo_organization, repo_name, token)
    return '\n'.join(pull_request_message(pr) for pr in pull_requests)


def get_open_pull_requests(repo_organization, repo_name, token=None):

    repository = gh.repository(repo_organization, repo_name)
    return repository.pull_requests(
        state='open', sort='created', direction='asc')


def pull_request_message(pull_request):
    return """
- "{title}" was created {days_ago} days ago by @{user}.
  {url}""".format(
        title=pull_request.title,
        days_ago=(dt.now(tz=utc_tz) - pull_request.created_at).days,
        user=pull_request.user.login,
        url=pull_request.html_url
    )


def post_to_slack(text, webhook_url):
    json = {
        "text": text
    }
    requests.post(webhook_url, json=json)
