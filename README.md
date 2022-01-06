# DexSlack
A simple and nice way to display Dexcom G4/G5/G6 informations on Slack status

![Exemple](https://i.imgur.com/p57N9CZ.png)

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

## Contributing
Contributions are not needed for this project. Feel free to contribute if you want.
