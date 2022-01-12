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

[![Buy Me a Coffee](https://img.buymeacoffee.com/api/?url=aHR0cHM6Ly9pbWcuYnV5bWVhY29mZmVlLmNvbS9hcGkvP3VybD1hSFIwY0hNNkx5OWpaRzR1WW5WNWJXVmhZMjltWm1WbExtTnZiUzkxY0d4dllXUnpMM0J5YjJacGJHVmZjR2xqZEhWeVpYTXZNakF5TVM4d015ODBZekkwT0RnNE1XWmxOVE5pWmprM1lUa3pOV1kxWm1NNFlqRXpPV1EyTWk1d2JtYz0mc2l6ZT0zMDAmbmFtZT1raWtpbWFuamFybw==&creator=kikimanjaro&is_creating=creating%20mobile%20apps%20and%20plugins&design_code=1&design_color=%23ff813f&slug=kikimanjaro)](https://www.buymeacoffee.com/kikimanjaro)
