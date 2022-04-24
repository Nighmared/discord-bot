
<!-- DO NOT EDIT THE README.md FILE IF YOU WANT TO CHANGE IT'S CONTENT, EDIT README_TEXT.md BECAUSE THE README IS FREQUENTLY REGENERATED-->

# discord-bot
A discord-bot with some useful-ish features, most methods are kinda okayish commented but theres no actual docs;
Running the bot requires a DB that isnt currently tracked by the git repo, hmu if u actually want to run it and need a db scheme lol, additionally theres
- a file "PREFIX.txt" that contains ONE symbol used as the bots command prefix
- a file ".token.txt" with the discord token
- a file ".imgflip_creds.txt" containing credentials to imgflip in order to use the api for meme generation [format: username;password]

[![Tests](https://github.com/Nighmared/discord-bot/actions/workflows/tests.yml/badge.svg)](https://github.com/Nighmared/discord-bot/actions/workflows/tests.yml)



#### Structure

 

 ``` 

../
├── src
│   ├── loops
│   │   ├── guesscleaner.py
│   │   ├── __init__.py
│   │   └── polyring.py
│   ├── nhentai
│   │   ├── __init__.py
│   │   ├── nhentai.py
│   │   └── tags.blacklist
│   ├── bot.log
│   ├── botlogger.py
│   ├── bot.py
│   ├── client2.py
│   ├── client_debug.log
│   ├── clientdebug.log
│   ├── client_log.log
│   ├── client.py
│   ├── commandhandler.py
│   ├── curses_metrics.log
│   ├── dbhandler.py
│   ├── discordbot.db
│   ├── dotree.sh
│   ├── handler.py
│   ├── inspirobot.py
│   ├── issues_failing.png
│   ├── issues_passing.png
│   ├── issues.py
│   ├── joniii.pub
│   ├── keys.log
│   ├── loophandler.py
│   ├── meme.py
│   ├── msglist.py
│   ├── neko.py
│   ├── PREFIX.txt
│   ├── push.sh
│   ├── robohash.py
│   ├── runner.sh
│   ├── shorten.py
│   ├── stalk.py
│   ├── test_sanity_check.py
│   ├── uptime.py
│   └── xkcd.py
├── LICENSE
├── README.md
├── README_TEXT.md
└── requirements.txt

3 directories, 43 files
 ``` 

