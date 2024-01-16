
<!-- DO NOT EDIT THE README.md FILE IF YOU WANT TO CHANGE IT'S CONTENT, EDIT README_TEXT.md BECAUSE THE README IS FREQUENTLY REGENERATED-->

# discord-bot

A discord-bot with some useful-ish features, most methods are kinda okayish commented but theres no actual docs;
Running the bot requires a DB that isnt currently tracked by the git repo, hmu if u actually want to run it and need a db scheme lol, additionally theres

- a file "PREFIX.txt" that contains ONE symbol used as the bots command prefix
- a file ".token.txt" with the discord token
- a file ".imgflip_creds.txt" containing credentials to imgflip in order to use the api for meme generation [format: username;password]

# running it

```
pip install -e .
python botrun/bot.py
```


[![Exec Tests](https://github.com/Nighmared/discord-bot/actions/workflows/tests.yml/badge.svg)](https://github.com/Nighmared/discord-bot/actions/workflows/tests.yml)
[![Code Style](https://github.com/Nighmared/discord-bot/actions/workflows/compliance.yml/badge.svg)](https://github.com/Nighmared/discord-bot/actions/workflows/compliance.yml)
[![CodeQL](https://github.com/Nighmared/discord-bot/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/Nighmared/discord-bot/actions/workflows/github-code-scanning/codeql)

#### Structure
 

 ``` 

./
├── botpy
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
│   │   ├── loophandler.py
│   │   └── polyring.py
│   ├── meme
│   │   └── meme.py
│   ├── msglist
│   │   └── msglist.py
│   ├── neko
│   │   └── neko.py
│   ├── nhentai
│   │   ├── nhentai.py
│   │   └── tags.blacklist
│   ├── robohash
│   │   └── robohash.py
│   ├── shorten
│   │   └── shorten.py
│   ├── sql
│   │   ├── dbhandler.py
│   │   └── __init__.py
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
│   ├── __init__.py
│   ├── joniii.pub
│   ├── runner.sh
│   └── test_sanity_check.py
├── botpy.egg-info
│   ├── dependency_links.txt
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   └── top_level.txt
├── botrun
│   └── bot.py
├── build
│   ├── bdist.linux-x86_64
│   └── lib
│       └── botpy
│           ├── __init__.py
│           └── test_sanity_check.py
├── data
│   └── discordbot.db
├── discord_bot.egg-info
│   ├── dependency_links.txt
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   └── top_level.txt
├── dist
│   ├── discord_bot-1.0-py3.11.egg
│   └── discord_bot-1.0-py3.9.egg
├── bot.log
├── discordbot.db
├── dotree.sh
├── LICENSE
├── push.sh
├── README.md
├── README_TEXT.md
├── requirements.txt
├── setup.py
└── update-readme.sh

28 directories, 53 files
 ``` 

