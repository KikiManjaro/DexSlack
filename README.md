# DexSlack
A simple a nice way to display Dexcom G4/G5/G6 informations on Slack status 

![Exemple](https://imgur.com/a/3RN1gi2)

## Setup
You will need to install :

- [pydexom](https://github.com/gagebenne/pydexcom) by gagebenne
- [slack_sdk](https://github.com/slackapi/python-slack-sdk) by slackapi

## Usage
- Replace `username` and `password` with your Dexcom credentials
- Replace `slack_token` with your Slack token

Run the script `DexSlack.py` with [python3](https://www.python.org/) and [cron](https://en.wikipedia.org/wiki/Cron)

```
15     *     *     *     *         /usr/bin/python DexSlack.py.py
```