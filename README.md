# discord-bot
A discord-bot with some useful-ish features, most methods are kinda okayish commented but theres no actual docs;
Running the bot requires a DB that isnt currently tracked by the git repo, hmu if u actually want to run it and need a db scheme lol, additionally theres
- a file "PREFIX.txt" that contains ONE symbol used as the bots command prefix
- a file ".token.txt" with the discord token
- a file ".imgflip_creds.txt" containing credentials to imgflip in order to use the api for meme generation [format: username;password]

[![Tests](https://github.com/Nighmared/discord-bot/actions/workflows/tests.yml/badge.svg)](https://github.com/Nighmared/discord-bot/actions/workflows/tests.yml)



#### Structure
```
├── src
│   ├── loops
│   │   ├── __init__.py
│   │   └── polyring.py
│   ├── bot.log
│   ├── botlogger.py
│   ├── bot.py
│   ├── client.py
│   ├── commandhandler.py
│   ├── dbhandler.py
│   ├── discordbot.db
│   ├── dotree.sh
│   ├── handler.py
│   ├── inspirobot.py
│   ├── issues.py
│   ├── joniii.pub
│   ├── loophandler.py
│   ├── meme.py
│   ├── msglist.py
│   ├── neko.py
│   ├── nhentai.py
│   ├── PREFIX.txt
│   ├── push.sh
│   ├── robohash.py
│   ├── runner.sh
│   ├── shorten.py
│   ├── stalk.py
│   ├── test_sanity_check.py
│   ├── tree.txt
│   ├── uptime.py
│   └── xkcd.py
├── LICENSE
└── README.md

2 directories, 31 files
```
