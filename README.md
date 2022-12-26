
<!-- DO NOT EDIT THE README.md FILE IF YOU WANT TO CHANGE IT'S CONTENT, EDIT README_TEXT.md BECAUSE THE README IS FREQUENTLY REGENERATED-->

# discord-bot

A discord-bot with some useful-ish features, most methods are kinda okayish commented but theres no actual docs;
Running the bot requires a DB that isnt currently tracked by the git repo, hmu if u actually want to run it and need a db scheme lol, additionally theres

- a file "PREFIX.txt" that contains ONE symbol used as the bots command prefix
- a file ".token.txt" with the discord token
- a file ".imgflip_creds.txt" containing credentials to imgflip in order to use the api for meme generation [format: username;password]

[![Exec Tests](https://github.com/Nighmared/discord-bot/actions/workflows/tests.yml/badge.svg)](https://github.com/Nighmared/discord-bot/actions/workflows/tests.yml)
[![Code Style](https://github.com/Nighmared/discord-bot/actions/workflows/compliance.yml/badge.svg)](https://github.com/Nighmared/discord-bot/actions/workflows/compliance.yml)

#### Structure
 

 ``` 

../
├── bot
│   ├── botlogger
│   │   └── botlogger.py
│   ├── cmd
│   │   └── commandhandler.py
│   ├── handler
│   │   └── handler.py
│   ├── inspirobot
│   │   └── inspirobot.py
│   ├── issues
│   │   ├── issues_failing.png
│   │   ├── issues_passing.png
│   │   └── issues.py
│   ├── loops
│   │   ├── guesscleaner.py
│   │   ├── __init__.py
│   │   ├── loophandler.py
│   │   └── polyring.py
│   ├── meme
│   │   └── meme.py
│   ├── msglist
│   │   └── msglist.py
│   ├── neko
│   │   └── neko.py
│   ├── nhentai
│   │   ├── __init__.py
│   │   ├── nhentai.py
│   │   └── tags.blacklist
│   ├── robohash
│   │   └── robohash.py
│   ├── shorten
│   │   └── shorten.py
│   ├── sql
│   │   └── dbhandler.py
│   ├── stalk
│   │   └── stalk.py
│   ├── uptime
│   │   └── uptime.py
│   ├── util
│   │   ├── client2.py
│   │   └── client.py
│   ├── xkcd
│   │   └── xkcd.py
│   ├── bot.log
│   ├── bot.py
│   ├── discordbot.db
│   ├── dotree.sh
│   ├── __init__.py
│   ├── joniii.pub
│   ├── push.sh
│   ├── runner.sh
│   └── test_sanity_check.py
├── LICENSE
├── README.md
├── README_TEXT.md
└── requirements.txt

18 directories, 38 files
 ``` 

