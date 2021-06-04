
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
│   │   ├── __pycache__
│   │   │   ├── guesscleaner.cpython-38.pyc
│   │   │   ├── __init__.cpython-38.pyc
│   │   │   └── polyring.cpython-38.pyc
│   │   ├── guesscleaner.py
│   │   ├── __init__.py
│   │   └── polyring.py
│   ├── nhentai
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-38.pyc
│   │   │   └── nhentai.cpython-38.pyc
│   │   ├── __init__.py
│   │   ├── nhentai.py
│   │   └── tags.blacklist
│   ├── __pycache__
│   │   ├── bot.cpython-38.pyc
│   │   ├── botlogger.cpython-38.pyc
│   │   ├── commandhandler.cpython-38.pyc
│   │   ├── dbhandler.cpython-38.pyc
│   │   ├── handler.cpython-38.pyc
│   │   ├── inspirobot.cpython-38.pyc
│   │   ├── issuefetcher.cpython-38.pyc
│   │   ├── issues.cpython-38.pyc
│   │   ├── logger.cpython-38.pyc
│   │   ├── loophandler.cpython-38.pyc
│   │   ├── loops.cpython-38.pyc
│   │   ├── meme.cpython-38.pyc
│   │   ├── msghandler.cpython-38.pyc
│   │   ├── msglist.cpython-38.pyc
│   │   ├── neko.cpython-38.pyc
│   │   ├── nhentai.cpython-38.pyc
│   │   ├── pubkey.cpython-38.pyc
│   │   ├── robohash.cpython-38.pyc
│   │   ├── shorten.cpython-38.pyc
│   │   ├── stalk.cpython-38.pyc
│   │   ├── test_print.cpython-38-pytest-6.1.2.pyc
│   │   ├── test_sanity_check.cpython-38-pytest-6.1.2.pyc
│   │   ├── uptime.cpython-38.pyc
│   │   └── xkcd.cpython-38.pyc
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
│   ├── spam.log
│   ├── stalk.py
│   ├── test_sanity_check.py
│   ├── uptime.py
│   └── xkcd.py
├── venv
│   ├── bin
│   │   ├── activate
│   │   ├── activate.csh
│   │   ├── activate.fish
│   │   ├── Activate.ps1
│   │   ├── chardetect
│   │   ├── f2py
│   │   ├── f2py3
│   │   ├── f2py3.8
│   │   ├── imageio_download_bin
│   │   ├── imageio_remove_bin
│   │   ├── lsm2bin
│   │   ├── pip
│   │   ├── pip3
│   │   ├── pip3.8
│   │   ├── py.test
│   │   ├── pytest
│   │   ├── python -> python3.8
│   │   ├── python3 -> python3.8
│   │   ├── python3.8 -> /usr/bin/python3.8
│   │   ├── skivi
│   │   ├── tiff2fsspec
│   │   ├── tiffcomment
│   │   └── tifffile
│   ├── include
│   ├── lib
│   │   └── python3.8
│   │       └── site-packages
│   │           ├── aiohttp
│   │           │   ├── __pycache__
│   │           │   │   ├── abc.cpython-38.pyc
│   │           │   │   ├── base_protocol.cpython-38.pyc
│   │           │   │   ├── client.cpython-38.pyc
│   │           │   │   ├── client_exceptions.cpython-38.pyc
│   │           │   │   ├── client_proto.cpython-38.pyc
│   │           │   │   ├── client_reqrep.cpython-38.pyc
│   │           │   │   ├── client_ws.cpython-38.pyc
│   │           │   │   ├── connector.cpython-38.pyc
│   │           │   │   ├── cookiejar.cpython-38.pyc
│   │           │   │   ├── formdata.cpython-38.pyc
│   │           │   │   ├── frozenlist.cpython-38.pyc
│   │           │   │   ├── hdrs.cpython-38.pyc
│   │           │   │   ├── helpers.cpython-38.pyc
│   │           │   │   ├── http.cpython-38.pyc
│   │           │   │   ├── http_exceptions.cpython-38.pyc
│   │           │   │   ├── http_parser.cpython-38.pyc
│   │           │   │   ├── http_websocket.cpython-38.pyc
│   │           │   │   ├── http_writer.cpython-38.pyc
│   │           │   │   ├── __init__.cpython-38.pyc
│   │           │   │   ├── locks.cpython-38.pyc
│   │           │   │   ├── log.cpython-38.pyc
│   │           │   │   ├── multipart.cpython-38.pyc
│   │           │   │   ├── payload.cpython-38.pyc
│   │           │   │   ├── payload_streamer.cpython-38.pyc
│   │           │   │   ├── pytest_plugin.cpython-38.pyc
│   │           │   │   ├── resolver.cpython-38.pyc
│   │           │   │   ├── signals.cpython-38.pyc
│   │           │   │   ├── streams.cpython-38.pyc
│   │           │   │   ├── tcp_helpers.cpython-38.pyc
│   │           │   │   ├── test_utils.cpython-38.pyc
│   │           │   │   ├── tracing.cpython-38.pyc
│   │           │   │   ├── typedefs.cpython-38.pyc
│   │           │   │   ├── web_app.cpython-38.pyc
│   │           │   │   ├── web.cpython-38.pyc
│   │           │   │   ├── web_exceptions.cpython-38.pyc
│   │           │   │   ├── web_fileresponse.cpython-38.pyc
│   │           │   │   ├── web_log.cpython-38.pyc
│   │           │   │   ├── web_middlewares.cpython-38.pyc
│   │           │   │   ├── web_protocol.cpython-38.pyc
│   │           │   │   ├── web_request.cpython-38.pyc
│   │           │   │   ├── web_response.cpython-38.pyc
│   │           │   │   ├── web_routedef.cpython-38.pyc
│   │           │   │   ├── web_runner.cpython-38.pyc
│   │           │   │   ├── web_server.cpython-38.pyc
│   │           │   │   ├── web_urldispatcher.cpython-38.pyc
│   │           │   │   ├── web_ws.cpython-38.pyc
│   │           │   │   └── worker.cpython-38.pyc
│   │           │   ├── abc.py
│   │           │   ├── base_protocol.py
│   │           │   ├── client_exceptions.py
│   │           │   ├── client_proto.py
│   │           │   ├── client.py
│   │           │   ├── client_reqrep.py
│   │           │   ├── client_ws.py
│   │           │   ├── connector.py
│   │           │   ├── cookiejar.py
│   │           │   ├── _cparser.pxd
│   │           │   ├── _find_header.c
│   │           │   ├── _find_header.h
│   │           │   ├── _find_header.pxd
│   │           │   ├── formdata.py
│   │           │   ├── _frozenlist.c
│   │           │   ├── _frozenlist.cpython-38-x86_64-linux-gnu.so
│   │           │   ├── frozenlist.py
│   │           │   ├── frozenlist.pyi
│   │           │   ├── _frozenlist.pyx
│   │           │   ├── hdrs.py
│   │           │   ├── _headers.pxi
│   │           │   ├── _helpers.c
│   │           │   ├── _helpers.cpython-38-x86_64-linux-gnu.so
│   │           │   ├── helpers.py
│   │           │   ├── _helpers.pyi
│   │           │   ├── _helpers.pyx
│   │           │   ├── http_exceptions.py
│   │           │   ├── _http_parser.c
│   │           │   ├── _http_parser.cpython-38-x86_64-linux-gnu.so
│   │           │   ├── http_parser.py
│   │           │   ├── _http_parser.pyx
│   │           │   ├── http.py
│   │           │   ├── http_websocket.py
│   │           │   ├── _http_writer.c
│   │           │   ├── _http_writer.cpython-38-x86_64-linux-gnu.so
│   │           │   ├── http_writer.py
│   │           │   ├── _http_writer.pyx
│   │           │   ├── __init__.py
│   │           │   ├── locks.py
│   │           │   ├── log.py
│   │           │   ├── multipart.py
│   │           │   ├── payload.py
│   │           │   ├── payload_streamer.py
│   │           │   ├── pytest_plugin.py
│   │           │   ├── py.typed
│   │           │   ├── resolver.py
│   │           │   ├── signals.py
│   │           │   ├── signals.pyi
│   │           │   ├── streams.py
│   │           │   ├── tcp_helpers.py
│   │           │   ├── test_utils.py
│   │           │   ├── tracing.py
│   │           │   ├── typedefs.py
│   │           │   ├── web_app.py
│   │           │   ├── web_exceptions.py
│   │           │   ├── web_fileresponse.py
│   │           │   ├── web_log.py
│   │           │   ├── web_middlewares.py
│   │           │   ├── web_protocol.py
│   │           │   ├── web.py
│   │           │   ├── web_request.py
│   │           │   ├── web_response.py
│   │           │   ├── web_routedef.py
│   │           │   ├── web_runner.py
│   │           │   ├── web_server.py
│   │           │   ├── _websocket.c
│   │           │   ├── _websocket.cpython-38-x86_64-linux-gnu.so
│   │           │   ├── _websocket.pyx
│   │           │   ├── web_urldispatcher.py
│   │           │   ├── web_ws.py
│   │           │   └── worker.py
│   │           ├── aiohttp-3.7.4.post0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE.txt
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── async_timeout
│   │           │   ├── __pycache__
│   │           │   │   └── __init__.cpython-38.pyc
│   │           │   ├── __init__.py
│   │           │   └── py.typed
│   │           ├── async_timeout-3.0.1.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── attr
│   │           │   ├── __pycache__
│   │           │   │   ├── _cmp.cpython-38.pyc
│   │           │   │   ├── _compat.cpython-38.pyc
│   │           │   │   ├── _config.cpython-38.pyc
│   │           │   │   ├── converters.cpython-38.pyc
│   │           │   │   ├── exceptions.cpython-38.pyc
│   │           │   │   ├── filters.cpython-38.pyc
│   │           │   │   ├── _funcs.cpython-38.pyc
│   │           │   │   ├── __init__.cpython-38.pyc
│   │           │   │   ├── _make.cpython-38.pyc
│   │           │   │   ├── _next_gen.cpython-38.pyc
│   │           │   │   ├── setters.cpython-38.pyc
│   │           │   │   ├── validators.cpython-38.pyc
│   │           │   │   └── _version_info.cpython-38.pyc
│   │           │   ├── _cmp.py
│   │           │   ├── _cmp.pyi
│   │           │   ├── _compat.py
│   │           │   ├── _config.py
│   │           │   ├── converters.py
│   │           │   ├── converters.pyi
│   │           │   ├── exceptions.py
│   │           │   ├── exceptions.pyi
│   │           │   ├── filters.py
│   │           │   ├── filters.pyi
│   │           │   ├── _funcs.py
│   │           │   ├── __init__.py
│   │           │   ├── __init__.pyi
│   │           │   ├── _make.py
│   │           │   ├── _next_gen.py
│   │           │   ├── py.typed
│   │           │   ├── setters.py
│   │           │   ├── setters.pyi
│   │           │   ├── validators.py
│   │           │   ├── validators.pyi
│   │           │   ├── _version_info.py
│   │           │   └── _version_info.pyi
│   │           ├── attrs-21.2.0.dist-info
│   │           │   ├── AUTHORS.rst
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── beautifulsoup4-4.9.3.dist-info
│   │           │   ├── AUTHORS
│   │           │   ├── COPYING.txt
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── bs4
│   │           │   ├── builder
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── _html5lib.cpython-38.pyc
│   │           │   │   │   └── __init__.cpython-38.pyc
│   │           │   │   ├── _html5lib.py
│   │           │   │   ├── _htmlparser.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── _lxml.py
│   │           │   ├── __pycache__
│   │           │   │   └── __init__.cpython-38.pyc
│   │           │   ├── tests
│   │           │   │   ├── __init__.py
│   │           │   │   ├── test_builder_registry.py
│   │           │   │   ├── test_docs.py
│   │           │   │   ├── test_html5lib.py
│   │           │   │   ├── test_htmlparser.py
│   │           │   │   ├── test_lxml.py
│   │           │   │   ├── test_soup.py
│   │           │   │   └── test_tree.py
│   │           │   ├── dammit.py
│   │           │   ├── diagnose.py
│   │           │   ├── element.py
│   │           │   ├── formatter.py
│   │           │   ├── __init__.py
│   │           │   └── testing.py
│   │           ├── certifi
│   │           │   ├── __pycache__
│   │           │   │   ├── core.cpython-38.pyc
│   │           │   │   ├── __init__.cpython-38.pyc
│   │           │   │   └── __main__.cpython-38.pyc
│   │           │   ├── cacert.pem
│   │           │   ├── core.py
│   │           │   ├── __init__.py
│   │           │   └── __main__.py
│   │           ├── certifi-2021.5.30.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── chardet
│   │           │   ├── cli
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── chardetect.cpython-38.pyc
│   │           │   │   │   └── __init__.cpython-38.pyc
│   │           │   │   ├── chardetect.py
│   │           │   │   └── __init__.py
│   │           │   ├── metadata
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   └── languages.cpython-38.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   └── languages.py
│   │           │   ├── __pycache__
│   │           │   │   ├── big5freq.cpython-38.pyc
│   │           │   │   ├── big5prober.cpython-38.pyc
│   │           │   │   ├── chardistribution.cpython-38.pyc
│   │           │   │   ├── charsetgroupprober.cpython-38.pyc
│   │           │   │   ├── charsetprober.cpython-38.pyc
│   │           │   │   ├── codingstatemachine.cpython-38.pyc
│   │           │   │   ├── compat.cpython-38.pyc
│   │           │   │   ├── cp949prober.cpython-38.pyc
│   │           │   │   ├── enums.cpython-38.pyc
│   │           │   │   ├── escprober.cpython-38.pyc
│   │           │   │   ├── escsm.cpython-38.pyc
│   │           │   │   ├── eucjpprober.cpython-38.pyc
│   │           │   │   ├── euckrfreq.cpython-38.pyc
│   │           │   │   ├── euckrprober.cpython-38.pyc
│   │           │   │   ├── euctwfreq.cpython-38.pyc
│   │           │   │   ├── euctwprober.cpython-38.pyc
│   │           │   │   ├── gb2312freq.cpython-38.pyc
│   │           │   │   ├── gb2312prober.cpython-38.pyc
│   │           │   │   ├── hebrewprober.cpython-38.pyc
│   │           │   │   ├── __init__.cpython-38.pyc
│   │           │   │   ├── jisfreq.cpython-38.pyc
│   │           │   │   ├── jpcntx.cpython-38.pyc
│   │           │   │   ├── langbulgarianmodel.cpython-38.pyc
│   │           │   │   ├── langgreekmodel.cpython-38.pyc
│   │           │   │   ├── langhebrewmodel.cpython-38.pyc
│   │           │   │   ├── langhungarianmodel.cpython-38.pyc
│   │           │   │   ├── langrussianmodel.cpython-38.pyc
│   │           │   │   ├── langthaimodel.cpython-38.pyc
│   │           │   │   ├── langturkishmodel.cpython-38.pyc
│   │           │   │   ├── latin1prober.cpython-38.pyc
│   │           │   │   ├── mbcharsetprober.cpython-38.pyc
│   │           │   │   ├── mbcsgroupprober.cpython-38.pyc
│   │           │   │   ├── mbcssm.cpython-38.pyc
│   │           │   │   ├── sbcharsetprober.cpython-38.pyc
│   │           │   │   ├── sbcsgroupprober.cpython-38.pyc
│   │           │   │   ├── sjisprober.cpython-38.pyc
│   │           │   │   ├── universaldetector.cpython-38.pyc
│   │           │   │   ├── utf8prober.cpython-38.pyc
│   │           │   │   └── version.cpython-38.pyc
│   │           │   ├── big5freq.py
│   │           │   ├── big5prober.py
│   │           │   ├── chardistribution.py
│   │           │   ├── charsetgroupprober.py
│   │           │   ├── charsetprober.py
│   │           │   ├── codingstatemachine.py
│   │           │   ├── compat.py
│   │           │   ├── cp949prober.py
│   │           │   ├── enums.py
│   │           │   ├── escprober.py
│   │           │   ├── escsm.py
│   │           │   ├── eucjpprober.py
│   │           │   ├── euckrfreq.py
│   │           │   ├── euckrprober.py
│   │           │   ├── euctwfreq.py
│   │           │   ├── euctwprober.py
│   │           │   ├── gb2312freq.py
│   │           │   ├── gb2312prober.py
│   │           │   ├── hebrewprober.py
│   │           │   ├── __init__.py
│   │           │   ├── jisfreq.py
│   │           │   ├── jpcntx.py
│   │           │   ├── langbulgarianmodel.py
│   │           │   ├── langgreekmodel.py
│   │           │   ├── langhebrewmodel.py
│   │           │   ├── langhungarianmodel.py
│   │           │   ├── langrussianmodel.py
│   │           │   ├── langthaimodel.py
│   │           │   ├── langturkishmodel.py
│   │           │   ├── latin1prober.py
│   │           │   ├── mbcharsetprober.py
│   │           │   ├── mbcsgroupprober.py
│   │           │   ├── mbcssm.py
│   │           │   ├── sbcharsetprober.py
│   │           │   ├── sbcsgroupprober.py
│   │           │   ├── sjisprober.py
│   │           │   ├── universaldetector.py
│   │           │   ├── utf8prober.py
│   │           │   └── version.py
│   │           ├── chardet-4.0.0.dist-info
│   │           │   ├── entry_points.txt
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── cycler-0.10.0.dist-info
│   │           │   ├── DESCRIPTION.rst
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── metadata.json
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── dateutil
│   │           │   ├── parser
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── isoparser.cpython-38.pyc
│   │           │   │   │   └── _parser.cpython-38.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── isoparser.py
│   │           │   │   └── _parser.py
│   │           │   ├── __pycache__
│   │           │   │   ├── _common.cpython-38.pyc
│   │           │   │   ├── easter.cpython-38.pyc
│   │           │   │   ├── __init__.cpython-38.pyc
│   │           │   │   ├── relativedelta.cpython-38.pyc
│   │           │   │   ├── rrule.cpython-38.pyc
│   │           │   │   ├── tzwin.cpython-38.pyc
│   │           │   │   ├── utils.cpython-38.pyc
│   │           │   │   └── _version.cpython-38.pyc
│   │           │   ├── tz
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── _common.cpython-38.pyc
│   │           │   │   │   ├── _factories.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── tz.cpython-38.pyc
│   │           │   │   │   └── win.cpython-38.pyc
│   │           │   │   ├── _common.py
│   │           │   │   ├── _factories.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── tz.py
│   │           │   │   └── win.py
│   │           │   ├── zoneinfo
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   └── rebuild.cpython-38.pyc
│   │           │   │   ├── dateutil-zoneinfo.tar.gz
│   │           │   │   ├── __init__.py
│   │           │   │   └── rebuild.py
│   │           │   ├── _common.py
│   │           │   ├── easter.py
│   │           │   ├── __init__.py
│   │           │   ├── relativedelta.py
│   │           │   ├── rrule.py
│   │           │   ├── tzwin.py
│   │           │   ├── utils.py
│   │           │   └── _version.py
│   │           ├── decorator-4.4.2.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE.txt
│   │           │   ├── METADATA
│   │           │   ├── pbr.json
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── discord
│   │           │   ├── bin
│   │           │   │   ├── libopus-0.x64.dll
│   │           │   │   └── libopus-0.x86.dll
│   │           │   ├── ext
│   │           │   │   ├── commands
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── bot.cpython-38.pyc
│   │           │   │   │   │   ├── cog.cpython-38.pyc
│   │           │   │   │   │   ├── context.cpython-38.pyc
│   │           │   │   │   │   ├── converter.cpython-38.pyc
│   │           │   │   │   │   ├── cooldowns.cpython-38.pyc
│   │           │   │   │   │   ├── core.cpython-38.pyc
│   │           │   │   │   │   ├── errors.cpython-38.pyc
│   │           │   │   │   │   ├── help.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── _types.cpython-38.pyc
│   │           │   │   │   │   └── view.cpython-38.pyc
│   │           │   │   │   ├── bot.py
│   │           │   │   │   ├── cog.py
│   │           │   │   │   ├── context.py
│   │           │   │   │   ├── converter.py
│   │           │   │   │   ├── cooldowns.py
│   │           │   │   │   ├── core.py
│   │           │   │   │   ├── errors.py
│   │           │   │   │   ├── help.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _types.py
│   │           │   │   │   └── view.py
│   │           │   │   └── tasks
│   │           │   │       ├── __pycache__
│   │           │   │       │   └── __init__.cpython-38.pyc
│   │           │   │       └── __init__.py
│   │           │   ├── __pycache__
│   │           │   │   ├── abc.cpython-38.pyc
│   │           │   │   ├── activity.cpython-38.pyc
│   │           │   │   ├── appinfo.cpython-38.pyc
│   │           │   │   ├── asset.cpython-38.pyc
│   │           │   │   ├── audit_logs.cpython-38.pyc
│   │           │   │   ├── backoff.cpython-38.pyc
│   │           │   │   ├── calls.cpython-38.pyc
│   │           │   │   ├── channel.cpython-38.pyc
│   │           │   │   ├── client.cpython-38.pyc
│   │           │   │   ├── colour.cpython-38.pyc
│   │           │   │   ├── context_managers.cpython-38.pyc
│   │           │   │   ├── embeds.cpython-38.pyc
│   │           │   │   ├── emoji.cpython-38.pyc
│   │           │   │   ├── enums.cpython-38.pyc
│   │           │   │   ├── errors.cpython-38.pyc
│   │           │   │   ├── file.cpython-38.pyc
│   │           │   │   ├── flags.cpython-38.pyc
│   │           │   │   ├── gateway.cpython-38.pyc
│   │           │   │   ├── guild.cpython-38.pyc
│   │           │   │   ├── http.cpython-38.pyc
│   │           │   │   ├── __init__.cpython-38.pyc
│   │           │   │   ├── integrations.cpython-38.pyc
│   │           │   │   ├── invite.cpython-38.pyc
│   │           │   │   ├── iterators.cpython-38.pyc
│   │           │   │   ├── __main__.cpython-38.pyc
│   │           │   │   ├── member.cpython-38.pyc
│   │           │   │   ├── mentions.cpython-38.pyc
│   │           │   │   ├── message.cpython-38.pyc
│   │           │   │   ├── mixins.cpython-38.pyc
│   │           │   │   ├── object.cpython-38.pyc
│   │           │   │   ├── oggparse.cpython-38.pyc
│   │           │   │   ├── opus.cpython-38.pyc
│   │           │   │   ├── partial_emoji.cpython-38.pyc
│   │           │   │   ├── permissions.cpython-38.pyc
│   │           │   │   ├── player.cpython-38.pyc
│   │           │   │   ├── raw_models.cpython-38.pyc
│   │           │   │   ├── reaction.cpython-38.pyc
│   │           │   │   ├── relationship.cpython-38.pyc
│   │           │   │   ├── role.cpython-38.pyc
│   │           │   │   ├── shard.cpython-38.pyc
│   │           │   │   ├── state.cpython-38.pyc
│   │           │   │   ├── sticker.cpython-38.pyc
│   │           │   │   ├── team.cpython-38.pyc
│   │           │   │   ├── template.cpython-38.pyc
│   │           │   │   ├── user.cpython-38.pyc
│   │           │   │   ├── utils.cpython-38.pyc
│   │           │   │   ├── voice_client.cpython-38.pyc
│   │           │   │   ├── webhook.cpython-38.pyc
│   │           │   │   └── widget.cpython-38.pyc
│   │           │   ├── abc.py
│   │           │   ├── activity.py
│   │           │   ├── appinfo.py
│   │           │   ├── asset.py
│   │           │   ├── audit_logs.py
│   │           │   ├── backoff.py
│   │           │   ├── calls.py
│   │           │   ├── channel.py
│   │           │   ├── client.py
│   │           │   ├── colour.py
│   │           │   ├── context_managers.py
│   │           │   ├── embeds.py
│   │           │   ├── emoji.py
│   │           │   ├── enums.py
│   │           │   ├── errors.py
│   │           │   ├── file.py
│   │           │   ├── flags.py
│   │           │   ├── gateway.py
│   │           │   ├── guild.py
│   │           │   ├── http.py
│   │           │   ├── __init__.py
│   │           │   ├── integrations.py
│   │           │   ├── invite.py
│   │           │   ├── iterators.py
│   │           │   ├── __main__.py
│   │           │   ├── member.py
│   │           │   ├── mentions.py
│   │           │   ├── message.py
│   │           │   ├── mixins.py
│   │           │   ├── object.py
│   │           │   ├── oggparse.py
│   │           │   ├── opus.py
│   │           │   ├── partial_emoji.py
│   │           │   ├── permissions.py
│   │           │   ├── player.py
│   │           │   ├── raw_models.py
│   │           │   ├── reaction.py
│   │           │   ├── relationship.py
│   │           │   ├── role.py
│   │           │   ├── shard.py
│   │           │   ├── state.py
│   │           │   ├── sticker.py
│   │           │   ├── team.py
│   │           │   ├── template.py
│   │           │   ├── user.py
│   │           │   ├── utils.py
│   │           │   ├── voice_client.py
│   │           │   ├── webhook.py
│   │           │   └── widget.py
│   │           ├── discord_buttons
│   │           │   ├── __pycache__
│   │           │   │   ├── button.cpython-38.pyc
│   │           │   │   ├── client.cpython-38.pyc
│   │           │   │   ├── context.cpython-38.pyc
│   │           │   │   ├── __init__.cpython-38.pyc
│   │           │   │   ├── interaction.cpython-38.pyc
│   │           │   │   └── message.cpython-38.pyc
│   │           │   ├── button.py
│   │           │   ├── client.py
│   │           │   ├── context.py
│   │           │   ├── __init__.py
│   │           │   ├── interaction.py
│   │           │   └── message.py
│   │           ├── discord_buttons-0.3.5.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── REQUESTED
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── discord.py-1.7.1.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── REQUESTED
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── _distutils_hack
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-38.pyc
│   │           │   │   └── override.cpython-38.pyc
│   │           │   ├── __init__.py
│   │           │   └── override.py
│   │           ├── idna
│   │           │   ├── __pycache__
│   │           │   │   ├── codec.cpython-38.pyc
│   │           │   │   ├── compat.cpython-38.pyc
│   │           │   │   ├── core.cpython-38.pyc
│   │           │   │   ├── idnadata.cpython-38.pyc
│   │           │   │   ├── __init__.cpython-38.pyc
│   │           │   │   ├── intranges.cpython-38.pyc
│   │           │   │   ├── package_data.cpython-38.pyc
│   │           │   │   └── uts46data.cpython-38.pyc
│   │           │   ├── codec.py
│   │           │   ├── compat.py
│   │           │   ├── core.py
│   │           │   ├── idnadata.py
│   │           │   ├── __init__.py
│   │           │   ├── intranges.py
│   │           │   ├── package_data.py
│   │           │   └── uts46data.py
│   │           ├── idna-2.10.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE.rst
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── imageio
│   │           │   ├── core
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── fetching.cpython-38.pyc
│   │           │   │   │   ├── findlib.cpython-38.pyc
│   │           │   │   │   ├── format.cpython-38.pyc
│   │           │   │   │   ├── functions.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── request.cpython-38.pyc
│   │           │   │   │   └── util.cpython-38.pyc
│   │           │   │   ├── fetching.py
│   │           │   │   ├── findlib.py
│   │           │   │   ├── format.py
│   │           │   │   ├── functions.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── request.py
│   │           │   │   └── util.py
│   │           │   ├── plugins
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── _bsdf.cpython-38.pyc
│   │           │   │   │   ├── bsdf.cpython-38.pyc
│   │           │   │   │   ├── _dicom.cpython-38.pyc
│   │           │   │   │   ├── dicom.cpython-38.pyc
│   │           │   │   │   ├── example.cpython-38.pyc
│   │           │   │   │   ├── feisem.cpython-38.pyc
│   │           │   │   │   ├── ffmpeg.cpython-38.pyc
│   │           │   │   │   ├── fits.cpython-38.pyc
│   │           │   │   │   ├── _freeimage.cpython-38.pyc
│   │           │   │   │   ├── freeimage.cpython-38.pyc
│   │           │   │   │   ├── freeimagemulti.cpython-38.pyc
│   │           │   │   │   ├── gdal.cpython-38.pyc
│   │           │   │   │   ├── grab.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── lytro.cpython-38.pyc
│   │           │   │   │   ├── npz.cpython-38.pyc
│   │           │   │   │   ├── pillow.cpython-38.pyc
│   │           │   │   │   ├── pillow_info.cpython-38.pyc
│   │           │   │   │   ├── pillowmulti.cpython-38.pyc
│   │           │   │   │   ├── simpleitk.cpython-38.pyc
│   │           │   │   │   ├── spe.cpython-38.pyc
│   │           │   │   │   ├── _swf.cpython-38.pyc
│   │           │   │   │   ├── swf.cpython-38.pyc
│   │           │   │   │   ├── _tifffile.cpython-38.pyc
│   │           │   │   │   └── tifffile.cpython-38.pyc
│   │           │   │   ├── _bsdf.py
│   │           │   │   ├── bsdf.py
│   │           │   │   ├── _dicom.py
│   │           │   │   ├── dicom.py
│   │           │   │   ├── example.py
│   │           │   │   ├── feisem.py
│   │           │   │   ├── ffmpeg.py
│   │           │   │   ├── fits.py
│   │           │   │   ├── freeimagemulti.py
│   │           │   │   ├── _freeimage.py
│   │           │   │   ├── freeimage.py
│   │           │   │   ├── gdal.py
│   │           │   │   ├── grab.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── lytro.py
│   │           │   │   ├── npz.py
│   │           │   │   ├── pillow_info.py
│   │           │   │   ├── pillowmulti.py
│   │           │   │   ├── pillow.py
│   │           │   │   ├── simpleitk.py
│   │           │   │   ├── spe.py
│   │           │   │   ├── _swf.py
│   │           │   │   ├── swf.py
│   │           │   │   ├── _tifffile.py
│   │           │   │   └── tifffile.py
│   │           │   ├── __pycache__
│   │           │   │   ├── freeze.cpython-38.pyc
│   │           │   │   ├── __init__.cpython-38.pyc
│   │           │   │   ├── __main__.cpython-38.pyc
│   │           │   │   └── testing.cpython-38.pyc
│   │           │   ├── resources
│   │           │   │   ├── images
│   │           │   │   │   ├── astronaut.png
│   │           │   │   │   ├── chelsea.png
│   │           │   │   │   ├── chelsea.zip
│   │           │   │   │   ├── cockatoo.mp4
│   │           │   │   │   ├── newtonscradle.gif
│   │           │   │   │   ├── realshort.mp4
│   │           │   │   │   └── stent.npz
│   │           │   │   └── shipped_resources_go_here
│   │           │   ├── freeze.py
│   │           │   ├── __init__.py
│   │           │   ├── __main__.py
│   │           │   └── testing.py
│   │           ├── imageio-2.9.0.dist-info
│   │           │   ├── entry_points.txt
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── iniconfig
│   │           │   ├── __pycache__
│   │           │   │   └── __init__.cpython-38.pyc
│   │           │   ├── __init__.py
│   │           │   ├── __init__.pyi
│   │           │   └── py.typed
│   │           ├── iniconfig-1.1.1.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── kiwisolver-1.3.1.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── lxml
│   │           │   ├── html
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── builder.cpython-38.pyc
│   │           │   │   │   ├── clean.cpython-38.pyc
│   │           │   │   │   ├── defs.cpython-38.pyc
│   │           │   │   │   ├── _diffcommand.cpython-38.pyc
│   │           │   │   │   ├── diff.cpython-38.pyc
│   │           │   │   │   ├── ElementSoup.cpython-38.pyc
│   │           │   │   │   ├── formfill.cpython-38.pyc
│   │           │   │   │   ├── _html5builder.cpython-38.pyc
│   │           │   │   │   ├── html5parser.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── _setmixin.cpython-38.pyc
│   │           │   │   │   ├── soupparser.cpython-38.pyc
│   │           │   │   │   └── usedoctest.cpython-38.pyc
│   │           │   │   ├── builder.py
│   │           │   │   ├── clean.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── clean.py
│   │           │   │   ├── defs.py
│   │           │   │   ├── _diffcommand.py
│   │           │   │   ├── diff.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── diff.py
│   │           │   │   ├── ElementSoup.py
│   │           │   │   ├── formfill.py
│   │           │   │   ├── _html5builder.py
│   │           │   │   ├── html5parser.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _setmixin.py
│   │           │   │   ├── soupparser.py
│   │           │   │   └── usedoctest.py
│   │           │   ├── includes
│   │           │   │   ├── libexslt
│   │           │   │   │   ├── exsltconfig.h
│   │           │   │   │   ├── exsltexports.h
│   │           │   │   │   └── exslt.h
│   │           │   │   ├── libxml
│   │           │   │   │   ├── c14n.h
│   │           │   │   │   ├── catalog.h
│   │           │   │   │   ├── chvalid.h
│   │           │   │   │   ├── debugXML.h
│   │           │   │   │   ├── dict.h
│   │           │   │   │   ├── DOCBparser.h
│   │           │   │   │   ├── encoding.h
│   │           │   │   │   ├── entities.h
│   │           │   │   │   ├── globals.h
│   │           │   │   │   ├── hash.h
│   │           │   │   │   ├── HTMLparser.h
│   │           │   │   │   ├── HTMLtree.h
│   │           │   │   │   ├── list.h
│   │           │   │   │   ├── nanoftp.h
│   │           │   │   │   ├── nanohttp.h
│   │           │   │   │   ├── parser.h
│   │           │   │   │   ├── parserInternals.h
│   │           │   │   │   ├── relaxng.h
│   │           │   │   │   ├── SAX2.h
│   │           │   │   │   ├── SAX.h
│   │           │   │   │   ├── schemasInternals.h
│   │           │   │   │   ├── schematron.h
│   │           │   │   │   ├── threads.h
│   │           │   │   │   ├── tree.h
│   │           │   │   │   ├── uri.h
│   │           │   │   │   ├── valid.h
│   │           │   │   │   ├── xinclude.h
│   │           │   │   │   ├── xlink.h
│   │           │   │   │   ├── xmlautomata.h
│   │           │   │   │   ├── xmlerror.h
│   │           │   │   │   ├── xmlexports.h
│   │           │   │   │   ├── xmlIO.h
│   │           │   │   │   ├── xmlmemory.h
│   │           │   │   │   ├── xmlmodule.h
│   │           │   │   │   ├── xmlreader.h
│   │           │   │   │   ├── xmlregexp.h
│   │           │   │   │   ├── xmlsave.h
│   │           │   │   │   ├── xmlschemas.h
│   │           │   │   │   ├── xmlschemastypes.h
│   │           │   │   │   ├── xmlstring.h
│   │           │   │   │   ├── xmlunicode.h
│   │           │   │   │   ├── xmlversion.h
│   │           │   │   │   ├── xmlwriter.h
│   │           │   │   │   ├── xpath.h
│   │           │   │   │   ├── xpathInternals.h
│   │           │   │   │   └── xpointer.h
│   │           │   │   ├── libxslt
│   │           │   │   │   ├── attributes.h
│   │           │   │   │   ├── documents.h
│   │           │   │   │   ├── extensions.h
│   │           │   │   │   ├── extra.h
│   │           │   │   │   ├── functions.h
│   │           │   │   │   ├── imports.h
│   │           │   │   │   ├── keys.h
│   │           │   │   │   ├── namespaces.h
│   │           │   │   │   ├── numbersInternals.h
│   │           │   │   │   ├── pattern.h
│   │           │   │   │   ├── preproc.h
│   │           │   │   │   ├── security.h
│   │           │   │   │   ├── templates.h
│   │           │   │   │   ├── transform.h
│   │           │   │   │   ├── variables.h
│   │           │   │   │   ├── xsltconfig.h
│   │           │   │   │   ├── xsltexports.h
│   │           │   │   │   ├── xslt.h
│   │           │   │   │   ├── xsltInternals.h
│   │           │   │   │   ├── xsltlocale.h
│   │           │   │   │   └── xsltutils.h
│   │           │   │   ├── __pycache__
│   │           │   │   │   └── __init__.cpython-38.pyc
│   │           │   │   ├── c14n.pxd
│   │           │   │   ├── config.pxd
│   │           │   │   ├── dtdvalid.pxd
│   │           │   │   ├── etree_defs.h
│   │           │   │   ├── etreepublic.pxd
│   │           │   │   ├── htmlparser.pxd
│   │           │   │   ├── __init__.pxd
│   │           │   │   ├── __init__.py
│   │           │   │   ├── lxml-version.h
│   │           │   │   ├── relaxng.pxd
│   │           │   │   ├── schematron.pxd
│   │           │   │   ├── tree.pxd
│   │           │   │   ├── uri.pxd
│   │           │   │   ├── xinclude.pxd
│   │           │   │   ├── xmlerror.pxd
│   │           │   │   ├── xmlparser.pxd
│   │           │   │   ├── xmlschema.pxd
│   │           │   │   ├── xpath.pxd
│   │           │   │   └── xslt.pxd
│   │           │   ├── isoschematron
│   │           │   │   ├── __pycache__
│   │           │   │   │   └── __init__.cpython-38.pyc
│   │           │   │   ├── resources
│   │           │   │   │   ├── rng
│   │           │   │   │   │   └── iso-schematron.rng
│   │           │   │   │   └── xsl
│   │           │   │   │       ├── iso-schematron-xslt1
│   │           │   │   │       │   ├── iso_abstract_expand.xsl
│   │           │   │   │       │   ├── iso_dsdl_include.xsl
│   │           │   │   │       │   ├── iso_schematron_message.xsl
│   │           │   │   │       │   ├── iso_schematron_skeleton_for_xslt1.xsl
│   │           │   │   │       │   ├── iso_svrl_for_xslt1.xsl
│   │           │   │   │       │   └── readme.txt
│   │           │   │   │       ├── RNG2Schtrn.xsl
│   │           │   │   │       └── XSD2Schtrn.xsl
│   │           │   │   └── __init__.py
│   │           │   ├── __pycache__
│   │           │   │   ├── builder.cpython-38.pyc
│   │           │   │   ├── cssselect.cpython-38.pyc
│   │           │   │   ├── doctestcompare.cpython-38.pyc
│   │           │   │   ├── ElementInclude.cpython-38.pyc
│   │           │   │   ├── _elementpath.cpython-38.pyc
│   │           │   │   ├── __init__.cpython-38.pyc
│   │           │   │   ├── pyclasslookup.cpython-38.pyc
│   │           │   │   ├── sax.cpython-38.pyc
│   │           │   │   └── usedoctest.cpython-38.pyc
│   │           │   ├── builder.cpython-38-x86_64-linux-gnu.so
│   │           │   ├── builder.py
│   │           │   ├── cssselect.py
│   │           │   ├── doctestcompare.py
│   │           │   ├── ElementInclude.py
│   │           │   ├── _elementpath.cpython-38-x86_64-linux-gnu.so
│   │           │   ├── _elementpath.py
│   │           │   ├── etree_api.h
│   │           │   ├── etree.cpython-38-x86_64-linux-gnu.so
│   │           │   ├── etree.h
│   │           │   ├── __init__.py
│   │           │   ├── lxml.etree_api.h
│   │           │   ├── lxml.etree.h
│   │           │   ├── objectify.cpython-38-x86_64-linux-gnu.so
│   │           │   ├── pyclasslookup.py
│   │           │   ├── sax.cpython-38-x86_64-linux-gnu.so
│   │           │   ├── sax.py
│   │           │   └── usedoctest.py
│   │           ├── lxml-4.6.3.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSES.txt
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── REQUESTED
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── matplotlib
│   │           │   ├── _api
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── deprecation.cpython-38.pyc
│   │           │   │   │   └── __init__.cpython-38.pyc
│   │           │   │   ├── deprecation.py
│   │           │   │   └── __init__.py
│   │           │   ├── axes
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── _axes.cpython-38.pyc
│   │           │   │   │   ├── _base.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── _secondary_axes.cpython-38.pyc
│   │           │   │   │   └── _subplots.cpython-38.pyc
│   │           │   │   ├── _axes.py
│   │           │   │   ├── _base.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _secondary_axes.py
│   │           │   │   └── _subplots.py
│   │           │   ├── backends
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── backend_agg.cpython-38.pyc
│   │           │   │   │   ├── backend_cairo.cpython-38.pyc
│   │           │   │   │   ├── backend_gtk3agg.cpython-38.pyc
│   │           │   │   │   ├── backend_gtk3cairo.cpython-38.pyc
│   │           │   │   │   ├── backend_gtk3.cpython-38.pyc
│   │           │   │   │   ├── backend_macosx.cpython-38.pyc
│   │           │   │   │   ├── backend_mixed.cpython-38.pyc
│   │           │   │   │   ├── backend_nbagg.cpython-38.pyc
│   │           │   │   │   ├── backend_pdf.cpython-38.pyc
│   │           │   │   │   ├── _backend_pdf_ps.cpython-38.pyc
│   │           │   │   │   ├── backend_pgf.cpython-38.pyc
│   │           │   │   │   ├── backend_ps.cpython-38.pyc
│   │           │   │   │   ├── backend_qt4agg.cpython-38.pyc
│   │           │   │   │   ├── backend_qt4cairo.cpython-38.pyc
│   │           │   │   │   ├── backend_qt4.cpython-38.pyc
│   │           │   │   │   ├── backend_qt5agg.cpython-38.pyc
│   │           │   │   │   ├── backend_qt5cairo.cpython-38.pyc
│   │           │   │   │   ├── backend_qt5.cpython-38.pyc
│   │           │   │   │   ├── backend_svg.cpython-38.pyc
│   │           │   │   │   ├── backend_template.cpython-38.pyc
│   │           │   │   │   ├── backend_tkagg.cpython-38.pyc
│   │           │   │   │   ├── backend_tkcairo.cpython-38.pyc
│   │           │   │   │   ├── _backend_tk.cpython-38.pyc
│   │           │   │   │   ├── backend_webagg_core.cpython-38.pyc
│   │           │   │   │   ├── backend_webagg.cpython-38.pyc
│   │           │   │   │   ├── backend_wxagg.cpython-38.pyc
│   │           │   │   │   ├── backend_wxcairo.cpython-38.pyc
│   │           │   │   │   ├── backend_wx.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   └── qt_compat.cpython-38.pyc
│   │           │   │   ├── qt_editor
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── figureoptions.cpython-38.pyc
│   │           │   │   │   │   ├── _formlayout.cpython-38.pyc
│   │           │   │   │   │   ├── _formsubplottool.cpython-38.pyc
│   │           │   │   │   │   ├── formsubplottool.cpython-38.pyc
│   │           │   │   │   │   └── __init__.cpython-38.pyc
│   │           │   │   │   ├── figureoptions.py
│   │           │   │   │   ├── _formlayout.py
│   │           │   │   │   ├── _formsubplottool.py
│   │           │   │   │   ├── formsubplottool.py
│   │           │   │   │   └── __init__.py
│   │           │   │   ├── web_backend
│   │           │   │   │   ├── css
│   │           │   │   │   │   ├── boilerplate.css
│   │           │   │   │   │   ├── fbm.css
│   │           │   │   │   │   ├── mpl.css
│   │           │   │   │   │   └── page.css
│   │           │   │   │   ├── js
│   │           │   │   │   │   ├── mpl.js
│   │           │   │   │   │   ├── mpl_tornado.js
│   │           │   │   │   │   └── nbagg_mpl.js
│   │           │   │   │   ├── all_figures.html
│   │           │   │   │   ├── ipython_inline_figure.html
│   │           │   │   │   ├── nbagg_uat.ipynb
│   │           │   │   │   ├── package.json
│   │           │   │   │   └── single_figure.html
│   │           │   │   ├── _backend_agg.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── backend_agg.py
│   │           │   │   ├── backend_cairo.py
│   │           │   │   ├── backend_gtk3agg.py
│   │           │   │   ├── backend_gtk3cairo.py
│   │           │   │   ├── backend_gtk3.py
│   │           │   │   ├── backend_macosx.py
│   │           │   │   ├── backend_mixed.py
│   │           │   │   ├── backend_nbagg.py
│   │           │   │   ├── _backend_pdf_ps.py
│   │           │   │   ├── backend_pdf.py
│   │           │   │   ├── backend_pgf.py
│   │           │   │   ├── backend_ps.py
│   │           │   │   ├── backend_qt4agg.py
│   │           │   │   ├── backend_qt4cairo.py
│   │           │   │   ├── backend_qt4.py
│   │           │   │   ├── backend_qt5agg.py
│   │           │   │   ├── backend_qt5cairo.py
│   │           │   │   ├── backend_qt5.py
│   │           │   │   ├── backend_svg.py
│   │           │   │   ├── backend_template.py
│   │           │   │   ├── backend_tkagg.py
│   │           │   │   ├── backend_tkcairo.py
│   │           │   │   ├── _backend_tk.py
│   │           │   │   ├── backend_webagg_core.py
│   │           │   │   ├── backend_webagg.py
│   │           │   │   ├── backend_wxagg.py
│   │           │   │   ├── backend_wxcairo.py
│   │           │   │   ├── backend_wx.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── qt_compat.py
│   │           │   │   └── _tkagg.cpython-38-x86_64-linux-gnu.so
│   │           │   ├── cbook
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── deprecation.cpython-38.pyc
│   │           │   │   │   └── __init__.cpython-38.pyc
│   │           │   │   ├── deprecation.py
│   │           │   │   └── __init__.py
│   │           │   ├── compat
│   │           │   │   ├── __pycache__
│   │           │   │   │   └── __init__.cpython-38.pyc
│   │           │   │   └── __init__.py
│   │           │   ├── mpl-data
│   │           │   │   ├── fonts
│   │           │   │   │   ├── afm
│   │           │   │   │   │   ├── cmex10.afm
│   │           │   │   │   │   ├── cmmi10.afm
│   │           │   │   │   │   ├── cmr10.afm
│   │           │   │   │   │   ├── cmsy10.afm
│   │           │   │   │   │   ├── cmtt10.afm
│   │           │   │   │   │   ├── pagd8a.afm
│   │           │   │   │   │   ├── pagdo8a.afm
│   │           │   │   │   │   ├── pagk8a.afm
│   │           │   │   │   │   ├── pagko8a.afm
│   │           │   │   │   │   ├── pbkd8a.afm
│   │           │   │   │   │   ├── pbkdi8a.afm
│   │           │   │   │   │   ├── pbkl8a.afm
│   │           │   │   │   │   ├── pbkli8a.afm
│   │           │   │   │   │   ├── pcrb8a.afm
│   │           │   │   │   │   ├── pcrbo8a.afm
│   │           │   │   │   │   ├── pcrr8a.afm
│   │           │   │   │   │   ├── pcrro8a.afm
│   │           │   │   │   │   ├── phvb8a.afm
│   │           │   │   │   │   ├── phvb8an.afm
│   │           │   │   │   │   ├── phvbo8a.afm
│   │           │   │   │   │   ├── phvbo8an.afm
│   │           │   │   │   │   ├── phvl8a.afm
│   │           │   │   │   │   ├── phvlo8a.afm
│   │           │   │   │   │   ├── phvr8a.afm
│   │           │   │   │   │   ├── phvr8an.afm
│   │           │   │   │   │   ├── phvro8a.afm
│   │           │   │   │   │   ├── phvro8an.afm
│   │           │   │   │   │   ├── pncb8a.afm
│   │           │   │   │   │   ├── pncbi8a.afm
│   │           │   │   │   │   ├── pncr8a.afm
│   │           │   │   │   │   ├── pncri8a.afm
│   │           │   │   │   │   ├── pplb8a.afm
│   │           │   │   │   │   ├── pplbi8a.afm
│   │           │   │   │   │   ├── pplr8a.afm
│   │           │   │   │   │   ├── pplri8a.afm
│   │           │   │   │   │   ├── psyr.afm
│   │           │   │   │   │   ├── ptmb8a.afm
│   │           │   │   │   │   ├── ptmbi8a.afm
│   │           │   │   │   │   ├── ptmr8a.afm
│   │           │   │   │   │   ├── ptmri8a.afm
│   │           │   │   │   │   ├── putb8a.afm
│   │           │   │   │   │   ├── putbi8a.afm
│   │           │   │   │   │   ├── putr8a.afm
│   │           │   │   │   │   ├── putri8a.afm
│   │           │   │   │   │   ├── pzcmi8a.afm
│   │           │   │   │   │   └── pzdr.afm
│   │           │   │   │   ├── pdfcorefonts
│   │           │   │   │   │   ├── Courier.afm
│   │           │   │   │   │   ├── Courier-Bold.afm
│   │           │   │   │   │   ├── Courier-BoldOblique.afm
│   │           │   │   │   │   ├── Courier-Oblique.afm
│   │           │   │   │   │   ├── Helvetica.afm
│   │           │   │   │   │   ├── Helvetica-Bold.afm
│   │           │   │   │   │   ├── Helvetica-BoldOblique.afm
│   │           │   │   │   │   ├── Helvetica-Oblique.afm
│   │           │   │   │   │   ├── readme.txt
│   │           │   │   │   │   ├── Symbol.afm
│   │           │   │   │   │   ├── Times-Bold.afm
│   │           │   │   │   │   ├── Times-BoldItalic.afm
│   │           │   │   │   │   ├── Times-Italic.afm
│   │           │   │   │   │   ├── Times-Roman.afm
│   │           │   │   │   │   └── ZapfDingbats.afm
│   │           │   │   │   └── ttf
│   │           │   │   │       ├── cmb10.ttf
│   │           │   │   │       ├── cmex10.ttf
│   │           │   │   │       ├── cmmi10.ttf
│   │           │   │   │       ├── cmr10.ttf
│   │           │   │   │       ├── cmss10.ttf
│   │           │   │   │       ├── cmsy10.ttf
│   │           │   │   │       ├── cmtt10.ttf
│   │           │   │   │       ├── DejaVuSans-BoldOblique.ttf
│   │           │   │   │       ├── DejaVuSans-Bold.ttf
│   │           │   │   │       ├── DejaVuSansDisplay.ttf
│   │           │   │   │       ├── DejaVuSansMono-BoldOblique.ttf
│   │           │   │   │       ├── DejaVuSansMono-Bold.ttf
│   │           │   │   │       ├── DejaVuSansMono-Oblique.ttf
│   │           │   │   │       ├── DejaVuSansMono.ttf
│   │           │   │   │       ├── DejaVuSans-Oblique.ttf
│   │           │   │   │       ├── DejaVuSans.ttf
│   │           │   │   │       ├── DejaVuSerif-BoldItalic.ttf
│   │           │   │   │       ├── DejaVuSerif-Bold.ttf
│   │           │   │   │       ├── DejaVuSerifDisplay.ttf
│   │           │   │   │       ├── DejaVuSerif-Italic.ttf
│   │           │   │   │       ├── DejaVuSerif.ttf
│   │           │   │   │       ├── LICENSE_DEJAVU
│   │           │   │   │       ├── LICENSE_STIX
│   │           │   │   │       ├── STIXGeneralBolIta.ttf
│   │           │   │   │       ├── STIXGeneralBol.ttf
│   │           │   │   │       ├── STIXGeneralItalic.ttf
│   │           │   │   │       ├── STIXGeneral.ttf
│   │           │   │   │       ├── STIXNonUniBolIta.ttf
│   │           │   │   │       ├── STIXNonUniBol.ttf
│   │           │   │   │       ├── STIXNonUniIta.ttf
│   │           │   │   │       ├── STIXNonUni.ttf
│   │           │   │   │       ├── STIXSizFiveSymReg.ttf
│   │           │   │   │       ├── STIXSizFourSymBol.ttf
│   │           │   │   │       ├── STIXSizFourSymReg.ttf
│   │           │   │   │       ├── STIXSizOneSymBol.ttf
│   │           │   │   │       ├── STIXSizOneSymReg.ttf
│   │           │   │   │       ├── STIXSizThreeSymBol.ttf
│   │           │   │   │       ├── STIXSizThreeSymReg.ttf
│   │           │   │   │       ├── STIXSizTwoSymBol.ttf
│   │           │   │   │       └── STIXSizTwoSymReg.ttf
│   │           │   │   ├── images
│   │           │   │   │   ├── back_large.png
│   │           │   │   │   ├── back.pdf
│   │           │   │   │   ├── back.png
│   │           │   │   │   ├── back.svg
│   │           │   │   │   ├── back-symbolic.svg
│   │           │   │   │   ├── filesave_large.png
│   │           │   │   │   ├── filesave.pdf
│   │           │   │   │   ├── filesave.png
│   │           │   │   │   ├── filesave.svg
│   │           │   │   │   ├── filesave-symbolic.svg
│   │           │   │   │   ├── forward_large.png
│   │           │   │   │   ├── forward.pdf
│   │           │   │   │   ├── forward.png
│   │           │   │   │   ├── forward.svg
│   │           │   │   │   ├── forward-symbolic.svg
│   │           │   │   │   ├── hand.pdf
│   │           │   │   │   ├── hand.png
│   │           │   │   │   ├── hand.svg
│   │           │   │   │   ├── help_large.png
│   │           │   │   │   ├── help.pdf
│   │           │   │   │   ├── help.png
│   │           │   │   │   ├── help.svg
│   │           │   │   │   ├── help-symbolic.svg
│   │           │   │   │   ├── home_large.png
│   │           │   │   │   ├── home.pdf
│   │           │   │   │   ├── home.png
│   │           │   │   │   ├── home.svg
│   │           │   │   │   ├── home-symbolic.svg
│   │           │   │   │   ├── matplotlib_128.ppm
│   │           │   │   │   ├── matplotlib_large.png
│   │           │   │   │   ├── matplotlib.pdf
│   │           │   │   │   ├── matplotlib.png
│   │           │   │   │   ├── matplotlib.svg
│   │           │   │   │   ├── move_large.png
│   │           │   │   │   ├── move.pdf
│   │           │   │   │   ├── move.png
│   │           │   │   │   ├── move.svg
│   │           │   │   │   ├── move-symbolic.svg
│   │           │   │   │   ├── qt4_editor_options_large.png
│   │           │   │   │   ├── qt4_editor_options.pdf
│   │           │   │   │   ├── qt4_editor_options.png
│   │           │   │   │   ├── qt4_editor_options.svg
│   │           │   │   │   ├── subplots_large.png
│   │           │   │   │   ├── subplots.pdf
│   │           │   │   │   ├── subplots.png
│   │           │   │   │   ├── subplots.svg
│   │           │   │   │   ├── subplots-symbolic.svg
│   │           │   │   │   ├── zoom_to_rect_large.png
│   │           │   │   │   ├── zoom_to_rect.pdf
│   │           │   │   │   ├── zoom_to_rect.png
│   │           │   │   │   ├── zoom_to_rect.svg
│   │           │   │   │   └── zoom_to_rect-symbolic.svg
│   │           │   │   ├── plot_directive
│   │           │   │   │   └── plot_directive.css
│   │           │   │   ├── sample_data
│   │           │   │   │   ├── axes_grid
│   │           │   │   │   │   └── bivariate_normal.npy
│   │           │   │   │   ├── data_x_x2_x3.csv
│   │           │   │   │   ├── eeg.dat
│   │           │   │   │   ├── embedding_in_wx3.xrc
│   │           │   │   │   ├── goog.npz
│   │           │   │   │   ├── grace_hopper.jpg
│   │           │   │   │   ├── jacksboro_fault_dem.npz
│   │           │   │   │   ├── logo2.png
│   │           │   │   │   ├── membrane.dat
│   │           │   │   │   ├── Minduka_Present_Blue_Pack.png
│   │           │   │   │   ├── msft.csv
│   │           │   │   │   ├── percent_bachelors_degrees_women_usa.csv
│   │           │   │   │   ├── README.txt
│   │           │   │   │   ├── s1045.ima.gz
│   │           │   │   │   └── topobathy.npz
│   │           │   │   ├── stylelib
│   │           │   │   │   ├── bmh.mplstyle
│   │           │   │   │   ├── classic.mplstyle
│   │           │   │   │   ├── _classic_test_patch.mplstyle
│   │           │   │   │   ├── dark_background.mplstyle
│   │           │   │   │   ├── fast.mplstyle
│   │           │   │   │   ├── fivethirtyeight.mplstyle
│   │           │   │   │   ├── ggplot.mplstyle
│   │           │   │   │   ├── grayscale.mplstyle
│   │           │   │   │   ├── seaborn-bright.mplstyle
│   │           │   │   │   ├── seaborn-colorblind.mplstyle
│   │           │   │   │   ├── seaborn-darkgrid.mplstyle
│   │           │   │   │   ├── seaborn-dark.mplstyle
│   │           │   │   │   ├── seaborn-dark-palette.mplstyle
│   │           │   │   │   ├── seaborn-deep.mplstyle
│   │           │   │   │   ├── seaborn.mplstyle
│   │           │   │   │   ├── seaborn-muted.mplstyle
│   │           │   │   │   ├── seaborn-notebook.mplstyle
│   │           │   │   │   ├── seaborn-paper.mplstyle
│   │           │   │   │   ├── seaborn-pastel.mplstyle
│   │           │   │   │   ├── seaborn-poster.mplstyle
│   │           │   │   │   ├── seaborn-talk.mplstyle
│   │           │   │   │   ├── seaborn-ticks.mplstyle
│   │           │   │   │   ├── seaborn-whitegrid.mplstyle
│   │           │   │   │   ├── seaborn-white.mplstyle
│   │           │   │   │   ├── Solarize_Light2.mplstyle
│   │           │   │   │   └── tableau-colorblind10.mplstyle
│   │           │   │   └── matplotlibrc
│   │           │   ├── projections
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── geo.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   └── polar.cpython-38.pyc
│   │           │   │   ├── geo.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── polar.py
│   │           │   ├── __pycache__
│   │           │   │   ├── afm.cpython-38.pyc
│   │           │   │   ├── animation.cpython-38.pyc
│   │           │   │   ├── _animation_data.cpython-38.pyc
│   │           │   │   ├── artist.cpython-38.pyc
│   │           │   │   ├── axis.cpython-38.pyc
│   │           │   │   ├── backend_bases.cpython-38.pyc
│   │           │   │   ├── backend_managers.cpython-38.pyc
│   │           │   │   ├── backend_tools.cpython-38.pyc
│   │           │   │   ├── bezier.cpython-38.pyc
│   │           │   │   ├── blocking_input.cpython-38.pyc
│   │           │   │   ├── category.cpython-38.pyc
│   │           │   │   ├── _cm.cpython-38.pyc
│   │           │   │   ├── cm.cpython-38.pyc
│   │           │   │   ├── _cm_listed.cpython-38.pyc
│   │           │   │   ├── collections.cpython-38.pyc
│   │           │   │   ├── colorbar.cpython-38.pyc
│   │           │   │   ├── _color_data.cpython-38.pyc
│   │           │   │   ├── colors.cpython-38.pyc
│   │           │   │   ├── _constrained_layout.cpython-38.pyc
│   │           │   │   ├── container.cpython-38.pyc
│   │           │   │   ├── contour.cpython-38.pyc
│   │           │   │   ├── dates.cpython-38.pyc
│   │           │   │   ├── docstring.cpython-38.pyc
│   │           │   │   ├── dviread.cpython-38.pyc
│   │           │   │   ├── _enums.cpython-38.pyc
│   │           │   │   ├── figure.cpython-38.pyc
│   │           │   │   ├── fontconfig_pattern.cpython-38.pyc
│   │           │   │   ├── font_manager.cpython-38.pyc
│   │           │   │   ├── gridspec.cpython-38.pyc
│   │           │   │   ├── hatch.cpython-38.pyc
│   │           │   │   ├── image.cpython-38.pyc
│   │           │   │   ├── __init__.cpython-38.pyc
│   │           │   │   ├── _internal_utils.cpython-38.pyc
│   │           │   │   ├── _layoutgrid.cpython-38.pyc
│   │           │   │   ├── legend.cpython-38.pyc
│   │           │   │   ├── legend_handler.cpython-38.pyc
│   │           │   │   ├── lines.cpython-38.pyc
│   │           │   │   ├── markers.cpython-38.pyc
│   │           │   │   ├── _mathtext.cpython-38.pyc
│   │           │   │   ├── mathtext.cpython-38.pyc
│   │           │   │   ├── _mathtext_data.cpython-38.pyc
│   │           │   │   ├── mlab.cpython-38.pyc
│   │           │   │   ├── offsetbox.cpython-38.pyc
│   │           │   │   ├── patches.cpython-38.pyc
│   │           │   │   ├── path.cpython-38.pyc
│   │           │   │   ├── patheffects.cpython-38.pyc
│   │           │   │   ├── pylab.cpython-38.pyc
│   │           │   │   ├── _pylab_helpers.cpython-38.pyc
│   │           │   │   ├── pyplot.cpython-38.pyc
│   │           │   │   ├── quiver.cpython-38.pyc
│   │           │   │   ├── rcsetup.cpython-38.pyc
│   │           │   │   ├── sankey.cpython-38.pyc
│   │           │   │   ├── scale.cpython-38.pyc
│   │           │   │   ├── spines.cpython-38.pyc
│   │           │   │   ├── stackplot.cpython-38.pyc
│   │           │   │   ├── streamplot.cpython-38.pyc
│   │           │   │   ├── table.cpython-38.pyc
│   │           │   │   ├── texmanager.cpython-38.pyc
│   │           │   │   ├── text.cpython-38.pyc
│   │           │   │   ├── _text_layout.cpython-38.pyc
│   │           │   │   ├── textpath.cpython-38.pyc
│   │           │   │   ├── ticker.cpython-38.pyc
│   │           │   │   ├── tight_bbox.cpython-38.pyc
│   │           │   │   ├── tight_layout.cpython-38.pyc
│   │           │   │   ├── transforms.cpython-38.pyc
│   │           │   │   ├── ttconv.cpython-38.pyc
│   │           │   │   ├── type1font.cpython-38.pyc
│   │           │   │   ├── units.cpython-38.pyc
│   │           │   │   ├── _version.cpython-38.pyc
│   │           │   │   └── widgets.cpython-38.pyc
│   │           │   ├── sphinxext
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── mathmpl.cpython-38.pyc
│   │           │   │   │   └── plot_directive.cpython-38.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── mathmpl.py
│   │           │   │   └── plot_directive.py
│   │           │   ├── style
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── core.cpython-38.pyc
│   │           │   │   │   └── __init__.cpython-38.pyc
│   │           │   │   ├── core.py
│   │           │   │   └── __init__.py
│   │           │   ├── testing
│   │           │   │   ├── jpl_units
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── Duration.cpython-38.pyc
│   │           │   │   │   │   ├── EpochConverter.cpython-38.pyc
│   │           │   │   │   │   ├── Epoch.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── StrConverter.cpython-38.pyc
│   │           │   │   │   │   ├── UnitDblConverter.cpython-38.pyc
│   │           │   │   │   │   ├── UnitDbl.cpython-38.pyc
│   │           │   │   │   │   └── UnitDblFormatter.cpython-38.pyc
│   │           │   │   │   ├── Duration.py
│   │           │   │   │   ├── EpochConverter.py
│   │           │   │   │   ├── Epoch.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── StrConverter.py
│   │           │   │   │   ├── UnitDblConverter.py
│   │           │   │   │   ├── UnitDblFormatter.py
│   │           │   │   │   └── UnitDbl.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── compare.cpython-38.pyc
│   │           │   │   │   ├── conftest.cpython-38.pyc
│   │           │   │   │   ├── decorators.cpython-38.pyc
│   │           │   │   │   ├── exceptions.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   └── widgets.cpython-38.pyc
│   │           │   │   ├── compare.py
│   │           │   │   ├── conftest.py
│   │           │   │   ├── decorators.py
│   │           │   │   ├── exceptions.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── widgets.py
│   │           │   ├── tests
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── conftest.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── test_afm.cpython-38.pyc
│   │           │   │   │   ├── test_agg.cpython-38.pyc
│   │           │   │   │   ├── test_agg_filter.cpython-38.pyc
│   │           │   │   │   ├── test_animation.cpython-38.pyc
│   │           │   │   │   ├── test_api.cpython-38.pyc
│   │           │   │   │   ├── test_arrow_patches.cpython-38.pyc
│   │           │   │   │   ├── test_artist.cpython-38.pyc
│   │           │   │   │   ├── test_axes.cpython-38.pyc
│   │           │   │   │   ├── test_backend_bases.cpython-38.pyc
│   │           │   │   │   ├── test_backend_cairo.cpython-38.pyc
│   │           │   │   │   ├── test_backend_gtk3.cpython-38.pyc
│   │           │   │   │   ├── test_backend_nbagg.cpython-38.pyc
│   │           │   │   │   ├── test_backend_pdf.cpython-38.pyc
│   │           │   │   │   ├── test_backend_pgf.cpython-38.pyc
│   │           │   │   │   ├── test_backend_ps.cpython-38.pyc
│   │           │   │   │   ├── test_backend_qt.cpython-38.pyc
│   │           │   │   │   ├── test_backends_interactive.cpython-38.pyc
│   │           │   │   │   ├── test_backend_svg.cpython-38.pyc
│   │           │   │   │   ├── test_backend_tk.cpython-38.pyc
│   │           │   │   │   ├── test_backend_tools.cpython-38.pyc
│   │           │   │   │   ├── test_backend_webagg.cpython-38.pyc
│   │           │   │   │   ├── test_basic.cpython-38.pyc
│   │           │   │   │   ├── test_bbox_tight.cpython-38.pyc
│   │           │   │   │   ├── test_category.cpython-38.pyc
│   │           │   │   │   ├── test_cbook.cpython-38.pyc
│   │           │   │   │   ├── test_collections.cpython-38.pyc
│   │           │   │   │   ├── test_colorbar.cpython-38.pyc
│   │           │   │   │   ├── test_colors.cpython-38.pyc
│   │           │   │   │   ├── test_compare_images.cpython-38.pyc
│   │           │   │   │   ├── test_constrainedlayout.cpython-38.pyc
│   │           │   │   │   ├── test_container.cpython-38.pyc
│   │           │   │   │   ├── test_contour.cpython-38.pyc
│   │           │   │   │   ├── test_cycles.cpython-38.pyc
│   │           │   │   │   ├── test_dates.cpython-38.pyc
│   │           │   │   │   ├── test_determinism.cpython-38.pyc
│   │           │   │   │   ├── test_dviread.cpython-38.pyc
│   │           │   │   │   ├── test_figure.cpython-38.pyc
│   │           │   │   │   ├── test_fontconfig_pattern.cpython-38.pyc
│   │           │   │   │   ├── test_font_manager.cpython-38.pyc
│   │           │   │   │   ├── test_gridspec.cpython-38.pyc
│   │           │   │   │   ├── test_image.cpython-38.pyc
│   │           │   │   │   ├── test_legend.cpython-38.pyc
│   │           │   │   │   ├── test_lines.cpython-38.pyc
│   │           │   │   │   ├── test_marker.cpython-38.pyc
│   │           │   │   │   ├── test_mathtext.cpython-38.pyc
│   │           │   │   │   ├── test_matplotlib.cpython-38.pyc
│   │           │   │   │   ├── test_mlab.cpython-38.pyc
│   │           │   │   │   ├── test_offsetbox.cpython-38.pyc
│   │           │   │   │   ├── test_patches.cpython-38.pyc
│   │           │   │   │   ├── test_path.cpython-38.pyc
│   │           │   │   │   ├── test_patheffects.cpython-38.pyc
│   │           │   │   │   ├── test_pickle.cpython-38.pyc
│   │           │   │   │   ├── test_png.cpython-38.pyc
│   │           │   │   │   ├── test_polar.cpython-38.pyc
│   │           │   │   │   ├── test_preprocess_data.cpython-38.pyc
│   │           │   │   │   ├── test_pyplot.cpython-38.pyc
│   │           │   │   │   ├── test_quiver.cpython-38.pyc
│   │           │   │   │   ├── test_rcparams.cpython-38.pyc
│   │           │   │   │   ├── test_sankey.cpython-38.pyc
│   │           │   │   │   ├── test_scale.cpython-38.pyc
│   │           │   │   │   ├── test_simplification.cpython-38.pyc
│   │           │   │   │   ├── test_skew.cpython-38.pyc
│   │           │   │   │   ├── test_sphinxext.cpython-38.pyc
│   │           │   │   │   ├── test_spines.cpython-38.pyc
│   │           │   │   │   ├── test_streamplot.cpython-38.pyc
│   │           │   │   │   ├── test_style.cpython-38.pyc
│   │           │   │   │   ├── test_subplots.cpython-38.pyc
│   │           │   │   │   ├── test_table.cpython-38.pyc
│   │           │   │   │   ├── test_testing.cpython-38.pyc
│   │           │   │   │   ├── test_texmanager.cpython-38.pyc
│   │           │   │   │   ├── test_text.cpython-38.pyc
│   │           │   │   │   ├── test_ticker.cpython-38.pyc
│   │           │   │   │   ├── test_tightlayout.cpython-38.pyc
│   │           │   │   │   ├── test_transforms.cpython-38.pyc
│   │           │   │   │   ├── test_triangulation.cpython-38.pyc
│   │           │   │   │   ├── test_ttconv.cpython-38.pyc
│   │           │   │   │   ├── test_type1font.cpython-38.pyc
│   │           │   │   │   ├── test_units.cpython-38.pyc
│   │           │   │   │   ├── test_usetex.cpython-38.pyc
│   │           │   │   │   └── test_widgets.cpython-38.pyc
│   │           │   │   ├── conftest.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── test_afm.py
│   │           │   │   ├── test_agg_filter.py
│   │           │   │   ├── test_agg.py
│   │           │   │   ├── test_animation.py
│   │           │   │   ├── test_api.py
│   │           │   │   ├── test_arrow_patches.py
│   │           │   │   ├── test_artist.py
│   │           │   │   ├── test_axes.py
│   │           │   │   ├── test_backend_bases.py
│   │           │   │   ├── test_backend_cairo.py
│   │           │   │   ├── test_backend_gtk3.py
│   │           │   │   ├── test_backend_nbagg.py
│   │           │   │   ├── test_backend_pdf.py
│   │           │   │   ├── test_backend_pgf.py
│   │           │   │   ├── test_backend_ps.py
│   │           │   │   ├── test_backend_qt.py
│   │           │   │   ├── test_backends_interactive.py
│   │           │   │   ├── test_backend_svg.py
│   │           │   │   ├── test_backend_tk.py
│   │           │   │   ├── test_backend_tools.py
│   │           │   │   ├── test_backend_webagg.py
│   │           │   │   ├── test_basic.py
│   │           │   │   ├── test_bbox_tight.py
│   │           │   │   ├── test_category.py
│   │           │   │   ├── test_cbook.py
│   │           │   │   ├── test_collections.py
│   │           │   │   ├── test_colorbar.py
│   │           │   │   ├── test_colors.py
│   │           │   │   ├── test_compare_images.py
│   │           │   │   ├── test_constrainedlayout.py
│   │           │   │   ├── test_container.py
│   │           │   │   ├── test_contour.py
│   │           │   │   ├── test_cycles.py
│   │           │   │   ├── test_dates.py
│   │           │   │   ├── test_determinism.py
│   │           │   │   ├── test_dviread.py
│   │           │   │   ├── test_figure.py
│   │           │   │   ├── test_fontconfig_pattern.py
│   │           │   │   ├── test_font_manager.py
│   │           │   │   ├── test_gridspec.py
│   │           │   │   ├── test_image.py
│   │           │   │   ├── test_legend.py
│   │           │   │   ├── test_lines.py
│   │           │   │   ├── test_marker.py
│   │           │   │   ├── test_mathtext.py
│   │           │   │   ├── test_matplotlib.py
│   │           │   │   ├── test_mlab.py
│   │           │   │   ├── test_offsetbox.py
│   │           │   │   ├── test_patches.py
│   │           │   │   ├── test_patheffects.py
│   │           │   │   ├── test_path.py
│   │           │   │   ├── test_pickle.py
│   │           │   │   ├── test_png.py
│   │           │   │   ├── test_polar.py
│   │           │   │   ├── test_preprocess_data.py
│   │           │   │   ├── test_pyplot.py
│   │           │   │   ├── test_quiver.py
│   │           │   │   ├── test_rcparams.py
│   │           │   │   ├── test_sankey.py
│   │           │   │   ├── test_scale.py
│   │           │   │   ├── test_simplification.py
│   │           │   │   ├── test_skew.py
│   │           │   │   ├── test_sphinxext.py
│   │           │   │   ├── test_spines.py
│   │           │   │   ├── test_streamplot.py
│   │           │   │   ├── test_style.py
│   │           │   │   ├── test_subplots.py
│   │           │   │   ├── test_table.py
│   │           │   │   ├── test_testing.py
│   │           │   │   ├── test_texmanager.py
│   │           │   │   ├── test_text.py
│   │           │   │   ├── test_ticker.py
│   │           │   │   ├── test_tightlayout.py
│   │           │   │   ├── test_transforms.py
│   │           │   │   ├── test_triangulation.py
│   │           │   │   ├── test_ttconv.py
│   │           │   │   ├── test_type1font.py
│   │           │   │   ├── test_units.py
│   │           │   │   ├── test_usetex.py
│   │           │   │   └── test_widgets.py
│   │           │   ├── tri
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── triangulation.cpython-38.pyc
│   │           │   │   │   ├── tricontour.cpython-38.pyc
│   │           │   │   │   ├── trifinder.cpython-38.pyc
│   │           │   │   │   ├── triinterpolate.cpython-38.pyc
│   │           │   │   │   ├── tripcolor.cpython-38.pyc
│   │           │   │   │   ├── triplot.cpython-38.pyc
│   │           │   │   │   ├── trirefine.cpython-38.pyc
│   │           │   │   │   └── tritools.cpython-38.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── triangulation.py
│   │           │   │   ├── tricontour.py
│   │           │   │   ├── trifinder.py
│   │           │   │   ├── triinterpolate.py
│   │           │   │   ├── tripcolor.py
│   │           │   │   ├── triplot.py
│   │           │   │   ├── trirefine.py
│   │           │   │   └── tritools.py
│   │           │   ├── afm.py
│   │           │   ├── _animation_data.py
│   │           │   ├── animation.py
│   │           │   ├── artist.py
│   │           │   ├── axis.py
│   │           │   ├── backend_bases.py
│   │           │   ├── backend_managers.py
│   │           │   ├── backend_tools.py
│   │           │   ├── bezier.py
│   │           │   ├── blocking_input.py
│   │           │   ├── category.py
│   │           │   ├── _c_internal_utils.cpython-38-x86_64-linux-gnu.so
│   │           │   ├── _cm_listed.py
│   │           │   ├── _cm.py
│   │           │   ├── cm.py
│   │           │   ├── collections.py
│   │           │   ├── colorbar.py
│   │           │   ├── _color_data.py
│   │           │   ├── colors.py
│   │           │   ├── _constrained_layout.py
│   │           │   ├── container.py
│   │           │   ├── _contour.cpython-38-x86_64-linux-gnu.so
│   │           │   ├── contour.py
│   │           │   ├── dates.py
│   │           │   ├── docstring.py
│   │           │   ├── dviread.py
│   │           │   ├── _enums.py
│   │           │   ├── figure.py
│   │           │   ├── fontconfig_pattern.py
│   │           │   ├── font_manager.py
│   │           │   ├── ft2font.cpython-38-x86_64-linux-gnu.so
│   │           │   ├── gridspec.py
│   │           │   ├── hatch.py
│   │           │   ├── _image.cpython-38-x86_64-linux-gnu.so
│   │           │   ├── image.py
│   │           │   ├── __init__.py
│   │           │   ├── _internal_utils.py
│   │           │   ├── _layoutgrid.py
│   │           │   ├── legend_handler.py
│   │           │   ├── legend.py
│   │           │   ├── lines.py
│   │           │   ├── markers.py
│   │           │   ├── _mathtext_data.py
│   │           │   ├── _mathtext.py
│   │           │   ├── mathtext.py
│   │           │   ├── mlab.py
│   │           │   ├── offsetbox.py
│   │           │   ├── patches.py
│   │           │   ├── _path.cpython-38-x86_64-linux-gnu.so
│   │           │   ├── patheffects.py
│   │           │   ├── path.py
│   │           │   ├── _pylab_helpers.py
│   │           │   ├── pylab.py
│   │           │   ├── pyplot.py
│   │           │   ├── _qhull.cpython-38-x86_64-linux-gnu.so
│   │           │   ├── quiver.py
│   │           │   ├── rcsetup.py
│   │           │   ├── sankey.py
│   │           │   ├── scale.py
│   │           │   ├── spines.py
│   │           │   ├── stackplot.py
│   │           │   ├── streamplot.py
│   │           │   ├── table.py
│   │           │   ├── texmanager.py
│   │           │   ├── _text_layout.py
│   │           │   ├── textpath.py
│   │           │   ├── text.py
│   │           │   ├── ticker.py
│   │           │   ├── tight_bbox.py
│   │           │   ├── tight_layout.py
│   │           │   ├── transforms.py
│   │           │   ├── _tri.cpython-38-x86_64-linux-gnu.so
│   │           │   ├── _ttconv.cpython-38-x86_64-linux-gnu.so
│   │           │   ├── ttconv.py
│   │           │   ├── type1font.py
│   │           │   ├── units.py
│   │           │   ├── _version.py
│   │           │   └── widgets.py
│   │           ├── matplotlib-3.4.2.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── LICENSE_AMSFONTS
│   │           │   ├── LICENSE_BAKOMA
│   │           │   ├── LICENSE_CARLOGO
│   │           │   ├── LICENSE_COLORBREWER
│   │           │   ├── LICENSE_JSXTOOLS_RESIZE_OBSERVER
│   │           │   ├── LICENSE_QHULL
│   │           │   ├── LICENSE_QT4_EDITOR
│   │           │   ├── LICENSE_SOLARIZED
│   │           │   ├── LICENSE_STIX
│   │           │   ├── LICENSE_YORICK
│   │           │   ├── METADATA
│   │           │   ├── namespace_packages.txt
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── mpl_toolkits
│   │           │   ├── axes_grid
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── anchored_artists.cpython-38.pyc
│   │           │   │   │   ├── angle_helper.cpython-38.pyc
│   │           │   │   │   ├── axes_divider.cpython-38.pyc
│   │           │   │   │   ├── axes_grid.cpython-38.pyc
│   │           │   │   │   ├── axes_rgb.cpython-38.pyc
│   │           │   │   │   ├── axes_size.cpython-38.pyc
│   │           │   │   │   ├── axis_artist.cpython-38.pyc
│   │           │   │   │   ├── axislines.cpython-38.pyc
│   │           │   │   │   ├── axisline_style.cpython-38.pyc
│   │           │   │   │   ├── clip_path.cpython-38.pyc
│   │           │   │   │   ├── floating_axes.cpython-38.pyc
│   │           │   │   │   ├── grid_finder.cpython-38.pyc
│   │           │   │   │   ├── grid_helper_curvelinear.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── inset_locator.cpython-38.pyc
│   │           │   │   │   └── parasite_axes.cpython-38.pyc
│   │           │   │   ├── anchored_artists.py
│   │           │   │   ├── angle_helper.py
│   │           │   │   ├── axes_divider.py
│   │           │   │   ├── axes_grid.py
│   │           │   │   ├── axes_rgb.py
│   │           │   │   ├── axes_size.py
│   │           │   │   ├── axis_artist.py
│   │           │   │   ├── axislines.py
│   │           │   │   ├── axisline_style.py
│   │           │   │   ├── clip_path.py
│   │           │   │   ├── floating_axes.py
│   │           │   │   ├── grid_finder.py
│   │           │   │   ├── grid_helper_curvelinear.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── inset_locator.py
│   │           │   │   └── parasite_axes.py
│   │           │   ├── axes_grid1
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── anchored_artists.cpython-38.pyc
│   │           │   │   │   ├── axes_divider.cpython-38.pyc
│   │           │   │   │   ├── axes_grid.cpython-38.pyc
│   │           │   │   │   ├── axes_rgb.cpython-38.pyc
│   │           │   │   │   ├── axes_size.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── inset_locator.cpython-38.pyc
│   │           │   │   │   ├── mpl_axes.cpython-38.pyc
│   │           │   │   │   └── parasite_axes.cpython-38.pyc
│   │           │   │   ├── anchored_artists.py
│   │           │   │   ├── axes_divider.py
│   │           │   │   ├── axes_grid.py
│   │           │   │   ├── axes_rgb.py
│   │           │   │   ├── axes_size.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── inset_locator.py
│   │           │   │   ├── mpl_axes.py
│   │           │   │   └── parasite_axes.py
│   │           │   ├── axisartist
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── angle_helper.cpython-38.pyc
│   │           │   │   │   ├── axes_divider.cpython-38.pyc
│   │           │   │   │   ├── axes_grid.cpython-38.pyc
│   │           │   │   │   ├── axes_rgb.cpython-38.pyc
│   │           │   │   │   ├── axis_artist.cpython-38.pyc
│   │           │   │   │   ├── axislines.cpython-38.pyc
│   │           │   │   │   ├── axisline_style.cpython-38.pyc
│   │           │   │   │   ├── clip_path.cpython-38.pyc
│   │           │   │   │   ├── floating_axes.cpython-38.pyc
│   │           │   │   │   ├── grid_finder.cpython-38.pyc
│   │           │   │   │   ├── grid_helper_curvelinear.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   └── parasite_axes.cpython-38.pyc
│   │           │   │   ├── angle_helper.py
│   │           │   │   ├── axes_divider.py
│   │           │   │   ├── axes_grid.py
│   │           │   │   ├── axes_rgb.py
│   │           │   │   ├── axis_artist.py
│   │           │   │   ├── axislines.py
│   │           │   │   ├── axisline_style.py
│   │           │   │   ├── clip_path.py
│   │           │   │   ├── floating_axes.py
│   │           │   │   ├── grid_finder.py
│   │           │   │   ├── grid_helper_curvelinear.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── parasite_axes.py
│   │           │   ├── mplot3d
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── art3d.cpython-38.pyc
│   │           │   │   │   ├── axes3d.cpython-38.pyc
│   │           │   │   │   ├── axis3d.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   └── proj3d.cpython-38.pyc
│   │           │   │   ├── art3d.py
│   │           │   │   ├── axes3d.py
│   │           │   │   ├── axis3d.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── proj3d.py
│   │           │   └── tests
│   │           │       ├── __pycache__
│   │           │       │   ├── conftest.cpython-38.pyc
│   │           │       │   ├── __init__.cpython-38.pyc
│   │           │       │   ├── test_axes_grid1.cpython-38.pyc
│   │           │       │   ├── test_axes_grid.cpython-38.pyc
│   │           │       │   ├── test_axisartist_angle_helper.cpython-38.pyc
│   │           │       │   ├── test_axisartist_axis_artist.cpython-38.pyc
│   │           │       │   ├── test_axisartist_axislines.cpython-38.pyc
│   │           │       │   ├── test_axisartist_clip_path.cpython-38.pyc
│   │           │       │   ├── test_axisartist_floating_axes.cpython-38.pyc
│   │           │       │   ├── test_axisartist_grid_finder.cpython-38.pyc
│   │           │       │   ├── test_axisartist_grid_helper_curvelinear.cpython-38.pyc
│   │           │       │   └── test_mplot3d.cpython-38.pyc
│   │           │       ├── conftest.py
│   │           │       ├── __init__.py
│   │           │       ├── test_axes_grid1.py
│   │           │       ├── test_axes_grid.py
│   │           │       ├── test_axisartist_angle_helper.py
│   │           │       ├── test_axisartist_axis_artist.py
│   │           │       ├── test_axisartist_axislines.py
│   │           │       ├── test_axisartist_clip_path.py
│   │           │       ├── test_axisartist_floating_axes.py
│   │           │       ├── test_axisartist_grid_finder.py
│   │           │       ├── test_axisartist_grid_helper_curvelinear.py
│   │           │       └── test_mplot3d.py
│   │           ├── multidict
│   │           │   ├── _multilib
│   │           │   │   ├── defs.h
│   │           │   │   ├── dict.h
│   │           │   │   ├── istr.h
│   │           │   │   ├── iter.h
│   │           │   │   ├── pair_list.h
│   │           │   │   └── views.h
│   │           │   ├── __pycache__
│   │           │   │   ├── _abc.cpython-38.pyc
│   │           │   │   ├── _compat.cpython-38.pyc
│   │           │   │   ├── __init__.cpython-38.pyc
│   │           │   │   ├── _multidict_base.cpython-38.pyc
│   │           │   │   └── _multidict_py.cpython-38.pyc
│   │           │   ├── _abc.py
│   │           │   ├── _compat.py
│   │           │   ├── __init__.py
│   │           │   ├── __init__.pyi
│   │           │   ├── _multidict_base.py
│   │           │   ├── _multidict.c
│   │           │   ├── _multidict.cpython-38-x86_64-linux-gnu.so
│   │           │   ├── _multidict_py.py
│   │           │   └── py.typed
│   │           ├── multidict-5.1.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── networkx
│   │           │   ├── algorithms
│   │           │   │   ├── approximation
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── clique.cpython-38.pyc
│   │           │   │   │   │   ├── clustering_coefficient.cpython-38.pyc
│   │           │   │   │   │   ├── connectivity.cpython-38.pyc
│   │           │   │   │   │   ├── dominating_set.cpython-38.pyc
│   │           │   │   │   │   ├── independent_set.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── kcomponents.cpython-38.pyc
│   │           │   │   │   │   ├── matching.cpython-38.pyc
│   │           │   │   │   │   ├── ramsey.cpython-38.pyc
│   │           │   │   │   │   ├── steinertree.cpython-38.pyc
│   │           │   │   │   │   ├── treewidth.cpython-38.pyc
│   │           │   │   │   │   └── vertex_cover.cpython-38.pyc
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_approx_clust_coeff.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_clique.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_connectivity.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_dominating_set.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_independent_set.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_kcomponents.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_matching.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_ramsey.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_steinertree.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_treewidth.cpython-38.pyc
│   │           │   │   │   │   │   └── test_vertex_cover.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── test_approx_clust_coeff.py
│   │           │   │   │   │   ├── test_clique.py
│   │           │   │   │   │   ├── test_connectivity.py
│   │           │   │   │   │   ├── test_dominating_set.py
│   │           │   │   │   │   ├── test_independent_set.py
│   │           │   │   │   │   ├── test_kcomponents.py
│   │           │   │   │   │   ├── test_matching.py
│   │           │   │   │   │   ├── test_ramsey.py
│   │           │   │   │   │   ├── test_steinertree.py
│   │           │   │   │   │   ├── test_treewidth.py
│   │           │   │   │   │   └── test_vertex_cover.py
│   │           │   │   │   ├── clique.py
│   │           │   │   │   ├── clustering_coefficient.py
│   │           │   │   │   ├── connectivity.py
│   │           │   │   │   ├── dominating_set.py
│   │           │   │   │   ├── independent_set.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── kcomponents.py
│   │           │   │   │   ├── matching.py
│   │           │   │   │   ├── ramsey.py
│   │           │   │   │   ├── steinertree.py
│   │           │   │   │   ├── treewidth.py
│   │           │   │   │   └── vertex_cover.py
│   │           │   │   ├── assortativity
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── connectivity.cpython-38.pyc
│   │           │   │   │   │   ├── correlation.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── mixing.cpython-38.pyc
│   │           │   │   │   │   ├── neighbor_degree.cpython-38.pyc
│   │           │   │   │   │   └── pairs.cpython-38.pyc
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── base_test.cpython-38.pyc
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_connectivity.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_correlation.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_mixing.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_neighbor_degree.cpython-38.pyc
│   │           │   │   │   │   │   └── test_pairs.cpython-38.pyc
│   │           │   │   │   │   ├── base_test.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── test_connectivity.py
│   │           │   │   │   │   ├── test_correlation.py
│   │           │   │   │   │   ├── test_mixing.py
│   │           │   │   │   │   ├── test_neighbor_degree.py
│   │           │   │   │   │   └── test_pairs.py
│   │           │   │   │   ├── connectivity.py
│   │           │   │   │   ├── correlation.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── mixing.py
│   │           │   │   │   ├── neighbor_degree.py
│   │           │   │   │   └── pairs.py
│   │           │   │   ├── bipartite
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── basic.cpython-38.pyc
│   │           │   │   │   │   ├── centrality.cpython-38.pyc
│   │           │   │   │   │   ├── cluster.cpython-38.pyc
│   │           │   │   │   │   ├── covering.cpython-38.pyc
│   │           │   │   │   │   ├── edgelist.cpython-38.pyc
│   │           │   │   │   │   ├── generators.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── matching.cpython-38.pyc
│   │           │   │   │   │   ├── matrix.cpython-38.pyc
│   │           │   │   │   │   ├── projection.cpython-38.pyc
│   │           │   │   │   │   ├── redundancy.cpython-38.pyc
│   │           │   │   │   │   └── spectral.cpython-38.pyc
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_basic.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_centrality.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_cluster.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_covering.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_edgelist.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_generators.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_matching.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_matrix.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_project.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_redundancy.cpython-38.pyc
│   │           │   │   │   │   │   └── test_spectral_bipartivity.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── test_basic.py
│   │           │   │   │   │   ├── test_centrality.py
│   │           │   │   │   │   ├── test_cluster.py
│   │           │   │   │   │   ├── test_covering.py
│   │           │   │   │   │   ├── test_edgelist.py
│   │           │   │   │   │   ├── test_generators.py
│   │           │   │   │   │   ├── test_matching.py
│   │           │   │   │   │   ├── test_matrix.py
│   │           │   │   │   │   ├── test_project.py
│   │           │   │   │   │   ├── test_redundancy.py
│   │           │   │   │   │   └── test_spectral_bipartivity.py
│   │           │   │   │   ├── basic.py
│   │           │   │   │   ├── centrality.py
│   │           │   │   │   ├── cluster.py
│   │           │   │   │   ├── covering.py
│   │           │   │   │   ├── edgelist.py
│   │           │   │   │   ├── generators.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── matching.py
│   │           │   │   │   ├── matrix.py
│   │           │   │   │   ├── projection.py
│   │           │   │   │   ├── redundancy.py
│   │           │   │   │   └── spectral.py
│   │           │   │   ├── centrality
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── betweenness.cpython-38.pyc
│   │           │   │   │   │   ├── betweenness_subset.cpython-38.pyc
│   │           │   │   │   │   ├── closeness.cpython-38.pyc
│   │           │   │   │   │   ├── current_flow_betweenness.cpython-38.pyc
│   │           │   │   │   │   ├── current_flow_betweenness_subset.cpython-38.pyc
│   │           │   │   │   │   ├── current_flow_closeness.cpython-38.pyc
│   │           │   │   │   │   ├── degree_alg.cpython-38.pyc
│   │           │   │   │   │   ├── dispersion.cpython-38.pyc
│   │           │   │   │   │   ├── eigenvector.cpython-38.pyc
│   │           │   │   │   │   ├── flow_matrix.cpython-38.pyc
│   │           │   │   │   │   ├── group.cpython-38.pyc
│   │           │   │   │   │   ├── harmonic.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── katz.cpython-38.pyc
│   │           │   │   │   │   ├── load.cpython-38.pyc
│   │           │   │   │   │   ├── percolation.cpython-38.pyc
│   │           │   │   │   │   ├── reaching.cpython-38.pyc
│   │           │   │   │   │   ├── second_order.cpython-38.pyc
│   │           │   │   │   │   ├── subgraph_alg.cpython-38.pyc
│   │           │   │   │   │   ├── trophic.cpython-38.pyc
│   │           │   │   │   │   └── voterank_alg.cpython-38.pyc
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_betweenness_centrality.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_betweenness_centrality_subset.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_closeness_centrality.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_current_flow_betweenness_centrality.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_current_flow_betweenness_centrality_subset.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_current_flow_closeness.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_degree_centrality.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_dispersion.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_eigenvector_centrality.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_group.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_harmonic_centrality.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_katz_centrality.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_load_centrality.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_percolation_centrality.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_reaching.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_second_order_centrality.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_subgraph.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_trophic.cpython-38.pyc
│   │           │   │   │   │   │   └── test_voterank.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── test_betweenness_centrality.py
│   │           │   │   │   │   ├── test_betweenness_centrality_subset.py
│   │           │   │   │   │   ├── test_closeness_centrality.py
│   │           │   │   │   │   ├── test_current_flow_betweenness_centrality.py
│   │           │   │   │   │   ├── test_current_flow_betweenness_centrality_subset.py
│   │           │   │   │   │   ├── test_current_flow_closeness.py
│   │           │   │   │   │   ├── test_degree_centrality.py
│   │           │   │   │   │   ├── test_dispersion.py
│   │           │   │   │   │   ├── test_eigenvector_centrality.py
│   │           │   │   │   │   ├── test_group.py
│   │           │   │   │   │   ├── test_harmonic_centrality.py
│   │           │   │   │   │   ├── test_katz_centrality.py
│   │           │   │   │   │   ├── test_load_centrality.py
│   │           │   │   │   │   ├── test_percolation_centrality.py
│   │           │   │   │   │   ├── test_reaching.py
│   │           │   │   │   │   ├── test_second_order_centrality.py
│   │           │   │   │   │   ├── test_subgraph.py
│   │           │   │   │   │   ├── test_trophic.py
│   │           │   │   │   │   └── test_voterank.py
│   │           │   │   │   ├── betweenness.py
│   │           │   │   │   ├── betweenness_subset.py
│   │           │   │   │   ├── closeness.py
│   │           │   │   │   ├── current_flow_betweenness.py
│   │           │   │   │   ├── current_flow_betweenness_subset.py
│   │           │   │   │   ├── current_flow_closeness.py
│   │           │   │   │   ├── degree_alg.py
│   │           │   │   │   ├── dispersion.py
│   │           │   │   │   ├── eigenvector.py
│   │           │   │   │   ├── flow_matrix.py
│   │           │   │   │   ├── group.py
│   │           │   │   │   ├── harmonic.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── katz.py
│   │           │   │   │   ├── load.py
│   │           │   │   │   ├── percolation.py
│   │           │   │   │   ├── reaching.py
│   │           │   │   │   ├── second_order.py
│   │           │   │   │   ├── subgraph_alg.py
│   │           │   │   │   ├── trophic.py
│   │           │   │   │   └── voterank_alg.py
│   │           │   │   ├── coloring
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── equitable_coloring.cpython-38.pyc
│   │           │   │   │   │   ├── greedy_coloring.cpython-38.pyc
│   │           │   │   │   │   ├── greedy_coloring_with_interchange.cpython-38.pyc
│   │           │   │   │   │   └── __init__.cpython-38.pyc
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   └── test_coloring.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── test_coloring.py
│   │           │   │   │   ├── equitable_coloring.py
│   │           │   │   │   ├── greedy_coloring.py
│   │           │   │   │   ├── greedy_coloring_with_interchange.py
│   │           │   │   │   └── __init__.py
│   │           │   │   ├── community
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── asyn_fluid.cpython-38.pyc
│   │           │   │   │   │   ├── centrality.cpython-38.pyc
│   │           │   │   │   │   ├── community_utils.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── kclique.cpython-38.pyc
│   │           │   │   │   │   ├── kernighan_lin.cpython-38.pyc
│   │           │   │   │   │   ├── label_propagation.cpython-38.pyc
│   │           │   │   │   │   ├── lukes.cpython-38.pyc
│   │           │   │   │   │   ├── modularity_max.cpython-38.pyc
│   │           │   │   │   │   └── quality.cpython-38.pyc
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_asyn_fluid.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_centrality.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_kclique.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_kernighan_lin.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_label_propagation.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_lukes.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_modularity_max.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_quality.cpython-38.pyc
│   │           │   │   │   │   │   └── test_utils.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── test_asyn_fluid.py
│   │           │   │   │   │   ├── test_centrality.py
│   │           │   │   │   │   ├── test_kclique.py
│   │           │   │   │   │   ├── test_kernighan_lin.py
│   │           │   │   │   │   ├── test_label_propagation.py
│   │           │   │   │   │   ├── test_lukes.py
│   │           │   │   │   │   ├── test_modularity_max.py
│   │           │   │   │   │   ├── test_quality.py
│   │           │   │   │   │   └── test_utils.py
│   │           │   │   │   ├── asyn_fluid.py
│   │           │   │   │   ├── centrality.py
│   │           │   │   │   ├── community_utils.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── kclique.py
│   │           │   │   │   ├── kernighan_lin.py
│   │           │   │   │   ├── label_propagation.py
│   │           │   │   │   ├── lukes.py
│   │           │   │   │   ├── modularity_max.py
│   │           │   │   │   └── quality.py
│   │           │   │   ├── components
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── attracting.cpython-38.pyc
│   │           │   │   │   │   ├── biconnected.cpython-38.pyc
│   │           │   │   │   │   ├── connected.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── semiconnected.cpython-38.pyc
│   │           │   │   │   │   ├── strongly_connected.cpython-38.pyc
│   │           │   │   │   │   └── weakly_connected.cpython-38.pyc
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_attracting.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_biconnected.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_connected.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_semiconnected.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_strongly_connected.cpython-38.pyc
│   │           │   │   │   │   │   └── test_weakly_connected.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── test_attracting.py
│   │           │   │   │   │   ├── test_biconnected.py
│   │           │   │   │   │   ├── test_connected.py
│   │           │   │   │   │   ├── test_semiconnected.py
│   │           │   │   │   │   ├── test_strongly_connected.py
│   │           │   │   │   │   └── test_weakly_connected.py
│   │           │   │   │   ├── attracting.py
│   │           │   │   │   ├── biconnected.py
│   │           │   │   │   ├── connected.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── semiconnected.py
│   │           │   │   │   ├── strongly_connected.py
│   │           │   │   │   └── weakly_connected.py
│   │           │   │   ├── connectivity
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── connectivity.cpython-38.pyc
│   │           │   │   │   │   ├── cuts.cpython-38.pyc
│   │           │   │   │   │   ├── disjoint_paths.cpython-38.pyc
│   │           │   │   │   │   ├── edge_augmentation.cpython-38.pyc
│   │           │   │   │   │   ├── edge_kcomponents.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── kcomponents.cpython-38.pyc
│   │           │   │   │   │   ├── kcutsets.cpython-38.pyc
│   │           │   │   │   │   ├── stoerwagner.cpython-38.pyc
│   │           │   │   │   │   └── utils.cpython-38.pyc
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_connectivity.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_cuts.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_disjoint_paths.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_edge_augmentation.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_edge_kcomponents.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_kcomponents.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_kcutsets.cpython-38.pyc
│   │           │   │   │   │   │   └── test_stoer_wagner.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── test_connectivity.py
│   │           │   │   │   │   ├── test_cuts.py
│   │           │   │   │   │   ├── test_disjoint_paths.py
│   │           │   │   │   │   ├── test_edge_augmentation.py
│   │           │   │   │   │   ├── test_edge_kcomponents.py
│   │           │   │   │   │   ├── test_kcomponents.py
│   │           │   │   │   │   ├── test_kcutsets.py
│   │           │   │   │   │   └── test_stoer_wagner.py
│   │           │   │   │   ├── connectivity.py
│   │           │   │   │   ├── cuts.py
│   │           │   │   │   ├── disjoint_paths.py
│   │           │   │   │   ├── edge_augmentation.py
│   │           │   │   │   ├── edge_kcomponents.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── kcomponents.py
│   │           │   │   │   ├── kcutsets.py
│   │           │   │   │   ├── stoerwagner.py
│   │           │   │   │   └── utils.py
│   │           │   │   ├── flow
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── boykovkolmogorov.cpython-38.pyc
│   │           │   │   │   │   ├── capacityscaling.cpython-38.pyc
│   │           │   │   │   │   ├── dinitz_alg.cpython-38.pyc
│   │           │   │   │   │   ├── edmondskarp.cpython-38.pyc
│   │           │   │   │   │   ├── gomory_hu.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── maxflow.cpython-38.pyc
│   │           │   │   │   │   ├── mincost.cpython-38.pyc
│   │           │   │   │   │   ├── networksimplex.cpython-38.pyc
│   │           │   │   │   │   ├── preflowpush.cpython-38.pyc
│   │           │   │   │   │   ├── shortestaugmentingpath.cpython-38.pyc
│   │           │   │   │   │   └── utils.cpython-38.pyc
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_gomory_hu.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_maxflow.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_maxflow_large_graph.cpython-38.pyc
│   │           │   │   │   │   │   └── test_mincost.cpython-38.pyc
│   │           │   │   │   │   ├── gl1.gpickle.bz2
│   │           │   │   │   │   ├── gw1.gpickle.bz2
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── netgen-2.gpickle.bz2
│   │           │   │   │   │   ├── test_gomory_hu.py
│   │           │   │   │   │   ├── test_maxflow_large_graph.py
│   │           │   │   │   │   ├── test_maxflow.py
│   │           │   │   │   │   ├── test_mincost.py
│   │           │   │   │   │   └── wlm3.gpickle.bz2
│   │           │   │   │   ├── boykovkolmogorov.py
│   │           │   │   │   ├── capacityscaling.py
│   │           │   │   │   ├── dinitz_alg.py
│   │           │   │   │   ├── edmondskarp.py
│   │           │   │   │   ├── gomory_hu.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── maxflow.py
│   │           │   │   │   ├── mincost.py
│   │           │   │   │   ├── networksimplex.py
│   │           │   │   │   ├── preflowpush.py
│   │           │   │   │   ├── shortestaugmentingpath.py
│   │           │   │   │   └── utils.py
│   │           │   │   ├── isomorphism
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── ismags.cpython-38.pyc
│   │           │   │   │   │   ├── isomorph.cpython-38.pyc
│   │           │   │   │   │   ├── isomorphvf2.cpython-38.pyc
│   │           │   │   │   │   ├── matchhelpers.cpython-38.pyc
│   │           │   │   │   │   ├── temporalisomorphvf2.cpython-38.pyc
│   │           │   │   │   │   ├── tree_isomorphism.cpython-38.pyc
│   │           │   │   │   │   └── vf2userfunc.cpython-38.pyc
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_ismags.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_isomorphism.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_isomorphvf2.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_match_helpers.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_temporalisomorphvf2.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_tree_isomorphism.cpython-38.pyc
│   │           │   │   │   │   │   └── test_vf2userfunc.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── iso_r01_s80.A99
│   │           │   │   │   │   ├── iso_r01_s80.B99
│   │           │   │   │   │   ├── si2_b06_m200.A99
│   │           │   │   │   │   ├── si2_b06_m200.B99
│   │           │   │   │   │   ├── test_ismags.py
│   │           │   │   │   │   ├── test_isomorphism.py
│   │           │   │   │   │   ├── test_isomorphvf2.py
│   │           │   │   │   │   ├── test_match_helpers.py
│   │           │   │   │   │   ├── test_temporalisomorphvf2.py
│   │           │   │   │   │   ├── test_tree_isomorphism.py
│   │           │   │   │   │   └── test_vf2userfunc.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── ismags.py
│   │           │   │   │   ├── isomorph.py
│   │           │   │   │   ├── isomorphvf2.py
│   │           │   │   │   ├── matchhelpers.py
│   │           │   │   │   ├── temporalisomorphvf2.py
│   │           │   │   │   ├── tree_isomorphism.py
│   │           │   │   │   └── vf2userfunc.py
│   │           │   │   ├── link_analysis
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── hits_alg.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   └── pagerank_alg.cpython-38.pyc
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_hits.cpython-38.pyc
│   │           │   │   │   │   │   └── test_pagerank.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── test_hits.py
│   │           │   │   │   │   └── test_pagerank.py
│   │           │   │   │   ├── hits_alg.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── pagerank_alg.py
│   │           │   │   ├── node_classification
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── hmn.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── lgc.cpython-38.pyc
│   │           │   │   │   │   └── utils.cpython-38.pyc
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_harmonic_function.cpython-38.pyc
│   │           │   │   │   │   │   └── test_local_and_global_consistency.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── test_harmonic_function.py
│   │           │   │   │   │   └── test_local_and_global_consistency.py
│   │           │   │   │   ├── hmn.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── lgc.py
│   │           │   │   │   └── utils.py
│   │           │   │   ├── operators
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── all.cpython-38.pyc
│   │           │   │   │   │   ├── binary.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── product.cpython-38.pyc
│   │           │   │   │   │   └── unary.cpython-38.pyc
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_all.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_binary.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_product.cpython-38.pyc
│   │           │   │   │   │   │   └── test_unary.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── test_all.py
│   │           │   │   │   │   ├── test_binary.py
│   │           │   │   │   │   ├── test_product.py
│   │           │   │   │   │   └── test_unary.py
│   │           │   │   │   ├── all.py
│   │           │   │   │   ├── binary.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── product.py
│   │           │   │   │   └── unary.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── asteroidal.cpython-38.pyc
│   │           │   │   │   ├── boundary.cpython-38.pyc
│   │           │   │   │   ├── bridges.cpython-38.pyc
│   │           │   │   │   ├── chains.cpython-38.pyc
│   │           │   │   │   ├── chordal.cpython-38.pyc
│   │           │   │   │   ├── clique.cpython-38.pyc
│   │           │   │   │   ├── cluster.cpython-38.pyc
│   │           │   │   │   ├── communicability_alg.cpython-38.pyc
│   │           │   │   │   ├── core.cpython-38.pyc
│   │           │   │   │   ├── covering.cpython-38.pyc
│   │           │   │   │   ├── cuts.cpython-38.pyc
│   │           │   │   │   ├── cycles.cpython-38.pyc
│   │           │   │   │   ├── dag.cpython-38.pyc
│   │           │   │   │   ├── distance_measures.cpython-38.pyc
│   │           │   │   │   ├── distance_regular.cpython-38.pyc
│   │           │   │   │   ├── dominance.cpython-38.pyc
│   │           │   │   │   ├── dominating.cpython-38.pyc
│   │           │   │   │   ├── d_separation.cpython-38.pyc
│   │           │   │   │   ├── efficiency_measures.cpython-38.pyc
│   │           │   │   │   ├── euler.cpython-38.pyc
│   │           │   │   │   ├── graph_hashing.cpython-38.pyc
│   │           │   │   │   ├── graphical.cpython-38.pyc
│   │           │   │   │   ├── hierarchy.cpython-38.pyc
│   │           │   │   │   ├── hybrid.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── isolate.cpython-38.pyc
│   │           │   │   │   ├── link_prediction.cpython-38.pyc
│   │           │   │   │   ├── lowest_common_ancestors.cpython-38.pyc
│   │           │   │   │   ├── matching.cpython-38.pyc
│   │           │   │   │   ├── minors.cpython-38.pyc
│   │           │   │   │   ├── mis.cpython-38.pyc
│   │           │   │   │   ├── moral.cpython-38.pyc
│   │           │   │   │   ├── non_randomness.cpython-38.pyc
│   │           │   │   │   ├── planar_drawing.cpython-38.pyc
│   │           │   │   │   ├── planarity.cpython-38.pyc
│   │           │   │   │   ├── reciprocity.cpython-38.pyc
│   │           │   │   │   ├── regular.cpython-38.pyc
│   │           │   │   │   ├── richclub.cpython-38.pyc
│   │           │   │   │   ├── similarity.cpython-38.pyc
│   │           │   │   │   ├── simple_paths.cpython-38.pyc
│   │           │   │   │   ├── smallworld.cpython-38.pyc
│   │           │   │   │   ├── smetric.cpython-38.pyc
│   │           │   │   │   ├── sparsifiers.cpython-38.pyc
│   │           │   │   │   ├── structuralholes.cpython-38.pyc
│   │           │   │   │   ├── swap.cpython-38.pyc
│   │           │   │   │   ├── threshold.cpython-38.pyc
│   │           │   │   │   ├── tournament.cpython-38.pyc
│   │           │   │   │   ├── triads.cpython-38.pyc
│   │           │   │   │   ├── vitality.cpython-38.pyc
│   │           │   │   │   ├── voronoi.cpython-38.pyc
│   │           │   │   │   └── wiener.cpython-38.pyc
│   │           │   │   ├── shortest_paths
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── astar.cpython-38.pyc
│   │           │   │   │   │   ├── dense.cpython-38.pyc
│   │           │   │   │   │   ├── generic.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── unweighted.cpython-38.pyc
│   │           │   │   │   │   └── weighted.cpython-38.pyc
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_astar.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_dense.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_dense_numpy.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_generic.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_unweighted.cpython-38.pyc
│   │           │   │   │   │   │   └── test_weighted.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── test_astar.py
│   │           │   │   │   │   ├── test_dense_numpy.py
│   │           │   │   │   │   ├── test_dense.py
│   │           │   │   │   │   ├── test_generic.py
│   │           │   │   │   │   ├── test_unweighted.py
│   │           │   │   │   │   └── test_weighted.py
│   │           │   │   │   ├── astar.py
│   │           │   │   │   ├── dense.py
│   │           │   │   │   ├── generic.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── unweighted.py
│   │           │   │   │   └── weighted.py
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_asteroidal.cpython-38.pyc
│   │           │   │   │   │   ├── test_boundary.cpython-38.pyc
│   │           │   │   │   │   ├── test_bridges.cpython-38.pyc
│   │           │   │   │   │   ├── test_chains.cpython-38.pyc
│   │           │   │   │   │   ├── test_chordal.cpython-38.pyc
│   │           │   │   │   │   ├── test_clique.cpython-38.pyc
│   │           │   │   │   │   ├── test_cluster.cpython-38.pyc
│   │           │   │   │   │   ├── test_communicability.cpython-38.pyc
│   │           │   │   │   │   ├── test_core.cpython-38.pyc
│   │           │   │   │   │   ├── test_covering.cpython-38.pyc
│   │           │   │   │   │   ├── test_cuts.cpython-38.pyc
│   │           │   │   │   │   ├── test_cycles.cpython-38.pyc
│   │           │   │   │   │   ├── test_dag.cpython-38.pyc
│   │           │   │   │   │   ├── test_distance_measures.cpython-38.pyc
│   │           │   │   │   │   ├── test_distance_regular.cpython-38.pyc
│   │           │   │   │   │   ├── test_dominance.cpython-38.pyc
│   │           │   │   │   │   ├── test_dominating.cpython-38.pyc
│   │           │   │   │   │   ├── test_d_separation.cpython-38.pyc
│   │           │   │   │   │   ├── test_efficiency.cpython-38.pyc
│   │           │   │   │   │   ├── test_euler.cpython-38.pyc
│   │           │   │   │   │   ├── test_graph_hashing.cpython-38.pyc
│   │           │   │   │   │   ├── test_graphical.cpython-38.pyc
│   │           │   │   │   │   ├── test_hierarchy.cpython-38.pyc
│   │           │   │   │   │   ├── test_hybrid.cpython-38.pyc
│   │           │   │   │   │   ├── test_isolate.cpython-38.pyc
│   │           │   │   │   │   ├── test_link_prediction.cpython-38.pyc
│   │           │   │   │   │   ├── test_lowest_common_ancestors.cpython-38.pyc
│   │           │   │   │   │   ├── test_matching.cpython-38.pyc
│   │           │   │   │   │   ├── test_max_weight_clique.cpython-38.pyc
│   │           │   │   │   │   ├── test_minors.cpython-38.pyc
│   │           │   │   │   │   ├── test_mis.cpython-38.pyc
│   │           │   │   │   │   ├── test_moral.cpython-38.pyc
│   │           │   │   │   │   ├── test_non_randomness.cpython-38.pyc
│   │           │   │   │   │   ├── test_planar_drawing.cpython-38.pyc
│   │           │   │   │   │   ├── test_planarity.cpython-38.pyc
│   │           │   │   │   │   ├── test_reciprocity.cpython-38.pyc
│   │           │   │   │   │   ├── test_regular.cpython-38.pyc
│   │           │   │   │   │   ├── test_richclub.cpython-38.pyc
│   │           │   │   │   │   ├── test_similarity.cpython-38.pyc
│   │           │   │   │   │   ├── test_simple_paths.cpython-38.pyc
│   │           │   │   │   │   ├── test_smallworld.cpython-38.pyc
│   │           │   │   │   │   ├── test_smetric.cpython-38.pyc
│   │           │   │   │   │   ├── test_sparsifiers.cpython-38.pyc
│   │           │   │   │   │   ├── test_structuralholes.cpython-38.pyc
│   │           │   │   │   │   ├── test_swap.cpython-38.pyc
│   │           │   │   │   │   ├── test_threshold.cpython-38.pyc
│   │           │   │   │   │   ├── test_tournament.cpython-38.pyc
│   │           │   │   │   │   ├── test_triads.cpython-38.pyc
│   │           │   │   │   │   ├── test_vitality.cpython-38.pyc
│   │           │   │   │   │   ├── test_voronoi.cpython-38.pyc
│   │           │   │   │   │   └── test_wiener.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_asteroidal.py
│   │           │   │   │   ├── test_boundary.py
│   │           │   │   │   ├── test_bridges.py
│   │           │   │   │   ├── test_chains.py
│   │           │   │   │   ├── test_chordal.py
│   │           │   │   │   ├── test_clique.py
│   │           │   │   │   ├── test_cluster.py
│   │           │   │   │   ├── test_communicability.py
│   │           │   │   │   ├── test_core.py
│   │           │   │   │   ├── test_covering.py
│   │           │   │   │   ├── test_cuts.py
│   │           │   │   │   ├── test_cycles.py
│   │           │   │   │   ├── test_dag.py
│   │           │   │   │   ├── test_distance_measures.py
│   │           │   │   │   ├── test_distance_regular.py
│   │           │   │   │   ├── test_dominance.py
│   │           │   │   │   ├── test_dominating.py
│   │           │   │   │   ├── test_d_separation.py
│   │           │   │   │   ├── test_efficiency.py
│   │           │   │   │   ├── test_euler.py
│   │           │   │   │   ├── test_graph_hashing.py
│   │           │   │   │   ├── test_graphical.py
│   │           │   │   │   ├── test_hierarchy.py
│   │           │   │   │   ├── test_hybrid.py
│   │           │   │   │   ├── test_isolate.py
│   │           │   │   │   ├── test_link_prediction.py
│   │           │   │   │   ├── test_lowest_common_ancestors.py
│   │           │   │   │   ├── test_matching.py
│   │           │   │   │   ├── test_max_weight_clique.py
│   │           │   │   │   ├── test_minors.py
│   │           │   │   │   ├── test_mis.py
│   │           │   │   │   ├── test_moral.py
│   │           │   │   │   ├── test_non_randomness.py
│   │           │   │   │   ├── test_planar_drawing.py
│   │           │   │   │   ├── test_planarity.py
│   │           │   │   │   ├── test_reciprocity.py
│   │           │   │   │   ├── test_regular.py
│   │           │   │   │   ├── test_richclub.py
│   │           │   │   │   ├── test_similarity.py
│   │           │   │   │   ├── test_simple_paths.py
│   │           │   │   │   ├── test_smallworld.py
│   │           │   │   │   ├── test_smetric.py
│   │           │   │   │   ├── test_sparsifiers.py
│   │           │   │   │   ├── test_structuralholes.py
│   │           │   │   │   ├── test_swap.py
│   │           │   │   │   ├── test_threshold.py
│   │           │   │   │   ├── test_tournament.py
│   │           │   │   │   ├── test_triads.py
│   │           │   │   │   ├── test_vitality.py
│   │           │   │   │   ├── test_voronoi.py
│   │           │   │   │   └── test_wiener.py
│   │           │   │   ├── traversal
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── beamsearch.cpython-38.pyc
│   │           │   │   │   │   ├── breadth_first_search.cpython-38.pyc
│   │           │   │   │   │   ├── depth_first_search.cpython-38.pyc
│   │           │   │   │   │   ├── edgebfs.cpython-38.pyc
│   │           │   │   │   │   ├── edgedfs.cpython-38.pyc
│   │           │   │   │   │   └── __init__.cpython-38.pyc
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_beamsearch.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_bfs.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_dfs.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_edgebfs.cpython-38.pyc
│   │           │   │   │   │   │   └── test_edgedfs.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── test_beamsearch.py
│   │           │   │   │   │   ├── test_bfs.py
│   │           │   │   │   │   ├── test_dfs.py
│   │           │   │   │   │   ├── test_edgebfs.py
│   │           │   │   │   │   └── test_edgedfs.py
│   │           │   │   │   ├── beamsearch.py
│   │           │   │   │   ├── breadth_first_search.py
│   │           │   │   │   ├── depth_first_search.py
│   │           │   │   │   ├── edgebfs.py
│   │           │   │   │   ├── edgedfs.py
│   │           │   │   │   └── __init__.py
│   │           │   │   ├── tree
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── branchings.cpython-38.pyc
│   │           │   │   │   │   ├── coding.cpython-38.pyc
│   │           │   │   │   │   ├── decomposition.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── mst.cpython-38.pyc
│   │           │   │   │   │   ├── operations.cpython-38.pyc
│   │           │   │   │   │   └── recognition.cpython-38.pyc
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_branchings.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_coding.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_decomposition.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_mst.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_operations.cpython-38.pyc
│   │           │   │   │   │   │   └── test_recognition.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── test_branchings.py
│   │           │   │   │   │   ├── test_coding.py
│   │           │   │   │   │   ├── test_decomposition.py
│   │           │   │   │   │   ├── test_mst.py
│   │           │   │   │   │   ├── test_operations.py
│   │           │   │   │   │   └── test_recognition.py
│   │           │   │   │   ├── branchings.py
│   │           │   │   │   ├── coding.py
│   │           │   │   │   ├── decomposition.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── mst.py
│   │           │   │   │   ├── operations.py
│   │           │   │   │   └── recognition.py
│   │           │   │   ├── asteroidal.py
│   │           │   │   ├── boundary.py
│   │           │   │   ├── bridges.py
│   │           │   │   ├── chains.py
│   │           │   │   ├── chordal.py
│   │           │   │   ├── clique.py
│   │           │   │   ├── cluster.py
│   │           │   │   ├── communicability_alg.py
│   │           │   │   ├── core.py
│   │           │   │   ├── covering.py
│   │           │   │   ├── cuts.py
│   │           │   │   ├── cycles.py
│   │           │   │   ├── dag.py
│   │           │   │   ├── distance_measures.py
│   │           │   │   ├── distance_regular.py
│   │           │   │   ├── dominance.py
│   │           │   │   ├── dominating.py
│   │           │   │   ├── d_separation.py
│   │           │   │   ├── efficiency_measures.py
│   │           │   │   ├── euler.py
│   │           │   │   ├── graph_hashing.py
│   │           │   │   ├── graphical.py
│   │           │   │   ├── hierarchy.py
│   │           │   │   ├── hybrid.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── isolate.py
│   │           │   │   ├── link_prediction.py
│   │           │   │   ├── lowest_common_ancestors.py
│   │           │   │   ├── matching.py
│   │           │   │   ├── minors.py
│   │           │   │   ├── mis.py
│   │           │   │   ├── moral.py
│   │           │   │   ├── non_randomness.py
│   │           │   │   ├── planar_drawing.py
│   │           │   │   ├── planarity.py
│   │           │   │   ├── reciprocity.py
│   │           │   │   ├── regular.py
│   │           │   │   ├── richclub.py
│   │           │   │   ├── similarity.py
│   │           │   │   ├── simple_paths.py
│   │           │   │   ├── smallworld.py
│   │           │   │   ├── smetric.py
│   │           │   │   ├── sparsifiers.py
│   │           │   │   ├── structuralholes.py
│   │           │   │   ├── swap.py
│   │           │   │   ├── threshold.py
│   │           │   │   ├── tournament.py
│   │           │   │   ├── triads.py
│   │           │   │   ├── vitality.py
│   │           │   │   ├── voronoi.py
│   │           │   │   └── wiener.py
│   │           │   ├── classes
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── coreviews.cpython-38.pyc
│   │           │   │   │   ├── digraph.cpython-38.pyc
│   │           │   │   │   ├── filters.cpython-38.pyc
│   │           │   │   │   ├── function.cpython-38.pyc
│   │           │   │   │   ├── graph.cpython-38.pyc
│   │           │   │   │   ├── graphviews.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── multidigraph.cpython-38.pyc
│   │           │   │   │   ├── multigraph.cpython-38.pyc
│   │           │   │   │   ├── ordered.cpython-38.pyc
│   │           │   │   │   └── reportviews.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── historical_tests.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_coreviews.cpython-38.pyc
│   │           │   │   │   │   ├── test_digraph.cpython-38.pyc
│   │           │   │   │   │   ├── test_digraph_historical.cpython-38.pyc
│   │           │   │   │   │   ├── test_filters.cpython-38.pyc
│   │           │   │   │   │   ├── test_function.cpython-38.pyc
│   │           │   │   │   │   ├── test_graph.cpython-38.pyc
│   │           │   │   │   │   ├── test_graph_historical.cpython-38.pyc
│   │           │   │   │   │   ├── test_graphviews.cpython-38.pyc
│   │           │   │   │   │   ├── test_multidigraph.cpython-38.pyc
│   │           │   │   │   │   ├── test_multigraph.cpython-38.pyc
│   │           │   │   │   │   ├── test_ordered.cpython-38.pyc
│   │           │   │   │   │   ├── test_reportviews.cpython-38.pyc
│   │           │   │   │   │   ├── test_special.cpython-38.pyc
│   │           │   │   │   │   └── test_subgraphviews.cpython-38.pyc
│   │           │   │   │   ├── historical_tests.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_coreviews.py
│   │           │   │   │   ├── test_digraph_historical.py
│   │           │   │   │   ├── test_digraph.py
│   │           │   │   │   ├── test_filters.py
│   │           │   │   │   ├── test_function.py
│   │           │   │   │   ├── test_graph_historical.py
│   │           │   │   │   ├── test_graph.py
│   │           │   │   │   ├── test_graphviews.py
│   │           │   │   │   ├── test_multidigraph.py
│   │           │   │   │   ├── test_multigraph.py
│   │           │   │   │   ├── test_ordered.py
│   │           │   │   │   ├── test_reportviews.py
│   │           │   │   │   ├── test_special.py
│   │           │   │   │   └── test_subgraphviews.py
│   │           │   │   ├── coreviews.py
│   │           │   │   ├── digraph.py
│   │           │   │   ├── filters.py
│   │           │   │   ├── function.py
│   │           │   │   ├── graph.py
│   │           │   │   ├── graphviews.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── multidigraph.py
│   │           │   │   ├── multigraph.py
│   │           │   │   ├── ordered.py
│   │           │   │   └── reportviews.py
│   │           │   ├── drawing
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── layout.cpython-38.pyc
│   │           │   │   │   ├── nx_agraph.cpython-38.pyc
│   │           │   │   │   ├── nx_pydot.cpython-38.pyc
│   │           │   │   │   └── nx_pylab.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_agraph.cpython-38.pyc
│   │           │   │   │   │   ├── test_layout.cpython-38.pyc
│   │           │   │   │   │   ├── test_pydot.cpython-38.pyc
│   │           │   │   │   │   └── test_pylab.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_agraph.py
│   │           │   │   │   ├── test_layout.py
│   │           │   │   │   ├── test_pydot.py
│   │           │   │   │   └── test_pylab.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── layout.py
│   │           │   │   ├── nx_agraph.py
│   │           │   │   ├── nx_pydot.py
│   │           │   │   └── nx_pylab.py
│   │           │   ├── generators
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── atlas.cpython-38.pyc
│   │           │   │   │   ├── classic.cpython-38.pyc
│   │           │   │   │   ├── cographs.cpython-38.pyc
│   │           │   │   │   ├── community.cpython-38.pyc
│   │           │   │   │   ├── degree_seq.cpython-38.pyc
│   │           │   │   │   ├── directed.cpython-38.pyc
│   │           │   │   │   ├── duplication.cpython-38.pyc
│   │           │   │   │   ├── ego.cpython-38.pyc
│   │           │   │   │   ├── expanders.cpython-38.pyc
│   │           │   │   │   ├── geometric.cpython-38.pyc
│   │           │   │   │   ├── harary_graph.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── internet_as_graphs.cpython-38.pyc
│   │           │   │   │   ├── intersection.cpython-38.pyc
│   │           │   │   │   ├── interval_graph.cpython-38.pyc
│   │           │   │   │   ├── joint_degree_seq.cpython-38.pyc
│   │           │   │   │   ├── lattice.cpython-38.pyc
│   │           │   │   │   ├── line.cpython-38.pyc
│   │           │   │   │   ├── mycielski.cpython-38.pyc
│   │           │   │   │   ├── nonisomorphic_trees.cpython-38.pyc
│   │           │   │   │   ├── random_clustered.cpython-38.pyc
│   │           │   │   │   ├── random_graphs.cpython-38.pyc
│   │           │   │   │   ├── small.cpython-38.pyc
│   │           │   │   │   ├── social.cpython-38.pyc
│   │           │   │   │   ├── spectral_graph_forge.cpython-38.pyc
│   │           │   │   │   ├── stochastic.cpython-38.pyc
│   │           │   │   │   ├── sudoku.cpython-38.pyc
│   │           │   │   │   ├── trees.cpython-38.pyc
│   │           │   │   │   └── triads.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_atlas.cpython-38.pyc
│   │           │   │   │   │   ├── test_classic.cpython-38.pyc
│   │           │   │   │   │   ├── test_cographs.cpython-38.pyc
│   │           │   │   │   │   ├── test_community.cpython-38.pyc
│   │           │   │   │   │   ├── test_degree_seq.cpython-38.pyc
│   │           │   │   │   │   ├── test_directed.cpython-38.pyc
│   │           │   │   │   │   ├── test_duplication.cpython-38.pyc
│   │           │   │   │   │   ├── test_ego.cpython-38.pyc
│   │           │   │   │   │   ├── test_expanders.cpython-38.pyc
│   │           │   │   │   │   ├── test_geometric.cpython-38.pyc
│   │           │   │   │   │   ├── test_harary_graph.cpython-38.pyc
│   │           │   │   │   │   ├── test_internet_as_graphs.cpython-38.pyc
│   │           │   │   │   │   ├── test_intersection.cpython-38.pyc
│   │           │   │   │   │   ├── test_interval_graph.cpython-38.pyc
│   │           │   │   │   │   ├── test_joint_degree_seq.cpython-38.pyc
│   │           │   │   │   │   ├── test_lattice.cpython-38.pyc
│   │           │   │   │   │   ├── test_line.cpython-38.pyc
│   │           │   │   │   │   ├── test_mycielski.cpython-38.pyc
│   │           │   │   │   │   ├── test_nonisomorphic_trees.cpython-38.pyc
│   │           │   │   │   │   ├── test_random_clustered.cpython-38.pyc
│   │           │   │   │   │   ├── test_random_graphs.cpython-38.pyc
│   │           │   │   │   │   ├── test_small.cpython-38.pyc
│   │           │   │   │   │   ├── test_spectral_graph_forge.cpython-38.pyc
│   │           │   │   │   │   ├── test_stochastic.cpython-38.pyc
│   │           │   │   │   │   ├── test_sudoku.cpython-38.pyc
│   │           │   │   │   │   ├── test_trees.cpython-38.pyc
│   │           │   │   │   │   └── test_triads.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_atlas.py
│   │           │   │   │   ├── test_classic.py
│   │           │   │   │   ├── test_cographs.py
│   │           │   │   │   ├── test_community.py
│   │           │   │   │   ├── test_degree_seq.py
│   │           │   │   │   ├── test_directed.py
│   │           │   │   │   ├── test_duplication.py
│   │           │   │   │   ├── test_ego.py
│   │           │   │   │   ├── test_expanders.py
│   │           │   │   │   ├── test_geometric.py
│   │           │   │   │   ├── test_harary_graph.py
│   │           │   │   │   ├── test_internet_as_graphs.py
│   │           │   │   │   ├── test_intersection.py
│   │           │   │   │   ├── test_interval_graph.py
│   │           │   │   │   ├── test_joint_degree_seq.py
│   │           │   │   │   ├── test_lattice.py
│   │           │   │   │   ├── test_line.py
│   │           │   │   │   ├── test_mycielski.py
│   │           │   │   │   ├── test_nonisomorphic_trees.py
│   │           │   │   │   ├── test_random_clustered.py
│   │           │   │   │   ├── test_random_graphs.py
│   │           │   │   │   ├── test_small.py
│   │           │   │   │   ├── test_spectral_graph_forge.py
│   │           │   │   │   ├── test_stochastic.py
│   │           │   │   │   ├── test_sudoku.py
│   │           │   │   │   ├── test_trees.py
│   │           │   │   │   └── test_triads.py
│   │           │   │   ├── atlas.dat.gz
│   │           │   │   ├── atlas.py
│   │           │   │   ├── classic.py
│   │           │   │   ├── cographs.py
│   │           │   │   ├── community.py
│   │           │   │   ├── degree_seq.py
│   │           │   │   ├── directed.py
│   │           │   │   ├── duplication.py
│   │           │   │   ├── ego.py
│   │           │   │   ├── expanders.py
│   │           │   │   ├── geometric.py
│   │           │   │   ├── harary_graph.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── internet_as_graphs.py
│   │           │   │   ├── intersection.py
│   │           │   │   ├── interval_graph.py
│   │           │   │   ├── joint_degree_seq.py
│   │           │   │   ├── lattice.py
│   │           │   │   ├── line.py
│   │           │   │   ├── mycielski.py
│   │           │   │   ├── nonisomorphic_trees.py
│   │           │   │   ├── random_clustered.py
│   │           │   │   ├── random_graphs.py
│   │           │   │   ├── small.py
│   │           │   │   ├── social.py
│   │           │   │   ├── spectral_graph_forge.py
│   │           │   │   ├── stochastic.py
│   │           │   │   ├── sudoku.py
│   │           │   │   ├── trees.py
│   │           │   │   └── triads.py
│   │           │   ├── linalg
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── algebraicconnectivity.cpython-38.pyc
│   │           │   │   │   ├── attrmatrix.cpython-38.pyc
│   │           │   │   │   ├── bethehessianmatrix.cpython-38.pyc
│   │           │   │   │   ├── graphmatrix.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── laplacianmatrix.cpython-38.pyc
│   │           │   │   │   ├── modularitymatrix.cpython-38.pyc
│   │           │   │   │   └── spectrum.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_algebraic_connectivity.cpython-38.pyc
│   │           │   │   │   │   ├── test_attrmatrix.cpython-38.pyc
│   │           │   │   │   │   ├── test_bethehessian.cpython-38.pyc
│   │           │   │   │   │   ├── test_graphmatrix.cpython-38.pyc
│   │           │   │   │   │   ├── test_laplacian.cpython-38.pyc
│   │           │   │   │   │   ├── test_modularity.cpython-38.pyc
│   │           │   │   │   │   └── test_spectrum.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_algebraic_connectivity.py
│   │           │   │   │   ├── test_attrmatrix.py
│   │           │   │   │   ├── test_bethehessian.py
│   │           │   │   │   ├── test_graphmatrix.py
│   │           │   │   │   ├── test_laplacian.py
│   │           │   │   │   ├── test_modularity.py
│   │           │   │   │   └── test_spectrum.py
│   │           │   │   ├── algebraicconnectivity.py
│   │           │   │   ├── attrmatrix.py
│   │           │   │   ├── bethehessianmatrix.py
│   │           │   │   ├── graphmatrix.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── laplacianmatrix.py
│   │           │   │   ├── modularitymatrix.py
│   │           │   │   └── spectrum.py
│   │           │   ├── __pycache__
│   │           │   │   ├── conftest.cpython-38.pyc
│   │           │   │   ├── convert.cpython-38.pyc
│   │           │   │   ├── convert_matrix.cpython-38.pyc
│   │           │   │   ├── exception.cpython-38.pyc
│   │           │   │   ├── __init__.cpython-38.pyc
│   │           │   │   ├── relabel.cpython-38.pyc
│   │           │   │   ├── release.cpython-38.pyc
│   │           │   │   └── version.cpython-38.pyc
│   │           │   ├── readwrite
│   │           │   │   ├── json_graph
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── adjacency.cpython-38.pyc
│   │           │   │   │   │   ├── cytoscape.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── jit.cpython-38.pyc
│   │           │   │   │   │   ├── node_link.cpython-38.pyc
│   │           │   │   │   │   └── tree.cpython-38.pyc
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_adjacency.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_cytoscape.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_jit.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_node_link.cpython-38.pyc
│   │           │   │   │   │   │   └── test_tree.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── test_adjacency.py
│   │           │   │   │   │   ├── test_cytoscape.py
│   │           │   │   │   │   ├── test_jit.py
│   │           │   │   │   │   ├── test_node_link.py
│   │           │   │   │   │   └── test_tree.py
│   │           │   │   │   ├── adjacency.py
│   │           │   │   │   ├── cytoscape.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── jit.py
│   │           │   │   │   ├── node_link.py
│   │           │   │   │   └── tree.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── adjlist.cpython-38.pyc
│   │           │   │   │   ├── edgelist.cpython-38.pyc
│   │           │   │   │   ├── gexf.cpython-38.pyc
│   │           │   │   │   ├── gml.cpython-38.pyc
│   │           │   │   │   ├── gpickle.cpython-38.pyc
│   │           │   │   │   ├── graph6.cpython-38.pyc
│   │           │   │   │   ├── graphml.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── leda.cpython-38.pyc
│   │           │   │   │   ├── multiline_adjlist.cpython-38.pyc
│   │           │   │   │   ├── nx_shp.cpython-38.pyc
│   │           │   │   │   ├── nx_yaml.cpython-38.pyc
│   │           │   │   │   ├── p2g.cpython-38.pyc
│   │           │   │   │   ├── pajek.cpython-38.pyc
│   │           │   │   │   └── sparse6.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_adjlist.cpython-38.pyc
│   │           │   │   │   │   ├── test_edgelist.cpython-38.pyc
│   │           │   │   │   │   ├── test_gexf.cpython-38.pyc
│   │           │   │   │   │   ├── test_gml.cpython-38.pyc
│   │           │   │   │   │   ├── test_gpickle.cpython-38.pyc
│   │           │   │   │   │   ├── test_graph6.cpython-38.pyc
│   │           │   │   │   │   ├── test_graphml.cpython-38.pyc
│   │           │   │   │   │   ├── test_leda.cpython-38.pyc
│   │           │   │   │   │   ├── test_p2g.cpython-38.pyc
│   │           │   │   │   │   ├── test_pajek.cpython-38.pyc
│   │           │   │   │   │   ├── test_shp.cpython-38.pyc
│   │           │   │   │   │   ├── test_sparse6.cpython-38.pyc
│   │           │   │   │   │   └── test_yaml.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_adjlist.py
│   │           │   │   │   ├── test_edgelist.py
│   │           │   │   │   ├── test_gexf.py
│   │           │   │   │   ├── test_gml.py
│   │           │   │   │   ├── test_gpickle.py
│   │           │   │   │   ├── test_graph6.py
│   │           │   │   │   ├── test_graphml.py
│   │           │   │   │   ├── test_leda.py
│   │           │   │   │   ├── test_p2g.py
│   │           │   │   │   ├── test_pajek.py
│   │           │   │   │   ├── test_shp.py
│   │           │   │   │   ├── test_sparse6.py
│   │           │   │   │   └── test_yaml.py
│   │           │   │   ├── adjlist.py
│   │           │   │   ├── edgelist.py
│   │           │   │   ├── gexf.py
│   │           │   │   ├── gml.py
│   │           │   │   ├── gpickle.py
│   │           │   │   ├── graph6.py
│   │           │   │   ├── graphml.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── leda.py
│   │           │   │   ├── multiline_adjlist.py
│   │           │   │   ├── nx_shp.py
│   │           │   │   ├── nx_yaml.py
│   │           │   │   ├── p2g.py
│   │           │   │   ├── pajek.py
│   │           │   │   └── sparse6.py
│   │           │   ├── testing
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── test.cpython-38.pyc
│   │           │   │   │   └── utils.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   └── test_utils.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── test_utils.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── test.py
│   │           │   │   └── utils.py
│   │           │   ├── tests
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── test_all_random_functions.cpython-38.pyc
│   │           │   │   │   ├── test_convert.cpython-38.pyc
│   │           │   │   │   ├── test_convert_numpy.cpython-38.pyc
│   │           │   │   │   ├── test_convert_pandas.cpython-38.pyc
│   │           │   │   │   ├── test_convert_scipy.cpython-38.pyc
│   │           │   │   │   ├── test_exceptions.cpython-38.pyc
│   │           │   │   │   └── test_relabel.cpython-38.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── test_all_random_functions.py
│   │           │   │   ├── test_convert_numpy.py
│   │           │   │   ├── test_convert_pandas.py
│   │           │   │   ├── test_convert.py
│   │           │   │   ├── test_convert_scipy.py
│   │           │   │   ├── test_exceptions.py
│   │           │   │   └── test_relabel.py
│   │           │   ├── utils
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── contextmanagers.cpython-38.pyc
│   │           │   │   │   ├── decorators.cpython-38.pyc
│   │           │   │   │   ├── heaps.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── mapped_queue.cpython-38.pyc
│   │           │   │   │   ├── misc.cpython-38.pyc
│   │           │   │   │   ├── random_sequence.cpython-38.pyc
│   │           │   │   │   ├── rcm.cpython-38.pyc
│   │           │   │   │   └── union_find.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_contextmanager.cpython-38.pyc
│   │           │   │   │   │   ├── test_decorators.cpython-38.pyc
│   │           │   │   │   │   ├── test_heaps.cpython-38.pyc
│   │           │   │   │   │   ├── test_mapped_queue.cpython-38.pyc
│   │           │   │   │   │   ├── test_misc.cpython-38.pyc
│   │           │   │   │   │   ├── test_random_sequence.cpython-38.pyc
│   │           │   │   │   │   ├── test_rcm.cpython-38.pyc
│   │           │   │   │   │   └── test_unionfind.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_contextmanager.py
│   │           │   │   │   ├── test_decorators.py
│   │           │   │   │   ├── test_heaps.py
│   │           │   │   │   ├── test_mapped_queue.py
│   │           │   │   │   ├── test_misc.py
│   │           │   │   │   ├── test_random_sequence.py
│   │           │   │   │   ├── test_rcm.py
│   │           │   │   │   └── test_unionfind.py
│   │           │   │   ├── contextmanagers.py
│   │           │   │   ├── decorators.py
│   │           │   │   ├── heaps.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── mapped_queue.py
│   │           │   │   ├── misc.py
│   │           │   │   ├── random_sequence.py
│   │           │   │   ├── rcm.py
│   │           │   │   └── union_find.py
│   │           │   ├── conftest.py
│   │           │   ├── convert_matrix.py
│   │           │   ├── convert.py
│   │           │   ├── exception.py
│   │           │   ├── __init__.py
│   │           │   ├── relabel.py
│   │           │   ├── release.py
│   │           │   └── version.py
│   │           ├── networkx-2.5.1.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE.txt
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── numpy
│   │           │   ├── compat
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── _inspect.cpython-38.pyc
│   │           │   │   │   ├── py3k.cpython-38.pyc
│   │           │   │   │   └── setup.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   └── test_compat.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── test_compat.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _inspect.py
│   │           │   │   ├── py3k.py
│   │           │   │   └── setup.py
│   │           │   ├── core
│   │           │   │   ├── include
│   │           │   │   │   └── numpy
│   │           │   │   │       ├── random
│   │           │   │   │       │   ├── bitgen.h
│   │           │   │   │       │   └── distributions.h
│   │           │   │   │       ├── arrayobject.h
│   │           │   │   │       ├── arrayscalars.h
│   │           │   │   │       ├── halffloat.h
│   │           │   │   │       ├── __multiarray_api.h
│   │           │   │   │       ├── multiarray_api.txt
│   │           │   │   │       ├── ndarrayobject.h
│   │           │   │   │       ├── ndarraytypes.h
│   │           │   │   │       ├── _neighborhood_iterator_imp.h
│   │           │   │   │       ├── noprefix.h
│   │           │   │   │       ├── npy_1_7_deprecated_api.h
│   │           │   │   │       ├── npy_3kcompat.h
│   │           │   │   │       ├── npy_common.h
│   │           │   │   │       ├── npy_cpu.h
│   │           │   │   │       ├── npy_endian.h
│   │           │   │   │       ├── npy_interrupt.h
│   │           │   │   │       ├── npy_math.h
│   │           │   │   │       ├── npy_no_deprecated_api.h
│   │           │   │   │       ├── npy_os.h
│   │           │   │   │       ├── _numpyconfig.h
│   │           │   │   │       ├── numpyconfig.h
│   │           │   │   │       ├── old_defines.h
│   │           │   │   │       ├── oldnumeric.h
│   │           │   │   │       ├── __ufunc_api.h
│   │           │   │   │       ├── ufunc_api.txt
│   │           │   │   │       ├── ufuncobject.h
│   │           │   │   │       └── utils.h
│   │           │   │   ├── lib
│   │           │   │   │   ├── npy-pkg-config
│   │           │   │   │   │   ├── mlib.ini
│   │           │   │   │   │   └── npymath.ini
│   │           │   │   │   └── libnpymath.a
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── _add_newdocs.cpython-38.pyc
│   │           │   │   │   ├── _add_newdocs_scalars.cpython-38.pyc
│   │           │   │   │   ├── arrayprint.cpython-38.pyc
│   │           │   │   │   ├── _asarray.cpython-38.pyc
│   │           │   │   │   ├── cversions.cpython-38.pyc
│   │           │   │   │   ├── defchararray.cpython-38.pyc
│   │           │   │   │   ├── _dtype.cpython-38.pyc
│   │           │   │   │   ├── _dtype_ctypes.cpython-38.pyc
│   │           │   │   │   ├── einsumfunc.cpython-38.pyc
│   │           │   │   │   ├── _exceptions.cpython-38.pyc
│   │           │   │   │   ├── fromnumeric.cpython-38.pyc
│   │           │   │   │   ├── function_base.cpython-38.pyc
│   │           │   │   │   ├── generate_numpy_api.cpython-38.pyc
│   │           │   │   │   ├── getlimits.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── _internal.cpython-38.pyc
│   │           │   │   │   ├── machar.cpython-38.pyc
│   │           │   │   │   ├── memmap.cpython-38.pyc
│   │           │   │   │   ├── _methods.cpython-38.pyc
│   │           │   │   │   ├── multiarray.cpython-38.pyc
│   │           │   │   │   ├── numeric.cpython-38.pyc
│   │           │   │   │   ├── numerictypes.cpython-38.pyc
│   │           │   │   │   ├── overrides.cpython-38.pyc
│   │           │   │   │   ├── records.cpython-38.pyc
│   │           │   │   │   ├── setup_common.cpython-38.pyc
│   │           │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   ├── shape_base.cpython-38.pyc
│   │           │   │   │   ├── _string_helpers.cpython-38.pyc
│   │           │   │   │   ├── _type_aliases.cpython-38.pyc
│   │           │   │   │   ├── _ufunc_config.cpython-38.pyc
│   │           │   │   │   ├── umath.cpython-38.pyc
│   │           │   │   │   └── umath_tests.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── data
│   │           │   │   │   │   ├── astype_copy.pkl
│   │           │   │   │   │   ├── recarray_from_file.fits
│   │           │   │   │   │   ├── umath-validation-set-cos
│   │           │   │   │   │   ├── umath-validation-set-exp
│   │           │   │   │   │   ├── umath-validation-set-log
│   │           │   │   │   │   ├── umath-validation-set-README
│   │           │   │   │   │   └── umath-validation-set-sin
│   │           │   │   │   ├── examples
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   └── setup.cpython-38.pyc
│   │           │   │   │   │   ├── checks.pyx
│   │           │   │   │   │   └── setup.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── _locales.cpython-38.pyc
│   │           │   │   │   │   ├── test_abc.cpython-38.pyc
│   │           │   │   │   │   ├── test_api.cpython-38.pyc
│   │           │   │   │   │   ├── test_array_coercion.cpython-38.pyc
│   │           │   │   │   │   ├── test_arrayprint.cpython-38.pyc
│   │           │   │   │   │   ├── test_casting_unittests.cpython-38.pyc
│   │           │   │   │   │   ├── test_conversion_utils.cpython-38.pyc
│   │           │   │   │   │   ├── test_cpu_dispatcher.cpython-38.pyc
│   │           │   │   │   │   ├── test_cpu_features.cpython-38.pyc
│   │           │   │   │   │   ├── test_cython.cpython-38.pyc
│   │           │   │   │   │   ├── test_datetime.cpython-38.pyc
│   │           │   │   │   │   ├── test_defchararray.cpython-38.pyc
│   │           │   │   │   │   ├── test_deprecations.cpython-38.pyc
│   │           │   │   │   │   ├── test_dtype.cpython-38.pyc
│   │           │   │   │   │   ├── test_einsum.cpython-38.pyc
│   │           │   │   │   │   ├── test_errstate.cpython-38.pyc
│   │           │   │   │   │   ├── test__exceptions.cpython-38.pyc
│   │           │   │   │   │   ├── test_extint128.cpython-38.pyc
│   │           │   │   │   │   ├── test_function_base.cpython-38.pyc
│   │           │   │   │   │   ├── test_getlimits.cpython-38.pyc
│   │           │   │   │   │   ├── test_half.cpython-38.pyc
│   │           │   │   │   │   ├── test_indexerrors.cpython-38.pyc
│   │           │   │   │   │   ├── test_indexing.cpython-38.pyc
│   │           │   │   │   │   ├── test_item_selection.cpython-38.pyc
│   │           │   │   │   │   ├── test_longdouble.cpython-38.pyc
│   │           │   │   │   │   ├── test_machar.cpython-38.pyc
│   │           │   │   │   │   ├── test_memmap.cpython-38.pyc
│   │           │   │   │   │   ├── test_mem_overlap.cpython-38.pyc
│   │           │   │   │   │   ├── test_multiarray.cpython-38.pyc
│   │           │   │   │   │   ├── test_nditer.cpython-38.pyc
│   │           │   │   │   │   ├── test_numeric.cpython-38.pyc
│   │           │   │   │   │   ├── test_numerictypes.cpython-38.pyc
│   │           │   │   │   │   ├── test_overrides.cpython-38.pyc
│   │           │   │   │   │   ├── test_print.cpython-38.pyc
│   │           │   │   │   │   ├── test_protocols.cpython-38.pyc
│   │           │   │   │   │   ├── test_records.cpython-38.pyc
│   │           │   │   │   │   ├── test_regression.cpython-38.pyc
│   │           │   │   │   │   ├── test_scalarbuffer.cpython-38.pyc
│   │           │   │   │   │   ├── test_scalar_ctors.cpython-38.pyc
│   │           │   │   │   │   ├── test_scalarinherit.cpython-38.pyc
│   │           │   │   │   │   ├── test_scalarmath.cpython-38.pyc
│   │           │   │   │   │   ├── test_scalar_methods.cpython-38.pyc
│   │           │   │   │   │   ├── test_scalarprint.cpython-38.pyc
│   │           │   │   │   │   ├── test_shape_base.cpython-38.pyc
│   │           │   │   │   │   ├── test_simd.cpython-38.pyc
│   │           │   │   │   │   ├── test_simd_module.cpython-38.pyc
│   │           │   │   │   │   ├── test_ufunc.cpython-38.pyc
│   │           │   │   │   │   ├── test_umath_accuracy.cpython-38.pyc
│   │           │   │   │   │   ├── test_umath_complex.cpython-38.pyc
│   │           │   │   │   │   ├── test_umath.cpython-38.pyc
│   │           │   │   │   │   └── test_unicode.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _locales.py
│   │           │   │   │   ├── test_abc.py
│   │           │   │   │   ├── test_api.py
│   │           │   │   │   ├── test_array_coercion.py
│   │           │   │   │   ├── test_arrayprint.py
│   │           │   │   │   ├── test_casting_unittests.py
│   │           │   │   │   ├── test_conversion_utils.py
│   │           │   │   │   ├── test_cpu_dispatcher.py
│   │           │   │   │   ├── test_cpu_features.py
│   │           │   │   │   ├── test_cython.py
│   │           │   │   │   ├── test_datetime.py
│   │           │   │   │   ├── test_defchararray.py
│   │           │   │   │   ├── test_deprecations.py
│   │           │   │   │   ├── test_dtype.py
│   │           │   │   │   ├── test_einsum.py
│   │           │   │   │   ├── test_errstate.py
│   │           │   │   │   ├── test__exceptions.py
│   │           │   │   │   ├── test_extint128.py
│   │           │   │   │   ├── test_function_base.py
│   │           │   │   │   ├── test_getlimits.py
│   │           │   │   │   ├── test_half.py
│   │           │   │   │   ├── test_indexerrors.py
│   │           │   │   │   ├── test_indexing.py
│   │           │   │   │   ├── test_item_selection.py
│   │           │   │   │   ├── test_longdouble.py
│   │           │   │   │   ├── test_machar.py
│   │           │   │   │   ├── test_memmap.py
│   │           │   │   │   ├── test_mem_overlap.py
│   │           │   │   │   ├── test_multiarray.py
│   │           │   │   │   ├── test_nditer.py
│   │           │   │   │   ├── test_numeric.py
│   │           │   │   │   ├── test_numerictypes.py
│   │           │   │   │   ├── test_overrides.py
│   │           │   │   │   ├── test_print.py
│   │           │   │   │   ├── test_protocols.py
│   │           │   │   │   ├── test_records.py
│   │           │   │   │   ├── test_regression.py
│   │           │   │   │   ├── test_scalarbuffer.py
│   │           │   │   │   ├── test_scalar_ctors.py
│   │           │   │   │   ├── test_scalarinherit.py
│   │           │   │   │   ├── test_scalarmath.py
│   │           │   │   │   ├── test_scalar_methods.py
│   │           │   │   │   ├── test_scalarprint.py
│   │           │   │   │   ├── test_shape_base.py
│   │           │   │   │   ├── test_simd_module.py
│   │           │   │   │   ├── test_simd.py
│   │           │   │   │   ├── test_ufunc.py
│   │           │   │   │   ├── test_umath_accuracy.py
│   │           │   │   │   ├── test_umath_complex.py
│   │           │   │   │   ├── test_umath.py
│   │           │   │   │   └── test_unicode.py
│   │           │   │   ├── _add_newdocs.py
│   │           │   │   ├── _add_newdocs_scalars.py
│   │           │   │   ├── arrayprint.py
│   │           │   │   ├── _asarray.py
│   │           │   │   ├── _asarray.pyi
│   │           │   │   ├── cversions.py
│   │           │   │   ├── defchararray.py
│   │           │   │   ├── _dtype_ctypes.py
│   │           │   │   ├── _dtype.py
│   │           │   │   ├── einsumfunc.py
│   │           │   │   ├── _exceptions.py
│   │           │   │   ├── fromnumeric.py
│   │           │   │   ├── fromnumeric.pyi
│   │           │   │   ├── function_base.py
│   │           │   │   ├── function_base.pyi
│   │           │   │   ├── generate_numpy_api.py
│   │           │   │   ├── getlimits.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __init__.pyi
│   │           │   │   ├── _internal.py
│   │           │   │   ├── _internal.pyi
│   │           │   │   ├── machar.py
│   │           │   │   ├── memmap.py
│   │           │   │   ├── _methods.py
│   │           │   │   ├── multiarray.py
│   │           │   │   ├── _multiarray_tests.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _multiarray_umath.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── numeric.py
│   │           │   │   ├── numeric.pyi
│   │           │   │   ├── numerictypes.py
│   │           │   │   ├── numerictypes.pyi
│   │           │   │   ├── _operand_flag_tests.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── overrides.py
│   │           │   │   ├── _rational_tests.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── records.py
│   │           │   │   ├── setup_common.py
│   │           │   │   ├── setup.py
│   │           │   │   ├── shape_base.py
│   │           │   │   ├── shape_base.pyi
│   │           │   │   ├── _simd.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _string_helpers.py
│   │           │   │   ├── _struct_ufunc_tests.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _type_aliases.py
│   │           │   │   ├── _type_aliases.pyi
│   │           │   │   ├── _ufunc_config.py
│   │           │   │   ├── _ufunc_config.pyi
│   │           │   │   ├── umath.py
│   │           │   │   ├── _umath_tests.cpython-38-x86_64-linux-gnu.so
│   │           │   │   └── umath_tests.py
│   │           │   ├── distutils
│   │           │   │   ├── checks
│   │           │   │   │   ├── cpu_asimd.c
│   │           │   │   │   ├── cpu_asimddp.c
│   │           │   │   │   ├── cpu_asimdfhm.c
│   │           │   │   │   ├── cpu_asimdhp.c
│   │           │   │   │   ├── cpu_avx2.c
│   │           │   │   │   ├── cpu_avx512cd.c
│   │           │   │   │   ├── cpu_avx512_clx.c
│   │           │   │   │   ├── cpu_avx512_cnl.c
│   │           │   │   │   ├── cpu_avx512f.c
│   │           │   │   │   ├── cpu_avx512_icl.c
│   │           │   │   │   ├── cpu_avx512_knl.c
│   │           │   │   │   ├── cpu_avx512_knm.c
│   │           │   │   │   ├── cpu_avx512_skx.c
│   │           │   │   │   ├── cpu_avx.c
│   │           │   │   │   ├── cpu_f16c.c
│   │           │   │   │   ├── cpu_fma3.c
│   │           │   │   │   ├── cpu_fma4.c
│   │           │   │   │   ├── cpu_neon.c
│   │           │   │   │   ├── cpu_neon_fp16.c
│   │           │   │   │   ├── cpu_neon_vfpv4.c
│   │           │   │   │   ├── cpu_popcnt.c
│   │           │   │   │   ├── cpu_sse2.c
│   │           │   │   │   ├── cpu_sse3.c
│   │           │   │   │   ├── cpu_sse41.c
│   │           │   │   │   ├── cpu_sse42.c
│   │           │   │   │   ├── cpu_sse.c
│   │           │   │   │   ├── cpu_ssse3.c
│   │           │   │   │   ├── cpu_vsx2.c
│   │           │   │   │   ├── cpu_vsx3.c
│   │           │   │   │   ├── cpu_vsx.c
│   │           │   │   │   ├── cpu_xop.c
│   │           │   │   │   ├── extra_avx512bw_mask.c
│   │           │   │   │   ├── extra_avx512dq_mask.c
│   │           │   │   │   ├── extra_avx512f_reduce.c
│   │           │   │   │   └── test_flags.c
│   │           │   │   ├── command
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── autodist.cpython-38.pyc
│   │           │   │   │   │   ├── bdist_rpm.cpython-38.pyc
│   │           │   │   │   │   ├── build_clib.cpython-38.pyc
│   │           │   │   │   │   ├── build.cpython-38.pyc
│   │           │   │   │   │   ├── build_ext.cpython-38.pyc
│   │           │   │   │   │   ├── build_py.cpython-38.pyc
│   │           │   │   │   │   ├── build_scripts.cpython-38.pyc
│   │           │   │   │   │   ├── build_src.cpython-38.pyc
│   │           │   │   │   │   ├── config_compiler.cpython-38.pyc
│   │           │   │   │   │   ├── config.cpython-38.pyc
│   │           │   │   │   │   ├── develop.cpython-38.pyc
│   │           │   │   │   │   ├── egg_info.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── install_clib.cpython-38.pyc
│   │           │   │   │   │   ├── install.cpython-38.pyc
│   │           │   │   │   │   ├── install_data.cpython-38.pyc
│   │           │   │   │   │   ├── install_headers.cpython-38.pyc
│   │           │   │   │   │   └── sdist.cpython-38.pyc
│   │           │   │   │   ├── autodist.py
│   │           │   │   │   ├── bdist_rpm.py
│   │           │   │   │   ├── build_clib.py
│   │           │   │   │   ├── build_ext.py
│   │           │   │   │   ├── build.py
│   │           │   │   │   ├── build_py.py
│   │           │   │   │   ├── build_scripts.py
│   │           │   │   │   ├── build_src.py
│   │           │   │   │   ├── config_compiler.py
│   │           │   │   │   ├── config.py
│   │           │   │   │   ├── develop.py
│   │           │   │   │   ├── egg_info.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── install_clib.py
│   │           │   │   │   ├── install_data.py
│   │           │   │   │   ├── install_headers.py
│   │           │   │   │   ├── install.py
│   │           │   │   │   └── sdist.py
│   │           │   │   ├── fcompiler
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── absoft.cpython-38.pyc
│   │           │   │   │   │   ├── compaq.cpython-38.pyc
│   │           │   │   │   │   ├── environment.cpython-38.pyc
│   │           │   │   │   │   ├── fujitsu.cpython-38.pyc
│   │           │   │   │   │   ├── g95.cpython-38.pyc
│   │           │   │   │   │   ├── gnu.cpython-38.pyc
│   │           │   │   │   │   ├── hpux.cpython-38.pyc
│   │           │   │   │   │   ├── ibm.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── intel.cpython-38.pyc
│   │           │   │   │   │   ├── lahey.cpython-38.pyc
│   │           │   │   │   │   ├── mips.cpython-38.pyc
│   │           │   │   │   │   ├── nag.cpython-38.pyc
│   │           │   │   │   │   ├── none.cpython-38.pyc
│   │           │   │   │   │   ├── nv.cpython-38.pyc
│   │           │   │   │   │   ├── pathf95.cpython-38.pyc
│   │           │   │   │   │   ├── pg.cpython-38.pyc
│   │           │   │   │   │   ├── sun.cpython-38.pyc
│   │           │   │   │   │   └── vast.cpython-38.pyc
│   │           │   │   │   ├── absoft.py
│   │           │   │   │   ├── compaq.py
│   │           │   │   │   ├── environment.py
│   │           │   │   │   ├── fujitsu.py
│   │           │   │   │   ├── g95.py
│   │           │   │   │   ├── gnu.py
│   │           │   │   │   ├── hpux.py
│   │           │   │   │   ├── ibm.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── intel.py
│   │           │   │   │   ├── lahey.py
│   │           │   │   │   ├── mips.py
│   │           │   │   │   ├── nag.py
│   │           │   │   │   ├── none.py
│   │           │   │   │   ├── nv.py
│   │           │   │   │   ├── pathf95.py
│   │           │   │   │   ├── pg.py
│   │           │   │   │   ├── sun.py
│   │           │   │   │   └── vast.py
│   │           │   │   ├── mingw
│   │           │   │   │   └── gfortran_vs2003_hack.c
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── ccompiler.cpython-38.pyc
│   │           │   │   │   ├── ccompiler_opt.cpython-38.pyc
│   │           │   │   │   ├── __config__.cpython-38.pyc
│   │           │   │   │   ├── conv_template.cpython-38.pyc
│   │           │   │   │   ├── core.cpython-38.pyc
│   │           │   │   │   ├── cpuinfo.cpython-38.pyc
│   │           │   │   │   ├── exec_command.cpython-38.pyc
│   │           │   │   │   ├── extension.cpython-38.pyc
│   │           │   │   │   ├── from_template.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── intelccompiler.cpython-38.pyc
│   │           │   │   │   ├── lib2def.cpython-38.pyc
│   │           │   │   │   ├── line_endings.cpython-38.pyc
│   │           │   │   │   ├── log.cpython-38.pyc
│   │           │   │   │   ├── mingw32ccompiler.cpython-38.pyc
│   │           │   │   │   ├── misc_util.cpython-38.pyc
│   │           │   │   │   ├── msvc9compiler.cpython-38.pyc
│   │           │   │   │   ├── msvccompiler.cpython-38.pyc
│   │           │   │   │   ├── npy_pkg_config.cpython-38.pyc
│   │           │   │   │   ├── numpy_distribution.cpython-38.pyc
│   │           │   │   │   ├── pathccompiler.cpython-38.pyc
│   │           │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   ├── _shell_utils.cpython-38.pyc
│   │           │   │   │   ├── system_info.cpython-38.pyc
│   │           │   │   │   └── unixccompiler.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_build_ext.cpython-38.pyc
│   │           │   │   │   │   ├── test_ccompiler_opt_conf.cpython-38.pyc
│   │           │   │   │   │   ├── test_ccompiler_opt.cpython-38.pyc
│   │           │   │   │   │   ├── test_exec_command.cpython-38.pyc
│   │           │   │   │   │   ├── test_fcompiler.cpython-38.pyc
│   │           │   │   │   │   ├── test_fcompiler_gnu.cpython-38.pyc
│   │           │   │   │   │   ├── test_fcompiler_intel.cpython-38.pyc
│   │           │   │   │   │   ├── test_fcompiler_nagfor.cpython-38.pyc
│   │           │   │   │   │   ├── test_from_template.cpython-38.pyc
│   │           │   │   │   │   ├── test_mingw32ccompiler.cpython-38.pyc
│   │           │   │   │   │   ├── test_misc_util.cpython-38.pyc
│   │           │   │   │   │   ├── test_npy_pkg_config.cpython-38.pyc
│   │           │   │   │   │   ├── test_shell_utils.cpython-38.pyc
│   │           │   │   │   │   └── test_system_info.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_build_ext.py
│   │           │   │   │   ├── test_ccompiler_opt_conf.py
│   │           │   │   │   ├── test_ccompiler_opt.py
│   │           │   │   │   ├── test_exec_command.py
│   │           │   │   │   ├── test_fcompiler_gnu.py
│   │           │   │   │   ├── test_fcompiler_intel.py
│   │           │   │   │   ├── test_fcompiler_nagfor.py
│   │           │   │   │   ├── test_fcompiler.py
│   │           │   │   │   ├── test_from_template.py
│   │           │   │   │   ├── test_mingw32ccompiler.py
│   │           │   │   │   ├── test_misc_util.py
│   │           │   │   │   ├── test_npy_pkg_config.py
│   │           │   │   │   ├── test_shell_utils.py
│   │           │   │   │   └── test_system_info.py
│   │           │   │   ├── ccompiler_opt.py
│   │           │   │   ├── ccompiler.py
│   │           │   │   ├── __config__.py
│   │           │   │   ├── conv_template.py
│   │           │   │   ├── core.py
│   │           │   │   ├── cpuinfo.py
│   │           │   │   ├── exec_command.py
│   │           │   │   ├── extension.py
│   │           │   │   ├── from_template.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __init__.pyi
│   │           │   │   ├── intelccompiler.py
│   │           │   │   ├── lib2def.py
│   │           │   │   ├── line_endings.py
│   │           │   │   ├── log.py
│   │           │   │   ├── mingw32ccompiler.py
│   │           │   │   ├── misc_util.py
│   │           │   │   ├── msvc9compiler.py
│   │           │   │   ├── msvccompiler.py
│   │           │   │   ├── npy_pkg_config.py
│   │           │   │   ├── numpy_distribution.py
│   │           │   │   ├── pathccompiler.py
│   │           │   │   ├── setup.py
│   │           │   │   ├── _shell_utils.py
│   │           │   │   ├── system_info.py
│   │           │   │   └── unixccompiler.py
│   │           │   ├── doc
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── constants.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   └── ufuncs.cpython-38.pyc
│   │           │   │   ├── constants.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── ufuncs.py
│   │           │   ├── f2py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── auxfuncs.cpython-38.pyc
│   │           │   │   │   ├── capi_maps.cpython-38.pyc
│   │           │   │   │   ├── cb_rules.cpython-38.pyc
│   │           │   │   │   ├── cfuncs.cpython-38.pyc
│   │           │   │   │   ├── common_rules.cpython-38.pyc
│   │           │   │   │   ├── crackfortran.cpython-38.pyc
│   │           │   │   │   ├── diagnose.cpython-38.pyc
│   │           │   │   │   ├── f2py2e.cpython-38.pyc
│   │           │   │   │   ├── f2py_testing.cpython-38.pyc
│   │           │   │   │   ├── f90mod_rules.cpython-38.pyc
│   │           │   │   │   ├── func2subr.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── __main__.cpython-38.pyc
│   │           │   │   │   ├── rules.cpython-38.pyc
│   │           │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   ├── use_rules.cpython-38.pyc
│   │           │   │   │   └── __version__.cpython-38.pyc
│   │           │   │   ├── src
│   │           │   │   │   ├── fortranobject.c
│   │           │   │   │   └── fortranobject.h
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_array_from_pyobj.cpython-38.pyc
│   │           │   │   │   │   ├── test_assumed_shape.cpython-38.pyc
│   │           │   │   │   │   ├── test_block_docstring.cpython-38.pyc
│   │           │   │   │   │   ├── test_callback.cpython-38.pyc
│   │           │   │   │   │   ├── test_common.cpython-38.pyc
│   │           │   │   │   │   ├── test_compile_function.cpython-38.pyc
│   │           │   │   │   │   ├── test_crackfortran.cpython-38.pyc
│   │           │   │   │   │   ├── test_kind.cpython-38.pyc
│   │           │   │   │   │   ├── test_mixed.cpython-38.pyc
│   │           │   │   │   │   ├── test_module_doc.cpython-38.pyc
│   │           │   │   │   │   ├── test_parameter.cpython-38.pyc
│   │           │   │   │   │   ├── test_quoted_character.cpython-38.pyc
│   │           │   │   │   │   ├── test_regression.cpython-38.pyc
│   │           │   │   │   │   ├── test_return_character.cpython-38.pyc
│   │           │   │   │   │   ├── test_return_complex.cpython-38.pyc
│   │           │   │   │   │   ├── test_return_integer.cpython-38.pyc
│   │           │   │   │   │   ├── test_return_logical.cpython-38.pyc
│   │           │   │   │   │   ├── test_return_real.cpython-38.pyc
│   │           │   │   │   │   ├── test_semicolon_split.cpython-38.pyc
│   │           │   │   │   │   ├── test_size.cpython-38.pyc
│   │           │   │   │   │   ├── test_string.cpython-38.pyc
│   │           │   │   │   │   └── util.cpython-38.pyc
│   │           │   │   │   ├── src
│   │           │   │   │   │   ├── array_from_pyobj
│   │           │   │   │   │   │   └── wrapmodule.c
│   │           │   │   │   │   ├── assumed_shape
│   │           │   │   │   │   │   ├── foo_free.f90
│   │           │   │   │   │   │   ├── foo_mod.f90
│   │           │   │   │   │   │   ├── foo_use.f90
│   │           │   │   │   │   │   └── precision.f90
│   │           │   │   │   │   ├── common
│   │           │   │   │   │   │   └── block.f
│   │           │   │   │   │   ├── kind
│   │           │   │   │   │   │   └── foo.f90
│   │           │   │   │   │   ├── mixed
│   │           │   │   │   │   │   ├── foo.f
│   │           │   │   │   │   │   ├── foo_fixed.f90
│   │           │   │   │   │   │   └── foo_free.f90
│   │           │   │   │   │   ├── module_data
│   │           │   │   │   │   │   ├── mod.mod
│   │           │   │   │   │   │   └── module_data_docstring.f90
│   │           │   │   │   │   ├── parameter
│   │           │   │   │   │   │   ├── constant_both.f90
│   │           │   │   │   │   │   ├── constant_compound.f90
│   │           │   │   │   │   │   ├── constant_integer.f90
│   │           │   │   │   │   │   ├── constant_non_compound.f90
│   │           │   │   │   │   │   └── constant_real.f90
│   │           │   │   │   │   ├── regression
│   │           │   │   │   │   │   └── inout.f90
│   │           │   │   │   │   ├── size
│   │           │   │   │   │   │   └── foo.f90
│   │           │   │   │   │   └── string
│   │           │   │   │   │       └── char.f90
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_array_from_pyobj.py
│   │           │   │   │   ├── test_assumed_shape.py
│   │           │   │   │   ├── test_block_docstring.py
│   │           │   │   │   ├── test_callback.py
│   │           │   │   │   ├── test_common.py
│   │           │   │   │   ├── test_compile_function.py
│   │           │   │   │   ├── test_crackfortran.py
│   │           │   │   │   ├── test_kind.py
│   │           │   │   │   ├── test_mixed.py
│   │           │   │   │   ├── test_module_doc.py
│   │           │   │   │   ├── test_parameter.py
│   │           │   │   │   ├── test_quoted_character.py
│   │           │   │   │   ├── test_regression.py
│   │           │   │   │   ├── test_return_character.py
│   │           │   │   │   ├── test_return_complex.py
│   │           │   │   │   ├── test_return_integer.py
│   │           │   │   │   ├── test_return_logical.py
│   │           │   │   │   ├── test_return_real.py
│   │           │   │   │   ├── test_semicolon_split.py
│   │           │   │   │   ├── test_size.py
│   │           │   │   │   ├── test_string.py
│   │           │   │   │   └── util.py
│   │           │   │   ├── auxfuncs.py
│   │           │   │   ├── capi_maps.py
│   │           │   │   ├── cb_rules.py
│   │           │   │   ├── cfuncs.py
│   │           │   │   ├── common_rules.py
│   │           │   │   ├── crackfortran.py
│   │           │   │   ├── diagnose.py
│   │           │   │   ├── f2py2e.py
│   │           │   │   ├── f2py_testing.py
│   │           │   │   ├── f90mod_rules.py
│   │           │   │   ├── func2subr.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __init__.pyi
│   │           │   │   ├── __main__.py
│   │           │   │   ├── rules.py
│   │           │   │   ├── setup.py
│   │           │   │   ├── use_rules.py
│   │           │   │   └── __version__.py
│   │           │   ├── fft
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── helper.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── _pocketfft.cpython-38.pyc
│   │           │   │   │   └── setup.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_helper.cpython-38.pyc
│   │           │   │   │   │   └── test_pocketfft.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_helper.py
│   │           │   │   │   └── test_pocketfft.py
│   │           │   │   ├── helper.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __init__.pyi
│   │           │   │   ├── _pocketfft_internal.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _pocketfft.py
│   │           │   │   └── setup.py
│   │           │   ├── lib
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── arraypad.cpython-38.pyc
│   │           │   │   │   ├── arraysetops.cpython-38.pyc
│   │           │   │   │   ├── arrayterator.cpython-38.pyc
│   │           │   │   │   ├── _datasource.cpython-38.pyc
│   │           │   │   │   ├── format.cpython-38.pyc
│   │           │   │   │   ├── function_base.cpython-38.pyc
│   │           │   │   │   ├── histograms.cpython-38.pyc
│   │           │   │   │   ├── index_tricks.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── _iotools.cpython-38.pyc
│   │           │   │   │   ├── mixins.cpython-38.pyc
│   │           │   │   │   ├── nanfunctions.cpython-38.pyc
│   │           │   │   │   ├── npyio.cpython-38.pyc
│   │           │   │   │   ├── polynomial.cpython-38.pyc
│   │           │   │   │   ├── recfunctions.cpython-38.pyc
│   │           │   │   │   ├── scimath.cpython-38.pyc
│   │           │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   ├── shape_base.cpython-38.pyc
│   │           │   │   │   ├── stride_tricks.cpython-38.pyc
│   │           │   │   │   ├── twodim_base.cpython-38.pyc
│   │           │   │   │   ├── type_check.cpython-38.pyc
│   │           │   │   │   ├── ufunclike.cpython-38.pyc
│   │           │   │   │   ├── user_array.cpython-38.pyc
│   │           │   │   │   ├── utils.cpython-38.pyc
│   │           │   │   │   └── _version.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── data
│   │           │   │   │   │   ├── py2-objarr.npy
│   │           │   │   │   │   ├── py2-objarr.npz
│   │           │   │   │   │   ├── py3-objarr.npy
│   │           │   │   │   │   ├── py3-objarr.npz
│   │           │   │   │   │   ├── python3.npy
│   │           │   │   │   │   └── win64python2.npy
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_arraypad.cpython-38.pyc
│   │           │   │   │   │   ├── test_arraysetops.cpython-38.pyc
│   │           │   │   │   │   ├── test_arrayterator.cpython-38.pyc
│   │           │   │   │   │   ├── test__datasource.cpython-38.pyc
│   │           │   │   │   │   ├── test_financial_expired.cpython-38.pyc
│   │           │   │   │   │   ├── test_format.cpython-38.pyc
│   │           │   │   │   │   ├── test_function_base.cpython-38.pyc
│   │           │   │   │   │   ├── test_histograms.cpython-38.pyc
│   │           │   │   │   │   ├── test_index_tricks.cpython-38.pyc
│   │           │   │   │   │   ├── test_io.cpython-38.pyc
│   │           │   │   │   │   ├── test__iotools.cpython-38.pyc
│   │           │   │   │   │   ├── test_mixins.cpython-38.pyc
│   │           │   │   │   │   ├── test_nanfunctions.cpython-38.pyc
│   │           │   │   │   │   ├── test_packbits.cpython-38.pyc
│   │           │   │   │   │   ├── test_polynomial.cpython-38.pyc
│   │           │   │   │   │   ├── test_recfunctions.cpython-38.pyc
│   │           │   │   │   │   ├── test_regression.cpython-38.pyc
│   │           │   │   │   │   ├── test_shape_base.cpython-38.pyc
│   │           │   │   │   │   ├── test_stride_tricks.cpython-38.pyc
│   │           │   │   │   │   ├── test_twodim_base.cpython-38.pyc
│   │           │   │   │   │   ├── test_type_check.cpython-38.pyc
│   │           │   │   │   │   ├── test_ufunclike.cpython-38.pyc
│   │           │   │   │   │   ├── test_utils.cpython-38.pyc
│   │           │   │   │   │   └── test__version.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_arraypad.py
│   │           │   │   │   ├── test_arraysetops.py
│   │           │   │   │   ├── test_arrayterator.py
│   │           │   │   │   ├── test__datasource.py
│   │           │   │   │   ├── test_financial_expired.py
│   │           │   │   │   ├── test_format.py
│   │           │   │   │   ├── test_function_base.py
│   │           │   │   │   ├── test_histograms.py
│   │           │   │   │   ├── test_index_tricks.py
│   │           │   │   │   ├── test_io.py
│   │           │   │   │   ├── test__iotools.py
│   │           │   │   │   ├── test_mixins.py
│   │           │   │   │   ├── test_nanfunctions.py
│   │           │   │   │   ├── test_packbits.py
│   │           │   │   │   ├── test_polynomial.py
│   │           │   │   │   ├── test_recfunctions.py
│   │           │   │   │   ├── test_regression.py
│   │           │   │   │   ├── test_shape_base.py
│   │           │   │   │   ├── test_stride_tricks.py
│   │           │   │   │   ├── test_twodim_base.py
│   │           │   │   │   ├── test_type_check.py
│   │           │   │   │   ├── test_ufunclike.py
│   │           │   │   │   ├── test_utils.py
│   │           │   │   │   └── test__version.py
│   │           │   │   ├── arraypad.py
│   │           │   │   ├── arraysetops.py
│   │           │   │   ├── arrayterator.py
│   │           │   │   ├── _datasource.py
│   │           │   │   ├── format.py
│   │           │   │   ├── function_base.py
│   │           │   │   ├── histograms.py
│   │           │   │   ├── index_tricks.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __init__.pyi
│   │           │   │   ├── _iotools.py
│   │           │   │   ├── mixins.py
│   │           │   │   ├── nanfunctions.py
│   │           │   │   ├── npyio.py
│   │           │   │   ├── polynomial.py
│   │           │   │   ├── recfunctions.py
│   │           │   │   ├── scimath.py
│   │           │   │   ├── setup.py
│   │           │   │   ├── shape_base.py
│   │           │   │   ├── stride_tricks.py
│   │           │   │   ├── twodim_base.py
│   │           │   │   ├── type_check.py
│   │           │   │   ├── ufunclike.py
│   │           │   │   ├── user_array.py
│   │           │   │   ├── utils.py
│   │           │   │   └── _version.py
│   │           │   ├── linalg
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── linalg.cpython-38.pyc
│   │           │   │   │   └── setup.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_build.cpython-38.pyc
│   │           │   │   │   │   ├── test_deprecations.cpython-38.pyc
│   │           │   │   │   │   ├── test_linalg.cpython-38.pyc
│   │           │   │   │   │   └── test_regression.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_build.py
│   │           │   │   │   ├── test_deprecations.py
│   │           │   │   │   ├── test_linalg.py
│   │           │   │   │   └── test_regression.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __init__.pyi
│   │           │   │   ├── lapack_lite.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── linalg.py
│   │           │   │   ├── setup.py
│   │           │   │   └── _umath_linalg.cpython-38-x86_64-linux-gnu.so
│   │           │   ├── ma
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── bench.cpython-38.pyc
│   │           │   │   │   ├── core.cpython-38.pyc
│   │           │   │   │   ├── extras.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── mrecords.cpython-38.pyc
│   │           │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   ├── testutils.cpython-38.pyc
│   │           │   │   │   └── timer_comparison.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_core.cpython-38.pyc
│   │           │   │   │   │   ├── test_deprecations.cpython-38.pyc
│   │           │   │   │   │   ├── test_extras.cpython-38.pyc
│   │           │   │   │   │   ├── test_mrecords.cpython-38.pyc
│   │           │   │   │   │   ├── test_old_ma.cpython-38.pyc
│   │           │   │   │   │   ├── test_regression.cpython-38.pyc
│   │           │   │   │   │   └── test_subclassing.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_core.py
│   │           │   │   │   ├── test_deprecations.py
│   │           │   │   │   ├── test_extras.py
│   │           │   │   │   ├── test_mrecords.py
│   │           │   │   │   ├── test_old_ma.py
│   │           │   │   │   ├── test_regression.py
│   │           │   │   │   └── test_subclassing.py
│   │           │   │   ├── bench.py
│   │           │   │   ├── core.py
│   │           │   │   ├── extras.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __init__.pyi
│   │           │   │   ├── mrecords.py
│   │           │   │   ├── setup.py
│   │           │   │   ├── testutils.py
│   │           │   │   └── timer_comparison.py
│   │           │   ├── matrixlib
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── defmatrix.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   └── setup.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_defmatrix.cpython-38.pyc
│   │           │   │   │   │   ├── test_interaction.cpython-38.pyc
│   │           │   │   │   │   ├── test_masked_matrix.cpython-38.pyc
│   │           │   │   │   │   ├── test_matrix_linalg.cpython-38.pyc
│   │           │   │   │   │   ├── test_multiarray.cpython-38.pyc
│   │           │   │   │   │   ├── test_numeric.cpython-38.pyc
│   │           │   │   │   │   └── test_regression.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_defmatrix.py
│   │           │   │   │   ├── test_interaction.py
│   │           │   │   │   ├── test_masked_matrix.py
│   │           │   │   │   ├── test_matrix_linalg.py
│   │           │   │   │   ├── test_multiarray.py
│   │           │   │   │   ├── test_numeric.py
│   │           │   │   │   └── test_regression.py
│   │           │   │   ├── defmatrix.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __init__.pyi
│   │           │   │   └── setup.py
│   │           │   ├── polynomial
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── chebyshev.cpython-38.pyc
│   │           │   │   │   ├── hermite.cpython-38.pyc
│   │           │   │   │   ├── hermite_e.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── laguerre.cpython-38.pyc
│   │           │   │   │   ├── legendre.cpython-38.pyc
│   │           │   │   │   ├── _polybase.cpython-38.pyc
│   │           │   │   │   ├── polynomial.cpython-38.pyc
│   │           │   │   │   ├── polyutils.cpython-38.pyc
│   │           │   │   │   └── setup.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_chebyshev.cpython-38.pyc
│   │           │   │   │   │   ├── test_classes.cpython-38.pyc
│   │           │   │   │   │   ├── test_hermite.cpython-38.pyc
│   │           │   │   │   │   ├── test_hermite_e.cpython-38.pyc
│   │           │   │   │   │   ├── test_laguerre.cpython-38.pyc
│   │           │   │   │   │   ├── test_legendre.cpython-38.pyc
│   │           │   │   │   │   ├── test_polynomial.cpython-38.pyc
│   │           │   │   │   │   ├── test_polyutils.cpython-38.pyc
│   │           │   │   │   │   └── test_printing.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_chebyshev.py
│   │           │   │   │   ├── test_classes.py
│   │           │   │   │   ├── test_hermite_e.py
│   │           │   │   │   ├── test_hermite.py
│   │           │   │   │   ├── test_laguerre.py
│   │           │   │   │   ├── test_legendre.py
│   │           │   │   │   ├── test_polynomial.py
│   │           │   │   │   ├── test_polyutils.py
│   │           │   │   │   └── test_printing.py
│   │           │   │   ├── chebyshev.py
│   │           │   │   ├── hermite_e.py
│   │           │   │   ├── hermite.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __init__.pyi
│   │           │   │   ├── laguerre.py
│   │           │   │   ├── legendre.py
│   │           │   │   ├── _polybase.py
│   │           │   │   ├── polynomial.py
│   │           │   │   ├── polyutils.py
│   │           │   │   └── setup.py
│   │           │   ├── __pycache__
│   │           │   │   ├── __config__.cpython-38.pyc
│   │           │   │   ├── conftest.cpython-38.pyc
│   │           │   │   ├── ctypeslib.cpython-38.pyc
│   │           │   │   ├── _distributor_init.cpython-38.pyc
│   │           │   │   ├── dual.cpython-38.pyc
│   │           │   │   ├── _globals.cpython-38.pyc
│   │           │   │   ├── __init__.cpython-38.pyc
│   │           │   │   ├── matlib.cpython-38.pyc
│   │           │   │   ├── _pytesttester.cpython-38.pyc
│   │           │   │   ├── setup.cpython-38.pyc
│   │           │   │   └── version.cpython-38.pyc
│   │           │   ├── random
│   │           │   │   ├── _examples
│   │           │   │   │   ├── cffi
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── extending.cpython-38.pyc
│   │           │   │   │   │   │   └── parse.cpython-38.pyc
│   │           │   │   │   │   ├── extending.py
│   │           │   │   │   │   └── parse.py
│   │           │   │   │   ├── cython
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   └── setup.cpython-38.pyc
│   │           │   │   │   │   ├── extending_distributions.pyx
│   │           │   │   │   │   ├── extending.pyx
│   │           │   │   │   │   └── setup.py
│   │           │   │   │   └── numba
│   │           │   │   │       ├── __pycache__
│   │           │   │   │       │   ├── extending.cpython-38.pyc
│   │           │   │   │       │   └── extending_distributions.cpython-38.pyc
│   │           │   │   │       ├── extending_distributions.py
│   │           │   │   │       └── extending.py
│   │           │   │   ├── lib
│   │           │   │   │   └── libnpyrandom.a
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── _pickle.cpython-38.pyc
│   │           │   │   │   └── setup.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── data
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   └── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── mt19937-testset-1.csv
│   │           │   │   │   │   ├── mt19937-testset-2.csv
│   │           │   │   │   │   ├── pcg64-testset-1.csv
│   │           │   │   │   │   ├── pcg64-testset-2.csv
│   │           │   │   │   │   ├── philox-testset-1.csv
│   │           │   │   │   │   ├── philox-testset-2.csv
│   │           │   │   │   │   ├── sfc64-testset-1.csv
│   │           │   │   │   │   └── sfc64-testset-2.csv
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_direct.cpython-38.pyc
│   │           │   │   │   │   ├── test_extending.cpython-38.pyc
│   │           │   │   │   │   ├── test_generator_mt19937.cpython-38.pyc
│   │           │   │   │   │   ├── test_generator_mt19937_regressions.cpython-38.pyc
│   │           │   │   │   │   ├── test_random.cpython-38.pyc
│   │           │   │   │   │   ├── test_randomstate.cpython-38.pyc
│   │           │   │   │   │   ├── test_randomstate_regression.cpython-38.pyc
│   │           │   │   │   │   ├── test_regression.cpython-38.pyc
│   │           │   │   │   │   ├── test_seed_sequence.cpython-38.pyc
│   │           │   │   │   │   └── test_smoke.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_direct.py
│   │           │   │   │   ├── test_extending.py
│   │           │   │   │   ├── test_generator_mt19937.py
│   │           │   │   │   ├── test_generator_mt19937_regressions.py
│   │           │   │   │   ├── test_random.py
│   │           │   │   │   ├── test_randomstate.py
│   │           │   │   │   ├── test_randomstate_regression.py
│   │           │   │   │   ├── test_regression.py
│   │           │   │   │   ├── test_seed_sequence.py
│   │           │   │   │   └── test_smoke.py
│   │           │   │   ├── bit_generator.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── bit_generator.pxd
│   │           │   │   ├── _bounded_integers.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _bounded_integers.pxd
│   │           │   │   ├── c_distributions.pxd
│   │           │   │   ├── _common.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _common.pxd
│   │           │   │   ├── _generator.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── __init__.pxd
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __init__.pyi
│   │           │   │   ├── _mt19937.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── mtrand.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _pcg64.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _philox.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _pickle.py
│   │           │   │   ├── setup.py
│   │           │   │   └── _sfc64.cpython-38-x86_64-linux-gnu.so
│   │           │   ├── testing
│   │           │   │   ├── _private
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── decorators.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── noseclasses.cpython-38.pyc
│   │           │   │   │   │   ├── nosetester.cpython-38.pyc
│   │           │   │   │   │   ├── parameterized.cpython-38.pyc
│   │           │   │   │   │   └── utils.cpython-38.pyc
│   │           │   │   │   ├── decorators.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── noseclasses.py
│   │           │   │   │   ├── nosetester.py
│   │           │   │   │   ├── parameterized.py
│   │           │   │   │   └── utils.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── print_coercion_tables.cpython-38.pyc
│   │           │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   └── utils.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_decorators.cpython-38.pyc
│   │           │   │   │   │   ├── test_doctesting.cpython-38.pyc
│   │           │   │   │   │   └── test_utils.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_decorators.py
│   │           │   │   │   ├── test_doctesting.py
│   │           │   │   │   └── test_utils.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── __init__.pyi
│   │           │   │   ├── print_coercion_tables.py
│   │           │   │   ├── setup.py
│   │           │   │   └── utils.py
│   │           │   ├── tests
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── test_ctypeslib.cpython-38.pyc
│   │           │   │   │   ├── test_matlib.cpython-38.pyc
│   │           │   │   │   ├── test_numpy_version.cpython-38.pyc
│   │           │   │   │   ├── test_public_api.cpython-38.pyc
│   │           │   │   │   ├── test_reloading.cpython-38.pyc
│   │           │   │   │   ├── test_scripts.cpython-38.pyc
│   │           │   │   │   └── test_warnings.cpython-38.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── test_ctypeslib.py
│   │           │   │   ├── test_matlib.py
│   │           │   │   ├── test_numpy_version.py
│   │           │   │   ├── test_public_api.py
│   │           │   │   ├── test_reloading.py
│   │           │   │   ├── test_scripts.py
│   │           │   │   └── test_warnings.py
│   │           │   ├── typing
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── _add_docstring.cpython-38.pyc
│   │           │   │   │   ├── _array_like.cpython-38.pyc
│   │           │   │   │   ├── _callable.cpython-38.pyc
│   │           │   │   │   ├── _dtype_like.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── _scalars.cpython-38.pyc
│   │           │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   └── _shape.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── data
│   │           │   │   │   │   ├── fail
│   │           │   │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   │   ├── arithmetic.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── array_constructors.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── array_like.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── bitwise_ops.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── constants.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── dtype.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── flatiter.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── fromnumeric.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── modules.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── ndarray.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── ndarray_misc.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── numerictypes.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── scalars.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── ufunc_config.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── ufuncs.cpython-38.pyc
│   │           │   │   │   │   │   │   └── warnings_and_errors.cpython-38.pyc
│   │           │   │   │   │   │   ├── arithmetic.py
│   │           │   │   │   │   │   ├── array_constructors.py
│   │           │   │   │   │   │   ├── array_like.py
│   │           │   │   │   │   │   ├── bitwise_ops.py
│   │           │   │   │   │   │   ├── constants.py
│   │           │   │   │   │   │   ├── dtype.py
│   │           │   │   │   │   │   ├── flatiter.py
│   │           │   │   │   │   │   ├── fromnumeric.py
│   │           │   │   │   │   │   ├── modules.py
│   │           │   │   │   │   │   ├── ndarray_misc.py
│   │           │   │   │   │   │   ├── ndarray.py
│   │           │   │   │   │   │   ├── numerictypes.py
│   │           │   │   │   │   │   ├── scalars.py
│   │           │   │   │   │   │   ├── ufunc_config.py
│   │           │   │   │   │   │   ├── ufuncs.py
│   │           │   │   │   │   │   └── warnings_and_errors.py
│   │           │   │   │   │   ├── pass
│   │           │   │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   │   ├── arithmetic.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── array_constructors.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── array_like.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── bitwise_ops.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── dtype.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── flatiter.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── fromnumeric.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── literal.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── mod.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── modules.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── ndarray_conversion.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── ndarray_misc.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── ndarray_shape_manipulation.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── numeric.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── numerictypes.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── scalars.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── simple.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── simple_py3.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── ufunc_config.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── ufuncs.cpython-38.pyc
│   │           │   │   │   │   │   │   └── warnings_and_errors.cpython-38.pyc
│   │           │   │   │   │   │   ├── arithmetic.py
│   │           │   │   │   │   │   ├── array_constructors.py
│   │           │   │   │   │   │   ├── array_like.py
│   │           │   │   │   │   │   ├── bitwise_ops.py
│   │           │   │   │   │   │   ├── dtype.py
│   │           │   │   │   │   │   ├── flatiter.py
│   │           │   │   │   │   │   ├── fromnumeric.py
│   │           │   │   │   │   │   ├── literal.py
│   │           │   │   │   │   │   ├── mod.py
│   │           │   │   │   │   │   ├── modules.py
│   │           │   │   │   │   │   ├── ndarray_conversion.py
│   │           │   │   │   │   │   ├── ndarray_misc.py
│   │           │   │   │   │   │   ├── ndarray_shape_manipulation.py
│   │           │   │   │   │   │   ├── numeric.py
│   │           │   │   │   │   │   ├── numerictypes.py
│   │           │   │   │   │   │   ├── scalars.py
│   │           │   │   │   │   │   ├── simple.py
│   │           │   │   │   │   │   ├── simple_py3.py
│   │           │   │   │   │   │   ├── ufunc_config.py
│   │           │   │   │   │   │   ├── ufuncs.py
│   │           │   │   │   │   │   └── warnings_and_errors.py
│   │           │   │   │   │   ├── reveal
│   │           │   │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   │   ├── arithmetic.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── array_constructors.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── bitwise_ops.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── constants.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── dtype.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── flatiter.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── fromnumeric.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── mod.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── modules.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── nbit_base_example.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── ndarray_conversion.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── ndarray_misc.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── ndarray_shape_manipulation.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── numeric.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── numerictypes.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── scalars.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── ufunc_config.cpython-38.pyc
│   │           │   │   │   │   │   │   └── warnings_and_errors.cpython-38.pyc
│   │           │   │   │   │   │   ├── arithmetic.py
│   │           │   │   │   │   │   ├── array_constructors.py
│   │           │   │   │   │   │   ├── bitwise_ops.py
│   │           │   │   │   │   │   ├── constants.py
│   │           │   │   │   │   │   ├── dtype.py
│   │           │   │   │   │   │   ├── flatiter.py
│   │           │   │   │   │   │   ├── fromnumeric.py
│   │           │   │   │   │   │   ├── mod.py
│   │           │   │   │   │   │   ├── modules.py
│   │           │   │   │   │   │   ├── nbit_base_example.py
│   │           │   │   │   │   │   ├── ndarray_conversion.py
│   │           │   │   │   │   │   ├── ndarray_misc.py
│   │           │   │   │   │   │   ├── ndarray_shape_manipulation.py
│   │           │   │   │   │   │   ├── numeric.py
│   │           │   │   │   │   │   ├── numerictypes.py
│   │           │   │   │   │   │   ├── scalars.py
│   │           │   │   │   │   │   ├── ufunc_config.py
│   │           │   │   │   │   │   └── warnings_and_errors.py
│   │           │   │   │   │   └── mypy.ini
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_isfile.cpython-38.pyc
│   │           │   │   │   │   └── test_typing.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_isfile.py
│   │           │   │   │   └── test_typing.py
│   │           │   │   ├── _add_docstring.py
│   │           │   │   ├── _array_like.py
│   │           │   │   ├── _callable.py
│   │           │   │   ├── _dtype_like.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _scalars.py
│   │           │   │   ├── setup.py
│   │           │   │   └── _shape.py
│   │           │   ├── char.pyi
│   │           │   ├── __config__.py
│   │           │   ├── conftest.py
│   │           │   ├── ctypeslib.py
│   │           │   ├── ctypeslib.pyi
│   │           │   ├── _distributor_init.py
│   │           │   ├── dual.py
│   │           │   ├── emath.pyi
│   │           │   ├── _globals.py
│   │           │   ├── __init__.cython-30.pxd
│   │           │   ├── __init__.pxd
│   │           │   ├── __init__.py
│   │           │   ├── __init__.pyi
│   │           │   ├── LICENSE.txt
│   │           │   ├── matlib.py
│   │           │   ├── _pytesttester.py
│   │           │   ├── py.typed
│   │           │   ├── rec.pyi
│   │           │   ├── setup.py
│   │           │   └── version.py
│   │           ├── numpy-1.20.3.dist-info
│   │           │   ├── entry_points.txt
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSES_bundled.txt
│   │           │   ├── LICENSE.txt
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── numpy.libs
│   │           │   ├── libgfortran-2e0d59d6.so.5.0.0
│   │           │   ├── libopenblasp-r0-5bebc122.3.13.dev.so
│   │           │   ├── libquadmath-2d0c479f.so.0.0.0
│   │           │   └── libz-eb09ad1d.so.1.2.3
│   │           ├── packaging
│   │           │   ├── __pycache__
│   │           │   │   ├── __about__.cpython-38.pyc
│   │           │   │   ├── _compat.cpython-38.pyc
│   │           │   │   ├── __init__.cpython-38.pyc
│   │           │   │   ├── markers.cpython-38.pyc
│   │           │   │   ├── requirements.cpython-38.pyc
│   │           │   │   ├── specifiers.cpython-38.pyc
│   │           │   │   ├── _structures.cpython-38.pyc
│   │           │   │   ├── tags.cpython-38.pyc
│   │           │   │   ├── _typing.cpython-38.pyc
│   │           │   │   ├── utils.cpython-38.pyc
│   │           │   │   └── version.cpython-38.pyc
│   │           │   ├── __about__.py
│   │           │   ├── _compat.py
│   │           │   ├── __init__.py
│   │           │   ├── markers.py
│   │           │   ├── py.typed
│   │           │   ├── requirements.py
│   │           │   ├── specifiers.py
│   │           │   ├── _structures.py
│   │           │   ├── tags.py
│   │           │   ├── _typing.py
│   │           │   ├── utils.py
│   │           │   └── version.py
│   │           ├── packaging-20.9.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── LICENSE.APACHE
│   │           │   ├── LICENSE.BSD
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── PIL
│   │           │   ├── __pycache__
│   │           │   │   ├── BdfFontFile.cpython-38.pyc
│   │           │   │   ├── _binary.cpython-38.pyc
│   │           │   │   ├── BlpImagePlugin.cpython-38.pyc
│   │           │   │   ├── BmpImagePlugin.cpython-38.pyc
│   │           │   │   ├── BufrStubImagePlugin.cpython-38.pyc
│   │           │   │   ├── ContainerIO.cpython-38.pyc
│   │           │   │   ├── CurImagePlugin.cpython-38.pyc
│   │           │   │   ├── DcxImagePlugin.cpython-38.pyc
│   │           │   │   ├── DdsImagePlugin.cpython-38.pyc
│   │           │   │   ├── EpsImagePlugin.cpython-38.pyc
│   │           │   │   ├── ExifTags.cpython-38.pyc
│   │           │   │   ├── features.cpython-38.pyc
│   │           │   │   ├── FitsStubImagePlugin.cpython-38.pyc
│   │           │   │   ├── FliImagePlugin.cpython-38.pyc
│   │           │   │   ├── FontFile.cpython-38.pyc
│   │           │   │   ├── FpxImagePlugin.cpython-38.pyc
│   │           │   │   ├── FtexImagePlugin.cpython-38.pyc
│   │           │   │   ├── GbrImagePlugin.cpython-38.pyc
│   │           │   │   ├── GdImageFile.cpython-38.pyc
│   │           │   │   ├── GifImagePlugin.cpython-38.pyc
│   │           │   │   ├── GimpGradientFile.cpython-38.pyc
│   │           │   │   ├── GimpPaletteFile.cpython-38.pyc
│   │           │   │   ├── GribStubImagePlugin.cpython-38.pyc
│   │           │   │   ├── Hdf5StubImagePlugin.cpython-38.pyc
│   │           │   │   ├── IcnsImagePlugin.cpython-38.pyc
│   │           │   │   ├── IcoImagePlugin.cpython-38.pyc
│   │           │   │   ├── ImageChops.cpython-38.pyc
│   │           │   │   ├── ImageCms.cpython-38.pyc
│   │           │   │   ├── ImageColor.cpython-38.pyc
│   │           │   │   ├── Image.cpython-38.pyc
│   │           │   │   ├── ImageDraw2.cpython-38.pyc
│   │           │   │   ├── ImageDraw.cpython-38.pyc
│   │           │   │   ├── ImageEnhance.cpython-38.pyc
│   │           │   │   ├── ImageFile.cpython-38.pyc
│   │           │   │   ├── ImageFilter.cpython-38.pyc
│   │           │   │   ├── ImageFont.cpython-38.pyc
│   │           │   │   ├── ImageGrab.cpython-38.pyc
│   │           │   │   ├── ImageMath.cpython-38.pyc
│   │           │   │   ├── ImageMode.cpython-38.pyc
│   │           │   │   ├── ImageMorph.cpython-38.pyc
│   │           │   │   ├── ImageOps.cpython-38.pyc
│   │           │   │   ├── ImagePalette.cpython-38.pyc
│   │           │   │   ├── ImagePath.cpython-38.pyc
│   │           │   │   ├── ImageQt.cpython-38.pyc
│   │           │   │   ├── ImageSequence.cpython-38.pyc
│   │           │   │   ├── ImageShow.cpython-38.pyc
│   │           │   │   ├── ImageStat.cpython-38.pyc
│   │           │   │   ├── ImageTk.cpython-38.pyc
│   │           │   │   ├── ImageTransform.cpython-38.pyc
│   │           │   │   ├── ImageWin.cpython-38.pyc
│   │           │   │   ├── ImImagePlugin.cpython-38.pyc
│   │           │   │   ├── ImtImagePlugin.cpython-38.pyc
│   │           │   │   ├── __init__.cpython-38.pyc
│   │           │   │   ├── IptcImagePlugin.cpython-38.pyc
│   │           │   │   ├── Jpeg2KImagePlugin.cpython-38.pyc
│   │           │   │   ├── JpegImagePlugin.cpython-38.pyc
│   │           │   │   ├── JpegPresets.cpython-38.pyc
│   │           │   │   ├── __main__.cpython-38.pyc
│   │           │   │   ├── McIdasImagePlugin.cpython-38.pyc
│   │           │   │   ├── MicImagePlugin.cpython-38.pyc
│   │           │   │   ├── MpegImagePlugin.cpython-38.pyc
│   │           │   │   ├── MpoImagePlugin.cpython-38.pyc
│   │           │   │   ├── MspImagePlugin.cpython-38.pyc
│   │           │   │   ├── PaletteFile.cpython-38.pyc
│   │           │   │   ├── PalmImagePlugin.cpython-38.pyc
│   │           │   │   ├── PcdImagePlugin.cpython-38.pyc
│   │           │   │   ├── PcfFontFile.cpython-38.pyc
│   │           │   │   ├── PcxImagePlugin.cpython-38.pyc
│   │           │   │   ├── PdfImagePlugin.cpython-38.pyc
│   │           │   │   ├── PdfParser.cpython-38.pyc
│   │           │   │   ├── PixarImagePlugin.cpython-38.pyc
│   │           │   │   ├── PngImagePlugin.cpython-38.pyc
│   │           │   │   ├── PpmImagePlugin.cpython-38.pyc
│   │           │   │   ├── PsdImagePlugin.cpython-38.pyc
│   │           │   │   ├── PSDraw.cpython-38.pyc
│   │           │   │   ├── PyAccess.cpython-38.pyc
│   │           │   │   ├── SgiImagePlugin.cpython-38.pyc
│   │           │   │   ├── SpiderImagePlugin.cpython-38.pyc
│   │           │   │   ├── SunImagePlugin.cpython-38.pyc
│   │           │   │   ├── TarIO.cpython-38.pyc
│   │           │   │   ├── TgaImagePlugin.cpython-38.pyc
│   │           │   │   ├── TiffImagePlugin.cpython-38.pyc
│   │           │   │   ├── TiffTags.cpython-38.pyc
│   │           │   │   ├── _tkinter_finder.cpython-38.pyc
│   │           │   │   ├── _util.cpython-38.pyc
│   │           │   │   ├── _version.cpython-38.pyc
│   │           │   │   ├── WalImageFile.cpython-38.pyc
│   │           │   │   ├── WebPImagePlugin.cpython-38.pyc
│   │           │   │   ├── WmfImagePlugin.cpython-38.pyc
│   │           │   │   ├── XbmImagePlugin.cpython-38.pyc
│   │           │   │   ├── XpmImagePlugin.cpython-38.pyc
│   │           │   │   └── XVThumbImagePlugin.cpython-38.pyc
│   │           │   ├── BdfFontFile.py
│   │           │   ├── _binary.py
│   │           │   ├── BlpImagePlugin.py
│   │           │   ├── BmpImagePlugin.py
│   │           │   ├── BufrStubImagePlugin.py
│   │           │   ├── ContainerIO.py
│   │           │   ├── CurImagePlugin.py
│   │           │   ├── DcxImagePlugin.py
│   │           │   ├── DdsImagePlugin.py
│   │           │   ├── EpsImagePlugin.py
│   │           │   ├── ExifTags.py
│   │           │   ├── features.py
│   │           │   ├── FitsStubImagePlugin.py
│   │           │   ├── FliImagePlugin.py
│   │           │   ├── FontFile.py
│   │           │   ├── FpxImagePlugin.py
│   │           │   ├── FtexImagePlugin.py
│   │           │   ├── GbrImagePlugin.py
│   │           │   ├── GdImageFile.py
│   │           │   ├── GifImagePlugin.py
│   │           │   ├── GimpGradientFile.py
│   │           │   ├── GimpPaletteFile.py
│   │           │   ├── GribStubImagePlugin.py
│   │           │   ├── Hdf5StubImagePlugin.py
│   │           │   ├── IcnsImagePlugin.py
│   │           │   ├── IcoImagePlugin.py
│   │           │   ├── ImageChops.py
│   │           │   ├── ImageCms.py
│   │           │   ├── ImageColor.py
│   │           │   ├── ImageDraw2.py
│   │           │   ├── ImageDraw.py
│   │           │   ├── ImageEnhance.py
│   │           │   ├── ImageFile.py
│   │           │   ├── ImageFilter.py
│   │           │   ├── ImageFont.py
│   │           │   ├── ImageGrab.py
│   │           │   ├── ImageMath.py
│   │           │   ├── ImageMode.py
│   │           │   ├── ImageMorph.py
│   │           │   ├── ImageOps.py
│   │           │   ├── ImagePalette.py
│   │           │   ├── ImagePath.py
│   │           │   ├── Image.py
│   │           │   ├── ImageQt.py
│   │           │   ├── ImageSequence.py
│   │           │   ├── ImageShow.py
│   │           │   ├── ImageStat.py
│   │           │   ├── ImageTk.py
│   │           │   ├── ImageTransform.py
│   │           │   ├── ImageWin.py
│   │           │   ├── _imagingcms.cpython-38-x86_64-linux-gnu.so
│   │           │   ├── _imaging.cpython-38-x86_64-linux-gnu.so
│   │           │   ├── _imagingft.cpython-38-x86_64-linux-gnu.so
│   │           │   ├── _imagingmath.cpython-38-x86_64-linux-gnu.so
│   │           │   ├── _imagingmorph.cpython-38-x86_64-linux-gnu.so
│   │           │   ├── _imagingtk.cpython-38-x86_64-linux-gnu.so
│   │           │   ├── ImImagePlugin.py
│   │           │   ├── ImtImagePlugin.py
│   │           │   ├── __init__.py
│   │           │   ├── IptcImagePlugin.py
│   │           │   ├── Jpeg2KImagePlugin.py
│   │           │   ├── JpegImagePlugin.py
│   │           │   ├── JpegPresets.py
│   │           │   ├── __main__.py
│   │           │   ├── McIdasImagePlugin.py
│   │           │   ├── MicImagePlugin.py
│   │           │   ├── MpegImagePlugin.py
│   │           │   ├── MpoImagePlugin.py
│   │           │   ├── MspImagePlugin.py
│   │           │   ├── PaletteFile.py
│   │           │   ├── PalmImagePlugin.py
│   │           │   ├── PcdImagePlugin.py
│   │           │   ├── PcfFontFile.py
│   │           │   ├── PcxImagePlugin.py
│   │           │   ├── PdfImagePlugin.py
│   │           │   ├── PdfParser.py
│   │           │   ├── PixarImagePlugin.py
│   │           │   ├── PngImagePlugin.py
│   │           │   ├── PpmImagePlugin.py
│   │           │   ├── PsdImagePlugin.py
│   │           │   ├── PSDraw.py
│   │           │   ├── PyAccess.py
│   │           │   ├── SgiImagePlugin.py
│   │           │   ├── SpiderImagePlugin.py
│   │           │   ├── SunImagePlugin.py
│   │           │   ├── TarIO.py
│   │           │   ├── TgaImagePlugin.py
│   │           │   ├── TiffImagePlugin.py
│   │           │   ├── TiffTags.py
│   │           │   ├── _tkinter_finder.py
│   │           │   ├── _util.py
│   │           │   ├── _version.py
│   │           │   ├── WalImageFile.py
│   │           │   ├── _webp.cpython-38-x86_64-linux-gnu.so
│   │           │   ├── WebPImagePlugin.py
│   │           │   ├── WmfImagePlugin.py
│   │           │   ├── XbmImagePlugin.py
│   │           │   ├── XpmImagePlugin.py
│   │           │   └── XVThumbImagePlugin.py
│   │           ├── Pillow-8.2.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   ├── WHEEL
│   │           │   └── zip-safe
│   │           ├── Pillow.libs
│   │           │   ├── libfreetype-6ad068c6.so.6.17.4
│   │           │   ├── libharfbuzz-ba5e3cba.so.0.20800.0
│   │           │   ├── libjpeg-ba7bf5af.so.9.4.0
│   │           │   ├── liblcms2-a76503ec.so.2.0.12
│   │           │   ├── liblzma-99449165.so.5.2.5
│   │           │   ├── libopenjp2-f0612b30.so.2.4.0
│   │           │   ├── libpng16-bedcb7ea.so.16.37.0
│   │           │   ├── libtiff-d147fec3.so.5.6.0
│   │           │   ├── libwebp-305e7d94.so.7.1.1
│   │           │   ├── libwebpdemux-2a7a19d5.so.2.0.7
│   │           │   ├── libwebpmux-1d369df0.so.3.0.6
│   │           │   ├── libXau-312dbc56.so.6.0.0
│   │           │   ├── libxcb-2dfad6c3.so.1.1.0
│   │           │   ├── libXdmcp-e15573e7.so.6.0.0
│   │           │   └── libz-a147dcb0.so.1.2.3
│   │           ├── pip
│   │           │   ├── _internal
│   │           │   │   ├── cli
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── autocompletion.cpython-38.pyc
│   │           │   │   │   │   ├── base_command.cpython-38.pyc
│   │           │   │   │   │   ├── cmdoptions.cpython-38.pyc
│   │           │   │   │   │   ├── command_context.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── main.cpython-38.pyc
│   │           │   │   │   │   ├── main_parser.cpython-38.pyc
│   │           │   │   │   │   ├── parser.cpython-38.pyc
│   │           │   │   │   │   ├── progress_bars.cpython-38.pyc
│   │           │   │   │   │   ├── req_command.cpython-38.pyc
│   │           │   │   │   │   ├── spinners.cpython-38.pyc
│   │           │   │   │   │   └── status_codes.cpython-38.pyc
│   │           │   │   │   ├── autocompletion.py
│   │           │   │   │   ├── base_command.py
│   │           │   │   │   ├── cmdoptions.py
│   │           │   │   │   ├── command_context.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── main_parser.py
│   │           │   │   │   ├── main.py
│   │           │   │   │   ├── parser.py
│   │           │   │   │   ├── progress_bars.py
│   │           │   │   │   ├── req_command.py
│   │           │   │   │   ├── spinners.py
│   │           │   │   │   └── status_codes.py
│   │           │   │   ├── commands
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── cache.cpython-38.pyc
│   │           │   │   │   │   ├── check.cpython-38.pyc
│   │           │   │   │   │   ├── completion.cpython-38.pyc
│   │           │   │   │   │   ├── configuration.cpython-38.pyc
│   │           │   │   │   │   ├── debug.cpython-38.pyc
│   │           │   │   │   │   ├── download.cpython-38.pyc
│   │           │   │   │   │   ├── freeze.cpython-38.pyc
│   │           │   │   │   │   ├── hash.cpython-38.pyc
│   │           │   │   │   │   ├── help.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── install.cpython-38.pyc
│   │           │   │   │   │   ├── list.cpython-38.pyc
│   │           │   │   │   │   ├── search.cpython-38.pyc
│   │           │   │   │   │   ├── show.cpython-38.pyc
│   │           │   │   │   │   ├── uninstall.cpython-38.pyc
│   │           │   │   │   │   └── wheel.cpython-38.pyc
│   │           │   │   │   ├── cache.py
│   │           │   │   │   ├── check.py
│   │           │   │   │   ├── completion.py
│   │           │   │   │   ├── configuration.py
│   │           │   │   │   ├── debug.py
│   │           │   │   │   ├── download.py
│   │           │   │   │   ├── freeze.py
│   │           │   │   │   ├── hash.py
│   │           │   │   │   ├── help.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── install.py
│   │           │   │   │   ├── list.py
│   │           │   │   │   ├── search.py
│   │           │   │   │   ├── show.py
│   │           │   │   │   ├── uninstall.py
│   │           │   │   │   └── wheel.py
│   │           │   │   ├── distributions
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── base.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── installed.cpython-38.pyc
│   │           │   │   │   │   ├── sdist.cpython-38.pyc
│   │           │   │   │   │   └── wheel.cpython-38.pyc
│   │           │   │   │   ├── base.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── installed.py
│   │           │   │   │   ├── sdist.py
│   │           │   │   │   └── wheel.py
│   │           │   │   ├── index
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── collector.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── package_finder.cpython-38.pyc
│   │           │   │   │   │   └── sources.cpython-38.pyc
│   │           │   │   │   ├── collector.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── package_finder.py
│   │           │   │   │   └── sources.py
│   │           │   │   ├── locations
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── base.cpython-38.pyc
│   │           │   │   │   │   ├── _distutils.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   └── _sysconfig.cpython-38.pyc
│   │           │   │   │   ├── base.py
│   │           │   │   │   ├── _distutils.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── _sysconfig.py
│   │           │   │   ├── metadata
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── base.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   └── pkg_resources.cpython-38.pyc
│   │           │   │   │   ├── base.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── pkg_resources.py
│   │           │   │   ├── models
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── candidate.cpython-38.pyc
│   │           │   │   │   │   ├── direct_url.cpython-38.pyc
│   │           │   │   │   │   ├── format_control.cpython-38.pyc
│   │           │   │   │   │   ├── index.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── link.cpython-38.pyc
│   │           │   │   │   │   ├── scheme.cpython-38.pyc
│   │           │   │   │   │   ├── search_scope.cpython-38.pyc
│   │           │   │   │   │   ├── selection_prefs.cpython-38.pyc
│   │           │   │   │   │   ├── target_python.cpython-38.pyc
│   │           │   │   │   │   └── wheel.cpython-38.pyc
│   │           │   │   │   ├── candidate.py
│   │           │   │   │   ├── direct_url.py
│   │           │   │   │   ├── format_control.py
│   │           │   │   │   ├── index.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── link.py
│   │           │   │   │   ├── scheme.py
│   │           │   │   │   ├── search_scope.py
│   │           │   │   │   ├── selection_prefs.py
│   │           │   │   │   ├── target_python.py
│   │           │   │   │   └── wheel.py
│   │           │   │   ├── network
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── auth.cpython-38.pyc
│   │           │   │   │   │   ├── cache.cpython-38.pyc
│   │           │   │   │   │   ├── download.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── lazy_wheel.cpython-38.pyc
│   │           │   │   │   │   ├── session.cpython-38.pyc
│   │           │   │   │   │   ├── utils.cpython-38.pyc
│   │           │   │   │   │   └── xmlrpc.cpython-38.pyc
│   │           │   │   │   ├── auth.py
│   │           │   │   │   ├── cache.py
│   │           │   │   │   ├── download.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── lazy_wheel.py
│   │           │   │   │   ├── session.py
│   │           │   │   │   ├── utils.py
│   │           │   │   │   └── xmlrpc.py
│   │           │   │   ├── operations
│   │           │   │   │   ├── build
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   ├── metadata.cpython-38.pyc
│   │           │   │   │   │   │   ├── metadata_legacy.cpython-38.pyc
│   │           │   │   │   │   │   ├── wheel.cpython-38.pyc
│   │           │   │   │   │   │   └── wheel_legacy.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── metadata_legacy.py
│   │           │   │   │   │   ├── metadata.py
│   │           │   │   │   │   ├── wheel_legacy.py
│   │           │   │   │   │   └── wheel.py
│   │           │   │   │   ├── install
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── editable_legacy.cpython-38.pyc
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   ├── legacy.cpython-38.pyc
│   │           │   │   │   │   │   └── wheel.cpython-38.pyc
│   │           │   │   │   │   ├── editable_legacy.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── legacy.py
│   │           │   │   │   │   └── wheel.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── check.cpython-38.pyc
│   │           │   │   │   │   ├── freeze.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   └── prepare.cpython-38.pyc
│   │           │   │   │   ├── check.py
│   │           │   │   │   ├── freeze.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── prepare.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── build_env.cpython-38.pyc
│   │           │   │   │   ├── cache.cpython-38.pyc
│   │           │   │   │   ├── configuration.cpython-38.pyc
│   │           │   │   │   ├── exceptions.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── main.cpython-38.pyc
│   │           │   │   │   ├── pyproject.cpython-38.pyc
│   │           │   │   │   ├── self_outdated_check.cpython-38.pyc
│   │           │   │   │   └── wheel_builder.cpython-38.pyc
│   │           │   │   ├── req
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── constructors.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── req_file.cpython-38.pyc
│   │           │   │   │   │   ├── req_install.cpython-38.pyc
│   │           │   │   │   │   ├── req_set.cpython-38.pyc
│   │           │   │   │   │   ├── req_tracker.cpython-38.pyc
│   │           │   │   │   │   └── req_uninstall.cpython-38.pyc
│   │           │   │   │   ├── constructors.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── req_file.py
│   │           │   │   │   ├── req_install.py
│   │           │   │   │   ├── req_set.py
│   │           │   │   │   ├── req_tracker.py
│   │           │   │   │   └── req_uninstall.py
│   │           │   │   ├── resolution
│   │           │   │   │   ├── legacy
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   └── resolver.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── resolver.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── base.cpython-38.pyc
│   │           │   │   │   │   └── __init__.cpython-38.pyc
│   │           │   │   │   ├── resolvelib
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── base.cpython-38.pyc
│   │           │   │   │   │   │   ├── candidates.cpython-38.pyc
│   │           │   │   │   │   │   ├── factory.cpython-38.pyc
│   │           │   │   │   │   │   ├── found_candidates.cpython-38.pyc
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   ├── provider.cpython-38.pyc
│   │           │   │   │   │   │   ├── reporter.cpython-38.pyc
│   │           │   │   │   │   │   ├── requirements.cpython-38.pyc
│   │           │   │   │   │   │   └── resolver.cpython-38.pyc
│   │           │   │   │   │   ├── base.py
│   │           │   │   │   │   ├── candidates.py
│   │           │   │   │   │   ├── factory.py
│   │           │   │   │   │   ├── found_candidates.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── provider.py
│   │           │   │   │   │   ├── reporter.py
│   │           │   │   │   │   ├── requirements.py
│   │           │   │   │   │   └── resolver.py
│   │           │   │   │   ├── base.py
│   │           │   │   │   └── __init__.py
│   │           │   │   ├── utils
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── appdirs.cpython-38.pyc
│   │           │   │   │   │   ├── compat.cpython-38.pyc
│   │           │   │   │   │   ├── compatibility_tags.cpython-38.pyc
│   │           │   │   │   │   ├── datetime.cpython-38.pyc
│   │           │   │   │   │   ├── deprecation.cpython-38.pyc
│   │           │   │   │   │   ├── direct_url_helpers.cpython-38.pyc
│   │           │   │   │   │   ├── distutils_args.cpython-38.pyc
│   │           │   │   │   │   ├── encoding.cpython-38.pyc
│   │           │   │   │   │   ├── entrypoints.cpython-38.pyc
│   │           │   │   │   │   ├── filesystem.cpython-38.pyc
│   │           │   │   │   │   ├── filetypes.cpython-38.pyc
│   │           │   │   │   │   ├── glibc.cpython-38.pyc
│   │           │   │   │   │   ├── hashes.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── inject_securetransport.cpython-38.pyc
│   │           │   │   │   │   ├── logging.cpython-38.pyc
│   │           │   │   │   │   ├── misc.cpython-38.pyc
│   │           │   │   │   │   ├── models.cpython-38.pyc
│   │           │   │   │   │   ├── packaging.cpython-38.pyc
│   │           │   │   │   │   ├── parallel.cpython-38.pyc
│   │           │   │   │   │   ├── pkg_resources.cpython-38.pyc
│   │           │   │   │   │   ├── setuptools_build.cpython-38.pyc
│   │           │   │   │   │   ├── subprocess.cpython-38.pyc
│   │           │   │   │   │   ├── temp_dir.cpython-38.pyc
│   │           │   │   │   │   ├── unpacking.cpython-38.pyc
│   │           │   │   │   │   ├── urls.cpython-38.pyc
│   │           │   │   │   │   ├── virtualenv.cpython-38.pyc
│   │           │   │   │   │   └── wheel.cpython-38.pyc
│   │           │   │   │   ├── appdirs.py
│   │           │   │   │   ├── compatibility_tags.py
│   │           │   │   │   ├── compat.py
│   │           │   │   │   ├── datetime.py
│   │           │   │   │   ├── deprecation.py
│   │           │   │   │   ├── direct_url_helpers.py
│   │           │   │   │   ├── distutils_args.py
│   │           │   │   │   ├── encoding.py
│   │           │   │   │   ├── entrypoints.py
│   │           │   │   │   ├── filesystem.py
│   │           │   │   │   ├── filetypes.py
│   │           │   │   │   ├── glibc.py
│   │           │   │   │   ├── hashes.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── inject_securetransport.py
│   │           │   │   │   ├── logging.py
│   │           │   │   │   ├── misc.py
│   │           │   │   │   ├── models.py
│   │           │   │   │   ├── packaging.py
│   │           │   │   │   ├── parallel.py
│   │           │   │   │   ├── pkg_resources.py
│   │           │   │   │   ├── setuptools_build.py
│   │           │   │   │   ├── subprocess.py
│   │           │   │   │   ├── temp_dir.py
│   │           │   │   │   ├── unpacking.py
│   │           │   │   │   ├── urls.py
│   │           │   │   │   ├── virtualenv.py
│   │           │   │   │   └── wheel.py
│   │           │   │   ├── vcs
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── bazaar.cpython-38.pyc
│   │           │   │   │   │   ├── git.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── mercurial.cpython-38.pyc
│   │           │   │   │   │   ├── subversion.cpython-38.pyc
│   │           │   │   │   │   └── versioncontrol.cpython-38.pyc
│   │           │   │   │   ├── bazaar.py
│   │           │   │   │   ├── git.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── mercurial.py
│   │           │   │   │   ├── subversion.py
│   │           │   │   │   └── versioncontrol.py
│   │           │   │   ├── build_env.py
│   │           │   │   ├── cache.py
│   │           │   │   ├── configuration.py
│   │           │   │   ├── exceptions.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── main.py
│   │           │   │   ├── pyproject.py
│   │           │   │   ├── self_outdated_check.py
│   │           │   │   └── wheel_builder.py
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-38.pyc
│   │           │   │   └── __main__.cpython-38.pyc
│   │           │   ├── _vendor
│   │           │   │   ├── cachecontrol
│   │           │   │   │   ├── caches
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── file_cache.cpython-38.pyc
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   └── redis_cache.cpython-38.pyc
│   │           │   │   │   │   ├── file_cache.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── redis_cache.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── adapter.cpython-38.pyc
│   │           │   │   │   │   ├── cache.cpython-38.pyc
│   │           │   │   │   │   ├── _cmd.cpython-38.pyc
│   │           │   │   │   │   ├── compat.cpython-38.pyc
│   │           │   │   │   │   ├── controller.cpython-38.pyc
│   │           │   │   │   │   ├── filewrapper.cpython-38.pyc
│   │           │   │   │   │   ├── heuristics.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── serialize.cpython-38.pyc
│   │           │   │   │   │   └── wrapper.cpython-38.pyc
│   │           │   │   │   ├── adapter.py
│   │           │   │   │   ├── cache.py
│   │           │   │   │   ├── _cmd.py
│   │           │   │   │   ├── compat.py
│   │           │   │   │   ├── controller.py
│   │           │   │   │   ├── filewrapper.py
│   │           │   │   │   ├── heuristics.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── serialize.py
│   │           │   │   │   └── wrapper.py
│   │           │   │   ├── certifi
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── core.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   └── __main__.cpython-38.pyc
│   │           │   │   │   ├── cacert.pem
│   │           │   │   │   ├── core.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── __main__.py
│   │           │   │   ├── chardet
│   │           │   │   │   ├── cli
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── chardetect.cpython-38.pyc
│   │           │   │   │   │   │   └── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── chardetect.py
│   │           │   │   │   │   └── __init__.py
│   │           │   │   │   ├── metadata
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   └── languages.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── languages.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── big5freq.cpython-38.pyc
│   │           │   │   │   │   ├── big5prober.cpython-38.pyc
│   │           │   │   │   │   ├── chardistribution.cpython-38.pyc
│   │           │   │   │   │   ├── charsetgroupprober.cpython-38.pyc
│   │           │   │   │   │   ├── charsetprober.cpython-38.pyc
│   │           │   │   │   │   ├── codingstatemachine.cpython-38.pyc
│   │           │   │   │   │   ├── compat.cpython-38.pyc
│   │           │   │   │   │   ├── cp949prober.cpython-38.pyc
│   │           │   │   │   │   ├── enums.cpython-38.pyc
│   │           │   │   │   │   ├── escprober.cpython-38.pyc
│   │           │   │   │   │   ├── escsm.cpython-38.pyc
│   │           │   │   │   │   ├── eucjpprober.cpython-38.pyc
│   │           │   │   │   │   ├── euckrfreq.cpython-38.pyc
│   │           │   │   │   │   ├── euckrprober.cpython-38.pyc
│   │           │   │   │   │   ├── euctwfreq.cpython-38.pyc
│   │           │   │   │   │   ├── euctwprober.cpython-38.pyc
│   │           │   │   │   │   ├── gb2312freq.cpython-38.pyc
│   │           │   │   │   │   ├── gb2312prober.cpython-38.pyc
│   │           │   │   │   │   ├── hebrewprober.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── jisfreq.cpython-38.pyc
│   │           │   │   │   │   ├── jpcntx.cpython-38.pyc
│   │           │   │   │   │   ├── langbulgarianmodel.cpython-38.pyc
│   │           │   │   │   │   ├── langgreekmodel.cpython-38.pyc
│   │           │   │   │   │   ├── langhebrewmodel.cpython-38.pyc
│   │           │   │   │   │   ├── langhungarianmodel.cpython-38.pyc
│   │           │   │   │   │   ├── langrussianmodel.cpython-38.pyc
│   │           │   │   │   │   ├── langthaimodel.cpython-38.pyc
│   │           │   │   │   │   ├── langturkishmodel.cpython-38.pyc
│   │           │   │   │   │   ├── latin1prober.cpython-38.pyc
│   │           │   │   │   │   ├── mbcharsetprober.cpython-38.pyc
│   │           │   │   │   │   ├── mbcsgroupprober.cpython-38.pyc
│   │           │   │   │   │   ├── mbcssm.cpython-38.pyc
│   │           │   │   │   │   ├── sbcharsetprober.cpython-38.pyc
│   │           │   │   │   │   ├── sbcsgroupprober.cpython-38.pyc
│   │           │   │   │   │   ├── sjisprober.cpython-38.pyc
│   │           │   │   │   │   ├── universaldetector.cpython-38.pyc
│   │           │   │   │   │   ├── utf8prober.cpython-38.pyc
│   │           │   │   │   │   └── version.cpython-38.pyc
│   │           │   │   │   ├── big5freq.py
│   │           │   │   │   ├── big5prober.py
│   │           │   │   │   ├── chardistribution.py
│   │           │   │   │   ├── charsetgroupprober.py
│   │           │   │   │   ├── charsetprober.py
│   │           │   │   │   ├── codingstatemachine.py
│   │           │   │   │   ├── compat.py
│   │           │   │   │   ├── cp949prober.py
│   │           │   │   │   ├── enums.py
│   │           │   │   │   ├── escprober.py
│   │           │   │   │   ├── escsm.py
│   │           │   │   │   ├── eucjpprober.py
│   │           │   │   │   ├── euckrfreq.py
│   │           │   │   │   ├── euckrprober.py
│   │           │   │   │   ├── euctwfreq.py
│   │           │   │   │   ├── euctwprober.py
│   │           │   │   │   ├── gb2312freq.py
│   │           │   │   │   ├── gb2312prober.py
│   │           │   │   │   ├── hebrewprober.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── jisfreq.py
│   │           │   │   │   ├── jpcntx.py
│   │           │   │   │   ├── langbulgarianmodel.py
│   │           │   │   │   ├── langgreekmodel.py
│   │           │   │   │   ├── langhebrewmodel.py
│   │           │   │   │   ├── langhungarianmodel.py
│   │           │   │   │   ├── langrussianmodel.py
│   │           │   │   │   ├── langthaimodel.py
│   │           │   │   │   ├── langturkishmodel.py
│   │           │   │   │   ├── latin1prober.py
│   │           │   │   │   ├── mbcharsetprober.py
│   │           │   │   │   ├── mbcsgroupprober.py
│   │           │   │   │   ├── mbcssm.py
│   │           │   │   │   ├── sbcharsetprober.py
│   │           │   │   │   ├── sbcsgroupprober.py
│   │           │   │   │   ├── sjisprober.py
│   │           │   │   │   ├── universaldetector.py
│   │           │   │   │   ├── utf8prober.py
│   │           │   │   │   └── version.py
│   │           │   │   ├── colorama
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── ansi.cpython-38.pyc
│   │           │   │   │   │   ├── ansitowin32.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── initialise.cpython-38.pyc
│   │           │   │   │   │   ├── win32.cpython-38.pyc
│   │           │   │   │   │   └── winterm.cpython-38.pyc
│   │           │   │   │   ├── ansi.py
│   │           │   │   │   ├── ansitowin32.py
│   │           │   │   │   ├── initialise.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── win32.py
│   │           │   │   │   └── winterm.py
│   │           │   │   ├── distlib
│   │           │   │   │   ├── _backport
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   ├── misc.cpython-38.pyc
│   │           │   │   │   │   │   ├── shutil.cpython-38.pyc
│   │           │   │   │   │   │   ├── sysconfig.cpython-38.pyc
│   │           │   │   │   │   │   └── tarfile.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── misc.py
│   │           │   │   │   │   ├── shutil.py
│   │           │   │   │   │   ├── sysconfig.cfg
│   │           │   │   │   │   ├── sysconfig.py
│   │           │   │   │   │   └── tarfile.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── compat.cpython-38.pyc
│   │           │   │   │   │   ├── database.cpython-38.pyc
│   │           │   │   │   │   ├── index.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── locators.cpython-38.pyc
│   │           │   │   │   │   ├── manifest.cpython-38.pyc
│   │           │   │   │   │   ├── markers.cpython-38.pyc
│   │           │   │   │   │   ├── metadata.cpython-38.pyc
│   │           │   │   │   │   ├── resources.cpython-38.pyc
│   │           │   │   │   │   ├── scripts.cpython-38.pyc
│   │           │   │   │   │   ├── util.cpython-38.pyc
│   │           │   │   │   │   ├── version.cpython-38.pyc
│   │           │   │   │   │   └── wheel.cpython-38.pyc
│   │           │   │   │   ├── compat.py
│   │           │   │   │   ├── database.py
│   │           │   │   │   ├── index.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── locators.py
│   │           │   │   │   ├── manifest.py
│   │           │   │   │   ├── markers.py
│   │           │   │   │   ├── metadata.py
│   │           │   │   │   ├── resources.py
│   │           │   │   │   ├── scripts.py
│   │           │   │   │   ├── t32.exe
│   │           │   │   │   ├── t64.exe
│   │           │   │   │   ├── util.py
│   │           │   │   │   ├── version.py
│   │           │   │   │   ├── w32.exe
│   │           │   │   │   ├── w64.exe
│   │           │   │   │   └── wheel.py
│   │           │   │   ├── html5lib
│   │           │   │   │   ├── filters
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── alphabeticalattributes.cpython-38.pyc
│   │           │   │   │   │   │   ├── base.cpython-38.pyc
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   ├── inject_meta_charset.cpython-38.pyc
│   │           │   │   │   │   │   ├── lint.cpython-38.pyc
│   │           │   │   │   │   │   ├── optionaltags.cpython-38.pyc
│   │           │   │   │   │   │   ├── sanitizer.cpython-38.pyc
│   │           │   │   │   │   │   └── whitespace.cpython-38.pyc
│   │           │   │   │   │   ├── alphabeticalattributes.py
│   │           │   │   │   │   ├── base.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── inject_meta_charset.py
│   │           │   │   │   │   ├── lint.py
│   │           │   │   │   │   ├── optionaltags.py
│   │           │   │   │   │   ├── sanitizer.py
│   │           │   │   │   │   └── whitespace.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── constants.cpython-38.pyc
│   │           │   │   │   │   ├── html5parser.cpython-38.pyc
│   │           │   │   │   │   ├── _ihatexml.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── _inputstream.cpython-38.pyc
│   │           │   │   │   │   ├── serializer.cpython-38.pyc
│   │           │   │   │   │   ├── _tokenizer.cpython-38.pyc
│   │           │   │   │   │   └── _utils.cpython-38.pyc
│   │           │   │   │   ├── treeadapters
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── genshi.cpython-38.pyc
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   └── sax.cpython-38.pyc
│   │           │   │   │   │   ├── genshi.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── sax.py
│   │           │   │   │   ├── treebuilders
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── base.cpython-38.pyc
│   │           │   │   │   │   │   ├── dom.cpython-38.pyc
│   │           │   │   │   │   │   ├── etree.cpython-38.pyc
│   │           │   │   │   │   │   ├── etree_lxml.cpython-38.pyc
│   │           │   │   │   │   │   └── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── base.py
│   │           │   │   │   │   ├── dom.py
│   │           │   │   │   │   ├── etree_lxml.py
│   │           │   │   │   │   ├── etree.py
│   │           │   │   │   │   └── __init__.py
│   │           │   │   │   ├── treewalkers
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── base.cpython-38.pyc
│   │           │   │   │   │   │   ├── dom.cpython-38.pyc
│   │           │   │   │   │   │   ├── etree.cpython-38.pyc
│   │           │   │   │   │   │   ├── etree_lxml.cpython-38.pyc
│   │           │   │   │   │   │   ├── genshi.cpython-38.pyc
│   │           │   │   │   │   │   └── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── base.py
│   │           │   │   │   │   ├── dom.py
│   │           │   │   │   │   ├── etree_lxml.py
│   │           │   │   │   │   ├── etree.py
│   │           │   │   │   │   ├── genshi.py
│   │           │   │   │   │   └── __init__.py
│   │           │   │   │   ├── _trie
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── _base.cpython-38.pyc
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   └── py.cpython-38.pyc
│   │           │   │   │   │   ├── _base.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── py.py
│   │           │   │   │   ├── constants.py
│   │           │   │   │   ├── html5parser.py
│   │           │   │   │   ├── _ihatexml.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _inputstream.py
│   │           │   │   │   ├── serializer.py
│   │           │   │   │   ├── _tokenizer.py
│   │           │   │   │   └── _utils.py
│   │           │   │   ├── idna
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── codec.cpython-38.pyc
│   │           │   │   │   │   ├── compat.cpython-38.pyc
│   │           │   │   │   │   ├── core.cpython-38.pyc
│   │           │   │   │   │   ├── idnadata.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── intranges.cpython-38.pyc
│   │           │   │   │   │   ├── package_data.cpython-38.pyc
│   │           │   │   │   │   └── uts46data.cpython-38.pyc
│   │           │   │   │   ├── codec.py
│   │           │   │   │   ├── compat.py
│   │           │   │   │   ├── core.py
│   │           │   │   │   ├── idnadata.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── intranges.py
│   │           │   │   │   ├── package_data.py
│   │           │   │   │   └── uts46data.py
│   │           │   │   ├── msgpack
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── exceptions.cpython-38.pyc
│   │           │   │   │   │   ├── ext.cpython-38.pyc
│   │           │   │   │   │   ├── fallback.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   └── _version.cpython-38.pyc
│   │           │   │   │   ├── exceptions.py
│   │           │   │   │   ├── ext.py
│   │           │   │   │   ├── fallback.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── _version.py
│   │           │   │   ├── packaging
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __about__.cpython-38.pyc
│   │           │   │   │   │   ├── _compat.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── markers.cpython-38.pyc
│   │           │   │   │   │   ├── requirements.cpython-38.pyc
│   │           │   │   │   │   ├── specifiers.cpython-38.pyc
│   │           │   │   │   │   ├── _structures.cpython-38.pyc
│   │           │   │   │   │   ├── tags.cpython-38.pyc
│   │           │   │   │   │   ├── _typing.cpython-38.pyc
│   │           │   │   │   │   ├── utils.cpython-38.pyc
│   │           │   │   │   │   └── version.cpython-38.pyc
│   │           │   │   │   ├── __about__.py
│   │           │   │   │   ├── _compat.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── markers.py
│   │           │   │   │   ├── requirements.py
│   │           │   │   │   ├── specifiers.py
│   │           │   │   │   ├── _structures.py
│   │           │   │   │   ├── tags.py
│   │           │   │   │   ├── _typing.py
│   │           │   │   │   ├── utils.py
│   │           │   │   │   └── version.py
│   │           │   │   ├── pep517
│   │           │   │   │   ├── in_process
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   └── _in_process.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── _in_process.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── build.cpython-38.pyc
│   │           │   │   │   │   ├── check.cpython-38.pyc
│   │           │   │   │   │   ├── colorlog.cpython-38.pyc
│   │           │   │   │   │   ├── compat.cpython-38.pyc
│   │           │   │   │   │   ├── dirtools.cpython-38.pyc
│   │           │   │   │   │   ├── envbuild.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── meta.cpython-38.pyc
│   │           │   │   │   │   └── wrappers.cpython-38.pyc
│   │           │   │   │   ├── build.py
│   │           │   │   │   ├── check.py
│   │           │   │   │   ├── colorlog.py
│   │           │   │   │   ├── compat.py
│   │           │   │   │   ├── dirtools.py
│   │           │   │   │   ├── envbuild.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── meta.py
│   │           │   │   │   └── wrappers.py
│   │           │   │   ├── pkg_resources
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   └── py31compat.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── py31compat.py
│   │           │   │   ├── progress
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── bar.cpython-38.pyc
│   │           │   │   │   │   ├── counter.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   └── spinner.cpython-38.pyc
│   │           │   │   │   ├── bar.py
│   │           │   │   │   ├── counter.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── spinner.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── appdirs.cpython-38.pyc
│   │           │   │   │   ├── distro.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── pyparsing.cpython-38.pyc
│   │           │   │   │   └── six.cpython-38.pyc
│   │           │   │   ├── requests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── adapters.cpython-38.pyc
│   │           │   │   │   │   ├── api.cpython-38.pyc
│   │           │   │   │   │   ├── auth.cpython-38.pyc
│   │           │   │   │   │   ├── certs.cpython-38.pyc
│   │           │   │   │   │   ├── compat.cpython-38.pyc
│   │           │   │   │   │   ├── cookies.cpython-38.pyc
│   │           │   │   │   │   ├── exceptions.cpython-38.pyc
│   │           │   │   │   │   ├── help.cpython-38.pyc
│   │           │   │   │   │   ├── hooks.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── _internal_utils.cpython-38.pyc
│   │           │   │   │   │   ├── models.cpython-38.pyc
│   │           │   │   │   │   ├── packages.cpython-38.pyc
│   │           │   │   │   │   ├── sessions.cpython-38.pyc
│   │           │   │   │   │   ├── status_codes.cpython-38.pyc
│   │           │   │   │   │   ├── structures.cpython-38.pyc
│   │           │   │   │   │   ├── utils.cpython-38.pyc
│   │           │   │   │   │   └── __version__.cpython-38.pyc
│   │           │   │   │   ├── adapters.py
│   │           │   │   │   ├── api.py
│   │           │   │   │   ├── auth.py
│   │           │   │   │   ├── certs.py
│   │           │   │   │   ├── compat.py
│   │           │   │   │   ├── cookies.py
│   │           │   │   │   ├── exceptions.py
│   │           │   │   │   ├── help.py
│   │           │   │   │   ├── hooks.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _internal_utils.py
│   │           │   │   │   ├── models.py
│   │           │   │   │   ├── packages.py
│   │           │   │   │   ├── sessions.py
│   │           │   │   │   ├── status_codes.py
│   │           │   │   │   ├── structures.py
│   │           │   │   │   ├── utils.py
│   │           │   │   │   └── __version__.py
│   │           │   │   ├── resolvelib
│   │           │   │   │   ├── compat
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── collections_abc.cpython-38.pyc
│   │           │   │   │   │   │   └── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── collections_abc.py
│   │           │   │   │   │   └── __init__.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── providers.cpython-38.pyc
│   │           │   │   │   │   ├── reporters.cpython-38.pyc
│   │           │   │   │   │   ├── resolvers.cpython-38.pyc
│   │           │   │   │   │   └── structs.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── providers.py
│   │           │   │   │   ├── reporters.py
│   │           │   │   │   ├── resolvers.py
│   │           │   │   │   └── structs.py
│   │           │   │   ├── tenacity
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── after.cpython-38.pyc
│   │           │   │   │   │   ├── _asyncio.cpython-38.pyc
│   │           │   │   │   │   ├── before.cpython-38.pyc
│   │           │   │   │   │   ├── before_sleep.cpython-38.pyc
│   │           │   │   │   │   ├── compat.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── nap.cpython-38.pyc
│   │           │   │   │   │   ├── retry.cpython-38.pyc
│   │           │   │   │   │   ├── stop.cpython-38.pyc
│   │           │   │   │   │   ├── tornadoweb.cpython-38.pyc
│   │           │   │   │   │   ├── _utils.cpython-38.pyc
│   │           │   │   │   │   └── wait.cpython-38.pyc
│   │           │   │   │   ├── after.py
│   │           │   │   │   ├── _asyncio.py
│   │           │   │   │   ├── before.py
│   │           │   │   │   ├── before_sleep.py
│   │           │   │   │   ├── compat.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── nap.py
│   │           │   │   │   ├── retry.py
│   │           │   │   │   ├── stop.py
│   │           │   │   │   ├── tornadoweb.py
│   │           │   │   │   ├── _utils.py
│   │           │   │   │   └── wait.py
│   │           │   │   ├── toml
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── decoder.cpython-38.pyc
│   │           │   │   │   │   ├── encoder.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── ordered.cpython-38.pyc
│   │           │   │   │   │   └── tz.cpython-38.pyc
│   │           │   │   │   ├── decoder.py
│   │           │   │   │   ├── encoder.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── ordered.py
│   │           │   │   │   └── tz.py
│   │           │   │   ├── urllib3
│   │           │   │   │   ├── contrib
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── appengine.cpython-38.pyc
│   │           │   │   │   │   │   ├── _appengine_environ.cpython-38.pyc
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   ├── ntlmpool.cpython-38.pyc
│   │           │   │   │   │   │   ├── pyopenssl.cpython-38.pyc
│   │           │   │   │   │   │   ├── securetransport.cpython-38.pyc
│   │           │   │   │   │   │   └── socks.cpython-38.pyc
│   │           │   │   │   │   ├── _securetransport
│   │           │   │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   │   ├── bindings.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   │   └── low_level.cpython-38.pyc
│   │           │   │   │   │   │   ├── bindings.py
│   │           │   │   │   │   │   ├── __init__.py
│   │           │   │   │   │   │   └── low_level.py
│   │           │   │   │   │   ├── _appengine_environ.py
│   │           │   │   │   │   ├── appengine.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── ntlmpool.py
│   │           │   │   │   │   ├── pyopenssl.py
│   │           │   │   │   │   ├── securetransport.py
│   │           │   │   │   │   └── socks.py
│   │           │   │   │   ├── packages
│   │           │   │   │   │   ├── backports
│   │           │   │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   │   └── makefile.cpython-38.pyc
│   │           │   │   │   │   │   ├── __init__.py
│   │           │   │   │   │   │   └── makefile.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   └── six.cpython-38.pyc
│   │           │   │   │   │   ├── ssl_match_hostname
│   │           │   │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   │   ├── _implementation.cpython-38.pyc
│   │           │   │   │   │   │   │   └── __init__.cpython-38.pyc
│   │           │   │   │   │   │   ├── _implementation.py
│   │           │   │   │   │   │   └── __init__.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── six.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── _collections.cpython-38.pyc
│   │           │   │   │   │   ├── connection.cpython-38.pyc
│   │           │   │   │   │   ├── connectionpool.cpython-38.pyc
│   │           │   │   │   │   ├── exceptions.cpython-38.pyc
│   │           │   │   │   │   ├── fields.cpython-38.pyc
│   │           │   │   │   │   ├── filepost.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── poolmanager.cpython-38.pyc
│   │           │   │   │   │   ├── request.cpython-38.pyc
│   │           │   │   │   │   ├── response.cpython-38.pyc
│   │           │   │   │   │   └── _version.cpython-38.pyc
│   │           │   │   │   ├── util
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── connection.cpython-38.pyc
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   ├── proxy.cpython-38.pyc
│   │           │   │   │   │   │   ├── queue.cpython-38.pyc
│   │           │   │   │   │   │   ├── request.cpython-38.pyc
│   │           │   │   │   │   │   ├── response.cpython-38.pyc
│   │           │   │   │   │   │   ├── retry.cpython-38.pyc
│   │           │   │   │   │   │   ├── ssl_.cpython-38.pyc
│   │           │   │   │   │   │   ├── ssltransport.cpython-38.pyc
│   │           │   │   │   │   │   ├── timeout.cpython-38.pyc
│   │           │   │   │   │   │   ├── url.cpython-38.pyc
│   │           │   │   │   │   │   └── wait.cpython-38.pyc
│   │           │   │   │   │   ├── connection.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── proxy.py
│   │           │   │   │   │   ├── queue.py
│   │           │   │   │   │   ├── request.py
│   │           │   │   │   │   ├── response.py
│   │           │   │   │   │   ├── retry.py
│   │           │   │   │   │   ├── ssl_.py
│   │           │   │   │   │   ├── ssltransport.py
│   │           │   │   │   │   ├── timeout.py
│   │           │   │   │   │   ├── url.py
│   │           │   │   │   │   └── wait.py
│   │           │   │   │   ├── _collections.py
│   │           │   │   │   ├── connectionpool.py
│   │           │   │   │   ├── connection.py
│   │           │   │   │   ├── exceptions.py
│   │           │   │   │   ├── fields.py
│   │           │   │   │   ├── filepost.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── poolmanager.py
│   │           │   │   │   ├── request.py
│   │           │   │   │   ├── response.py
│   │           │   │   │   └── _version.py
│   │           │   │   ├── webencodings
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── labels.cpython-38.pyc
│   │           │   │   │   │   ├── mklabels.cpython-38.pyc
│   │           │   │   │   │   ├── tests.cpython-38.pyc
│   │           │   │   │   │   └── x_user_defined.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── labels.py
│   │           │   │   │   ├── mklabels.py
│   │           │   │   │   ├── tests.py
│   │           │   │   │   └── x_user_defined.py
│   │           │   │   ├── appdirs.py
│   │           │   │   ├── distro.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── pyparsing.py
│   │           │   │   ├── six.py
│   │           │   │   └── vendor.txt
│   │           │   ├── __init__.py
│   │           │   ├── __main__.py
│   │           │   └── py.typed
│   │           ├── pip-21.1.2.dist-info
│   │           │   ├── entry_points.txt
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE.txt
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── pkg_resources
│   │           │   ├── extern
│   │           │   │   ├── __pycache__
│   │           │   │   │   └── __init__.cpython-38.pyc
│   │           │   │   └── __init__.py
│   │           │   ├── __pycache__
│   │           │   │   └── __init__.cpython-38.pyc
│   │           │   ├── tests
│   │           │   │   └── data
│   │           │   │       └── my-test-package-source
│   │           │   │           ├── __pycache__
│   │           │   │           │   └── setup.cpython-38.pyc
│   │           │   │           └── setup.py
│   │           │   ├── _vendor
│   │           │   │   ├── packaging
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __about__.cpython-38.pyc
│   │           │   │   │   │   ├── _compat.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── markers.cpython-38.pyc
│   │           │   │   │   │   ├── requirements.cpython-38.pyc
│   │           │   │   │   │   ├── specifiers.cpython-38.pyc
│   │           │   │   │   │   ├── _structures.cpython-38.pyc
│   │           │   │   │   │   ├── tags.cpython-38.pyc
│   │           │   │   │   │   ├── _typing.cpython-38.pyc
│   │           │   │   │   │   ├── utils.cpython-38.pyc
│   │           │   │   │   │   └── version.cpython-38.pyc
│   │           │   │   │   ├── __about__.py
│   │           │   │   │   ├── _compat.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── markers.py
│   │           │   │   │   ├── requirements.py
│   │           │   │   │   ├── specifiers.py
│   │           │   │   │   ├── _structures.py
│   │           │   │   │   ├── tags.py
│   │           │   │   │   ├── _typing.py
│   │           │   │   │   ├── utils.py
│   │           │   │   │   └── version.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── appdirs.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   └── pyparsing.cpython-38.pyc
│   │           │   │   ├── appdirs.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── pyparsing.py
│   │           │   └── __init__.py
│   │           ├── pluggy
│   │           │   ├── __pycache__
│   │           │   │   ├── callers.cpython-38.pyc
│   │           │   │   ├── hooks.cpython-38.pyc
│   │           │   │   ├── __init__.cpython-38.pyc
│   │           │   │   ├── manager.cpython-38.pyc
│   │           │   │   ├── _tracing.cpython-38.pyc
│   │           │   │   └── _version.cpython-38.pyc
│   │           │   ├── callers.py
│   │           │   ├── hooks.py
│   │           │   ├── __init__.py
│   │           │   ├── manager.py
│   │           │   ├── _tracing.py
│   │           │   └── _version.py
│   │           ├── pluggy-0.13.1.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── py
│   │           │   ├── _code
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── assertion.cpython-38.pyc
│   │           │   │   │   ├── _assertionnew.cpython-38.pyc
│   │           │   │   │   ├── _assertionold.cpython-38.pyc
│   │           │   │   │   ├── code.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── _py2traceback.cpython-38.pyc
│   │           │   │   │   └── source.cpython-38.pyc
│   │           │   │   ├── _assertionnew.py
│   │           │   │   ├── _assertionold.py
│   │           │   │   ├── assertion.py
│   │           │   │   ├── code.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _py2traceback.py
│   │           │   │   └── source.py
│   │           │   ├── _io
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── capture.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── saferepr.cpython-38.pyc
│   │           │   │   │   └── terminalwriter.cpython-38.pyc
│   │           │   │   ├── capture.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── saferepr.py
│   │           │   │   └── terminalwriter.py
│   │           │   ├── _log
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── log.cpython-38.pyc
│   │           │   │   │   └── warning.cpython-38.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── log.py
│   │           │   │   └── warning.py
│   │           │   ├── _path
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── cacheutil.cpython-38.pyc
│   │           │   │   │   ├── common.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── local.cpython-38.pyc
│   │           │   │   │   ├── svnurl.cpython-38.pyc
│   │           │   │   │   └── svnwc.cpython-38.pyc
│   │           │   │   ├── cacheutil.py
│   │           │   │   ├── common.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── local.py
│   │           │   │   ├── svnurl.py
│   │           │   │   └── svnwc.py
│   │           │   ├── _process
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── cmdexec.cpython-38.pyc
│   │           │   │   │   ├── forkedfunc.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   └── killproc.cpython-38.pyc
│   │           │   │   ├── cmdexec.py
│   │           │   │   ├── forkedfunc.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── killproc.py
│   │           │   ├── __pycache__
│   │           │   │   ├── _builtin.cpython-38.pyc
│   │           │   │   ├── _error.cpython-38.pyc
│   │           │   │   ├── __init__.cpython-38.pyc
│   │           │   │   ├── __metainfo.cpython-38.pyc
│   │           │   │   ├── _std.cpython-38.pyc
│   │           │   │   ├── test.cpython-38.pyc
│   │           │   │   ├── _version.cpython-38.pyc
│   │           │   │   └── _xmlgen.cpython-38.pyc
│   │           │   ├── _vendored_packages
│   │           │   │   ├── apipkg
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   └── version.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── version.py
│   │           │   │   ├── apipkg-1.5.dist-info
│   │           │   │   │   ├── INSTALLER
│   │           │   │   │   ├── METADATA
│   │           │   │   │   ├── RECORD
│   │           │   │   │   ├── REQUESTED
│   │           │   │   │   ├── top_level.txt
│   │           │   │   │   └── WHEEL
│   │           │   │   ├── iniconfig
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   └── __init__.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── __init__.pyi
│   │           │   │   │   └── py.typed
│   │           │   │   ├── iniconfig-1.1.1.dist-info
│   │           │   │   │   ├── INSTALLER
│   │           │   │   │   ├── LICENSE
│   │           │   │   │   ├── METADATA
│   │           │   │   │   ├── RECORD
│   │           │   │   │   ├── REQUESTED
│   │           │   │   │   ├── top_level.txt
│   │           │   │   │   └── WHEEL
│   │           │   │   ├── __pycache__
│   │           │   │   │   └── __init__.cpython-38.pyc
│   │           │   │   └── __init__.py
│   │           │   ├── _builtin.py
│   │           │   ├── _error.py
│   │           │   ├── error.pyi
│   │           │   ├── iniconfig.pyi
│   │           │   ├── __init__.py
│   │           │   ├── __init__.pyi
│   │           │   ├── io.pyi
│   │           │   ├── __metainfo.py
│   │           │   ├── path.pyi
│   │           │   ├── py.typed
│   │           │   ├── _std.py
│   │           │   ├── test.py
│   │           │   ├── _version.py
│   │           │   ├── _xmlgen.py
│   │           │   └── xml.pyi
│   │           ├── py-1.10.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── __pycache__
│   │           │   ├── cycler.cpython-38.pyc
│   │           │   ├── decorator.cpython-38.pyc
│   │           │   ├── pylab.cpython-38.pyc
│   │           │   ├── pyparsing.cpython-38.pyc
│   │           │   ├── six.cpython-38.pyc
│   │           │   └── typing_extensions.cpython-38.pyc
│   │           ├── pyparsing-2.4.7.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── _pytest
│   │           │   ├── assertion
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── rewrite.cpython-38.pyc
│   │           │   │   │   ├── truncate.cpython-38.pyc
│   │           │   │   │   └── util.cpython-38.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── rewrite.py
│   │           │   │   ├── truncate.py
│   │           │   │   └── util.py
│   │           │   ├── _code
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── code.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   └── source.cpython-38.pyc
│   │           │   │   ├── code.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── source.py
│   │           │   ├── config
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── argparsing.cpython-38.pyc
│   │           │   │   │   ├── exceptions.cpython-38.pyc
│   │           │   │   │   ├── findpaths.cpython-38.pyc
│   │           │   │   │   └── __init__.cpython-38.pyc
│   │           │   │   ├── argparsing.py
│   │           │   │   ├── exceptions.py
│   │           │   │   ├── findpaths.py
│   │           │   │   └── __init__.py
│   │           │   ├── _io
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── saferepr.cpython-38.pyc
│   │           │   │   │   ├── terminalwriter.cpython-38.pyc
│   │           │   │   │   └── wcwidth.cpython-38.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── saferepr.py
│   │           │   │   ├── terminalwriter.py
│   │           │   │   └── wcwidth.py
│   │           │   ├── mark
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── expression.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   └── structures.cpython-38.pyc
│   │           │   │   ├── expression.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── structures.py
│   │           │   ├── __pycache__
│   │           │   │   ├── _argcomplete.cpython-38.pyc
│   │           │   │   ├── cacheprovider.cpython-38.pyc
│   │           │   │   ├── capture.cpython-38.pyc
│   │           │   │   ├── compat.cpython-38.pyc
│   │           │   │   ├── debugging.cpython-38.pyc
│   │           │   │   ├── deprecated.cpython-38.pyc
│   │           │   │   ├── doctest.cpython-38.pyc
│   │           │   │   ├── faulthandler.cpython-38.pyc
│   │           │   │   ├── fixtures.cpython-38.pyc
│   │           │   │   ├── freeze_support.cpython-38.pyc
│   │           │   │   ├── helpconfig.cpython-38.pyc
│   │           │   │   ├── hookspec.cpython-38.pyc
│   │           │   │   ├── __init__.cpython-38.pyc
│   │           │   │   ├── junitxml.cpython-38.pyc
│   │           │   │   ├── logging.cpython-38.pyc
│   │           │   │   ├── main.cpython-38.pyc
│   │           │   │   ├── monkeypatch.cpython-38.pyc
│   │           │   │   ├── nodes.cpython-38.pyc
│   │           │   │   ├── nose.cpython-38.pyc
│   │           │   │   ├── outcomes.cpython-38.pyc
│   │           │   │   ├── pastebin.cpython-38.pyc
│   │           │   │   ├── pathlib.cpython-38.pyc
│   │           │   │   ├── pytester_assertions.cpython-38.pyc
│   │           │   │   ├── pytester.cpython-38.pyc
│   │           │   │   ├── python_api.cpython-38.pyc
│   │           │   │   ├── python.cpython-38.pyc
│   │           │   │   ├── recwarn.cpython-38.pyc
│   │           │   │   ├── reports.cpython-38.pyc
│   │           │   │   ├── runner.cpython-38.pyc
│   │           │   │   ├── setuponly.cpython-38.pyc
│   │           │   │   ├── setupplan.cpython-38.pyc
│   │           │   │   ├── skipping.cpython-38.pyc
│   │           │   │   ├── stepwise.cpython-38.pyc
│   │           │   │   ├── store.cpython-38.pyc
│   │           │   │   ├── terminal.cpython-38.pyc
│   │           │   │   ├── threadexception.cpython-38.pyc
│   │           │   │   ├── timing.cpython-38.pyc
│   │           │   │   ├── tmpdir.cpython-38.pyc
│   │           │   │   ├── unittest.cpython-38.pyc
│   │           │   │   ├── unraisableexception.cpython-38.pyc
│   │           │   │   ├── _version.cpython-38.pyc
│   │           │   │   ├── warnings.cpython-38.pyc
│   │           │   │   └── warning_types.cpython-38.pyc
│   │           │   ├── _argcomplete.py
│   │           │   ├── cacheprovider.py
│   │           │   ├── capture.py
│   │           │   ├── compat.py
│   │           │   ├── debugging.py
│   │           │   ├── deprecated.py
│   │           │   ├── doctest.py
│   │           │   ├── faulthandler.py
│   │           │   ├── fixtures.py
│   │           │   ├── freeze_support.py
│   │           │   ├── helpconfig.py
│   │           │   ├── hookspec.py
│   │           │   ├── __init__.py
│   │           │   ├── junitxml.py
│   │           │   ├── logging.py
│   │           │   ├── main.py
│   │           │   ├── monkeypatch.py
│   │           │   ├── nodes.py
│   │           │   ├── nose.py
│   │           │   ├── outcomes.py
│   │           │   ├── pastebin.py
│   │           │   ├── pathlib.py
│   │           │   ├── pytester_assertions.py
│   │           │   ├── pytester.py
│   │           │   ├── python_api.py
│   │           │   ├── python.py
│   │           │   ├── py.typed
│   │           │   ├── recwarn.py
│   │           │   ├── reports.py
│   │           │   ├── runner.py
│   │           │   ├── setuponly.py
│   │           │   ├── setupplan.py
│   │           │   ├── skipping.py
│   │           │   ├── stepwise.py
│   │           │   ├── store.py
│   │           │   ├── terminal.py
│   │           │   ├── threadexception.py
│   │           │   ├── timing.py
│   │           │   ├── tmpdir.py
│   │           │   ├── unittest.py
│   │           │   ├── unraisableexception.py
│   │           │   ├── _version.py
│   │           │   ├── warnings.py
│   │           │   └── warning_types.py
│   │           ├── pytest
│   │           │   ├── __pycache__
│   │           │   │   ├── collect.cpython-38.pyc
│   │           │   │   ├── __init__.cpython-38.pyc
│   │           │   │   └── __main__.cpython-38.pyc
│   │           │   ├── collect.py
│   │           │   ├── __init__.py
│   │           │   ├── __main__.py
│   │           │   └── py.typed
│   │           ├── pytest-6.2.4.dist-info
│   │           │   ├── entry_points.txt
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── REQUESTED
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── python_dateutil-2.8.1.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   ├── WHEEL
│   │           │   └── zip-safe
│   │           ├── PyWavelets-1.1.1.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── pywt
│   │           │   ├── data
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── create_dat.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── _readers.cpython-38.pyc
│   │           │   │   │   └── _wavelab_signals.cpython-38.pyc
│   │           │   │   ├── aero.npz
│   │           │   │   ├── ascent.npz
│   │           │   │   ├── camera.npz
│   │           │   │   ├── create_dat.py
│   │           │   │   ├── ecg.npy
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _readers.py
│   │           │   │   ├── sst_nino3.npz
│   │           │   │   └── _wavelab_signals.py
│   │           │   ├── _extensions
│   │           │   │   ├── __pycache__
│   │           │   │   │   └── __init__.cpython-38.pyc
│   │           │   │   ├── _cwt.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _dwt.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _pywt.cpython-38-x86_64-linux-gnu.so
│   │           │   │   └── _swt.cpython-38-x86_64-linux-gnu.so
│   │           │   ├── __pycache__
│   │           │   │   ├── _c99_config.cpython-38.pyc
│   │           │   │   ├── conftest.cpython-38.pyc
│   │           │   │   ├── _cwt.cpython-38.pyc
│   │           │   │   ├── _doc_utils.cpython-38.pyc
│   │           │   │   ├── _dwt.cpython-38.pyc
│   │           │   │   ├── _functions.cpython-38.pyc
│   │           │   │   ├── __init__.cpython-38.pyc
│   │           │   │   ├── _multidim.cpython-38.pyc
│   │           │   │   ├── _multilevel.cpython-38.pyc
│   │           │   │   ├── _pytest.cpython-38.pyc
│   │           │   │   ├── _pytesttester.cpython-38.pyc
│   │           │   │   ├── _swt.cpython-38.pyc
│   │           │   │   ├── _thresholding.cpython-38.pyc
│   │           │   │   ├── _utils.cpython-38.pyc
│   │           │   │   ├── version.cpython-38.pyc
│   │           │   │   └── _wavelet_packets.cpython-38.pyc
│   │           │   ├── tests
│   │           │   │   ├── data
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── generate_matlab_data.cpython-38.pyc
│   │           │   │   │   │   └── generate_matlab_data_cwt.cpython-38.pyc
│   │           │   │   │   ├── cwt_matlabR2015b_result.npz
│   │           │   │   │   ├── dwt_matlabR2012a_result.npz
│   │           │   │   │   ├── generate_matlab_data_cwt.py
│   │           │   │   │   ├── generate_matlab_data.py
│   │           │   │   │   └── wavelab_test_signals.npz
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── test_concurrent.cpython-38.pyc
│   │           │   │   │   ├── test_cwt_wavelets.cpython-38.pyc
│   │           │   │   │   ├── test_data.cpython-38.pyc
│   │           │   │   │   ├── test_deprecations.cpython-38.pyc
│   │           │   │   │   ├── test_doc.cpython-38.pyc
│   │           │   │   │   ├── test_dwt_idwt.cpython-38.pyc
│   │           │   │   │   ├── test_functions.cpython-38.pyc
│   │           │   │   │   ├── test_matlab_compatibility.cpython-38.pyc
│   │           │   │   │   ├── test_matlab_compatibility_cwt.cpython-38.pyc
│   │           │   │   │   ├── test_modes.cpython-38.pyc
│   │           │   │   │   ├── test_multidim.cpython-38.pyc
│   │           │   │   │   ├── test_multilevel.cpython-38.pyc
│   │           │   │   │   ├── test_perfect_reconstruction.cpython-38.pyc
│   │           │   │   │   ├── test__pywt.cpython-38.pyc
│   │           │   │   │   ├── test_swt.cpython-38.pyc
│   │           │   │   │   ├── test_thresholding.cpython-38.pyc
│   │           │   │   │   ├── test_wavelet.cpython-38.pyc
│   │           │   │   │   ├── test_wp2d.cpython-38.pyc
│   │           │   │   │   └── test_wp.cpython-38.pyc
│   │           │   │   ├── test_concurrent.py
│   │           │   │   ├── test_cwt_wavelets.py
│   │           │   │   ├── test_data.py
│   │           │   │   ├── test_deprecations.py
│   │           │   │   ├── test_doc.py
│   │           │   │   ├── test_dwt_idwt.py
│   │           │   │   ├── test_functions.py
│   │           │   │   ├── test_matlab_compatibility_cwt.py
│   │           │   │   ├── test_matlab_compatibility.py
│   │           │   │   ├── test_modes.py
│   │           │   │   ├── test_multidim.py
│   │           │   │   ├── test_multilevel.py
│   │           │   │   ├── test_perfect_reconstruction.py
│   │           │   │   ├── test__pywt.py
│   │           │   │   ├── test_swt.py
│   │           │   │   ├── test_thresholding.py
│   │           │   │   ├── test_wavelet.py
│   │           │   │   ├── test_wp2d.py
│   │           │   │   └── test_wp.py
│   │           │   ├── _c99_config.py
│   │           │   ├── conftest.py
│   │           │   ├── _cwt.py
│   │           │   ├── _doc_utils.py
│   │           │   ├── _dwt.py
│   │           │   ├── _functions.py
│   │           │   ├── __init__.py
│   │           │   ├── _multidim.py
│   │           │   ├── _multilevel.py
│   │           │   ├── _pytest.py
│   │           │   ├── _pytesttester.py
│   │           │   ├── _swt.py
│   │           │   ├── _thresholding.py
│   │           │   ├── _utils.py
│   │           │   ├── version.py
│   │           │   └── _wavelet_packets.py
│   │           ├── requests
│   │           │   ├── __pycache__
│   │           │   │   ├── adapters.cpython-38.pyc
│   │           │   │   ├── api.cpython-38.pyc
│   │           │   │   ├── auth.cpython-38.pyc
│   │           │   │   ├── certs.cpython-38.pyc
│   │           │   │   ├── compat.cpython-38.pyc
│   │           │   │   ├── cookies.cpython-38.pyc
│   │           │   │   ├── exceptions.cpython-38.pyc
│   │           │   │   ├── help.cpython-38.pyc
│   │           │   │   ├── hooks.cpython-38.pyc
│   │           │   │   ├── __init__.cpython-38.pyc
│   │           │   │   ├── _internal_utils.cpython-38.pyc
│   │           │   │   ├── models.cpython-38.pyc
│   │           │   │   ├── packages.cpython-38.pyc
│   │           │   │   ├── sessions.cpython-38.pyc
│   │           │   │   ├── status_codes.cpython-38.pyc
│   │           │   │   ├── structures.cpython-38.pyc
│   │           │   │   ├── utils.cpython-38.pyc
│   │           │   │   └── __version__.cpython-38.pyc
│   │           │   ├── adapters.py
│   │           │   ├── api.py
│   │           │   ├── auth.py
│   │           │   ├── certs.py
│   │           │   ├── compat.py
│   │           │   ├── cookies.py
│   │           │   ├── exceptions.py
│   │           │   ├── help.py
│   │           │   ├── hooks.py
│   │           │   ├── __init__.py
│   │           │   ├── _internal_utils.py
│   │           │   ├── models.py
│   │           │   ├── packages.py
│   │           │   ├── sessions.py
│   │           │   ├── status_codes.py
│   │           │   ├── structures.py
│   │           │   ├── utils.py
│   │           │   └── __version__.py
│   │           ├── requests-2.25.1.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── REQUESTED
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── scikit_image-0.18.1.dist-info
│   │           │   ├── entry_points.txt
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE.txt
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── REQUESTED
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── scikit_image.libs
│   │           │   └── libgomp-3300acd3.so.1.0.0
│   │           ├── scipy
│   │           │   ├── _build_utils
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── compiler_helper.cpython-38.pyc
│   │           │   │   │   ├── _fortran.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   └── system_info.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   └── test_scipy_version.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── test_scipy_version.py
│   │           │   │   ├── compiler_helper.py
│   │           │   │   ├── _fortran.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── setup.py
│   │           │   │   └── system_info.py
│   │           │   ├── cluster
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── hierarchy.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   └── vq.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── hierarchy_test_data.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_disjoint_set.cpython-38.pyc
│   │           │   │   │   │   ├── test_hierarchy.cpython-38.pyc
│   │           │   │   │   │   └── test_vq.cpython-38.pyc
│   │           │   │   │   ├── hierarchy_test_data.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_disjoint_set.py
│   │           │   │   │   ├── test_hierarchy.py
│   │           │   │   │   └── test_vq.py
│   │           │   │   ├── _hierarchy.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── hierarchy.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _optimal_leaf_ordering.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── setup.py
│   │           │   │   ├── _vq.cpython-38-x86_64-linux-gnu.so
│   │           │   │   └── vq.py
│   │           │   ├── constants
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── codata.cpython-38.pyc
│   │           │   │   │   ├── constants.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   └── setup.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_codata.cpython-38.pyc
│   │           │   │   │   │   └── test_constants.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_codata.py
│   │           │   │   │   └── test_constants.py
│   │           │   │   ├── codata.py
│   │           │   │   ├── constants.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── setup.py
│   │           │   ├── fft
│   │           │   │   ├── _pocketfft
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── basic.cpython-38.pyc
│   │           │   │   │   │   ├── helper.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── realtransforms.cpython-38.pyc
│   │           │   │   │   │   └── setup.cpython-38.pyc
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_basic.cpython-38.pyc
│   │           │   │   │   │   │   └── test_real_transforms.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── test_basic.py
│   │           │   │   │   │   └── test_real_transforms.py
│   │           │   │   │   ├── basic.py
│   │           │   │   │   ├── helper.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── LICENSE.md
│   │           │   │   │   ├── pypocketfft.cpython-38-x86_64-linux-gnu.so
│   │           │   │   │   ├── realtransforms.py
│   │           │   │   │   └── setup.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── _backend.cpython-38.pyc
│   │           │   │   │   ├── _basic.cpython-38.pyc
│   │           │   │   │   ├── _debug_backends.cpython-38.pyc
│   │           │   │   │   ├── _helper.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── _realtransforms.cpython-38.pyc
│   │           │   │   │   └── setup.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── mock_backend.cpython-38.pyc
│   │           │   │   │   │   ├── test_backend.cpython-38.pyc
│   │           │   │   │   │   ├── test_fft_function.cpython-38.pyc
│   │           │   │   │   │   ├── test_helper.cpython-38.pyc
│   │           │   │   │   │   ├── test_multithreading.cpython-38.pyc
│   │           │   │   │   │   ├── test_numpy.cpython-38.pyc
│   │           │   │   │   │   └── test_real_transforms.cpython-38.pyc
│   │           │   │   │   ├── mock_backend.py
│   │           │   │   │   ├── test_backend.py
│   │           │   │   │   ├── test_fft_function.py
│   │           │   │   │   ├── test_helper.py
│   │           │   │   │   ├── test_multithreading.py
│   │           │   │   │   ├── test_numpy.py
│   │           │   │   │   └── test_real_transforms.py
│   │           │   │   ├── _backend.py
│   │           │   │   ├── _basic.py
│   │           │   │   ├── _debug_backends.py
│   │           │   │   ├── _helper.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _realtransforms.py
│   │           │   │   └── setup.py
│   │           │   ├── fftpack
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── basic.cpython-38.pyc
│   │           │   │   │   ├── helper.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── pseudo_diffs.cpython-38.pyc
│   │           │   │   │   ├── realtransforms.cpython-38.pyc
│   │           │   │   │   └── setup.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── gendata.cpython-38.pyc
│   │           │   │   │   │   ├── gen_fftw_ref.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_basic.cpython-38.pyc
│   │           │   │   │   │   ├── test_helper.cpython-38.pyc
│   │           │   │   │   │   ├── test_import.cpython-38.pyc
│   │           │   │   │   │   ├── test_pseudo_diffs.cpython-38.pyc
│   │           │   │   │   │   └── test_real_transforms.cpython-38.pyc
│   │           │   │   │   ├── fftw_dct.c
│   │           │   │   │   ├── fftw_double_ref.npz
│   │           │   │   │   ├── fftw_longdouble_ref.npz
│   │           │   │   │   ├── fftw_single_ref.npz
│   │           │   │   │   ├── gendata.m
│   │           │   │   │   ├── gendata.py
│   │           │   │   │   ├── gen_fftw_ref.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── Makefile
│   │           │   │   │   ├── test_basic.py
│   │           │   │   │   ├── test_helper.py
│   │           │   │   │   ├── test_import.py
│   │           │   │   │   ├── test.npz
│   │           │   │   │   ├── test_pseudo_diffs.py
│   │           │   │   │   └── test_real_transforms.py
│   │           │   │   ├── basic.py
│   │           │   │   ├── convolve.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── helper.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── pseudo_diffs.py
│   │           │   │   ├── realtransforms.py
│   │           │   │   └── setup.py
│   │           │   ├── integrate
│   │           │   │   ├── _ivp
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── base.cpython-38.pyc
│   │           │   │   │   │   ├── bdf.cpython-38.pyc
│   │           │   │   │   │   ├── common.cpython-38.pyc
│   │           │   │   │   │   ├── dop853_coefficients.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── ivp.cpython-38.pyc
│   │           │   │   │   │   ├── lsoda.cpython-38.pyc
│   │           │   │   │   │   ├── radau.cpython-38.pyc
│   │           │   │   │   │   ├── rk.cpython-38.pyc
│   │           │   │   │   │   └── setup.cpython-38.pyc
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── test_ivp.cpython-38.pyc
│   │           │   │   │   │   │   └── test_rk.cpython-38.pyc
│   │           │   │   │   │   ├── test_ivp.py
│   │           │   │   │   │   └── test_rk.py
│   │           │   │   │   ├── base.py
│   │           │   │   │   ├── bdf.py
│   │           │   │   │   ├── common.py
│   │           │   │   │   ├── dop853_coefficients.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── ivp.py
│   │           │   │   │   ├── lsoda.py
│   │           │   │   │   ├── radau.py
│   │           │   │   │   ├── rk.py
│   │           │   │   │   └── setup.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── _bvp.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── _ode.cpython-38.pyc
│   │           │   │   │   ├── odepack.cpython-38.pyc
│   │           │   │   │   ├── quadpack.cpython-38.pyc
│   │           │   │   │   ├── _quadrature.cpython-38.pyc
│   │           │   │   │   ├── _quad_vec.cpython-38.pyc
│   │           │   │   │   └── setup.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_banded_ode_solvers.cpython-38.pyc
│   │           │   │   │   │   ├── test_bvp.cpython-38.pyc
│   │           │   │   │   │   ├── test_integrate.cpython-38.pyc
│   │           │   │   │   │   ├── test_odeint_jac.cpython-38.pyc
│   │           │   │   │   │   ├── test_quadpack.cpython-38.pyc
│   │           │   │   │   │   ├── test_quadrature.cpython-38.pyc
│   │           │   │   │   │   └── test__quad_vec.cpython-38.pyc
│   │           │   │   │   ├── banded5x5.f
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_banded_ode_solvers.py
│   │           │   │   │   ├── test_bvp.py
│   │           │   │   │   ├── test_integrate.py
│   │           │   │   │   ├── _test_multivariate.c
│   │           │   │   │   ├── test_odeint_jac.py
│   │           │   │   │   ├── test_quadpack.py
│   │           │   │   │   ├── test_quadrature.py
│   │           │   │   │   └── test__quad_vec.py
│   │           │   │   ├── _bvp.py
│   │           │   │   ├── _dop.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── __init__.py
│   │           │   │   ├── lsoda.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _odepack.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── odepack.py
│   │           │   │   ├── _ode.py
│   │           │   │   ├── _quadpack.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── quadpack.py
│   │           │   │   ├── _quadrature.py
│   │           │   │   ├── _quad_vec.py
│   │           │   │   ├── setup.py
│   │           │   │   ├── _test_multivariate.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _test_odeint_banded.cpython-38-x86_64-linux-gnu.so
│   │           │   │   └── vode.cpython-38-x86_64-linux-gnu.so
│   │           │   ├── interpolate
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── _bsplines.cpython-38.pyc
│   │           │   │   │   ├── _cubic.cpython-38.pyc
│   │           │   │   │   ├── fitpack2.cpython-38.pyc
│   │           │   │   │   ├── fitpack.cpython-38.pyc
│   │           │   │   │   ├── _fitpack_impl.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── interpnd_info.cpython-38.pyc
│   │           │   │   │   ├── interpolate.cpython-38.pyc
│   │           │   │   │   ├── ndgriddata.cpython-38.pyc
│   │           │   │   │   ├── _pade.cpython-38.pyc
│   │           │   │   │   ├── polyint.cpython-38.pyc
│   │           │   │   │   ├── rbf.cpython-38.pyc
│   │           │   │   │   └── setup.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── data
│   │           │   │   │   │   ├── bug-1310.npz
│   │           │   │   │   │   └── estimate_gradients_hang.npy
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_bsplines.cpython-38.pyc
│   │           │   │   │   │   ├── test_fitpack2.cpython-38.pyc
│   │           │   │   │   │   ├── test_fitpack.cpython-38.pyc
│   │           │   │   │   │   ├── test_gil.cpython-38.pyc
│   │           │   │   │   │   ├── test_interpnd.cpython-38.pyc
│   │           │   │   │   │   ├── test_interpolate.cpython-38.pyc
│   │           │   │   │   │   ├── test_ndgriddata.cpython-38.pyc
│   │           │   │   │   │   ├── test_pade.cpython-38.pyc
│   │           │   │   │   │   ├── test_polyint.cpython-38.pyc
│   │           │   │   │   │   ├── test_rbf.cpython-38.pyc
│   │           │   │   │   │   └── test_regression.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_bsplines.py
│   │           │   │   │   ├── test_fitpack2.py
│   │           │   │   │   ├── test_fitpack.py
│   │           │   │   │   ├── test_gil.py
│   │           │   │   │   ├── test_interpnd.py
│   │           │   │   │   ├── test_interpolate.py
│   │           │   │   │   ├── test_ndgriddata.py
│   │           │   │   │   ├── test_pade.py
│   │           │   │   │   ├── test_polyint.py
│   │           │   │   │   ├── test_rbf.py
│   │           │   │   │   └── test_regression.py
│   │           │   │   ├── _bspl.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _bsplines.py
│   │           │   │   ├── _cubic.py
│   │           │   │   ├── dfitpack.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── fitpack2.py
│   │           │   │   ├── _fitpack.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _fitpack_impl.py
│   │           │   │   ├── fitpack.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── interpnd.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── interpnd_info.py
│   │           │   │   ├── interpolate.py
│   │           │   │   ├── ndgriddata.py
│   │           │   │   ├── _pade.py
│   │           │   │   ├── polyint.py
│   │           │   │   ├── _ppoly.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── rbf.py
│   │           │   │   └── setup.py
│   │           │   ├── io
│   │           │   │   ├── arff
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── arffread.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   └── setup.cpython-38.pyc
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── data
│   │           │   │   │   │   │   ├── iris.arff
│   │           │   │   │   │   │   ├── missing.arff
│   │           │   │   │   │   │   ├── nodata.arff
│   │           │   │   │   │   │   ├── quoted_nominal.arff
│   │           │   │   │   │   │   ├── quoted_nominal_spaces.arff
│   │           │   │   │   │   │   ├── test10.arff
│   │           │   │   │   │   │   ├── test11.arff
│   │           │   │   │   │   │   ├── test1.arff
│   │           │   │   │   │   │   ├── test2.arff
│   │           │   │   │   │   │   ├── test3.arff
│   │           │   │   │   │   │   ├── test4.arff
│   │           │   │   │   │   │   ├── test5.arff
│   │           │   │   │   │   │   ├── test6.arff
│   │           │   │   │   │   │   ├── test7.arff
│   │           │   │   │   │   │   ├── test8.arff
│   │           │   │   │   │   │   └── test9.arff
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   └── test_arffread.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── test_arffread.py
│   │           │   │   │   ├── arffread.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── setup.py
│   │           │   │   ├── harwell_boeing
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── _fortran_format_parser.cpython-38.pyc
│   │           │   │   │   │   ├── hb.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   └── setup.cpython-38.pyc
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_fortran_format.cpython-38.pyc
│   │           │   │   │   │   │   └── test_hb.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── test_fortran_format.py
│   │           │   │   │   │   └── test_hb.py
│   │           │   │   │   ├── _fortran_format_parser.py
│   │           │   │   │   ├── hb.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── setup.py
│   │           │   │   ├── matlab
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── byteordercodes.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── mio4.cpython-38.pyc
│   │           │   │   │   │   ├── mio5.cpython-38.pyc
│   │           │   │   │   │   ├── mio5_params.cpython-38.pyc
│   │           │   │   │   │   ├── miobase.cpython-38.pyc
│   │           │   │   │   │   ├── mio.cpython-38.pyc
│   │           │   │   │   │   └── setup.cpython-38.pyc
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── data
│   │           │   │   │   │   │   ├── bad_miuint32.mat
│   │           │   │   │   │   │   ├── bad_miutf8_array_name.mat
│   │           │   │   │   │   │   ├── big_endian.mat
│   │           │   │   │   │   │   ├── broken_utf8.mat
│   │           │   │   │   │   │   ├── corrupted_zlib_checksum.mat
│   │           │   │   │   │   │   ├── corrupted_zlib_data.mat
│   │           │   │   │   │   │   ├── japanese_utf8.txt
│   │           │   │   │   │   │   ├── little_endian.mat
│   │           │   │   │   │   │   ├── logical_sparse.mat
│   │           │   │   │   │   │   ├── malformed1.mat
│   │           │   │   │   │   │   ├── miuint32_for_miint32.mat
│   │           │   │   │   │   │   ├── miutf8_array_name.mat
│   │           │   │   │   │   │   ├── nasty_duplicate_fieldnames.mat
│   │           │   │   │   │   │   ├── one_by_zero_char.mat
│   │           │   │   │   │   │   ├── parabola.mat
│   │           │   │   │   │   │   ├── single_empty_string.mat
│   │           │   │   │   │   │   ├── some_functions.mat
│   │           │   │   │   │   │   ├── sqr.mat
│   │           │   │   │   │   │   ├── test3dmatrix_6.1_SOL2.mat
│   │           │   │   │   │   │   ├── test3dmatrix_6.5.1_GLNX86.mat
│   │           │   │   │   │   │   ├── test3dmatrix_7.1_GLNX86.mat
│   │           │   │   │   │   │   ├── test3dmatrix_7.4_GLNX86.mat
│   │           │   │   │   │   │   ├── testbool_8_WIN64.mat
│   │           │   │   │   │   │   ├── testcell_6.1_SOL2.mat
│   │           │   │   │   │   │   ├── testcell_6.5.1_GLNX86.mat
│   │           │   │   │   │   │   ├── testcell_7.1_GLNX86.mat
│   │           │   │   │   │   │   ├── testcell_7.4_GLNX86.mat
│   │           │   │   │   │   │   ├── testcellnest_6.1_SOL2.mat
│   │           │   │   │   │   │   ├── testcellnest_6.5.1_GLNX86.mat
│   │           │   │   │   │   │   ├── testcellnest_7.1_GLNX86.mat
│   │           │   │   │   │   │   ├── testcellnest_7.4_GLNX86.mat
│   │           │   │   │   │   │   ├── testcomplex_4.2c_SOL2.mat
│   │           │   │   │   │   │   ├── testcomplex_6.1_SOL2.mat
│   │           │   │   │   │   │   ├── testcomplex_6.5.1_GLNX86.mat
│   │           │   │   │   │   │   ├── testcomplex_7.1_GLNX86.mat
│   │           │   │   │   │   │   ├── testcomplex_7.4_GLNX86.mat
│   │           │   │   │   │   │   ├── testdouble_4.2c_SOL2.mat
│   │           │   │   │   │   │   ├── testdouble_6.1_SOL2.mat
│   │           │   │   │   │   │   ├── testdouble_6.5.1_GLNX86.mat
│   │           │   │   │   │   │   ├── testdouble_7.1_GLNX86.mat
│   │           │   │   │   │   │   ├── testdouble_7.4_GLNX86.mat
│   │           │   │   │   │   │   ├── testemptycell_5.3_SOL2.mat
│   │           │   │   │   │   │   ├── testemptycell_6.5.1_GLNX86.mat
│   │           │   │   │   │   │   ├── testemptycell_7.1_GLNX86.mat
│   │           │   │   │   │   │   ├── testemptycell_7.4_GLNX86.mat
│   │           │   │   │   │   │   ├── test_empty_struct.mat
│   │           │   │   │   │   │   ├── testfunc_7.4_GLNX86.mat
│   │           │   │   │   │   │   ├── testhdf5_7.4_GLNX86.mat
│   │           │   │   │   │   │   ├── test_mat4_le_floats.mat
│   │           │   │   │   │   │   ├── testmatrix_4.2c_SOL2.mat
│   │           │   │   │   │   │   ├── testmatrix_6.1_SOL2.mat
│   │           │   │   │   │   │   ├── testmatrix_6.5.1_GLNX86.mat
│   │           │   │   │   │   │   ├── testmatrix_7.1_GLNX86.mat
│   │           │   │   │   │   │   ├── testmatrix_7.4_GLNX86.mat
│   │           │   │   │   │   │   ├── testminus_4.2c_SOL2.mat
│   │           │   │   │   │   │   ├── testminus_6.1_SOL2.mat
│   │           │   │   │   │   │   ├── testminus_6.5.1_GLNX86.mat
│   │           │   │   │   │   │   ├── testminus_7.1_GLNX86.mat
│   │           │   │   │   │   │   ├── testminus_7.4_GLNX86.mat
│   │           │   │   │   │   │   ├── testmulti_4.2c_SOL2.mat
│   │           │   │   │   │   │   ├── testmulti_7.1_GLNX86.mat
│   │           │   │   │   │   │   ├── testmulti_7.4_GLNX86.mat
│   │           │   │   │   │   │   ├── testobject_6.1_SOL2.mat
│   │           │   │   │   │   │   ├── testobject_6.5.1_GLNX86.mat
│   │           │   │   │   │   │   ├── testobject_7.1_GLNX86.mat
│   │           │   │   │   │   │   ├── testobject_7.4_GLNX86.mat
│   │           │   │   │   │   │   ├── testonechar_4.2c_SOL2.mat
│   │           │   │   │   │   │   ├── testonechar_6.1_SOL2.mat
│   │           │   │   │   │   │   ├── testonechar_6.5.1_GLNX86.mat
│   │           │   │   │   │   │   ├── testonechar_7.1_GLNX86.mat
│   │           │   │   │   │   │   ├── testonechar_7.4_GLNX86.mat
│   │           │   │   │   │   │   ├── testscalarcell_7.4_GLNX86.mat
│   │           │   │   │   │   │   ├── testsimplecell.mat
│   │           │   │   │   │   │   ├── test_skip_variable.mat
│   │           │   │   │   │   │   ├── testsparse_4.2c_SOL2.mat
│   │           │   │   │   │   │   ├── testsparse_6.1_SOL2.mat
│   │           │   │   │   │   │   ├── testsparse_6.5.1_GLNX86.mat
│   │           │   │   │   │   │   ├── testsparse_7.1_GLNX86.mat
│   │           │   │   │   │   │   ├── testsparse_7.4_GLNX86.mat
│   │           │   │   │   │   │   ├── testsparsecomplex_4.2c_SOL2.mat
│   │           │   │   │   │   │   ├── testsparsecomplex_6.1_SOL2.mat
│   │           │   │   │   │   │   ├── testsparsecomplex_6.5.1_GLNX86.mat
│   │           │   │   │   │   │   ├── testsparsecomplex_7.1_GLNX86.mat
│   │           │   │   │   │   │   ├── testsparsecomplex_7.4_GLNX86.mat
│   │           │   │   │   │   │   ├── testsparsefloat_7.4_GLNX86.mat
│   │           │   │   │   │   │   ├── teststring_4.2c_SOL2.mat
│   │           │   │   │   │   │   ├── teststring_6.1_SOL2.mat
│   │           │   │   │   │   │   ├── teststring_6.5.1_GLNX86.mat
│   │           │   │   │   │   │   ├── teststring_7.1_GLNX86.mat
│   │           │   │   │   │   │   ├── teststring_7.4_GLNX86.mat
│   │           │   │   │   │   │   ├── teststringarray_4.2c_SOL2.mat
│   │           │   │   │   │   │   ├── teststringarray_6.1_SOL2.mat
│   │           │   │   │   │   │   ├── teststringarray_6.5.1_GLNX86.mat
│   │           │   │   │   │   │   ├── teststringarray_7.1_GLNX86.mat
│   │           │   │   │   │   │   ├── teststringarray_7.4_GLNX86.mat
│   │           │   │   │   │   │   ├── teststruct_6.1_SOL2.mat
│   │           │   │   │   │   │   ├── teststruct_6.5.1_GLNX86.mat
│   │           │   │   │   │   │   ├── teststruct_7.1_GLNX86.mat
│   │           │   │   │   │   │   ├── teststruct_7.4_GLNX86.mat
│   │           │   │   │   │   │   ├── teststructarr_6.1_SOL2.mat
│   │           │   │   │   │   │   ├── teststructarr_6.5.1_GLNX86.mat
│   │           │   │   │   │   │   ├── teststructarr_7.1_GLNX86.mat
│   │           │   │   │   │   │   ├── teststructarr_7.4_GLNX86.mat
│   │           │   │   │   │   │   ├── teststructnest_6.1_SOL2.mat
│   │           │   │   │   │   │   ├── teststructnest_6.5.1_GLNX86.mat
│   │           │   │   │   │   │   ├── teststructnest_7.1_GLNX86.mat
│   │           │   │   │   │   │   ├── teststructnest_7.4_GLNX86.mat
│   │           │   │   │   │   │   ├── testunicode_7.1_GLNX86.mat
│   │           │   │   │   │   │   ├── testunicode_7.4_GLNX86.mat
│   │           │   │   │   │   │   └── testvec_4_GLNX86.mat
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_byteordercodes.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_mio5_utils.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_miobase.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_mio.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_mio_funcs.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_mio_utils.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_pathological.cpython-38.pyc
│   │           │   │   │   │   │   └── test_streams.cpython-38.pyc
│   │           │   │   │   │   ├── afunc.m
│   │           │   │   │   │   ├── gen_mat4files.m
│   │           │   │   │   │   ├── gen_mat5files.m
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── save_matfile.m
│   │           │   │   │   │   ├── test_byteordercodes.py
│   │           │   │   │   │   ├── test_mio5_utils.py
│   │           │   │   │   │   ├── test_miobase.py
│   │           │   │   │   │   ├── test_mio_funcs.py
│   │           │   │   │   │   ├── test_mio.py
│   │           │   │   │   │   ├── test_mio_utils.py
│   │           │   │   │   │   ├── test_pathological.py
│   │           │   │   │   │   └── test_streams.py
│   │           │   │   │   ├── byteordercodes.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── mio4.py
│   │           │   │   │   ├── mio5_params.py
│   │           │   │   │   ├── mio5.py
│   │           │   │   │   ├── mio5_utils.cpython-38-x86_64-linux-gnu.so
│   │           │   │   │   ├── miobase.py
│   │           │   │   │   ├── mio.py
│   │           │   │   │   ├── mio_utils.cpython-38-x86_64-linux-gnu.so
│   │           │   │   │   ├── setup.py
│   │           │   │   │   └── streams.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── _fortran.cpython-38.pyc
│   │           │   │   │   ├── idl.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── mmio.cpython-38.pyc
│   │           │   │   │   ├── netcdf.cpython-38.pyc
│   │           │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   └── wavfile.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── data
│   │           │   │   │   │   ├── array_float32_1d.sav
│   │           │   │   │   │   ├── array_float32_2d.sav
│   │           │   │   │   │   ├── array_float32_3d.sav
│   │           │   │   │   │   ├── array_float32_4d.sav
│   │           │   │   │   │   ├── array_float32_5d.sav
│   │           │   │   │   │   ├── array_float32_6d.sav
│   │           │   │   │   │   ├── array_float32_7d.sav
│   │           │   │   │   │   ├── array_float32_8d.sav
│   │           │   │   │   │   ├── array_float32_pointer_1d.sav
│   │           │   │   │   │   ├── array_float32_pointer_2d.sav
│   │           │   │   │   │   ├── array_float32_pointer_3d.sav
│   │           │   │   │   │   ├── array_float32_pointer_4d.sav
│   │           │   │   │   │   ├── array_float32_pointer_5d.sav
│   │           │   │   │   │   ├── array_float32_pointer_6d.sav
│   │           │   │   │   │   ├── array_float32_pointer_7d.sav
│   │           │   │   │   │   ├── array_float32_pointer_8d.sav
│   │           │   │   │   │   ├── example_1.nc
│   │           │   │   │   │   ├── example_2.nc
│   │           │   │   │   │   ├── example_3_maskedvals.nc
│   │           │   │   │   │   ├── fortran-3x3d-2i.dat
│   │           │   │   │   │   ├── fortran-mixed.dat
│   │           │   │   │   │   ├── fortran-sf8-11x1x10.dat
│   │           │   │   │   │   ├── fortran-sf8-15x10x22.dat
│   │           │   │   │   │   ├── fortran-sf8-1x1x1.dat
│   │           │   │   │   │   ├── fortran-sf8-1x1x5.dat
│   │           │   │   │   │   ├── fortran-sf8-1x1x7.dat
│   │           │   │   │   │   ├── fortran-sf8-1x3x5.dat
│   │           │   │   │   │   ├── fortran-si4-11x1x10.dat
│   │           │   │   │   │   ├── fortran-si4-15x10x22.dat
│   │           │   │   │   │   ├── fortran-si4-1x1x1.dat
│   │           │   │   │   │   ├── fortran-si4-1x1x5.dat
│   │           │   │   │   │   ├── fortran-si4-1x1x7.dat
│   │           │   │   │   │   ├── fortran-si4-1x3x5.dat
│   │           │   │   │   │   ├── invalid_pointer.sav
│   │           │   │   │   │   ├── null_pointer.sav
│   │           │   │   │   │   ├── scalar_byte_descr.sav
│   │           │   │   │   │   ├── scalar_byte.sav
│   │           │   │   │   │   ├── scalar_complex32.sav
│   │           │   │   │   │   ├── scalar_complex64.sav
│   │           │   │   │   │   ├── scalar_float32.sav
│   │           │   │   │   │   ├── scalar_float64.sav
│   │           │   │   │   │   ├── scalar_heap_pointer.sav
│   │           │   │   │   │   ├── scalar_int16.sav
│   │           │   │   │   │   ├── scalar_int32.sav
│   │           │   │   │   │   ├── scalar_int64.sav
│   │           │   │   │   │   ├── scalar_string.sav
│   │           │   │   │   │   ├── scalar_uint16.sav
│   │           │   │   │   │   ├── scalar_uint32.sav
│   │           │   │   │   │   ├── scalar_uint64.sav
│   │           │   │   │   │   ├── struct_arrays_byte_idl80.sav
│   │           │   │   │   │   ├── struct_arrays_replicated_3d.sav
│   │           │   │   │   │   ├── struct_arrays_replicated.sav
│   │           │   │   │   │   ├── struct_arrays.sav
│   │           │   │   │   │   ├── struct_inherit.sav
│   │           │   │   │   │   ├── struct_pointer_arrays_replicated_3d.sav
│   │           │   │   │   │   ├── struct_pointer_arrays_replicated.sav
│   │           │   │   │   │   ├── struct_pointer_arrays.sav
│   │           │   │   │   │   ├── struct_pointers_replicated_3d.sav
│   │           │   │   │   │   ├── struct_pointers_replicated.sav
│   │           │   │   │   │   ├── struct_pointers.sav
│   │           │   │   │   │   ├── struct_scalars_replicated_3d.sav
│   │           │   │   │   │   ├── struct_scalars_replicated.sav
│   │           │   │   │   │   ├── struct_scalars.sav
│   │           │   │   │   │   ├── test-44100Hz-2ch-32bit-float-be.wav
│   │           │   │   │   │   ├── test-44100Hz-2ch-32bit-float-le.wav
│   │           │   │   │   │   ├── test-44100Hz-be-1ch-4bytes.wav
│   │           │   │   │   │   ├── test-44100Hz-le-1ch-4bytes-early-eof-no-data.wav
│   │           │   │   │   │   ├── test-44100Hz-le-1ch-4bytes-early-eof.wav
│   │           │   │   │   │   ├── test-44100Hz-le-1ch-4bytes-incomplete-chunk.wav
│   │           │   │   │   │   ├── test-44100Hz-le-1ch-4bytes.wav
│   │           │   │   │   │   ├── test-48000Hz-2ch-64bit-float-le-wavex.wav
│   │           │   │   │   │   ├── test-8000Hz-be-3ch-5S-24bit.wav
│   │           │   │   │   │   ├── test-8000Hz-le-1ch-10S-20bit-extra.wav
│   │           │   │   │   │   ├── test-8000Hz-le-1ch-1byte-ulaw.wav
│   │           │   │   │   │   ├── test-8000Hz-le-2ch-1byteu.wav
│   │           │   │   │   │   ├── test-8000Hz-le-3ch-5S-24bit.wav
│   │           │   │   │   │   ├── test-8000Hz-le-3ch-5S-36bit.wav
│   │           │   │   │   │   ├── test-8000Hz-le-3ch-5S-45bit.wav
│   │           │   │   │   │   ├── test-8000Hz-le-3ch-5S-53bit.wav
│   │           │   │   │   │   ├── test-8000Hz-le-3ch-5S-64bit.wav
│   │           │   │   │   │   ├── test-8000Hz-le-4ch-9S-12bit.wav
│   │           │   │   │   │   ├── test-8000Hz-le-5ch-9S-5bit.wav
│   │           │   │   │   │   ├── Transparent Busy.ani
│   │           │   │   │   │   └── various_compressed.sav
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_fortran.cpython-38.pyc
│   │           │   │   │   │   ├── test_idl.cpython-38.pyc
│   │           │   │   │   │   ├── test_mmio.cpython-38.pyc
│   │           │   │   │   │   ├── test_netcdf.cpython-38.pyc
│   │           │   │   │   │   ├── test_paths.cpython-38.pyc
│   │           │   │   │   │   └── test_wavfile.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_fortran.py
│   │           │   │   │   ├── test_idl.py
│   │           │   │   │   ├── test_mmio.py
│   │           │   │   │   ├── test_netcdf.py
│   │           │   │   │   ├── test_paths.py
│   │           │   │   │   └── test_wavfile.py
│   │           │   │   ├── _fortran.py
│   │           │   │   ├── idl.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── mmio.py
│   │           │   │   ├── netcdf.py
│   │           │   │   ├── setup.py
│   │           │   │   ├── _test_fortran.cpython-38-x86_64-linux-gnu.so
│   │           │   │   └── wavfile.py
│   │           │   ├── _lib
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── _bunch.cpython-38.pyc
│   │           │   │   │   ├── _ccallback.cpython-38.pyc
│   │           │   │   │   ├── decorator.cpython-38.pyc
│   │           │   │   │   ├── deprecation.cpython-38.pyc
│   │           │   │   │   ├── _disjoint_set.cpython-38.pyc
│   │           │   │   │   ├── doccer.cpython-38.pyc
│   │           │   │   │   ├── _gcutils.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── _pep440.cpython-38.pyc
│   │           │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   ├── _testutils.cpython-38.pyc
│   │           │   │   │   ├── _threadsafety.cpython-38.pyc
│   │           │   │   │   ├── _tmpdirs.cpython-38.pyc
│   │           │   │   │   ├── uarray.cpython-38.pyc
│   │           │   │   │   └── _util.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_bunch.cpython-38.pyc
│   │           │   │   │   │   ├── test_ccallback.cpython-38.pyc
│   │           │   │   │   │   ├── test_deprecation.cpython-38.pyc
│   │           │   │   │   │   ├── test__gcutils.cpython-38.pyc
│   │           │   │   │   │   ├── test_import_cycles.cpython-38.pyc
│   │           │   │   │   │   ├── test_linear_assignment.cpython-38.pyc
│   │           │   │   │   │   ├── test__pep440.cpython-38.pyc
│   │           │   │   │   │   ├── test__testutils.cpython-38.pyc
│   │           │   │   │   │   ├── test__threadsafety.cpython-38.pyc
│   │           │   │   │   │   ├── test_tmpdirs.cpython-38.pyc
│   │           │   │   │   │   ├── test__util.cpython-38.pyc
│   │           │   │   │   │   └── test_warnings.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_bunch.py
│   │           │   │   │   ├── test_ccallback.py
│   │           │   │   │   ├── test_deprecation.py
│   │           │   │   │   ├── test__gcutils.py
│   │           │   │   │   ├── test_import_cycles.py
│   │           │   │   │   ├── test_linear_assignment.py
│   │           │   │   │   ├── test__pep440.py
│   │           │   │   │   ├── test__testutils.py
│   │           │   │   │   ├── test__threadsafety.py
│   │           │   │   │   ├── test_tmpdirs.py
│   │           │   │   │   ├── test__util.py
│   │           │   │   │   └── test_warnings.py
│   │           │   │   ├── _uarray
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── _backend.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   └── setup.cpython-38.pyc
│   │           │   │   │   ├── _backend.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── LICENSE
│   │           │   │   │   ├── setup.py
│   │           │   │   │   └── _uarray.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _bunch.py
│   │           │   │   ├── _ccallback_c.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _ccallback.py
│   │           │   │   ├── decorator.py
│   │           │   │   ├── deprecation.py
│   │           │   │   ├── _disjoint_set.py
│   │           │   │   ├── doccer.py
│   │           │   │   ├── _fpumode.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _gcutils.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── messagestream.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _pep440.py
│   │           │   │   ├── setup.py
│   │           │   │   ├── _test_ccallback.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _test_deprecation_call.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _test_deprecation_def.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _testutils.py
│   │           │   │   ├── _threadsafety.py
│   │           │   │   ├── _tmpdirs.py
│   │           │   │   ├── uarray.py
│   │           │   │   └── _util.py
│   │           │   ├── linalg
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── basic.cpython-38.pyc
│   │           │   │   │   ├── blas.cpython-38.pyc
│   │           │   │   │   ├── _cython_signature_generator.cpython-38.pyc
│   │           │   │   │   ├── decomp_cholesky.cpython-38.pyc
│   │           │   │   │   ├── _decomp_cossin.cpython-38.pyc
│   │           │   │   │   ├── decomp.cpython-38.pyc
│   │           │   │   │   ├── _decomp_ldl.cpython-38.pyc
│   │           │   │   │   ├── decomp_lu.cpython-38.pyc
│   │           │   │   │   ├── _decomp_polar.cpython-38.pyc
│   │           │   │   │   ├── decomp_qr.cpython-38.pyc
│   │           │   │   │   ├── _decomp_qz.cpython-38.pyc
│   │           │   │   │   ├── decomp_schur.cpython-38.pyc
│   │           │   │   │   ├── decomp_svd.cpython-38.pyc
│   │           │   │   │   ├── _expm_frechet.cpython-38.pyc
│   │           │   │   │   ├── flinalg.cpython-38.pyc
│   │           │   │   │   ├── _generate_pyx.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── _interpolative_backend.cpython-38.pyc
│   │           │   │   │   ├── interpolative.cpython-38.pyc
│   │           │   │   │   ├── lapack.cpython-38.pyc
│   │           │   │   │   ├── matfuncs.cpython-38.pyc
│   │           │   │   │   ├── _matfuncs_inv_ssq.cpython-38.pyc
│   │           │   │   │   ├── _matfuncs_sqrtm.cpython-38.pyc
│   │           │   │   │   ├── misc.cpython-38.pyc
│   │           │   │   │   ├── _procrustes.cpython-38.pyc
│   │           │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   ├── _sketches.cpython-38.pyc
│   │           │   │   │   ├── _solvers.cpython-38.pyc
│   │           │   │   │   ├── special_matrices.cpython-38.pyc
│   │           │   │   │   └── _testutils.cpython-38.pyc
│   │           │   │   ├── src
│   │           │   │   │   ├── id_dist
│   │           │   │   │   │   └── doc
│   │           │   │   │   │       └── doc.tex
│   │           │   │   │   └── lapack_deprecations
│   │           │   │   │       └── LICENSE
│   │           │   │   ├── tests
│   │           │   │   │   ├── data
│   │           │   │   │   │   ├── carex_15_data.npz
│   │           │   │   │   │   ├── carex_18_data.npz
│   │           │   │   │   │   ├── carex_19_data.npz
│   │           │   │   │   │   ├── carex_20_data.npz
│   │           │   │   │   │   ├── carex_6_data.npz
│   │           │   │   │   │   └── gendare_20170120_data.npz
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_basic.cpython-38.pyc
│   │           │   │   │   │   ├── test_blas.cpython-38.pyc
│   │           │   │   │   │   ├── test_build.cpython-38.pyc
│   │           │   │   │   │   ├── test_cython_blas.cpython-38.pyc
│   │           │   │   │   │   ├── test_cython_lapack.cpython-38.pyc
│   │           │   │   │   │   ├── test_decomp_cholesky.cpython-38.pyc
│   │           │   │   │   │   ├── test_decomp_cossin.cpython-38.pyc
│   │           │   │   │   │   ├── test_decomp.cpython-38.pyc
│   │           │   │   │   │   ├── test_decomp_ldl.cpython-38.pyc
│   │           │   │   │   │   ├── test_decomp_polar.cpython-38.pyc
│   │           │   │   │   │   ├── test_decomp_update.cpython-38.pyc
│   │           │   │   │   │   ├── test_fblas.cpython-38.pyc
│   │           │   │   │   │   ├── test_interpolative.cpython-38.pyc
│   │           │   │   │   │   ├── test_lapack.cpython-38.pyc
│   │           │   │   │   │   ├── test_matfuncs.cpython-38.pyc
│   │           │   │   │   │   ├── test_matmul_toeplitz.cpython-38.pyc
│   │           │   │   │   │   ├── test_procrustes.cpython-38.pyc
│   │           │   │   │   │   ├── test_sketches.cpython-38.pyc
│   │           │   │   │   │   ├── test_solvers.cpython-38.pyc
│   │           │   │   │   │   ├── test_solve_toeplitz.cpython-38.pyc
│   │           │   │   │   │   └── test_special_matrices.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_basic.py
│   │           │   │   │   ├── test_blas.py
│   │           │   │   │   ├── test_build.py
│   │           │   │   │   ├── test_cython_blas.py
│   │           │   │   │   ├── test_cython_lapack.py
│   │           │   │   │   ├── test_decomp_cholesky.py
│   │           │   │   │   ├── test_decomp_cossin.py
│   │           │   │   │   ├── test_decomp_ldl.py
│   │           │   │   │   ├── test_decomp_polar.py
│   │           │   │   │   ├── test_decomp.py
│   │           │   │   │   ├── test_decomp_update.py
│   │           │   │   │   ├── test_fblas.py
│   │           │   │   │   ├── test_interpolative.py
│   │           │   │   │   ├── test_lapack.py
│   │           │   │   │   ├── test_matfuncs.py
│   │           │   │   │   ├── test_matmul_toeplitz.py
│   │           │   │   │   ├── test_procrustes.py
│   │           │   │   │   ├── test_sketches.py
│   │           │   │   │   ├── test_solvers.py
│   │           │   │   │   ├── test_solve_toeplitz.py
│   │           │   │   │   └── test_special_matrices.py
│   │           │   │   ├── basic.py
│   │           │   │   ├── blas.py
│   │           │   │   ├── cython_blas.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── cython_blas.pxd
│   │           │   │   ├── cython_lapack.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── cython_lapack.pxd
│   │           │   │   ├── _cython_signature_generator.py
│   │           │   │   ├── decomp_cholesky.py
│   │           │   │   ├── _decomp_cossin.py
│   │           │   │   ├── _decomp_ldl.py
│   │           │   │   ├── decomp_lu.py
│   │           │   │   ├── _decomp_polar.py
│   │           │   │   ├── decomp.py
│   │           │   │   ├── decomp_qr.py
│   │           │   │   ├── _decomp_qz.py
│   │           │   │   ├── decomp_schur.py
│   │           │   │   ├── decomp_svd.py
│   │           │   │   ├── _decomp_update.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _expm_frechet.py
│   │           │   │   ├── _fblas.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _flapack.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _flinalg.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── flinalg.py
│   │           │   │   ├── _generate_pyx.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _interpolative_backend.py
│   │           │   │   ├── _interpolative.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── interpolative.py
│   │           │   │   ├── lapack.py
│   │           │   │   ├── _matfuncs_inv_ssq.py
│   │           │   │   ├── matfuncs.py
│   │           │   │   ├── _matfuncs_sqrtm.py
│   │           │   │   ├── _matfuncs_sqrtm_triu.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── misc.py
│   │           │   │   ├── _procrustes.py
│   │           │   │   ├── setup.py
│   │           │   │   ├── _sketches.py
│   │           │   │   ├── _solvers.py
│   │           │   │   ├── _solve_toeplitz.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── special_matrices.py
│   │           │   │   └── _testutils.py
│   │           │   ├── misc
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── common.cpython-38.pyc
│   │           │   │   │   ├── doccer.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   └── setup.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_common.cpython-38.pyc
│   │           │   │   │   │   └── test_doccer.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_common.py
│   │           │   │   │   └── test_doccer.py
│   │           │   │   ├── ascent.dat
│   │           │   │   ├── common.py
│   │           │   │   ├── doccer.py
│   │           │   │   ├── ecg.dat
│   │           │   │   ├── face.dat
│   │           │   │   ├── __init__.py
│   │           │   │   └── setup.py
│   │           │   ├── ndimage
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── filters.cpython-38.pyc
│   │           │   │   │   ├── fourier.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── interpolation.cpython-38.pyc
│   │           │   │   │   ├── measurements.cpython-38.pyc
│   │           │   │   │   ├── morphology.cpython-38.pyc
│   │           │   │   │   ├── _ni_docstrings.cpython-38.pyc
│   │           │   │   │   ├── _ni_support.cpython-38.pyc
│   │           │   │   │   └── setup.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── data
│   │           │   │   │   │   ├── label_inputs.txt
│   │           │   │   │   │   ├── label_results.txt
│   │           │   │   │   │   ├── label_strels.txt
│   │           │   │   │   │   └── README.txt
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_c_api.cpython-38.pyc
│   │           │   │   │   │   ├── test_datatypes.cpython-38.pyc
│   │           │   │   │   │   ├── test_filters.cpython-38.pyc
│   │           │   │   │   │   ├── test_fourier.cpython-38.pyc
│   │           │   │   │   │   ├── test_interpolation.cpython-38.pyc
│   │           │   │   │   │   ├── test_measurements.cpython-38.pyc
│   │           │   │   │   │   ├── test_morphology.cpython-38.pyc
│   │           │   │   │   │   └── test_splines.cpython-38.pyc
│   │           │   │   │   ├── dots.png
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_c_api.py
│   │           │   │   │   ├── test_datatypes.py
│   │           │   │   │   ├── test_filters.py
│   │           │   │   │   ├── test_fourier.py
│   │           │   │   │   ├── test_interpolation.py
│   │           │   │   │   ├── test_measurements.py
│   │           │   │   │   ├── test_morphology.py
│   │           │   │   │   └── test_splines.py
│   │           │   │   ├── _ctest.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _cytest.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── filters.py
│   │           │   │   ├── fourier.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── interpolation.py
│   │           │   │   ├── measurements.py
│   │           │   │   ├── morphology.py
│   │           │   │   ├── _nd_image.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _ni_docstrings.py
│   │           │   │   ├── _ni_label.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _ni_support.py
│   │           │   │   └── setup.py
│   │           │   ├── odr
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── _add_newdocs.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── models.cpython-38.pyc
│   │           │   │   │   ├── odrpack.cpython-38.pyc
│   │           │   │   │   └── setup.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   └── test_odr.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── test_odr.py
│   │           │   │   ├── _add_newdocs.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── models.py
│   │           │   │   ├── __odrpack.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── odrpack.py
│   │           │   │   └── setup.py
│   │           │   ├── optimize
│   │           │   │   ├── cython_optimize
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   └── __init__.cpython-38.pyc
│   │           │   │   │   ├── c_zeros.pxd
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _zeros.cpython-38-x86_64-linux-gnu.so
│   │           │   │   │   └── _zeros.pxd
│   │           │   │   ├── _highs
│   │           │   │   │   ├── cython
│   │           │   │   │   │   └── src
│   │           │   │   │   │       ├── HConst.pxd
│   │           │   │   │   │       ├── highs_c_api.pxd
│   │           │   │   │   │       ├── HighsInfo.pxd
│   │           │   │   │   │       ├── HighsIO.pxd
│   │           │   │   │   │       ├── HighsLp.pxd
│   │           │   │   │   │       ├── HighsLpUtils.pxd
│   │           │   │   │   │       ├── HighsMipSolver.pxd
│   │           │   │   │   │       ├── HighsModelUtils.pxd
│   │           │   │   │   │       ├── HighsOptions.pxd
│   │           │   │   │   │       ├── Highs.pxd
│   │           │   │   │   │       ├── HighsRuntimeOptions.pxd
│   │           │   │   │   │       ├── HighsStatus.pxd
│   │           │   │   │   │       └── SimplexConst.pxd
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   └── setup.cpython-38.pyc
│   │           │   │   │   ├── _highs_constants.cpython-38-x86_64-linux-gnu.so
│   │           │   │   │   ├── _highs_wrapper.cpython-38-x86_64-linux-gnu.so
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _mpswriter.cpython-38-x86_64-linux-gnu.so
│   │           │   │   │   └── setup.py
│   │           │   │   ├── lbfgsb_src
│   │           │   │   │   └── README
│   │           │   │   ├── _lsq
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── bvls.cpython-38.pyc
│   │           │   │   │   │   ├── common.cpython-38.pyc
│   │           │   │   │   │   ├── dogbox.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── least_squares.cpython-38.pyc
│   │           │   │   │   │   ├── lsq_linear.cpython-38.pyc
│   │           │   │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   │   ├── trf.cpython-38.pyc
│   │           │   │   │   │   └── trf_linear.cpython-38.pyc
│   │           │   │   │   ├── bvls.py
│   │           │   │   │   ├── common.py
│   │           │   │   │   ├── dogbox.py
│   │           │   │   │   ├── givens_elimination.cpython-38-x86_64-linux-gnu.so
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── least_squares.py
│   │           │   │   │   ├── lsq_linear.py
│   │           │   │   │   ├── setup.py
│   │           │   │   │   ├── trf_linear.py
│   │           │   │   │   └── trf.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── _basinhopping.cpython-38.pyc
│   │           │   │   │   ├── cobyla.cpython-38.pyc
│   │           │   │   │   ├── _constraints.cpython-38.pyc
│   │           │   │   │   ├── _differentiable_functions.cpython-38.pyc
│   │           │   │   │   ├── _differentialevolution.cpython-38.pyc
│   │           │   │   │   ├── _dual_annealing.cpython-38.pyc
│   │           │   │   │   ├── _hessian_update_strategy.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── lbfgsb.cpython-38.pyc
│   │           │   │   │   ├── linesearch.cpython-38.pyc
│   │           │   │   │   ├── _linprog.cpython-38.pyc
│   │           │   │   │   ├── _linprog_doc.cpython-38.pyc
│   │           │   │   │   ├── _linprog_highs.cpython-38.pyc
│   │           │   │   │   ├── _linprog_ip.cpython-38.pyc
│   │           │   │   │   ├── _linprog_rs.cpython-38.pyc
│   │           │   │   │   ├── _linprog_simplex.cpython-38.pyc
│   │           │   │   │   ├── _linprog_util.cpython-38.pyc
│   │           │   │   │   ├── _lsap.cpython-38.pyc
│   │           │   │   │   ├── _minimize.cpython-38.pyc
│   │           │   │   │   ├── minpack.cpython-38.pyc
│   │           │   │   │   ├── _nnls.cpython-38.pyc
│   │           │   │   │   ├── nonlin.cpython-38.pyc
│   │           │   │   │   ├── _numdiff.cpython-38.pyc
│   │           │   │   │   ├── optimize.cpython-38.pyc
│   │           │   │   │   ├── _qap.cpython-38.pyc
│   │           │   │   │   ├── _remove_redundancy.cpython-38.pyc
│   │           │   │   │   ├── _root.cpython-38.pyc
│   │           │   │   │   ├── _root_scalar.cpython-38.pyc
│   │           │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   ├── _shgo.cpython-38.pyc
│   │           │   │   │   ├── slsqp.cpython-38.pyc
│   │           │   │   │   ├── _spectral.cpython-38.pyc
│   │           │   │   │   ├── tnc.cpython-38.pyc
│   │           │   │   │   ├── _trustregion.cpython-38.pyc
│   │           │   │   │   ├── _trustregion_dogleg.cpython-38.pyc
│   │           │   │   │   ├── _trustregion_exact.cpython-38.pyc
│   │           │   │   │   ├── _trustregion_krylov.cpython-38.pyc
│   │           │   │   │   ├── _trustregion_ncg.cpython-38.pyc
│   │           │   │   │   ├── _tstutils.cpython-38.pyc
│   │           │   │   │   └── zeros.cpython-38.pyc
│   │           │   │   ├── _shgo_lib
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── sobol_seq.cpython-38.pyc
│   │           │   │   │   │   └── triangulation.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── sobol_seq.py
│   │           │   │   │   ├── sobol_vec.gz
│   │           │   │   │   └── triangulation.py
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test__basinhopping.cpython-38.pyc
│   │           │   │   │   │   ├── test_cobyla.cpython-38.pyc
│   │           │   │   │   │   ├── test_constraint_conversion.cpython-38.pyc
│   │           │   │   │   │   ├── test_constraints.cpython-38.pyc
│   │           │   │   │   │   ├── test_cython_optimize.cpython-38.pyc
│   │           │   │   │   │   ├── test_differentiable_functions.cpython-38.pyc
│   │           │   │   │   │   ├── test__differential_evolution.cpython-38.pyc
│   │           │   │   │   │   ├── test__dual_annealing.cpython-38.pyc
│   │           │   │   │   │   ├── test_hessian_update_strategy.cpython-38.pyc
│   │           │   │   │   │   ├── test_lbfgsb_hessinv.cpython-38.pyc
│   │           │   │   │   │   ├── test_lbfgsb_setulb.cpython-38.pyc
│   │           │   │   │   │   ├── test_least_squares.cpython-38.pyc
│   │           │   │   │   │   ├── test_linear_assignment.cpython-38.pyc
│   │           │   │   │   │   ├── test_linesearch.cpython-38.pyc
│   │           │   │   │   │   ├── test__linprog_clean_inputs.cpython-38.pyc
│   │           │   │   │   │   ├── test_linprog.cpython-38.pyc
│   │           │   │   │   │   ├── test_lsq_common.cpython-38.pyc
│   │           │   │   │   │   ├── test_lsq_linear.cpython-38.pyc
│   │           │   │   │   │   ├── test_minimize_constrained.cpython-38.pyc
│   │           │   │   │   │   ├── test_minpack.cpython-38.pyc
│   │           │   │   │   │   ├── test_nnls.cpython-38.pyc
│   │           │   │   │   │   ├── test_nonlin.cpython-38.pyc
│   │           │   │   │   │   ├── test__numdiff.cpython-38.pyc
│   │           │   │   │   │   ├── test_optimize.cpython-38.pyc
│   │           │   │   │   │   ├── test_quadratic_assignment.cpython-38.pyc
│   │           │   │   │   │   ├── test_regression.cpython-38.pyc
│   │           │   │   │   │   ├── test__remove_redundancy.cpython-38.pyc
│   │           │   │   │   │   ├── test__root.cpython-38.pyc
│   │           │   │   │   │   ├── test__shgo.cpython-38.pyc
│   │           │   │   │   │   ├── test_slsqp.cpython-38.pyc
│   │           │   │   │   │   ├── test__spectral.cpython-38.pyc
│   │           │   │   │   │   ├── test_tnc.cpython-38.pyc
│   │           │   │   │   │   ├── test_trustregion.cpython-38.pyc
│   │           │   │   │   │   ├── test_trustregion_exact.cpython-38.pyc
│   │           │   │   │   │   ├── test_trustregion_krylov.cpython-38.pyc
│   │           │   │   │   │   └── test_zeros.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test__basinhopping.py
│   │           │   │   │   ├── test_cobyla.py
│   │           │   │   │   ├── test_constraint_conversion.py
│   │           │   │   │   ├── test_constraints.py
│   │           │   │   │   ├── test_cython_optimize.py
│   │           │   │   │   ├── test_differentiable_functions.py
│   │           │   │   │   ├── test__differential_evolution.py
│   │           │   │   │   ├── test__dual_annealing.py
│   │           │   │   │   ├── test_hessian_update_strategy.py
│   │           │   │   │   ├── test_lbfgsb_hessinv.py
│   │           │   │   │   ├── test_lbfgsb_setulb.py
│   │           │   │   │   ├── test_least_squares.py
│   │           │   │   │   ├── test_linear_assignment.py
│   │           │   │   │   ├── test_linesearch.py
│   │           │   │   │   ├── test__linprog_clean_inputs.py
│   │           │   │   │   ├── test_linprog.py
│   │           │   │   │   ├── test_lsq_common.py
│   │           │   │   │   ├── test_lsq_linear.py
│   │           │   │   │   ├── test_minimize_constrained.py
│   │           │   │   │   ├── test_minpack.py
│   │           │   │   │   ├── test_nnls.py
│   │           │   │   │   ├── test_nonlin.py
│   │           │   │   │   ├── test__numdiff.py
│   │           │   │   │   ├── test_optimize.py
│   │           │   │   │   ├── test_quadratic_assignment.py
│   │           │   │   │   ├── test_regression.py
│   │           │   │   │   ├── test__remove_redundancy.py
│   │           │   │   │   ├── test__root.py
│   │           │   │   │   ├── test__shgo.py
│   │           │   │   │   ├── test_slsqp.py
│   │           │   │   │   ├── test__spectral.py
│   │           │   │   │   ├── test_tnc.py
│   │           │   │   │   ├── test_trustregion_exact.py
│   │           │   │   │   ├── test_trustregion_krylov.py
│   │           │   │   │   ├── test_trustregion.py
│   │           │   │   │   └── test_zeros.py
│   │           │   │   ├── _trlib
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   └── setup.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── setup.py
│   │           │   │   │   └── _trlib.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _trustregion_constr
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── canonical_constraint.cpython-38.pyc
│   │           │   │   │   │   ├── equality_constrained_sqp.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── minimize_trustregion_constr.cpython-38.pyc
│   │           │   │   │   │   ├── projections.cpython-38.pyc
│   │           │   │   │   │   ├── qp_subproblem.cpython-38.pyc
│   │           │   │   │   │   ├── report.cpython-38.pyc
│   │           │   │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   │   └── tr_interior_point.cpython-38.pyc
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_canonical_constraint.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_projections.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_qp_subproblem.cpython-38.pyc
│   │           │   │   │   │   │   └── test_report.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── test_canonical_constraint.py
│   │           │   │   │   │   ├── test_projections.py
│   │           │   │   │   │   ├── test_qp_subproblem.py
│   │           │   │   │   │   └── test_report.py
│   │           │   │   │   ├── canonical_constraint.py
│   │           │   │   │   ├── equality_constrained_sqp.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── minimize_trustregion_constr.py
│   │           │   │   │   ├── projections.py
│   │           │   │   │   ├── qp_subproblem.py
│   │           │   │   │   ├── report.py
│   │           │   │   │   ├── setup.py
│   │           │   │   │   └── tr_interior_point.py
│   │           │   │   ├── _basinhopping.py
│   │           │   │   ├── _bglu_dense.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _cobyla.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── cobyla.py
│   │           │   │   ├── _constraints.py
│   │           │   │   ├── cython_optimize.pxd
│   │           │   │   ├── _differentiable_functions.py
│   │           │   │   ├── _differentialevolution.py
│   │           │   │   ├── _dual_annealing.py
│   │           │   │   ├── _group_columns.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _hessian_update_strategy.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _lbfgsb.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── lbfgsb.py
│   │           │   │   ├── linesearch.py
│   │           │   │   ├── _linprog_doc.py
│   │           │   │   ├── _linprog_highs.py
│   │           │   │   ├── _linprog_ip.py
│   │           │   │   ├── _linprog.py
│   │           │   │   ├── _linprog_rs.py
│   │           │   │   ├── _linprog_simplex.py
│   │           │   │   ├── _linprog_util.py
│   │           │   │   ├── _lsap_module.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _lsap.py
│   │           │   │   ├── _minimize.py
│   │           │   │   ├── minpack2.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _minpack.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── minpack.py
│   │           │   │   ├── moduleTNC.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── __nnls.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _nnls.py
│   │           │   │   ├── nonlin.py
│   │           │   │   ├── _numdiff.py
│   │           │   │   ├── optimize.py
│   │           │   │   ├── _qap.py
│   │           │   │   ├── _remove_redundancy.py
│   │           │   │   ├── _root.py
│   │           │   │   ├── _root_scalar.py
│   │           │   │   ├── setup.py
│   │           │   │   ├── _shgo.py
│   │           │   │   ├── _slsqp.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── slsqp.py
│   │           │   │   ├── _spectral.py
│   │           │   │   ├── tnc.py
│   │           │   │   ├── _trustregion_dogleg.py
│   │           │   │   ├── _trustregion_exact.py
│   │           │   │   ├── _trustregion_krylov.py
│   │           │   │   ├── _trustregion_ncg.py
│   │           │   │   ├── _trustregion.py
│   │           │   │   ├── _tstutils.py
│   │           │   │   ├── _zeros.cpython-38-x86_64-linux-gnu.so
│   │           │   │   └── zeros.py
│   │           │   ├── __pycache__
│   │           │   │   ├── __config__.cpython-38.pyc
│   │           │   │   ├── conftest.cpython-38.pyc
│   │           │   │   ├── _distributor_init.cpython-38.pyc
│   │           │   │   ├── __init__.cpython-38.pyc
│   │           │   │   ├── setup.cpython-38.pyc
│   │           │   │   └── version.cpython-38.pyc
│   │           │   ├── signal
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── _arraytools.cpython-38.pyc
│   │           │   │   │   ├── bsplines.cpython-38.pyc
│   │           │   │   │   ├── filter_design.cpython-38.pyc
│   │           │   │   │   ├── fir_filter_design.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── lti_conversion.cpython-38.pyc
│   │           │   │   │   ├── ltisys.cpython-38.pyc
│   │           │   │   │   ├── _max_len_seq.cpython-38.pyc
│   │           │   │   │   ├── _peak_finding.cpython-38.pyc
│   │           │   │   │   ├── _savitzky_golay.cpython-38.pyc
│   │           │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   ├── signaltools.cpython-38.pyc
│   │           │   │   │   ├── spectral.cpython-38.pyc
│   │           │   │   │   ├── _upfirdn.cpython-38.pyc
│   │           │   │   │   ├── waveforms.cpython-38.pyc
│   │           │   │   │   └── wavelets.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── mpsig.cpython-38.pyc
│   │           │   │   │   │   ├── test_array_tools.cpython-38.pyc
│   │           │   │   │   │   ├── test_bsplines.cpython-38.pyc
│   │           │   │   │   │   ├── test_cont2discrete.cpython-38.pyc
│   │           │   │   │   │   ├── test_dltisys.cpython-38.pyc
│   │           │   │   │   │   ├── test_filter_design.cpython-38.pyc
│   │           │   │   │   │   ├── test_fir_filter_design.cpython-38.pyc
│   │           │   │   │   │   ├── test_ltisys.cpython-38.pyc
│   │           │   │   │   │   ├── test_max_len_seq.cpython-38.pyc
│   │           │   │   │   │   ├── test_peak_finding.cpython-38.pyc
│   │           │   │   │   │   ├── test_result_type.cpython-38.pyc
│   │           │   │   │   │   ├── test_savitzky_golay.cpython-38.pyc
│   │           │   │   │   │   ├── test_signaltools.cpython-38.pyc
│   │           │   │   │   │   ├── test_spectral.cpython-38.pyc
│   │           │   │   │   │   ├── test_upfirdn.cpython-38.pyc
│   │           │   │   │   │   ├── test_waveforms.cpython-38.pyc
│   │           │   │   │   │   ├── test_wavelets.cpython-38.pyc
│   │           │   │   │   │   └── test_windows.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── mpsig.py
│   │           │   │   │   ├── test_array_tools.py
│   │           │   │   │   ├── test_bsplines.py
│   │           │   │   │   ├── test_cont2discrete.py
│   │           │   │   │   ├── test_dltisys.py
│   │           │   │   │   ├── test_filter_design.py
│   │           │   │   │   ├── test_fir_filter_design.py
│   │           │   │   │   ├── test_ltisys.py
│   │           │   │   │   ├── test_max_len_seq.py
│   │           │   │   │   ├── test_peak_finding.py
│   │           │   │   │   ├── test_result_type.py
│   │           │   │   │   ├── test_savitzky_golay.py
│   │           │   │   │   ├── test_signaltools.py
│   │           │   │   │   ├── test_spectral.py
│   │           │   │   │   ├── test_upfirdn.py
│   │           │   │   │   ├── test_waveforms.py
│   │           │   │   │   ├── test_wavelets.py
│   │           │   │   │   └── test_windows.py
│   │           │   │   ├── windows
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   │   └── windows.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── setup.py
│   │           │   │   │   └── windows.py
│   │           │   │   ├── _arraytools.py
│   │           │   │   ├── bsplines.py
│   │           │   │   ├── filter_design.py
│   │           │   │   ├── fir_filter_design.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── lti_conversion.py
│   │           │   │   ├── ltisys.py
│   │           │   │   ├── _max_len_seq_inner.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _max_len_seq.py
│   │           │   │   ├── _peak_finding.py
│   │           │   │   ├── _peak_finding_utils.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _savitzky_golay.py
│   │           │   │   ├── setup.py
│   │           │   │   ├── signaltools.py
│   │           │   │   ├── sigtools.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _sosfilt.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _spectral.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── spectral.py
│   │           │   │   ├── spline.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _upfirdn_apply.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _upfirdn.py
│   │           │   │   ├── waveforms.py
│   │           │   │   └── wavelets.py
│   │           │   ├── sparse
│   │           │   │   ├── csgraph
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── _laplacian.cpython-38.pyc
│   │           │   │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   │   └── _validation.cpython-38.pyc
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_connected_components.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_conversions.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_flow.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_graph_laplacian.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_matching.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_reordering.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_shortest_path.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_spanning_tree.cpython-38.pyc
│   │           │   │   │   │   │   └── test_traversal.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── test_connected_components.py
│   │           │   │   │   │   ├── test_conversions.py
│   │           │   │   │   │   ├── test_flow.py
│   │           │   │   │   │   ├── test_graph_laplacian.py
│   │           │   │   │   │   ├── test_matching.py
│   │           │   │   │   │   ├── test_reordering.py
│   │           │   │   │   │   ├── test_shortest_path.py
│   │           │   │   │   │   ├── test_spanning_tree.py
│   │           │   │   │   │   └── test_traversal.py
│   │           │   │   │   ├── _flow.cpython-38-x86_64-linux-gnu.so
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _laplacian.py
│   │           │   │   │   ├── _matching.cpython-38-x86_64-linux-gnu.so
│   │           │   │   │   ├── _min_spanning_tree.cpython-38-x86_64-linux-gnu.so
│   │           │   │   │   ├── _reordering.cpython-38-x86_64-linux-gnu.so
│   │           │   │   │   ├── setup.py
│   │           │   │   │   ├── _shortest_path.cpython-38-x86_64-linux-gnu.so
│   │           │   │   │   ├── _tools.cpython-38-x86_64-linux-gnu.so
│   │           │   │   │   ├── _traversal.cpython-38-x86_64-linux-gnu.so
│   │           │   │   │   └── _validation.py
│   │           │   │   ├── linalg
│   │           │   │   │   ├── dsolve
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── _add_newdocs.cpython-38.pyc
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   ├── linsolve.cpython-38.pyc
│   │           │   │   │   │   │   └── setup.cpython-38.pyc
│   │           │   │   │   │   ├── SuperLU
│   │           │   │   │   │   │   └── License.txt
│   │           │   │   │   │   ├── tests
│   │           │   │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   │   └── test_linsolve.cpython-38.pyc
│   │           │   │   │   │   │   ├── __init__.py
│   │           │   │   │   │   │   └── test_linsolve.py
│   │           │   │   │   │   ├── _add_newdocs.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── linsolve.py
│   │           │   │   │   │   ├── setup.py
│   │           │   │   │   │   └── _superlu.cpython-38-x86_64-linux-gnu.so
│   │           │   │   │   ├── eigen
│   │           │   │   │   │   ├── arpack
│   │           │   │   │   │   │   ├── ARPACK
│   │           │   │   │   │   │   │   └── COPYING
│   │           │   │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   │   ├── arpack.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   │   └── setup.cpython-38.pyc
│   │           │   │   │   │   │   ├── tests
│   │           │   │   │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   │   │   └── test_arpack.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── __init__.py
│   │           │   │   │   │   │   │   └── test_arpack.py
│   │           │   │   │   │   │   ├── _arpack.cpython-38-x86_64-linux-gnu.so
│   │           │   │   │   │   │   ├── arpack.py
│   │           │   │   │   │   │   ├── __init__.py
│   │           │   │   │   │   │   └── setup.py
│   │           │   │   │   │   ├── lobpcg
│   │           │   │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── lobpcg.cpython-38.pyc
│   │           │   │   │   │   │   │   └── setup.cpython-38.pyc
│   │           │   │   │   │   │   ├── tests
│   │           │   │   │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   │   │   └── test_lobpcg.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── __init__.py
│   │           │   │   │   │   │   │   └── test_lobpcg.py
│   │           │   │   │   │   │   ├── __init__.py
│   │           │   │   │   │   │   ├── lobpcg.py
│   │           │   │   │   │   │   └── setup.py
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   └── setup.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── setup.py
│   │           │   │   │   ├── isolve
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── _gcrotmk.cpython-38.pyc
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   ├── iterative.cpython-38.pyc
│   │           │   │   │   │   │   ├── lgmres.cpython-38.pyc
│   │           │   │   │   │   │   ├── lsmr.cpython-38.pyc
│   │           │   │   │   │   │   ├── lsqr.cpython-38.pyc
│   │           │   │   │   │   │   ├── minres.cpython-38.pyc
│   │           │   │   │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   │   │   └── utils.cpython-38.pyc
│   │           │   │   │   │   ├── tests
│   │           │   │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   │   ├── demo_lgmres.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── test_gcrotmk.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── test_iterative.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── test_lgmres.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── test_lsmr.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── test_lsqr.cpython-38.pyc
│   │           │   │   │   │   │   │   ├── test_minres.cpython-38.pyc
│   │           │   │   │   │   │   │   └── test_utils.cpython-38.pyc
│   │           │   │   │   │   │   ├── demo_lgmres.py
│   │           │   │   │   │   │   ├── __init__.py
│   │           │   │   │   │   │   ├── test_gcrotmk.py
│   │           │   │   │   │   │   ├── test_iterative.py
│   │           │   │   │   │   │   ├── test_lgmres.py
│   │           │   │   │   │   │   ├── test_lsmr.py
│   │           │   │   │   │   │   ├── test_lsqr.py
│   │           │   │   │   │   │   ├── test_minres.py
│   │           │   │   │   │   │   └── test_utils.py
│   │           │   │   │   │   ├── _gcrotmk.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── _iterative.cpython-38-x86_64-linux-gnu.so
│   │           │   │   │   │   ├── iterative.py
│   │           │   │   │   │   ├── lgmres.py
│   │           │   │   │   │   ├── lsmr.py
│   │           │   │   │   │   ├── lsqr.py
│   │           │   │   │   │   ├── minres.py
│   │           │   │   │   │   ├── setup.py
│   │           │   │   │   │   └── utils.py
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── _expm_multiply.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── interface.cpython-38.pyc
│   │           │   │   │   │   ├── matfuncs.cpython-38.pyc
│   │           │   │   │   │   ├── _norm.cpython-38.pyc
│   │           │   │   │   │   ├── _onenormest.cpython-38.pyc
│   │           │   │   │   │   └── setup.cpython-38.pyc
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_expm_multiply.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_interface.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_matfuncs.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_norm.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_onenormest.cpython-38.pyc
│   │           │   │   │   │   │   └── test_pydata_sparse.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── test_expm_multiply.py
│   │           │   │   │   │   ├── test_interface.py
│   │           │   │   │   │   ├── test_matfuncs.py
│   │           │   │   │   │   ├── test_norm.py
│   │           │   │   │   │   ├── test_onenormest.py
│   │           │   │   │   │   └── test_pydata_sparse.py
│   │           │   │   │   ├── _expm_multiply.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── interface.py
│   │           │   │   │   ├── matfuncs.py
│   │           │   │   │   ├── _norm.py
│   │           │   │   │   ├── _onenormest.py
│   │           │   │   │   └── setup.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── base.cpython-38.pyc
│   │           │   │   │   ├── bsr.cpython-38.pyc
│   │           │   │   │   ├── compressed.cpython-38.pyc
│   │           │   │   │   ├── construct.cpython-38.pyc
│   │           │   │   │   ├── coo.cpython-38.pyc
│   │           │   │   │   ├── csc.cpython-38.pyc
│   │           │   │   │   ├── csr.cpython-38.pyc
│   │           │   │   │   ├── data.cpython-38.pyc
│   │           │   │   │   ├── dia.cpython-38.pyc
│   │           │   │   │   ├── dok.cpython-38.pyc
│   │           │   │   │   ├── extract.cpython-38.pyc
│   │           │   │   │   ├── generate_sparsetools.cpython-38.pyc
│   │           │   │   │   ├── _index.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── lil.cpython-38.pyc
│   │           │   │   │   ├── _matrix_io.cpython-38.pyc
│   │           │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   ├── sparsetools.cpython-38.pyc
│   │           │   │   │   ├── spfuncs.cpython-38.pyc
│   │           │   │   │   └── sputils.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── data
│   │           │   │   │   │   ├── csc_py2.npz
│   │           │   │   │   │   └── csc_py3.npz
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_base.cpython-38.pyc
│   │           │   │   │   │   ├── test_construct.cpython-38.pyc
│   │           │   │   │   │   ├── test_csc.cpython-38.pyc
│   │           │   │   │   │   ├── test_csr.cpython-38.pyc
│   │           │   │   │   │   ├── test_extract.cpython-38.pyc
│   │           │   │   │   │   ├── test_matrix_io.cpython-38.pyc
│   │           │   │   │   │   ├── test_sparsetools.cpython-38.pyc
│   │           │   │   │   │   ├── test_spfuncs.cpython-38.pyc
│   │           │   │   │   │   └── test_sputils.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_base.py
│   │           │   │   │   ├── test_construct.py
│   │           │   │   │   ├── test_csc.py
│   │           │   │   │   ├── test_csr.py
│   │           │   │   │   ├── test_extract.py
│   │           │   │   │   ├── test_matrix_io.py
│   │           │   │   │   ├── test_sparsetools.py
│   │           │   │   │   ├── test_spfuncs.py
│   │           │   │   │   └── test_sputils.py
│   │           │   │   ├── base.py
│   │           │   │   ├── bsr.py
│   │           │   │   ├── compressed.py
│   │           │   │   ├── construct.py
│   │           │   │   ├── coo.py
│   │           │   │   ├── csc.py
│   │           │   │   ├── _csparsetools.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── csr.py
│   │           │   │   ├── data.py
│   │           │   │   ├── dia.py
│   │           │   │   ├── dok.py
│   │           │   │   ├── extract.py
│   │           │   │   ├── generate_sparsetools.py
│   │           │   │   ├── _index.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── lil.py
│   │           │   │   ├── _matrix_io.py
│   │           │   │   ├── setup.py
│   │           │   │   ├── _sparsetools.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── sparsetools.py
│   │           │   │   ├── spfuncs.py
│   │           │   │   └── sputils.py
│   │           │   ├── spatial
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── distance.cpython-38.pyc
│   │           │   │   │   ├── _geometric_slerp.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── kdtree.cpython-38.pyc
│   │           │   │   │   ├── _plotutils.cpython-38.pyc
│   │           │   │   │   ├── _procrustes.cpython-38.pyc
│   │           │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   └── _spherical_voronoi.cpython-38.pyc
│   │           │   │   ├── qhull_src
│   │           │   │   │   └── COPYING.txt
│   │           │   │   ├── tests
│   │           │   │   │   ├── data
│   │           │   │   │   │   ├── cdist-X1.txt
│   │           │   │   │   │   ├── cdist-X2.txt
│   │           │   │   │   │   ├── degenerate_pointset.npz
│   │           │   │   │   │   ├── iris.txt
│   │           │   │   │   │   ├── pdist-boolean-inp.txt
│   │           │   │   │   │   ├── pdist-chebyshev-ml-iris.txt
│   │           │   │   │   │   ├── pdist-chebyshev-ml.txt
│   │           │   │   │   │   ├── pdist-cityblock-ml-iris.txt
│   │           │   │   │   │   ├── pdist-cityblock-ml.txt
│   │           │   │   │   │   ├── pdist-correlation-ml-iris.txt
│   │           │   │   │   │   ├── pdist-correlation-ml.txt
│   │           │   │   │   │   ├── pdist-cosine-ml-iris.txt
│   │           │   │   │   │   ├── pdist-cosine-ml.txt
│   │           │   │   │   │   ├── pdist-double-inp.txt
│   │           │   │   │   │   ├── pdist-euclidean-ml-iris.txt
│   │           │   │   │   │   ├── pdist-euclidean-ml.txt
│   │           │   │   │   │   ├── pdist-hamming-ml.txt
│   │           │   │   │   │   ├── pdist-jaccard-ml.txt
│   │           │   │   │   │   ├── pdist-jensenshannon-ml-iris.txt
│   │           │   │   │   │   ├── pdist-jensenshannon-ml.txt
│   │           │   │   │   │   ├── pdist-minkowski-3.2-ml-iris.txt
│   │           │   │   │   │   ├── pdist-minkowski-3.2-ml.txt
│   │           │   │   │   │   ├── pdist-minkowski-5.8-ml-iris.txt
│   │           │   │   │   │   ├── pdist-seuclidean-ml-iris.txt
│   │           │   │   │   │   ├── pdist-seuclidean-ml.txt
│   │           │   │   │   │   ├── pdist-spearman-ml.txt
│   │           │   │   │   │   ├── random-bool-data.txt
│   │           │   │   │   │   ├── random-double-data.txt
│   │           │   │   │   │   ├── random-int-data.txt
│   │           │   │   │   │   ├── random-uint-data.txt
│   │           │   │   │   │   └── selfdual-4d-polytope.txt
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_distance.cpython-38.pyc
│   │           │   │   │   │   ├── test_hausdorff.cpython-38.pyc
│   │           │   │   │   │   ├── test_kdtree.cpython-38.pyc
│   │           │   │   │   │   ├── test__plotutils.cpython-38.pyc
│   │           │   │   │   │   ├── test__procrustes.cpython-38.pyc
│   │           │   │   │   │   ├── test_qhull.cpython-38.pyc
│   │           │   │   │   │   ├── test_slerp.cpython-38.pyc
│   │           │   │   │   │   └── test_spherical_voronoi.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_distance.py
│   │           │   │   │   ├── test_hausdorff.py
│   │           │   │   │   ├── test_kdtree.py
│   │           │   │   │   ├── test__plotutils.py
│   │           │   │   │   ├── test__procrustes.py
│   │           │   │   │   ├── test_qhull.py
│   │           │   │   │   ├── test_slerp.py
│   │           │   │   │   └── test_spherical_voronoi.py
│   │           │   │   ├── transform
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── _rotation_groups.cpython-38.pyc
│   │           │   │   │   │   ├── _rotation_spline.cpython-38.pyc
│   │           │   │   │   │   └── setup.cpython-38.pyc
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_rotation.cpython-38.pyc
│   │           │   │   │   │   │   ├── test_rotation_groups.cpython-38.pyc
│   │           │   │   │   │   │   └── test_rotation_spline.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── test_rotation_groups.py
│   │           │   │   │   │   ├── test_rotation.py
│   │           │   │   │   │   └── test_rotation_spline.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── rotation.cpython-38-x86_64-linux-gnu.so
│   │           │   │   │   ├── _rotation_groups.py
│   │           │   │   │   ├── _rotation_spline.py
│   │           │   │   │   └── setup.py
│   │           │   │   ├── ckdtree.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── ckdtree.pyi
│   │           │   │   ├── distance.py
│   │           │   │   ├── _distance_wrap.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _geometric_slerp.py
│   │           │   │   ├── _hausdorff.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── __init__.py
│   │           │   │   ├── kdtree.py
│   │           │   │   ├── _plotutils.py
│   │           │   │   ├── _procrustes.py
│   │           │   │   ├── qhull.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── setup.py
│   │           │   │   ├── _spherical_voronoi.py
│   │           │   │   ├── _voronoi.cpython-38-x86_64-linux-gnu.so
│   │           │   │   └── _voronoi.pyi
│   │           │   ├── special
│   │           │   │   ├── _precompute
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── expn_asy.cpython-38.pyc
│   │           │   │   │   │   ├── gammainc_asy.cpython-38.pyc
│   │           │   │   │   │   ├── gammainc_data.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── lambertw.cpython-38.pyc
│   │           │   │   │   │   ├── loggamma.cpython-38.pyc
│   │           │   │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   │   ├── struve_convergence.cpython-38.pyc
│   │           │   │   │   │   ├── utils.cpython-38.pyc
│   │           │   │   │   │   ├── wrightomega.cpython-38.pyc
│   │           │   │   │   │   └── zetac.cpython-38.pyc
│   │           │   │   │   ├── expn_asy.py
│   │           │   │   │   ├── gammainc_asy.py
│   │           │   │   │   ├── gammainc_data.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── lambertw.py
│   │           │   │   │   ├── loggamma.py
│   │           │   │   │   ├── setup.py
│   │           │   │   │   ├── struve_convergence.py
│   │           │   │   │   ├── utils.py
│   │           │   │   │   ├── wrightomega.py
│   │           │   │   │   └── zetac.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── add_newdocs.cpython-38.pyc
│   │           │   │   │   ├── _basic.cpython-38.pyc
│   │           │   │   │   ├── basic.cpython-38.pyc
│   │           │   │   │   ├── _ellip_harm.cpython-38.pyc
│   │           │   │   │   ├── _generate_pyx.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── _lambertw.cpython-38.pyc
│   │           │   │   │   ├── _logsumexp.cpython-38.pyc
│   │           │   │   │   ├── _mptestutils.cpython-38.pyc
│   │           │   │   │   ├── orthogonal.cpython-38.pyc
│   │           │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   ├── sf_error.cpython-38.pyc
│   │           │   │   │   ├── spfun_stats.cpython-38.pyc
│   │           │   │   │   ├── _spherical_bessel.cpython-38.pyc
│   │           │   │   │   └── _testutils.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── data
│   │           │   │   │   │   ├── boost.npz
│   │           │   │   │   │   ├── gsl.npz
│   │           │   │   │   │   ├── local.npz
│   │           │   │   │   │   └── README
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_basic.cpython-38.pyc
│   │           │   │   │   │   ├── test_bdtr.cpython-38.pyc
│   │           │   │   │   │   ├── test_boxcox.cpython-38.pyc
│   │           │   │   │   │   ├── test_cdflib.cpython-38.pyc
│   │           │   │   │   │   ├── test_cython_special.cpython-38.pyc
│   │           │   │   │   │   ├── test_data.cpython-38.pyc
│   │           │   │   │   │   ├── test_digamma.cpython-38.pyc
│   │           │   │   │   │   ├── test_ellip_harm.cpython-38.pyc
│   │           │   │   │   │   ├── test_erfinv.cpython-38.pyc
│   │           │   │   │   │   ├── test_exponential_integrals.cpython-38.pyc
│   │           │   │   │   │   ├── test_faddeeva.cpython-38.pyc
│   │           │   │   │   │   ├── test_gamma.cpython-38.pyc
│   │           │   │   │   │   ├── test_gammainc.cpython-38.pyc
│   │           │   │   │   │   ├── test_hypergeometric.cpython-38.pyc
│   │           │   │   │   │   ├── test_kolmogorov.cpython-38.pyc
│   │           │   │   │   │   ├── test_lambertw.cpython-38.pyc
│   │           │   │   │   │   ├── test_loggamma.cpython-38.pyc
│   │           │   │   │   │   ├── test_logit.cpython-38.pyc
│   │           │   │   │   │   ├── test_log_softmax.cpython-38.pyc
│   │           │   │   │   │   ├── test_logsumexp.cpython-38.pyc
│   │           │   │   │   │   ├── test_mpmath.cpython-38.pyc
│   │           │   │   │   │   ├── test_nan_inputs.cpython-38.pyc
│   │           │   │   │   │   ├── test_ndtr.cpython-38.pyc
│   │           │   │   │   │   ├── test_orthogonal.cpython-38.pyc
│   │           │   │   │   │   ├── test_orthogonal_eval.cpython-38.pyc
│   │           │   │   │   │   ├── test_owens_t.cpython-38.pyc
│   │           │   │   │   │   ├── test_pcf.cpython-38.pyc
│   │           │   │   │   │   ├── test_pdtr.cpython-38.pyc
│   │           │   │   │   │   ├── test_precompute_expn_asy.cpython-38.pyc
│   │           │   │   │   │   ├── test_precompute_gammainc.cpython-38.pyc
│   │           │   │   │   │   ├── test_precompute_utils.cpython-38.pyc
│   │           │   │   │   │   ├── test_round.cpython-38.pyc
│   │           │   │   │   │   ├── test_sf_error.cpython-38.pyc
│   │           │   │   │   │   ├── test_sici.cpython-38.pyc
│   │           │   │   │   │   ├── test_spence.cpython-38.pyc
│   │           │   │   │   │   ├── test_spfun_stats.cpython-38.pyc
│   │           │   │   │   │   ├── test_spherical_bessel.cpython-38.pyc
│   │           │   │   │   │   ├── test_sph_harm.cpython-38.pyc
│   │           │   │   │   │   ├── test_trig.cpython-38.pyc
│   │           │   │   │   │   ├── test_wrightomega.cpython-38.pyc
│   │           │   │   │   │   └── test_zeta.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_basic.py
│   │           │   │   │   ├── test_bdtr.py
│   │           │   │   │   ├── test_boxcox.py
│   │           │   │   │   ├── test_cdflib.py
│   │           │   │   │   ├── test_cython_special.py
│   │           │   │   │   ├── test_data.py
│   │           │   │   │   ├── test_digamma.py
│   │           │   │   │   ├── test_ellip_harm.py
│   │           │   │   │   ├── test_erfinv.py
│   │           │   │   │   ├── test_exponential_integrals.py
│   │           │   │   │   ├── test_faddeeva.py
│   │           │   │   │   ├── test_gammainc.py
│   │           │   │   │   ├── test_gamma.py
│   │           │   │   │   ├── test_hypergeometric.py
│   │           │   │   │   ├── test_kolmogorov.py
│   │           │   │   │   ├── test_lambertw.py
│   │           │   │   │   ├── test_loggamma.py
│   │           │   │   │   ├── test_logit.py
│   │           │   │   │   ├── test_log_softmax.py
│   │           │   │   │   ├── test_logsumexp.py
│   │           │   │   │   ├── test_mpmath.py
│   │           │   │   │   ├── test_nan_inputs.py
│   │           │   │   │   ├── test_ndtr.py
│   │           │   │   │   ├── test_orthogonal_eval.py
│   │           │   │   │   ├── test_orthogonal.py
│   │           │   │   │   ├── test_owens_t.py
│   │           │   │   │   ├── test_pcf.py
│   │           │   │   │   ├── test_pdtr.py
│   │           │   │   │   ├── test_precompute_expn_asy.py
│   │           │   │   │   ├── test_precompute_gammainc.py
│   │           │   │   │   ├── test_precompute_utils.py
│   │           │   │   │   ├── test_round.py
│   │           │   │   │   ├── test_sf_error.py
│   │           │   │   │   ├── test_sici.py
│   │           │   │   │   ├── test_spence.py
│   │           │   │   │   ├── test_spfun_stats.py
│   │           │   │   │   ├── test_spherical_bessel.py
│   │           │   │   │   ├── test_sph_harm.py
│   │           │   │   │   ├── test_trig.py
│   │           │   │   │   ├── test_wrightomega.py
│   │           │   │   │   └── test_zeta.py
│   │           │   │   ├── add_newdocs.py
│   │           │   │   ├── _basic.py
│   │           │   │   ├── basic.py
│   │           │   │   ├── _comb.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── cython_special.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── cython_special.pxd
│   │           │   │   ├── cython_special.pyi
│   │           │   │   ├── _ellip_harm_2.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _ellip_harm.py
│   │           │   │   ├── _generate_pyx.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _lambertw.py
│   │           │   │   ├── _logsumexp.py
│   │           │   │   ├── _mptestutils.py
│   │           │   │   ├── orthogonal.py
│   │           │   │   ├── orthogonal.pyi
│   │           │   │   ├── setup.py
│   │           │   │   ├── sf_error.py
│   │           │   │   ├── specfun.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── spfun_stats.py
│   │           │   │   ├── _spherical_bessel.py
│   │           │   │   ├── _test_round.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _test_round.pyi
│   │           │   │   ├── _testutils.py
│   │           │   │   ├── _ufuncs.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _ufuncs_cxx.cpython-38-x86_64-linux-gnu.so
│   │           │   │   └── _ufuncs.pyi
│   │           │   ├── stats
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── _binned_statistic.cpython-38.pyc
│   │           │   │   │   ├── _constants.cpython-38.pyc
│   │           │   │   │   ├── contingency.cpython-38.pyc
│   │           │   │   │   ├── _continuous_distns.cpython-38.pyc
│   │           │   │   │   ├── _discrete_distns.cpython-38.pyc
│   │           │   │   │   ├── _distn_infrastructure.cpython-38.pyc
│   │           │   │   │   ├── distributions.cpython-38.pyc
│   │           │   │   │   ├── _distr_params.cpython-38.pyc
│   │           │   │   │   ├── _hypotests.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── kde.cpython-38.pyc
│   │           │   │   │   ├── _ksstats.cpython-38.pyc
│   │           │   │   │   ├── morestats.cpython-38.pyc
│   │           │   │   │   ├── mstats_basic.cpython-38.pyc
│   │           │   │   │   ├── mstats.cpython-38.pyc
│   │           │   │   │   ├── mstats_extras.cpython-38.pyc
│   │           │   │   │   ├── _multivariate.cpython-38.pyc
│   │           │   │   │   ├── _rvs_sampling.cpython-38.pyc
│   │           │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   ├── stats.cpython-38.pyc
│   │           │   │   │   ├── _stats_mstats_common.cpython-38.pyc
│   │           │   │   │   ├── _tukeylambda_stats.cpython-38.pyc
│   │           │   │   │   └── _wilcoxon_data.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── data
│   │           │   │   │   │   ├── nist_anova
│   │           │   │   │   │   │   ├── AtmWtAg.dat
│   │           │   │   │   │   │   ├── SiRstv.dat
│   │           │   │   │   │   │   ├── SmLs01.dat
│   │           │   │   │   │   │   ├── SmLs02.dat
│   │           │   │   │   │   │   ├── SmLs03.dat
│   │           │   │   │   │   │   ├── SmLs04.dat
│   │           │   │   │   │   │   ├── SmLs05.dat
│   │           │   │   │   │   │   ├── SmLs06.dat
│   │           │   │   │   │   │   ├── SmLs07.dat
│   │           │   │   │   │   │   ├── SmLs08.dat
│   │           │   │   │   │   │   └── SmLs09.dat
│   │           │   │   │   │   ├── nist_linregress
│   │           │   │   │   │   │   └── Norris.dat
│   │           │   │   │   │   ├── stable-cdf-sample-data.npy
│   │           │   │   │   │   └── stable-pdf-sample-data.npy
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── common_tests.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_binned_statistic.cpython-38.pyc
│   │           │   │   │   │   ├── test_contingency.cpython-38.pyc
│   │           │   │   │   │   ├── test_continuous_basic.cpython-38.pyc
│   │           │   │   │   │   ├── test_discrete_basic.cpython-38.pyc
│   │           │   │   │   │   ├── test_discrete_distns.cpython-38.pyc
│   │           │   │   │   │   ├── test_distributions.cpython-38.pyc
│   │           │   │   │   │   ├── test_fit.cpython-38.pyc
│   │           │   │   │   │   ├── test_hypotests.cpython-38.pyc
│   │           │   │   │   │   ├── test_kdeoth.cpython-38.pyc
│   │           │   │   │   │   ├── test_morestats.cpython-38.pyc
│   │           │   │   │   │   ├── test_mstats_basic.cpython-38.pyc
│   │           │   │   │   │   ├── test_mstats_extras.cpython-38.pyc
│   │           │   │   │   │   ├── test_multivariate.cpython-38.pyc
│   │           │   │   │   │   ├── test_rank.cpython-38.pyc
│   │           │   │   │   │   ├── test_stats.cpython-38.pyc
│   │           │   │   │   │   └── test_tukeylambda_stats.cpython-38.pyc
│   │           │   │   │   ├── common_tests.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_binned_statistic.py
│   │           │   │   │   ├── test_contingency.py
│   │           │   │   │   ├── test_continuous_basic.py
│   │           │   │   │   ├── test_discrete_basic.py
│   │           │   │   │   ├── test_discrete_distns.py
│   │           │   │   │   ├── test_distributions.py
│   │           │   │   │   ├── test_fit.py
│   │           │   │   │   ├── test_hypotests.py
│   │           │   │   │   ├── test_kdeoth.py
│   │           │   │   │   ├── test_morestats.py
│   │           │   │   │   ├── test_mstats_basic.py
│   │           │   │   │   ├── test_mstats_extras.py
│   │           │   │   │   ├── test_multivariate.py
│   │           │   │   │   ├── test_rank.py
│   │           │   │   │   ├── test_stats.py
│   │           │   │   │   └── test_tukeylambda_stats.py
│   │           │   │   ├── _binned_statistic.py
│   │           │   │   ├── _constants.py
│   │           │   │   ├── contingency.py
│   │           │   │   ├── _continuous_distns.py
│   │           │   │   ├── _discrete_distns.py
│   │           │   │   ├── _distn_infrastructure.py
│   │           │   │   ├── distributions.py
│   │           │   │   ├── _distr_params.py
│   │           │   │   ├── _hypotests.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── kde.py
│   │           │   │   ├── _ksstats.py
│   │           │   │   ├── morestats.py
│   │           │   │   ├── mstats_basic.py
│   │           │   │   ├── mstats_extras.py
│   │           │   │   ├── mstats.py
│   │           │   │   ├── _multivariate.py
│   │           │   │   ├── mvn.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _rvs_sampling.py
│   │           │   │   ├── setup.py
│   │           │   │   ├── statlib.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _stats.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _stats_mstats_common.py
│   │           │   │   ├── stats.py
│   │           │   │   ├── _tukeylambda_stats.py
│   │           │   │   └── _wilcoxon_data.py
│   │           │   ├── __config__.py
│   │           │   ├── conftest.py
│   │           │   ├── _distributor_init.py
│   │           │   ├── HACKING.rst.txt
│   │           │   ├── __init__.py
│   │           │   ├── INSTALL.rst.txt
│   │           │   ├── LICENSES_bundled.txt
│   │           │   ├── LICENSE.txt
│   │           │   ├── linalg.pxd
│   │           │   ├── mypy_requirements.txt
│   │           │   ├── optimize.pxd
│   │           │   ├── setup.py
│   │           │   ├── special.pxd
│   │           │   └── version.py
│   │           ├── scipy-1.6.3.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSES_bundled.txt
│   │           │   ├── LICENSE.txt
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── REQUESTED
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── scipy.libs
│   │           │   ├── libgfortran-ed201abd.so.3.0.0
│   │           │   └── libopenblasp-r0-085ca80a.3.9.so
│   │           ├── setuptools
│   │           │   ├── command
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── alias.cpython-38.pyc
│   │           │   │   │   ├── bdist_egg.cpython-38.pyc
│   │           │   │   │   ├── bdist_rpm.cpython-38.pyc
│   │           │   │   │   ├── build_clib.cpython-38.pyc
│   │           │   │   │   ├── build_ext.cpython-38.pyc
│   │           │   │   │   ├── build_py.cpython-38.pyc
│   │           │   │   │   ├── develop.cpython-38.pyc
│   │           │   │   │   ├── dist_info.cpython-38.pyc
│   │           │   │   │   ├── easy_install.cpython-38.pyc
│   │           │   │   │   ├── egg_info.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── install.cpython-38.pyc
│   │           │   │   │   ├── install_egg_info.cpython-38.pyc
│   │           │   │   │   ├── install_lib.cpython-38.pyc
│   │           │   │   │   ├── install_scripts.cpython-38.pyc
│   │           │   │   │   ├── py36compat.cpython-38.pyc
│   │           │   │   │   ├── register.cpython-38.pyc
│   │           │   │   │   ├── rotate.cpython-38.pyc
│   │           │   │   │   ├── saveopts.cpython-38.pyc
│   │           │   │   │   ├── sdist.cpython-38.pyc
│   │           │   │   │   ├── setopt.cpython-38.pyc
│   │           │   │   │   ├── test.cpython-38.pyc
│   │           │   │   │   ├── upload.cpython-38.pyc
│   │           │   │   │   └── upload_docs.cpython-38.pyc
│   │           │   │   ├── alias.py
│   │           │   │   ├── bdist_egg.py
│   │           │   │   ├── bdist_rpm.py
│   │           │   │   ├── build_clib.py
│   │           │   │   ├── build_ext.py
│   │           │   │   ├── build_py.py
│   │           │   │   ├── develop.py
│   │           │   │   ├── dist_info.py
│   │           │   │   ├── easy_install.py
│   │           │   │   ├── egg_info.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── install_egg_info.py
│   │           │   │   ├── install_lib.py
│   │           │   │   ├── install.py
│   │           │   │   ├── install_scripts.py
│   │           │   │   ├── launcher manifest.xml
│   │           │   │   ├── py36compat.py
│   │           │   │   ├── register.py
│   │           │   │   ├── rotate.py
│   │           │   │   ├── saveopts.py
│   │           │   │   ├── sdist.py
│   │           │   │   ├── setopt.py
│   │           │   │   ├── test.py
│   │           │   │   ├── upload_docs.py
│   │           │   │   └── upload.py
│   │           │   ├── _distutils
│   │           │   │   ├── command
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── bdist.cpython-38.pyc
│   │           │   │   │   │   ├── bdist_dumb.cpython-38.pyc
│   │           │   │   │   │   ├── bdist_msi.cpython-38.pyc
│   │           │   │   │   │   ├── bdist_rpm.cpython-38.pyc
│   │           │   │   │   │   ├── bdist_wininst.cpython-38.pyc
│   │           │   │   │   │   ├── build_clib.cpython-38.pyc
│   │           │   │   │   │   ├── build.cpython-38.pyc
│   │           │   │   │   │   ├── build_ext.cpython-38.pyc
│   │           │   │   │   │   ├── build_py.cpython-38.pyc
│   │           │   │   │   │   ├── build_scripts.cpython-38.pyc
│   │           │   │   │   │   ├── check.cpython-38.pyc
│   │           │   │   │   │   ├── clean.cpython-38.pyc
│   │           │   │   │   │   ├── config.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── install.cpython-38.pyc
│   │           │   │   │   │   ├── install_data.cpython-38.pyc
│   │           │   │   │   │   ├── install_egg_info.cpython-38.pyc
│   │           │   │   │   │   ├── install_headers.cpython-38.pyc
│   │           │   │   │   │   ├── install_lib.cpython-38.pyc
│   │           │   │   │   │   ├── install_scripts.cpython-38.pyc
│   │           │   │   │   │   ├── py37compat.cpython-38.pyc
│   │           │   │   │   │   ├── register.cpython-38.pyc
│   │           │   │   │   │   ├── sdist.cpython-38.pyc
│   │           │   │   │   │   └── upload.cpython-38.pyc
│   │           │   │   │   ├── bdist_dumb.py
│   │           │   │   │   ├── bdist_msi.py
│   │           │   │   │   ├── bdist.py
│   │           │   │   │   ├── bdist_rpm.py
│   │           │   │   │   ├── bdist_wininst.py
│   │           │   │   │   ├── build_clib.py
│   │           │   │   │   ├── build_ext.py
│   │           │   │   │   ├── build.py
│   │           │   │   │   ├── build_py.py
│   │           │   │   │   ├── build_scripts.py
│   │           │   │   │   ├── check.py
│   │           │   │   │   ├── clean.py
│   │           │   │   │   ├── config.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── install_data.py
│   │           │   │   │   ├── install_egg_info.py
│   │           │   │   │   ├── install_headers.py
│   │           │   │   │   ├── install_lib.py
│   │           │   │   │   ├── install.py
│   │           │   │   │   ├── install_scripts.py
│   │           │   │   │   ├── py37compat.py
│   │           │   │   │   ├── register.py
│   │           │   │   │   ├── sdist.py
│   │           │   │   │   └── upload.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── archive_util.cpython-38.pyc
│   │           │   │   │   ├── bcppcompiler.cpython-38.pyc
│   │           │   │   │   ├── ccompiler.cpython-38.pyc
│   │           │   │   │   ├── cmd.cpython-38.pyc
│   │           │   │   │   ├── config.cpython-38.pyc
│   │           │   │   │   ├── core.cpython-38.pyc
│   │           │   │   │   ├── cygwinccompiler.cpython-38.pyc
│   │           │   │   │   ├── debug.cpython-38.pyc
│   │           │   │   │   ├── dep_util.cpython-38.pyc
│   │           │   │   │   ├── dir_util.cpython-38.pyc
│   │           │   │   │   ├── dist.cpython-38.pyc
│   │           │   │   │   ├── errors.cpython-38.pyc
│   │           │   │   │   ├── extension.cpython-38.pyc
│   │           │   │   │   ├── fancy_getopt.cpython-38.pyc
│   │           │   │   │   ├── filelist.cpython-38.pyc
│   │           │   │   │   ├── file_util.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── log.cpython-38.pyc
│   │           │   │   │   ├── msvc9compiler.cpython-38.pyc
│   │           │   │   │   ├── _msvccompiler.cpython-38.pyc
│   │           │   │   │   ├── msvccompiler.cpython-38.pyc
│   │           │   │   │   ├── py35compat.cpython-38.pyc
│   │           │   │   │   ├── py38compat.cpython-38.pyc
│   │           │   │   │   ├── spawn.cpython-38.pyc
│   │           │   │   │   ├── sysconfig.cpython-38.pyc
│   │           │   │   │   ├── text_file.cpython-38.pyc
│   │           │   │   │   ├── unixccompiler.cpython-38.pyc
│   │           │   │   │   ├── util.cpython-38.pyc
│   │           │   │   │   ├── version.cpython-38.pyc
│   │           │   │   │   └── versionpredicate.cpython-38.pyc
│   │           │   │   ├── archive_util.py
│   │           │   │   ├── bcppcompiler.py
│   │           │   │   ├── ccompiler.py
│   │           │   │   ├── cmd.py
│   │           │   │   ├── config.py
│   │           │   │   ├── core.py
│   │           │   │   ├── cygwinccompiler.py
│   │           │   │   ├── debug.py
│   │           │   │   ├── dep_util.py
│   │           │   │   ├── dir_util.py
│   │           │   │   ├── dist.py
│   │           │   │   ├── errors.py
│   │           │   │   ├── extension.py
│   │           │   │   ├── fancy_getopt.py
│   │           │   │   ├── filelist.py
│   │           │   │   ├── file_util.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── log.py
│   │           │   │   ├── msvc9compiler.py
│   │           │   │   ├── _msvccompiler.py
│   │           │   │   ├── msvccompiler.py
│   │           │   │   ├── py35compat.py
│   │           │   │   ├── py38compat.py
│   │           │   │   ├── spawn.py
│   │           │   │   ├── sysconfig.py
│   │           │   │   ├── text_file.py
│   │           │   │   ├── unixccompiler.py
│   │           │   │   ├── util.py
│   │           │   │   ├── versionpredicate.py
│   │           │   │   └── version.py
│   │           │   ├── extern
│   │           │   │   ├── __pycache__
│   │           │   │   │   └── __init__.cpython-38.pyc
│   │           │   │   └── __init__.py
│   │           │   ├── __pycache__
│   │           │   │   ├── archive_util.cpython-38.pyc
│   │           │   │   ├── build_meta.cpython-38.pyc
│   │           │   │   ├── config.cpython-38.pyc
│   │           │   │   ├── depends.cpython-38.pyc
│   │           │   │   ├── _deprecation_warning.cpython-38.pyc
│   │           │   │   ├── dep_util.cpython-38.pyc
│   │           │   │   ├── dist.cpython-38.pyc
│   │           │   │   ├── errors.cpython-38.pyc
│   │           │   │   ├── extension.cpython-38.pyc
│   │           │   │   ├── glob.cpython-38.pyc
│   │           │   │   ├── _imp.cpython-38.pyc
│   │           │   │   ├── __init__.cpython-38.pyc
│   │           │   │   ├── installer.cpython-38.pyc
│   │           │   │   ├── launch.cpython-38.pyc
│   │           │   │   ├── lib2to3_ex.cpython-38.pyc
│   │           │   │   ├── monkey.cpython-38.pyc
│   │           │   │   ├── msvc.cpython-38.pyc
│   │           │   │   ├── namespaces.cpython-38.pyc
│   │           │   │   ├── package_index.cpython-38.pyc
│   │           │   │   ├── py34compat.cpython-38.pyc
│   │           │   │   ├── sandbox.cpython-38.pyc
│   │           │   │   ├── ssl_support.cpython-38.pyc
│   │           │   │   ├── unicode_utils.cpython-38.pyc
│   │           │   │   ├── version.cpython-38.pyc
│   │           │   │   ├── wheel.cpython-38.pyc
│   │           │   │   └── windows_support.cpython-38.pyc
│   │           │   ├── _vendor
│   │           │   │   ├── more_itertools
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── more.cpython-38.pyc
│   │           │   │   │   │   └── recipes.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── more.py
│   │           │   │   │   └── recipes.py
│   │           │   │   ├── packaging
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __about__.cpython-38.pyc
│   │           │   │   │   │   ├── _compat.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── markers.cpython-38.pyc
│   │           │   │   │   │   ├── requirements.cpython-38.pyc
│   │           │   │   │   │   ├── specifiers.cpython-38.pyc
│   │           │   │   │   │   ├── _structures.cpython-38.pyc
│   │           │   │   │   │   ├── tags.cpython-38.pyc
│   │           │   │   │   │   ├── _typing.cpython-38.pyc
│   │           │   │   │   │   ├── utils.cpython-38.pyc
│   │           │   │   │   │   └── version.cpython-38.pyc
│   │           │   │   │   ├── __about__.py
│   │           │   │   │   ├── _compat.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── markers.py
│   │           │   │   │   ├── requirements.py
│   │           │   │   │   ├── specifiers.py
│   │           │   │   │   ├── _structures.py
│   │           │   │   │   ├── tags.py
│   │           │   │   │   ├── _typing.py
│   │           │   │   │   ├── utils.py
│   │           │   │   │   └── version.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── ordered_set.cpython-38.pyc
│   │           │   │   │   └── pyparsing.cpython-38.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── ordered_set.py
│   │           │   │   └── pyparsing.py
│   │           │   ├── archive_util.py
│   │           │   ├── build_meta.py
│   │           │   ├── cli-32.exe
│   │           │   ├── cli-64.exe
│   │           │   ├── cli.exe
│   │           │   ├── config.py
│   │           │   ├── depends.py
│   │           │   ├── _deprecation_warning.py
│   │           │   ├── dep_util.py
│   │           │   ├── dist.py
│   │           │   ├── errors.py
│   │           │   ├── extension.py
│   │           │   ├── glob.py
│   │           │   ├── gui-32.exe
│   │           │   ├── gui-64.exe
│   │           │   ├── gui.exe
│   │           │   ├── _imp.py
│   │           │   ├── __init__.py
│   │           │   ├── installer.py
│   │           │   ├── launch.py
│   │           │   ├── lib2to3_ex.py
│   │           │   ├── monkey.py
│   │           │   ├── msvc.py
│   │           │   ├── namespaces.py
│   │           │   ├── package_index.py
│   │           │   ├── py34compat.py
│   │           │   ├── sandbox.py
│   │           │   ├── script (dev).tmpl
│   │           │   ├── script.tmpl
│   │           │   ├── ssl_support.py
│   │           │   ├── unicode_utils.py
│   │           │   ├── version.py
│   │           │   ├── wheel.py
│   │           │   └── windows_support.py
│   │           ├── setuptools-57.0.0.dist-info
│   │           │   ├── dependency_links.txt
│   │           │   ├── entry_points.txt
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── six-1.16.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── skimage
│   │           │   ├── color
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── adapt_rgb.cpython-38.pyc
│   │           │   │   │   ├── colorconv.cpython-38.pyc
│   │           │   │   │   ├── colorlabel.cpython-38.pyc
│   │           │   │   │   ├── delta_e.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   └── rgb_colors.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_adapt_rgb.cpython-38.pyc
│   │           │   │   │   │   ├── test_colorconv.cpython-38.pyc
│   │           │   │   │   │   ├── test_colorlabel.cpython-38.pyc
│   │           │   │   │   │   └── test_delta_e.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_adapt_rgb.py
│   │           │   │   │   ├── test_colorconv.py
│   │           │   │   │   ├── test_colorlabel.py
│   │           │   │   │   └── test_delta_e.py
│   │           │   │   ├── adapt_rgb.py
│   │           │   │   ├── colorconv.py
│   │           │   │   ├── colorlabel.py
│   │           │   │   ├── delta_e.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── rgb_colors.py
│   │           │   ├── data
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── _binary_blobs.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── _registry.cpython-38.pyc
│   │           │   │   │   └── setup.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   └── test_data.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── test_data.py
│   │           │   │   ├── astronaut.png
│   │           │   │   ├── _binary_blobs.py
│   │           │   │   ├── brick.png
│   │           │   │   ├── camera.png
│   │           │   │   ├── cell.png
│   │           │   │   ├── chelsea.png
│   │           │   │   ├── chessboard_GRAY.png
│   │           │   │   ├── chessboard_RGB.png
│   │           │   │   ├── clock_motion.png
│   │           │   │   ├── coffee.png
│   │           │   │   ├── coins.png
│   │           │   │   ├── color.png
│   │           │   │   ├── grass.png
│   │           │   │   ├── gravel.png
│   │           │   │   ├── horse.png
│   │           │   │   ├── hubble_deep_field.jpg
│   │           │   │   ├── ihc.png
│   │           │   │   ├── __init__.py
│   │           │   │   ├── lbpcascade_frontalface_opencv.xml
│   │           │   │   ├── lfw_subset.npy
│   │           │   │   ├── logo.png
│   │           │   │   ├── microaneurysms.png
│   │           │   │   ├── moon.png
│   │           │   │   ├── motorcycle_disp.npz
│   │           │   │   ├── motorcycle_left.png
│   │           │   │   ├── motorcycle_right.png
│   │           │   │   ├── page.png
│   │           │   │   ├── phantom.png
│   │           │   │   ├── README.txt
│   │           │   │   ├── _registry.py
│   │           │   │   ├── retina.jpg
│   │           │   │   ├── rocket.jpg
│   │           │   │   ├── setup.py
│   │           │   │   └── text.png
│   │           │   ├── draw
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── draw3d.cpython-38.pyc
│   │           │   │   │   ├── draw.cpython-38.pyc
│   │           │   │   │   ├── draw_nd.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── _polygon2mask.cpython-38.pyc
│   │           │   │   │   ├── _random_shapes.cpython-38.pyc
│   │           │   │   │   └── setup.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_draw3d.cpython-38.pyc
│   │           │   │   │   │   ├── test_draw.cpython-38.pyc
│   │           │   │   │   │   ├── test_draw_nd.cpython-38.pyc
│   │           │   │   │   │   ├── test_polygon2mask.cpython-38.pyc
│   │           │   │   │   │   └── test_random_shapes.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_draw3d.py
│   │           │   │   │   ├── test_draw_nd.py
│   │           │   │   │   ├── test_draw.py
│   │           │   │   │   ├── test_polygon2mask.py
│   │           │   │   │   └── test_random_shapes.py
│   │           │   │   ├── draw3d.py
│   │           │   │   ├── _draw.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── draw_nd.py
│   │           │   │   ├── draw.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _polygon2mask.py
│   │           │   │   ├── _random_shapes.py
│   │           │   │   └── setup.py
│   │           │   ├── exposure
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── _adapthist.cpython-38.pyc
│   │           │   │   │   ├── exposure.cpython-38.pyc
│   │           │   │   │   ├── histogram_matching.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   └── setup.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_exposure.cpython-38.pyc
│   │           │   │   │   │   └── test_histogram_matching.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_exposure.py
│   │           │   │   │   └── test_histogram_matching.py
│   │           │   │   ├── _adapthist.py
│   │           │   │   ├── exposure.py
│   │           │   │   ├── histogram_matching.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── setup.py
│   │           │   ├── feature
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── _basic_features.cpython-38.pyc
│   │           │   │   │   ├── blob.cpython-38.pyc
│   │           │   │   │   ├── brief.cpython-38.pyc
│   │           │   │   │   ├── _canny.cpython-38.pyc
│   │           │   │   │   ├── censure.cpython-38.pyc
│   │           │   │   │   ├── corner.cpython-38.pyc
│   │           │   │   │   ├── _daisy.cpython-38.pyc
│   │           │   │   │   ├── haar.cpython-38.pyc
│   │           │   │   │   ├── _hog.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── match.cpython-38.pyc
│   │           │   │   │   ├── orb.cpython-38.pyc
│   │           │   │   │   ├── _orb_descriptor_positions.cpython-38.pyc
│   │           │   │   │   ├── peak.cpython-38.pyc
│   │           │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   ├── template.cpython-38.pyc
│   │           │   │   │   ├── texture.cpython-38.pyc
│   │           │   │   │   └── util.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_basic_features.cpython-38.pyc
│   │           │   │   │   │   ├── test_blob.cpython-38.pyc
│   │           │   │   │   │   ├── test_brief.cpython-38.pyc
│   │           │   │   │   │   ├── test_canny.cpython-38.pyc
│   │           │   │   │   │   ├── test_cascade.cpython-38.pyc
│   │           │   │   │   │   ├── test_censure.cpython-38.pyc
│   │           │   │   │   │   ├── test_corner.cpython-38.pyc
│   │           │   │   │   │   ├── test_daisy.cpython-38.pyc
│   │           │   │   │   │   ├── test_haar.cpython-38.pyc
│   │           │   │   │   │   ├── test_hog.cpython-38.pyc
│   │           │   │   │   │   ├── test_match.cpython-38.pyc
│   │           │   │   │   │   ├── test_orb.cpython-38.pyc
│   │           │   │   │   │   ├── test_peak.cpython-38.pyc
│   │           │   │   │   │   ├── test_template.cpython-38.pyc
│   │           │   │   │   │   ├── test_texture.cpython-38.pyc
│   │           │   │   │   │   └── test_util.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_basic_features.py
│   │           │   │   │   ├── test_blob.py
│   │           │   │   │   ├── test_brief.py
│   │           │   │   │   ├── test_canny.py
│   │           │   │   │   ├── test_cascade.py
│   │           │   │   │   ├── test_censure.py
│   │           │   │   │   ├── test_corner.py
│   │           │   │   │   ├── test_daisy.py
│   │           │   │   │   ├── test_haar.py
│   │           │   │   │   ├── test_hog.py
│   │           │   │   │   ├── test_match.py
│   │           │   │   │   ├── test_orb.py
│   │           │   │   │   ├── test_peak.py
│   │           │   │   │   ├── test_template.py
│   │           │   │   │   ├── test_texture.py
│   │           │   │   │   └── test_util.py
│   │           │   │   ├── _basic_features.py
│   │           │   │   ├── blob.py
│   │           │   │   ├── brief_cy.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── brief.py
│   │           │   │   ├── _canny.py
│   │           │   │   ├── _cascade.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── censure_cy.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── censure.py
│   │           │   │   ├── corner_cy.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── corner.py
│   │           │   │   ├── _daisy.py
│   │           │   │   ├── _haar.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── haar.py
│   │           │   │   ├── _hessian_det_appx.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _hoghistogram.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _hog.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── match.py
│   │           │   │   ├── orb_cy.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _orb_descriptor_positions.py
│   │           │   │   ├── orb_descriptor_positions.txt
│   │           │   │   ├── orb.py
│   │           │   │   ├── peak.py
│   │           │   │   ├── setup.py
│   │           │   │   ├── template.py
│   │           │   │   ├── _texture.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── texture.py
│   │           │   │   └── util.py
│   │           │   ├── filters
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── edges.cpython-38.pyc
│   │           │   │   │   ├── _gabor.cpython-38.pyc
│   │           │   │   │   ├── _gaussian.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── lpi_filter.cpython-38.pyc
│   │           │   │   │   ├── _median.cpython-38.pyc
│   │           │   │   │   ├── _rank_order.cpython-38.pyc
│   │           │   │   │   ├── ridges.cpython-38.pyc
│   │           │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   ├── _sparse.cpython-38.pyc
│   │           │   │   │   ├── thresholding.cpython-38.pyc
│   │           │   │   │   ├── _unsharp_mask.cpython-38.pyc
│   │           │   │   │   └── _window.cpython-38.pyc
│   │           │   │   ├── rank
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── bilateral.cpython-38.pyc
│   │           │   │   │   │   ├── generic.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   └── _percentile.cpython-38.pyc
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __pycache__
│   │           │   │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   │   └── test_rank.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── test_rank.py
│   │           │   │   │   ├── bilateral_cy.cpython-38-x86_64-linux-gnu.so
│   │           │   │   │   ├── bilateral.py
│   │           │   │   │   ├── core_cy_3d.cpython-38-x86_64-linux-gnu.so
│   │           │   │   │   ├── core_cy.cpython-38-x86_64-linux-gnu.so
│   │           │   │   │   ├── generic_cy.cpython-38-x86_64-linux-gnu.so
│   │           │   │   │   ├── generic.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── percentile_cy.cpython-38-x86_64-linux-gnu.so
│   │           │   │   │   └── _percentile.py
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_correlate.cpython-38.pyc
│   │           │   │   │   │   ├── test_edges.cpython-38.pyc
│   │           │   │   │   │   ├── test_gabor.cpython-38.pyc
│   │           │   │   │   │   ├── test_gaussian.cpython-38.pyc
│   │           │   │   │   │   ├── test_lpi_filter.cpython-38.pyc
│   │           │   │   │   │   ├── test_median.cpython-38.pyc
│   │           │   │   │   │   ├── test_ridges.cpython-38.pyc
│   │           │   │   │   │   ├── test_thresholding.cpython-38.pyc
│   │           │   │   │   │   ├── test_unsharp_mask.cpython-38.pyc
│   │           │   │   │   │   └── test_window.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_correlate.py
│   │           │   │   │   ├── test_edges.py
│   │           │   │   │   ├── test_gabor.py
│   │           │   │   │   ├── test_gaussian.py
│   │           │   │   │   ├── test_lpi_filter.py
│   │           │   │   │   ├── test_median.py
│   │           │   │   │   ├── test_ridges.py
│   │           │   │   │   ├── test_thresholding.py
│   │           │   │   │   ├── test_unsharp_mask.py
│   │           │   │   │   └── test_window.py
│   │           │   │   ├── edges.py
│   │           │   │   ├── _gabor.py
│   │           │   │   ├── _gaussian.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── lpi_filter.py
│   │           │   │   ├── _median.py
│   │           │   │   ├── _multiotsu.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _rank_order.py
│   │           │   │   ├── ridges.py
│   │           │   │   ├── setup.py
│   │           │   │   ├── _sparse_cy.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _sparse.py
│   │           │   │   ├── thresholding.py
│   │           │   │   ├── _unsharp_mask.py
│   │           │   │   └── _window.py
│   │           │   ├── future
│   │           │   │   ├── graph
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── graph_cut.cpython-38.pyc
│   │           │   │   │   │   ├── graph_merge.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── _ncut.cpython-38.pyc
│   │           │   │   │   │   ├── rag.cpython-38.pyc
│   │           │   │   │   │   └── setup.cpython-38.pyc
│   │           │   │   │   ├── graph_cut.py
│   │           │   │   │   ├── graph_merge.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _ncut_cy.cpython-38-x86_64-linux-gnu.so
│   │           │   │   │   ├── _ncut.py
│   │           │   │   │   ├── rag.py
│   │           │   │   │   └── setup.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── manual_segmentation.cpython-38.pyc
│   │           │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   └── trainable_segmentation.cpython-38.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── manual_segmentation.py
│   │           │   │   ├── setup.py
│   │           │   │   └── trainable_segmentation.py
│   │           │   ├── graph
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── mcp.cpython-38.pyc
│   │           │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   └── spath.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_anisotropy.cpython-38.pyc
│   │           │   │   │   │   ├── test_connect.cpython-38.pyc
│   │           │   │   │   │   ├── test_flexible.cpython-38.pyc
│   │           │   │   │   │   ├── test_heap.cpython-38.pyc
│   │           │   │   │   │   ├── test_mcp.cpython-38.pyc
│   │           │   │   │   │   └── test_spath.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_anisotropy.py
│   │           │   │   │   ├── test_connect.py
│   │           │   │   │   ├── test_flexible.py
│   │           │   │   │   ├── test_heap.py
│   │           │   │   │   ├── test_mcp.py
│   │           │   │   │   └── test_spath.py
│   │           │   │   ├── heap.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _mcp.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── mcp.py
│   │           │   │   ├── setup.py
│   │           │   │   ├── _spath.cpython-38-x86_64-linux-gnu.so
│   │           │   │   └── spath.py
│   │           │   ├── io
│   │           │   │   ├── _plugins
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── fits_plugin.cpython-38.pyc
│   │           │   │   │   │   ├── gdal_plugin.cpython-38.pyc
│   │           │   │   │   │   ├── gtk_plugin.cpython-38.pyc
│   │           │   │   │   │   ├── imageio_plugin.cpython-38.pyc
│   │           │   │   │   │   ├── imread_plugin.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── matplotlib_plugin.cpython-38.pyc
│   │           │   │   │   │   ├── pil_plugin.cpython-38.pyc
│   │           │   │   │   │   ├── q_color_mixer.cpython-38.pyc
│   │           │   │   │   │   ├── q_histogram.cpython-38.pyc
│   │           │   │   │   │   ├── qt_plugin.cpython-38.pyc
│   │           │   │   │   │   ├── simpleitk_plugin.cpython-38.pyc
│   │           │   │   │   │   ├── skivi.cpython-38.pyc
│   │           │   │   │   │   ├── tifffile_plugin.cpython-38.pyc
│   │           │   │   │   │   └── util.cpython-38.pyc
│   │           │   │   │   ├── _colormixer.cpython-38-x86_64-linux-gnu.so
│   │           │   │   │   ├── fits_plugin.ini
│   │           │   │   │   ├── fits_plugin.py
│   │           │   │   │   ├── gdal_plugin.ini
│   │           │   │   │   ├── gdal_plugin.py
│   │           │   │   │   ├── gtk_plugin.ini
│   │           │   │   │   ├── gtk_plugin.py
│   │           │   │   │   ├── _histograms.cpython-38-x86_64-linux-gnu.so
│   │           │   │   │   ├── imageio_plugin.ini
│   │           │   │   │   ├── imageio_plugin.py
│   │           │   │   │   ├── imread_plugin.ini
│   │           │   │   │   ├── imread_plugin.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── matplotlib_plugin.ini
│   │           │   │   │   ├── matplotlib_plugin.py
│   │           │   │   │   ├── pil_plugin.ini
│   │           │   │   │   ├── pil_plugin.py
│   │           │   │   │   ├── q_color_mixer.py
│   │           │   │   │   ├── q_histogram.py
│   │           │   │   │   ├── qt_plugin.ini
│   │           │   │   │   ├── qt_plugin.py
│   │           │   │   │   ├── simpleitk_plugin.ini
│   │           │   │   │   ├── simpleitk_plugin.py
│   │           │   │   │   ├── skivi.py
│   │           │   │   │   ├── tifffile_plugin.ini
│   │           │   │   │   ├── tifffile_plugin.py
│   │           │   │   │   └── util.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── collection.cpython-38.pyc
│   │           │   │   │   ├── _image_stack.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── _io.cpython-38.pyc
│   │           │   │   │   ├── manage_plugins.cpython-38.pyc
│   │           │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   ├── sift.cpython-38.pyc
│   │           │   │   │   └── util.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_collection.cpython-38.pyc
│   │           │   │   │   │   ├── test_colormixer.cpython-38.pyc
│   │           │   │   │   │   ├── test_fits.cpython-38.pyc
│   │           │   │   │   │   ├── test_histograms.cpython-38.pyc
│   │           │   │   │   │   ├── test_imageio.cpython-38.pyc
│   │           │   │   │   │   ├── test_imread.cpython-38.pyc
│   │           │   │   │   │   ├── test_io.cpython-38.pyc
│   │           │   │   │   │   ├── test_mpl_imshow.cpython-38.pyc
│   │           │   │   │   │   ├── test_multi_image.cpython-38.pyc
│   │           │   │   │   │   ├── test_pil.cpython-38.pyc
│   │           │   │   │   │   ├── test_plugin.cpython-38.pyc
│   │           │   │   │   │   ├── test_plugin_util.cpython-38.pyc
│   │           │   │   │   │   ├── test_sift.cpython-38.pyc
│   │           │   │   │   │   ├── test_simpleitk.cpython-38.pyc
│   │           │   │   │   │   └── test_tifffile.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_collection.py
│   │           │   │   │   ├── test_colormixer.py
│   │           │   │   │   ├── test_fits.py
│   │           │   │   │   ├── test_histograms.py
│   │           │   │   │   ├── test_imageio.py
│   │           │   │   │   ├── test_imread.py
│   │           │   │   │   ├── test_io.py
│   │           │   │   │   ├── test_mpl_imshow.py
│   │           │   │   │   ├── test_multi_image.py
│   │           │   │   │   ├── test_pil.py
│   │           │   │   │   ├── test_plugin.py
│   │           │   │   │   ├── test_plugin_util.py
│   │           │   │   │   ├── test_sift.py
│   │           │   │   │   ├── test_simpleitk.py
│   │           │   │   │   └── test_tifffile.py
│   │           │   │   ├── collection.py
│   │           │   │   ├── _image_stack.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _io.py
│   │           │   │   ├── manage_plugins.py
│   │           │   │   ├── setup.py
│   │           │   │   ├── sift.py
│   │           │   │   └── util.py
│   │           │   ├── measure
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── block.cpython-38.pyc
│   │           │   │   │   ├── entropy.cpython-38.pyc
│   │           │   │   │   ├── _find_contours.cpython-38.pyc
│   │           │   │   │   ├── fit.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── _label.cpython-38.pyc
│   │           │   │   │   ├── _marching_cubes_classic.cpython-38.pyc
│   │           │   │   │   ├── _marching_cubes_lewiner.cpython-38.pyc
│   │           │   │   │   ├── _marching_cubes_lewiner_luts.cpython-38.pyc
│   │           │   │   │   ├── _moments.cpython-38.pyc
│   │           │   │   │   ├── pnpoly.cpython-38.pyc
│   │           │   │   │   ├── _polygon.cpython-38.pyc
│   │           │   │   │   ├── profile.cpython-38.pyc
│   │           │   │   │   ├── _regionprops.cpython-38.pyc
│   │           │   │   │   ├── _regionprops_utils.cpython-38.pyc
│   │           │   │   │   └── setup.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_block.cpython-38.pyc
│   │           │   │   │   │   ├── test_ccomp.cpython-38.pyc
│   │           │   │   │   │   ├── test_entropy.cpython-38.pyc
│   │           │   │   │   │   ├── test_find_contours.cpython-38.pyc
│   │           │   │   │   │   ├── test_fit.cpython-38.pyc
│   │           │   │   │   │   ├── test_label.cpython-38.pyc
│   │           │   │   │   │   ├── test_marching_cubes.cpython-38.pyc
│   │           │   │   │   │   ├── test_moments.cpython-38.pyc
│   │           │   │   │   │   ├── test_pnpoly.cpython-38.pyc
│   │           │   │   │   │   ├── test_polygon.cpython-38.pyc
│   │           │   │   │   │   ├── test_profile.cpython-38.pyc
│   │           │   │   │   │   ├── test_regionprops.cpython-38.pyc
│   │           │   │   │   │   └── test_structural_similarity.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_block.py
│   │           │   │   │   ├── test_ccomp.py
│   │           │   │   │   ├── test_entropy.py
│   │           │   │   │   ├── test_find_contours.py
│   │           │   │   │   ├── test_fit.py
│   │           │   │   │   ├── test_label.py
│   │           │   │   │   ├── test_marching_cubes.py
│   │           │   │   │   ├── test_moments.py
│   │           │   │   │   ├── test_pnpoly.py
│   │           │   │   │   ├── test_polygon.py
│   │           │   │   │   ├── test_profile.py
│   │           │   │   │   ├── test_regionprops.py
│   │           │   │   │   └── test_structural_similarity.py
│   │           │   │   ├── block.py
│   │           │   │   ├── _ccomp.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── entropy.py
│   │           │   │   ├── _find_contours_cy.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _find_contours.py
│   │           │   │   ├── fit.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _label.py
│   │           │   │   ├── _marching_cubes_classic_cy.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _marching_cubes_classic.py
│   │           │   │   ├── _marching_cubes_lewiner_cy.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _marching_cubes_lewiner_luts.py
│   │           │   │   ├── _marching_cubes_lewiner.py
│   │           │   │   ├── _moments_cy.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _moments.py
│   │           │   │   ├── _pnpoly.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── pnpoly.py
│   │           │   │   ├── _polygon.py
│   │           │   │   ├── profile.py
│   │           │   │   ├── _regionprops.py
│   │           │   │   ├── _regionprops_utils.py
│   │           │   │   └── setup.py
│   │           │   ├── metrics
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── _adapted_rand_error.cpython-38.pyc
│   │           │   │   │   ├── _contingency_table.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── set_metrics.cpython-38.pyc
│   │           │   │   │   ├── simple_metrics.cpython-38.pyc
│   │           │   │   │   ├── _structural_similarity.cpython-38.pyc
│   │           │   │   │   └── _variation_of_information.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_segmentation_metrics.cpython-38.pyc
│   │           │   │   │   │   ├── test_set_metrics.cpython-38.pyc
│   │           │   │   │   │   ├── test_simple_metrics.cpython-38.pyc
│   │           │   │   │   │   └── test_structural_similarity.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_segmentation_metrics.py
│   │           │   │   │   ├── test_set_metrics.py
│   │           │   │   │   ├── test_simple_metrics.py
│   │           │   │   │   └── test_structural_similarity.py
│   │           │   │   ├── _adapted_rand_error.py
│   │           │   │   ├── _contingency_table.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── set_metrics.py
│   │           │   │   ├── simple_metrics.py
│   │           │   │   ├── _structural_similarity.py
│   │           │   │   └── _variation_of_information.py
│   │           │   ├── morphology
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── binary.cpython-38.pyc
│   │           │   │   │   ├── convex_hull.cpython-38.pyc
│   │           │   │   │   ├── _deprecated.cpython-38.pyc
│   │           │   │   │   ├── extrema.cpython-38.pyc
│   │           │   │   │   ├── _flood_fill.cpython-38.pyc
│   │           │   │   │   ├── grey.cpython-38.pyc
│   │           │   │   │   ├── greyreconstruct.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── max_tree.cpython-38.pyc
│   │           │   │   │   ├── misc.cpython-38.pyc
│   │           │   │   │   ├── selem.cpython-38.pyc
│   │           │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   ├── _skeletonize.cpython-38.pyc
│   │           │   │   │   └── _util.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_binary.cpython-38.pyc
│   │           │   │   │   │   ├── test_convex_hull.cpython-38.pyc
│   │           │   │   │   │   ├── test_extrema.cpython-38.pyc
│   │           │   │   │   │   ├── test_flood_fill.cpython-38.pyc
│   │           │   │   │   │   ├── test_grey.cpython-38.pyc
│   │           │   │   │   │   ├── test_max_tree.cpython-38.pyc
│   │           │   │   │   │   ├── test_misc.cpython-38.pyc
│   │           │   │   │   │   ├── test_reconstruction.cpython-38.pyc
│   │           │   │   │   │   ├── test_selem.cpython-38.pyc
│   │           │   │   │   │   ├── test_skeletonize_3d.cpython-38.pyc
│   │           │   │   │   │   ├── test_skeletonize.cpython-38.pyc
│   │           │   │   │   │   └── test_util.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_binary.py
│   │           │   │   │   ├── test_convex_hull.py
│   │           │   │   │   ├── test_extrema.py
│   │           │   │   │   ├── test_flood_fill.py
│   │           │   │   │   ├── test_grey.py
│   │           │   │   │   ├── test_max_tree.py
│   │           │   │   │   ├── test_misc.py
│   │           │   │   │   ├── test_reconstruction.py
│   │           │   │   │   ├── test_selem.py
│   │           │   │   │   ├── test_skeletonize_3d.py
│   │           │   │   │   ├── test_skeletonize.py
│   │           │   │   │   └── test_util.py
│   │           │   │   ├── binary.py
│   │           │   │   ├── _convex_hull.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── convex_hull.py
│   │           │   │   ├── _deprecated.py
│   │           │   │   ├── _extrema_cy.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── extrema.py
│   │           │   │   ├── _flood_fill_cy.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _flood_fill.py
│   │           │   │   ├── grey.py
│   │           │   │   ├── _greyreconstruct.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── greyreconstruct.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _max_tree.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── max_tree.py
│   │           │   │   ├── misc.py
│   │           │   │   ├── selem.py
│   │           │   │   ├── setup.py
│   │           │   │   ├── _skeletonize_3d_cy.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _skeletonize_cy.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _skeletonize.py
│   │           │   │   └── _util.py
│   │           │   ├── __pycache__
│   │           │   │   ├── _build.cpython-38.pyc
│   │           │   │   ├── conftest.cpython-38.pyc
│   │           │   │   ├── __init__.cpython-38.pyc
│   │           │   │   └── setup.cpython-38.pyc
│   │           │   ├── registration
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── _masked_phase_cross_correlation.cpython-38.pyc
│   │           │   │   │   ├── _optical_flow.cpython-38.pyc
│   │           │   │   │   ├── _optical_flow_utils.cpython-38.pyc
│   │           │   │   │   └── _phase_cross_correlation.cpython-38.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _masked_phase_cross_correlation.py
│   │           │   │   ├── _optical_flow.py
│   │           │   │   ├── _optical_flow_utils.py
│   │           │   │   └── _phase_cross_correlation.py
│   │           │   ├── restoration
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── _cycle_spin.cpython-38.pyc
│   │           │   │   │   ├── deconvolution.cpython-38.pyc
│   │           │   │   │   ├── _denoise.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── inpaint.cpython-38.pyc
│   │           │   │   │   ├── j_invariant.cpython-38.pyc
│   │           │   │   │   ├── non_local_means.cpython-38.pyc
│   │           │   │   │   ├── rolling_ball.cpython-38.pyc
│   │           │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   ├── uft.cpython-38.pyc
│   │           │   │   │   └── unwrap.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_denoise.cpython-38.pyc
│   │           │   │   │   │   ├── test_inpaint.cpython-38.pyc
│   │           │   │   │   │   ├── test_j_invariant.cpython-38.pyc
│   │           │   │   │   │   ├── test_restoration.cpython-38.pyc
│   │           │   │   │   │   ├── test_rolling_ball.cpython-38.pyc
│   │           │   │   │   │   └── test_unwrap.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_denoise.py
│   │           │   │   │   ├── test_inpaint.py
│   │           │   │   │   ├── test_j_invariant.py
│   │           │   │   │   ├── test_restoration.py
│   │           │   │   │   ├── test_rolling_ball.py
│   │           │   │   │   └── test_unwrap.py
│   │           │   │   ├── _cycle_spin.py
│   │           │   │   ├── deconvolution.py
│   │           │   │   ├── _denoise_cy.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _denoise.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── inpaint.py
│   │           │   │   ├── j_invariant.py
│   │           │   │   ├── _nl_means_denoising.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── non_local_means.py
│   │           │   │   ├── _rolling_ball_cy.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── rolling_ball.py
│   │           │   │   ├── setup.py
│   │           │   │   ├── uft.py
│   │           │   │   ├── _unwrap_1d.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _unwrap_2d.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _unwrap_3d.cpython-38-x86_64-linux-gnu.so
│   │           │   │   └── unwrap.py
│   │           │   ├── scripts
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   └── skivi.cpython-38.pyc
│   │           │   │   ├── __init__.py
│   │           │   │   └── skivi.py
│   │           │   ├── segmentation
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── active_contour_model.cpython-38.pyc
│   │           │   │   │   ├── boundaries.cpython-38.pyc
│   │           │   │   │   ├── _chan_vese.cpython-38.pyc
│   │           │   │   │   ├── _clear_border.cpython-38.pyc
│   │           │   │   │   ├── _expand_labels.cpython-38.pyc
│   │           │   │   │   ├── _felzenszwalb.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── _join.cpython-38.pyc
│   │           │   │   │   ├── morphsnakes.cpython-38.pyc
│   │           │   │   │   ├── _quickshift.cpython-38.pyc
│   │           │   │   │   ├── random_walker_segmentation.cpython-38.pyc
│   │           │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   ├── slic_superpixels.cpython-38.pyc
│   │           │   │   │   └── _watershed.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_active_contour_model.cpython-38.pyc
│   │           │   │   │   │   ├── test_boundaries.cpython-38.pyc
│   │           │   │   │   │   ├── test_chan_vese.cpython-38.pyc
│   │           │   │   │   │   ├── test_clear_border.cpython-38.pyc
│   │           │   │   │   │   ├── test_expand_labels.cpython-38.pyc
│   │           │   │   │   │   ├── test_felzenszwalb.cpython-38.pyc
│   │           │   │   │   │   ├── test_join.cpython-38.pyc
│   │           │   │   │   │   ├── test_morphsnakes.cpython-38.pyc
│   │           │   │   │   │   ├── test_quickshift.cpython-38.pyc
│   │           │   │   │   │   ├── test_random_walker.cpython-38.pyc
│   │           │   │   │   │   ├── test_slic.cpython-38.pyc
│   │           │   │   │   │   └── test_watershed.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_active_contour_model.py
│   │           │   │   │   ├── test_boundaries.py
│   │           │   │   │   ├── test_chan_vese.py
│   │           │   │   │   ├── test_clear_border.py
│   │           │   │   │   ├── test_expand_labels.py
│   │           │   │   │   ├── test_felzenszwalb.py
│   │           │   │   │   ├── test_join.py
│   │           │   │   │   ├── test_morphsnakes.py
│   │           │   │   │   ├── test_quickshift.py
│   │           │   │   │   ├── test_random_walker.py
│   │           │   │   │   ├── test_slic.py
│   │           │   │   │   └── test_watershed.py
│   │           │   │   ├── active_contour_model.py
│   │           │   │   ├── boundaries.py
│   │           │   │   ├── _chan_vese.py
│   │           │   │   ├── _clear_border.py
│   │           │   │   ├── _expand_labels.py
│   │           │   │   ├── _felzenszwalb_cy.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _felzenszwalb.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _join.py
│   │           │   │   ├── morphsnakes.py
│   │           │   │   ├── _quickshift_cy.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _quickshift.py
│   │           │   │   ├── random_walker_segmentation.py
│   │           │   │   ├── setup.py
│   │           │   │   ├── _slic.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── slic_superpixels.py
│   │           │   │   ├── _watershed_cy.cpython-38-x86_64-linux-gnu.so
│   │           │   │   └── _watershed.py
│   │           │   ├── _shared
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── coord.cpython-38.pyc
│   │           │   │   │   ├── fft.cpython-38.pyc
│   │           │   │   │   ├── _geometry.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   ├── _tempfile.cpython-38.pyc
│   │           │   │   │   ├── testing.cpython-38.pyc
│   │           │   │   │   ├── utils.cpython-38.pyc
│   │           │   │   │   ├── version_requirements.cpython-38.pyc
│   │           │   │   │   └── _warnings.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_coord.cpython-38.pyc
│   │           │   │   │   │   ├── test_fast_exp.cpython-38.pyc
│   │           │   │   │   │   ├── test_geometry.cpython-38.pyc
│   │           │   │   │   │   ├── test_interpolation.cpython-38.pyc
│   │           │   │   │   │   ├── test_safe_as_int.cpython-38.pyc
│   │           │   │   │   │   ├── test_testing.cpython-38.pyc
│   │           │   │   │   │   ├── test_utils.cpython-38.pyc
│   │           │   │   │   │   ├── test_version_requirements.cpython-38.pyc
│   │           │   │   │   │   └── test_warnings.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_coord.py
│   │           │   │   │   ├── test_fast_exp.py
│   │           │   │   │   ├── test_geometry.py
│   │           │   │   │   ├── test_interpolation.py
│   │           │   │   │   ├── test_safe_as_int.py
│   │           │   │   │   ├── test_testing.py
│   │           │   │   │   ├── test_utils.py
│   │           │   │   │   ├── test_version_requirements.py
│   │           │   │   │   └── test_warnings.py
│   │           │   │   ├── coord.py
│   │           │   │   ├── fast_exp.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── fft.py
│   │           │   │   ├── geometry.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _geometry.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── interpolation.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── setup.py
│   │           │   │   ├── _tempfile.py
│   │           │   │   ├── testing.py
│   │           │   │   ├── transform.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── utils.py
│   │           │   │   ├── version_requirements.py
│   │           │   │   └── _warnings.py
│   │           │   ├── transform
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── finite_radon_transform.cpython-38.pyc
│   │           │   │   │   ├── _geometric.cpython-38.pyc
│   │           │   │   │   ├── hough_transform.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── integral.cpython-38.pyc
│   │           │   │   │   ├── pyramids.cpython-38.pyc
│   │           │   │   │   ├── radon_transform.cpython-38.pyc
│   │           │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   └── _warps.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_finite_radon_transform.cpython-38.pyc
│   │           │   │   │   │   ├── test_geometric.cpython-38.pyc
│   │           │   │   │   │   ├── test_hough_transform.cpython-38.pyc
│   │           │   │   │   │   ├── test_integral.cpython-38.pyc
│   │           │   │   │   │   ├── test_pyramids.cpython-38.pyc
│   │           │   │   │   │   ├── test_radon_transform.cpython-38.pyc
│   │           │   │   │   │   └── test_warps.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_finite_radon_transform.py
│   │           │   │   │   ├── test_geometric.py
│   │           │   │   │   ├── test_hough_transform.py
│   │           │   │   │   ├── test_integral.py
│   │           │   │   │   ├── test_pyramids.py
│   │           │   │   │   ├── test_radon_transform.py
│   │           │   │   │   └── test_warps.py
│   │           │   │   ├── finite_radon_transform.py
│   │           │   │   ├── _geometric.py
│   │           │   │   ├── _hough_transform.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── hough_transform.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── integral.py
│   │           │   │   ├── pyramids.py
│   │           │   │   ├── _radon_transform.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── radon_transform.py
│   │           │   │   ├── setup.py
│   │           │   │   ├── _warps_cy.cpython-38-x86_64-linux-gnu.so
│   │           │   │   └── _warps.py
│   │           │   ├── util
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── apply_parallel.cpython-38.pyc
│   │           │   │   │   ├── arraycrop.cpython-38.pyc
│   │           │   │   │   ├── compare.cpython-38.pyc
│   │           │   │   │   ├── dtype.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── _invert.cpython-38.pyc
│   │           │   │   │   ├── lookfor.cpython-38.pyc
│   │           │   │   │   ├── _map_array.cpython-38.pyc
│   │           │   │   │   ├── _montage.cpython-38.pyc
│   │           │   │   │   ├── noise.cpython-38.pyc
│   │           │   │   │   ├── _regular_grid.cpython-38.pyc
│   │           │   │   │   ├── setup.cpython-38.pyc
│   │           │   │   │   ├── shape.cpython-38.pyc
│   │           │   │   │   └── unique.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_apply_parallel.cpython-38.pyc
│   │           │   │   │   │   ├── test_arraycrop.cpython-38.pyc
│   │           │   │   │   │   ├── test_arraypad.cpython-38.pyc
│   │           │   │   │   │   ├── test_compare.cpython-38.pyc
│   │           │   │   │   │   ├── test_dtype.cpython-38.pyc
│   │           │   │   │   │   ├── test_invert.cpython-38.pyc
│   │           │   │   │   │   ├── test_map_array.cpython-38.pyc
│   │           │   │   │   │   ├── test_montage.cpython-38.pyc
│   │           │   │   │   │   ├── test_random_noise.cpython-38.pyc
│   │           │   │   │   │   ├── test_regular_grid.cpython-38.pyc
│   │           │   │   │   │   ├── test_shape.cpython-38.pyc
│   │           │   │   │   │   └── test_unique_rows.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_apply_parallel.py
│   │           │   │   │   ├── test_arraycrop.py
│   │           │   │   │   ├── test_arraypad.py
│   │           │   │   │   ├── test_compare.py
│   │           │   │   │   ├── test_dtype.py
│   │           │   │   │   ├── test_invert.py
│   │           │   │   │   ├── test_map_array.py
│   │           │   │   │   ├── test_montage.py
│   │           │   │   │   ├── test_random_noise.py
│   │           │   │   │   ├── test_regular_grid.py
│   │           │   │   │   ├── test_shape.py
│   │           │   │   │   └── test_unique_rows.py
│   │           │   │   ├── apply_parallel.py
│   │           │   │   ├── arraycrop.py
│   │           │   │   ├── compare.py
│   │           │   │   ├── dtype.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _invert.py
│   │           │   │   ├── lookfor.py
│   │           │   │   ├── _map_array.py
│   │           │   │   ├── _montage.py
│   │           │   │   ├── noise.py
│   │           │   │   ├── _regular_grid.py
│   │           │   │   ├── _remap.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── setup.py
│   │           │   │   ├── shape.py
│   │           │   │   └── unique.py
│   │           │   ├── viewer
│   │           │   │   ├── canvastools
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── base.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── linetool.cpython-38.pyc
│   │           │   │   │   │   ├── painttool.cpython-38.pyc
│   │           │   │   │   │   └── recttool.cpython-38.pyc
│   │           │   │   │   ├── base.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── linetool.py
│   │           │   │   │   ├── painttool.py
│   │           │   │   │   └── recttool.py
│   │           │   │   ├── plugins
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── base.cpython-38.pyc
│   │           │   │   │   │   ├── canny.cpython-38.pyc
│   │           │   │   │   │   ├── color_histogram.cpython-38.pyc
│   │           │   │   │   │   ├── crop.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── labelplugin.cpython-38.pyc
│   │           │   │   │   │   ├── lineprofile.cpython-38.pyc
│   │           │   │   │   │   ├── measure.cpython-38.pyc
│   │           │   │   │   │   ├── overlayplugin.cpython-38.pyc
│   │           │   │   │   │   └── plotplugin.cpython-38.pyc
│   │           │   │   │   ├── base.py
│   │           │   │   │   ├── canny.py
│   │           │   │   │   ├── color_histogram.py
│   │           │   │   │   ├── crop.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── labelplugin.py
│   │           │   │   │   ├── lineprofile.py
│   │           │   │   │   ├── measure.py
│   │           │   │   │   ├── overlayplugin.py
│   │           │   │   │   └── plotplugin.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   └── qt.cpython-38.pyc
│   │           │   │   ├── tests
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   ├── test_plugins.cpython-38.pyc
│   │           │   │   │   │   ├── test_tools.cpython-38.pyc
│   │           │   │   │   │   ├── test_utils.cpython-38.pyc
│   │           │   │   │   │   ├── test_viewer.cpython-38.pyc
│   │           │   │   │   │   └── test_widgets.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_plugins.py
│   │           │   │   │   ├── test_tools.py
│   │           │   │   │   ├── test_utils.py
│   │           │   │   │   ├── test_viewer.py
│   │           │   │   │   └── test_widgets.py
│   │           │   │   ├── utils
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── canvas.cpython-38.pyc
│   │           │   │   │   │   ├── core.cpython-38.pyc
│   │           │   │   │   │   ├── dialogs.cpython-38.pyc
│   │           │   │   │   │   └── __init__.cpython-38.pyc
│   │           │   │   │   ├── canvas.py
│   │           │   │   │   ├── core.py
│   │           │   │   │   ├── dialogs.py
│   │           │   │   │   └── __init__.py
│   │           │   │   ├── viewers
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── core.cpython-38.pyc
│   │           │   │   │   │   └── __init__.cpython-38.pyc
│   │           │   │   │   ├── core.py
│   │           │   │   │   └── __init__.py
│   │           │   │   ├── widgets
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── core.cpython-38.pyc
│   │           │   │   │   │   ├── history.cpython-38.pyc
│   │           │   │   │   │   └── __init__.cpython-38.pyc
│   │           │   │   │   ├── core.py
│   │           │   │   │   ├── history.py
│   │           │   │   │   └── __init__.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── qt.py
│   │           │   ├── _build.py
│   │           │   ├── conftest.py
│   │           │   ├── __init__.py
│   │           │   └── setup.py
│   │           ├── soupsieve
│   │           │   ├── __pycache__
│   │           │   │   ├── css_match.cpython-38.pyc
│   │           │   │   ├── css_parser.cpython-38.pyc
│   │           │   │   ├── css_types.cpython-38.pyc
│   │           │   │   ├── __init__.cpython-38.pyc
│   │           │   │   ├── __meta__.cpython-38.pyc
│   │           │   │   └── util.cpython-38.pyc
│   │           │   ├── css_match.py
│   │           │   ├── css_parser.py
│   │           │   ├── css_types.py
│   │           │   ├── __init__.py
│   │           │   ├── __meta__.py
│   │           │   └── util.py
│   │           ├── soupsieve-2.2.1.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE.md
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── tifffile
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-38.pyc
│   │           │   │   ├── lsm2bin.cpython-38.pyc
│   │           │   │   ├── __main__.cpython-38.pyc
│   │           │   │   ├── tiff2fsspec.cpython-38.pyc
│   │           │   │   ├── tiffcomment.cpython-38.pyc
│   │           │   │   ├── tifffile.cpython-38.pyc
│   │           │   │   └── tifffile_geodb.cpython-38.pyc
│   │           │   ├── __init__.py
│   │           │   ├── lsm2bin.py
│   │           │   ├── __main__.py
│   │           │   ├── tiff2fsspec.py
│   │           │   ├── tiffcomment.py
│   │           │   ├── tifffile_geodb.py
│   │           │   └── tifffile.py
│   │           ├── tifffile-2021.4.8.dist-info
│   │           │   ├── entry_points.txt
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── toml
│   │           │   ├── __pycache__
│   │           │   │   ├── decoder.cpython-38.pyc
│   │           │   │   ├── encoder.cpython-38.pyc
│   │           │   │   ├── __init__.cpython-38.pyc
│   │           │   │   ├── ordered.cpython-38.pyc
│   │           │   │   └── tz.cpython-38.pyc
│   │           │   ├── decoder.py
│   │           │   ├── encoder.py
│   │           │   ├── __init__.py
│   │           │   ├── ordered.py
│   │           │   └── tz.py
│   │           ├── toml-0.10.2.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── typing_extensions-3.10.0.0.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── urllib3
│   │           │   ├── contrib
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── appengine.cpython-38.pyc
│   │           │   │   │   ├── _appengine_environ.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── ntlmpool.cpython-38.pyc
│   │           │   │   │   ├── pyopenssl.cpython-38.pyc
│   │           │   │   │   ├── securetransport.cpython-38.pyc
│   │           │   │   │   └── socks.cpython-38.pyc
│   │           │   │   ├── _securetransport
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── bindings.cpython-38.pyc
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   └── low_level.cpython-38.pyc
│   │           │   │   │   ├── bindings.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── low_level.py
│   │           │   │   ├── _appengine_environ.py
│   │           │   │   ├── appengine.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── ntlmpool.py
│   │           │   │   ├── pyopenssl.py
│   │           │   │   ├── securetransport.py
│   │           │   │   └── socks.py
│   │           │   ├── packages
│   │           │   │   ├── backports
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   │   └── makefile.cpython-38.pyc
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── makefile.py
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   └── six.cpython-38.pyc
│   │           │   │   ├── ssl_match_hostname
│   │           │   │   │   ├── __pycache__
│   │           │   │   │   │   ├── _implementation.cpython-38.pyc
│   │           │   │   │   │   └── __init__.cpython-38.pyc
│   │           │   │   │   ├── _implementation.py
│   │           │   │   │   └── __init__.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── six.py
│   │           │   ├── __pycache__
│   │           │   │   ├── _collections.cpython-38.pyc
│   │           │   │   ├── connection.cpython-38.pyc
│   │           │   │   ├── connectionpool.cpython-38.pyc
│   │           │   │   ├── exceptions.cpython-38.pyc
│   │           │   │   ├── fields.cpython-38.pyc
│   │           │   │   ├── filepost.cpython-38.pyc
│   │           │   │   ├── __init__.cpython-38.pyc
│   │           │   │   ├── poolmanager.cpython-38.pyc
│   │           │   │   ├── request.cpython-38.pyc
│   │           │   │   ├── response.cpython-38.pyc
│   │           │   │   └── _version.cpython-38.pyc
│   │           │   ├── util
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── connection.cpython-38.pyc
│   │           │   │   │   ├── __init__.cpython-38.pyc
│   │           │   │   │   ├── proxy.cpython-38.pyc
│   │           │   │   │   ├── queue.cpython-38.pyc
│   │           │   │   │   ├── request.cpython-38.pyc
│   │           │   │   │   ├── response.cpython-38.pyc
│   │           │   │   │   ├── retry.cpython-38.pyc
│   │           │   │   │   ├── ssl_.cpython-38.pyc
│   │           │   │   │   ├── ssltransport.cpython-38.pyc
│   │           │   │   │   ├── timeout.cpython-38.pyc
│   │           │   │   │   ├── url.cpython-38.pyc
│   │           │   │   │   └── wait.cpython-38.pyc
│   │           │   │   ├── connection.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── proxy.py
│   │           │   │   ├── queue.py
│   │           │   │   ├── request.py
│   │           │   │   ├── response.py
│   │           │   │   ├── retry.py
│   │           │   │   ├── ssl_.py
│   │           │   │   ├── ssltransport.py
│   │           │   │   ├── timeout.py
│   │           │   │   ├── url.py
│   │           │   │   └── wait.py
│   │           │   ├── _collections.py
│   │           │   ├── connectionpool.py
│   │           │   ├── connection.py
│   │           │   ├── exceptions.py
│   │           │   ├── fields.py
│   │           │   ├── filepost.py
│   │           │   ├── __init__.py
│   │           │   ├── poolmanager.py
│   │           │   ├── request.py
│   │           │   ├── response.py
│   │           │   └── _version.py
│   │           ├── urllib3-1.26.5.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE.txt
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── yarl
│   │           │   ├── __pycache__
│   │           │   │   ├── __init__.cpython-38.pyc
│   │           │   │   ├── _quoting.cpython-38.pyc
│   │           │   │   ├── _quoting_py.cpython-38.pyc
│   │           │   │   └── _url.cpython-38.pyc
│   │           │   ├── __init__.py
│   │           │   ├── __init__.pyi
│   │           │   ├── py.typed
│   │           │   ├── _quoting_c.c
│   │           │   ├── _quoting_c.cpython-38-x86_64-linux-gnu.so
│   │           │   ├── _quoting_c.pyi
│   │           │   ├── _quoting_c.pyx
│   │           │   ├── _quoting.py
│   │           │   ├── _quoting_py.py
│   │           │   └── _url.py
│   │           ├── yarl-1.6.3.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── cycler.py
│   │           ├── decorator.py
│   │           ├── distutils-precedence.pth
│   │           ├── kiwisolver.cpython-38-x86_64-linux-gnu.so
│   │           ├── matplotlib-3.4.2-py3.8-nspkg.pth
│   │           ├── pylab.py
│   │           ├── pyparsing.py
│   │           ├── six.py
│   │           └── typing_extensions.py
│   ├── lib64 -> lib
│   ├── share
│   │   └── doc
│   │       └── networkx-2.5.1
│   │           ├── examples
│   │           │   ├── 3d_drawing
│   │           │   │   ├── __pycache__
│   │           │   │   │   └── mayavi2_spring.cpython-38.pyc
│   │           │   │   ├── mayavi2_spring.py
│   │           │   │   └── README.txt
│   │           │   ├── advanced
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── plot_eigenvalues.cpython-38.pyc
│   │           │   │   │   ├── plot_heavy_metal_umlaut.cpython-38.pyc
│   │           │   │   │   ├── plot_iterated_dynamical_systems.cpython-38.pyc
│   │           │   │   │   └── plot_parallel_betweenness.cpython-38.pyc
│   │           │   │   ├── plot_eigenvalues.py
│   │           │   │   ├── plot_heavy_metal_umlaut.py
│   │           │   │   ├── plot_iterated_dynamical_systems.py
│   │           │   │   ├── plot_parallel_betweenness.py
│   │           │   │   └── README.txt
│   │           │   ├── algorithms
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── plot_beam_search.cpython-38.pyc
│   │           │   │   │   ├── plot_blockmodel.cpython-38.pyc
│   │           │   │   │   ├── plot_davis_club.cpython-38.pyc
│   │           │   │   │   ├── plot_decomposition.cpython-38.pyc
│   │           │   │   │   ├── plot_krackhardt_centrality.cpython-38.pyc
│   │           │   │   │   └── plot_rcm.cpython-38.pyc
│   │           │   │   ├── hartford_drug.edgelist
│   │           │   │   ├── plot_beam_search.py
│   │           │   │   ├── plot_blockmodel.py
│   │           │   │   ├── plot_davis_club.py
│   │           │   │   ├── plot_decomposition.py
│   │           │   │   ├── plot_krackhardt_centrality.py
│   │           │   │   ├── plot_rcm.py
│   │           │   │   └── README.txt
│   │           │   ├── basic
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── plot_properties.cpython-38.pyc
│   │           │   │   │   └── plot_read_write.cpython-38.pyc
│   │           │   │   ├── plot_properties.py
│   │           │   │   ├── plot_read_write.py
│   │           │   │   └── README.txt
│   │           │   ├── drawing
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── plot_atlas.cpython-38.pyc
│   │           │   │   │   ├── plot_chess_masters.cpython-38.pyc
│   │           │   │   │   ├── plot_circular_tree.cpython-38.pyc
│   │           │   │   │   ├── plot_degree_histogram.cpython-38.pyc
│   │           │   │   │   ├── plot_degree_rank.cpython-38.pyc
│   │           │   │   │   ├── plot_directed.cpython-38.pyc
│   │           │   │   │   ├── plot_edge_colormap.cpython-38.pyc
│   │           │   │   │   ├── plot_ego_graph.cpython-38.pyc
│   │           │   │   │   ├── plot_four_grids.cpython-38.pyc
│   │           │   │   │   ├── plot_giant_component.cpython-38.pyc
│   │           │   │   │   ├── plot_house_with_colors.cpython-38.pyc
│   │           │   │   │   ├── plot_knuth_miles.cpython-38.pyc
│   │           │   │   │   ├── plot_labels_and_colors.cpython-38.pyc
│   │           │   │   │   ├── plot_lanl_routes.cpython-38.pyc
│   │           │   │   │   ├── plot_multipartite_graph.cpython-38.pyc
│   │           │   │   │   ├── plot_node_colormap.cpython-38.pyc
│   │           │   │   │   ├── plot_random_geometric_graph.cpython-38.pyc
│   │           │   │   │   ├── plot_sampson.cpython-38.pyc
│   │           │   │   │   ├── plot_simple_path.cpython-38.pyc
│   │           │   │   │   ├── plot_spectral_grid.cpython-38.pyc
│   │           │   │   │   ├── plot_unix_email.cpython-38.pyc
│   │           │   │   │   └── plot_weighted_graph.cpython-38.pyc
│   │           │   │   ├── chess_masters_WCC.pgn.bz2
│   │           │   │   ├── knuth_miles.txt.gz
│   │           │   │   ├── lanl_routes.edgelist
│   │           │   │   ├── plot_atlas.py
│   │           │   │   ├── plot_chess_masters.py
│   │           │   │   ├── plot_circular_tree.py
│   │           │   │   ├── plot_degree_histogram.py
│   │           │   │   ├── plot_degree_rank.py
│   │           │   │   ├── plot_directed.py
│   │           │   │   ├── plot_edge_colormap.py
│   │           │   │   ├── plot_ego_graph.py
│   │           │   │   ├── plot_four_grids.py
│   │           │   │   ├── plot_giant_component.py
│   │           │   │   ├── plot_house_with_colors.py
│   │           │   │   ├── plot_knuth_miles.py
│   │           │   │   ├── plot_labels_and_colors.py
│   │           │   │   ├── plot_lanl_routes.py
│   │           │   │   ├── plot_multipartite_graph.py
│   │           │   │   ├── plot_node_colormap.py
│   │           │   │   ├── plot_random_geometric_graph.py
│   │           │   │   ├── plot_sampson.py
│   │           │   │   ├── plot_simple_path.py
│   │           │   │   ├── plot_spectral_grid.py
│   │           │   │   ├── plot_unix_email.py
│   │           │   │   ├── plot_weighted_graph.py
│   │           │   │   ├── README.txt
│   │           │   │   └── unix_email.mbox
│   │           │   ├── graph
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── dot_atlas.cpython-38.pyc
│   │           │   │   │   ├── plot_degree_sequence.cpython-38.pyc
│   │           │   │   │   ├── plot_erdos_renyi.cpython-38.pyc
│   │           │   │   │   ├── plot_expected_degree_sequence.cpython-38.pyc
│   │           │   │   │   ├── plot_football.cpython-38.pyc
│   │           │   │   │   ├── plot_karate_club.cpython-38.pyc
│   │           │   │   │   ├── plot_napoleon_russian_campaign.cpython-38.pyc
│   │           │   │   │   ├── plot_roget.cpython-38.pyc
│   │           │   │   │   └── plot_words.cpython-38.pyc
│   │           │   │   ├── dot_atlas.py
│   │           │   │   ├── plot_degree_sequence.py
│   │           │   │   ├── plot_erdos_renyi.py
│   │           │   │   ├── plot_expected_degree_sequence.py
│   │           │   │   ├── plot_football.py
│   │           │   │   ├── plot_karate_club.py
│   │           │   │   ├── plot_napoleon_russian_campaign.py
│   │           │   │   ├── plot_roget.py
│   │           │   │   ├── plot_words.py
│   │           │   │   ├── README.txt
│   │           │   │   ├── roget_dat.txt.gz
│   │           │   │   └── words_dat.txt.gz
│   │           │   ├── javascript
│   │           │   │   ├── force
│   │           │   │   │   ├── force.css
│   │           │   │   │   ├── force.html
│   │           │   │   │   ├── force.js
│   │           │   │   │   └── README.txt
│   │           │   │   ├── __pycache__
│   │           │   │   │   └── force.cpython-38.pyc
│   │           │   │   ├── force.py
│   │           │   │   └── README.txt
│   │           │   ├── jit
│   │           │   │   ├── __pycache__
│   │           │   │   │   └── plot_rgraph.cpython-38.pyc
│   │           │   │   ├── plot_rgraph.py
│   │           │   │   └── README.txt
│   │           │   ├── pygraphviz
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── plot_pygraphviz_attributes.cpython-38.pyc
│   │           │   │   │   ├── plot_pygraphviz_draw.cpython-38.pyc
│   │           │   │   │   ├── plot_pygraphviz_simple.cpython-38.pyc
│   │           │   │   │   └── plot_write_dotfile.cpython-38.pyc
│   │           │   │   ├── plot_pygraphviz_attributes.py
│   │           │   │   ├── plot_pygraphviz_draw.py
│   │           │   │   ├── plot_pygraphviz_simple.py
│   │           │   │   ├── plot_write_dotfile.py
│   │           │   │   └── README.txt
│   │           │   ├── subclass
│   │           │   │   ├── __pycache__
│   │           │   │   │   ├── plot_antigraph.cpython-38.pyc
│   │           │   │   │   └── plot_printgraph.cpython-38.pyc
│   │           │   │   ├── plot_antigraph.py
│   │           │   │   ├── plot_printgraph.py
│   │           │   │   └── README.txt
│   │           │   └── README.txt
│   │           ├── LICENSE.txt
│   │           └── requirements.txt
│   └── pyvenv.cfg
├── LICENSE
├── README.md
├── README_TEXT.md
└── requirements.txt

887 directories, 8570 files

 ```
