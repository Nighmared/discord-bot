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
