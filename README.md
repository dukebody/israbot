# Israbot

Bot to send a reminder message about open PRs in a certain public repo.

## Usage

- Follow [the Slack instructions to create an incoming webhook](https://api.slack.com/incoming-webhooks) for the channel where you want the notifications to show up.
- Clone this repo to the host you want to use to send the notifications from.
- Install the requirements (better in a virtualenv) with:
```
pip install -r requirements.txt
```

- Create a script next to `israbot.py` with the contents:
```
import israbot

message = israbot.message_open_pull_requests('GH_ORGANIZATION', 'GH_REPO')
webhook_url = "https://hooks.slack.com/services/WEBHOOK_URL_FROM_FIRST_STEP"
israbot.post_to_slack(message, webhook_url)
```

That's it. Configure a cronjob or similar to run the script with the desired frequency and enjoy!
