
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
│   │           │   │   ├── _html5lib.py
│   │           │   │   ├── _htmlparser.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── _lxml.py
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
│   │           │   │   ├── chardetect.py
│   │           │   │   └── __init__.py
│   │           │   ├── metadata
│   │           │   │   ├── __init__.py
│   │           │   │   └── languages.py
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
│   │           │   │   ├── __init__.py
│   │           │   │   ├── isoparser.py
│   │           │   │   └── _parser.py
│   │           │   ├── tz
│   │           │   │   ├── _common.py
│   │           │   │   ├── _factories.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── tz.py
│   │           │   │   └── win.py
│   │           │   ├── zoneinfo
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
│   │           │   │       └── __init__.py
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
│   │           │   ├── __init__.py
│   │           │   └── override.py
│   │           ├── idna
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
│   │           │   │   ├── fetching.py
│   │           │   │   ├── findlib.py
│   │           │   │   ├── format.py
│   │           │   │   ├── functions.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── request.py
│   │           │   │   └── util.py
│   │           │   ├── plugins
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
│   │           │   │   ├── deprecation.py
│   │           │   │   └── __init__.py
│   │           │   ├── axes
│   │           │   │   ├── _axes.py
│   │           │   │   ├── _base.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _secondary_axes.py
│   │           │   │   └── _subplots.py
│   │           │   ├── backends
│   │           │   │   ├── qt_editor
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
│   │           │   │   ├── deprecation.py
│   │           │   │   └── __init__.py
│   │           │   ├── compat
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
│   │           │   │   ├── geo.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── polar.py
│   │           │   ├── sphinxext
│   │           │   │   ├── __init__.py
│   │           │   │   ├── mathmpl.py
│   │           │   │   └── plot_directive.py
│   │           │   ├── style
│   │           │   │   ├── core.py
│   │           │   │   └── __init__.py
│   │           │   ├── testing
│   │           │   │   ├── jpl_units
│   │           │   │   │   ├── Duration.py
│   │           │   │   │   ├── EpochConverter.py
│   │           │   │   │   ├── Epoch.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── StrConverter.py
│   │           │   │   │   ├── UnitDblConverter.py
│   │           │   │   │   ├── UnitDblFormatter.py
│   │           │   │   │   └── UnitDbl.py
│   │           │   │   ├── compare.py
│   │           │   │   ├── conftest.py
│   │           │   │   ├── decorators.py
│   │           │   │   ├── exceptions.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── widgets.py
│   │           │   ├── tests
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
│   │           │   │   ├── art3d.py
│   │           │   │   ├── axes3d.py
│   │           │   │   ├── axis3d.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── proj3d.py
│   │           │   └── tests
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
│   │           │   │   │   ├── tests
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
│   │           │   │   │   ├── tests
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
│   │           │   │   │   ├── tests
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
│   │           │   │   │   ├── tests
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
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── test_coloring.py
│   │           │   │   │   ├── equitable_coloring.py
│   │           │   │   │   ├── greedy_coloring.py
│   │           │   │   │   ├── greedy_coloring_with_interchange.py
│   │           │   │   │   └── __init__.py
│   │           │   │   ├── community
│   │           │   │   │   ├── tests
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
│   │           │   │   │   ├── tests
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
│   │           │   │   │   ├── tests
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
│   │           │   │   │   ├── tests
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
│   │           │   │   │   ├── tests
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
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── test_hits.py
│   │           │   │   │   │   └── test_pagerank.py
│   │           │   │   │   ├── hits_alg.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── pagerank_alg.py
│   │           │   │   ├── node_classification
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── test_harmonic_function.py
│   │           │   │   │   │   └── test_local_and_global_consistency.py
│   │           │   │   │   ├── hmn.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── lgc.py
│   │           │   │   │   └── utils.py
│   │           │   │   ├── operators
│   │           │   │   │   ├── tests
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
│   │           │   │   ├── shortest_paths
│   │           │   │   │   ├── tests
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
│   │           │   │   │   ├── tests
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
│   │           │   │   │   ├── tests
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
│   │           │   │   ├── tests
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
│   │           │   │   ├── tests
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
│   │           │   │   ├── tests
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
│   │           │   │   ├── tests
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
│   │           │   ├── readwrite
│   │           │   │   ├── json_graph
│   │           │   │   │   ├── tests
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
│   │           │   │   ├── tests
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
│   │           │   │   ├── tests
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── test_utils.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── test.py
│   │           │   │   └── utils.py
│   │           │   ├── tests
│   │           │   │   ├── __init__.py
│   │           │   │   ├── test_all_random_functions.py
│   │           │   │   ├── test_convert_numpy.py
│   │           │   │   ├── test_convert_pandas.py
│   │           │   │   ├── test_convert.py
│   │           │   │   ├── test_convert_scipy.py
│   │           │   │   ├── test_exceptions.py
│   │           │   │   └── test_relabel.py
│   │           │   ├── utils
│   │           │   │   ├── tests
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
│   │           │   │   ├── tests
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
│   │           │   │   │   │   ├── checks.pyx
│   │           │   │   │   │   └── setup.py
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
│   │           │   │   ├── tests
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
│   │           │   │   ├── constants.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── ufuncs.py
│   │           │   ├── f2py
│   │           │   │   ├── src
│   │           │   │   │   ├── fortranobject.c
│   │           │   │   │   └── fortranobject.h
│   │           │   │   ├── tests
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
│   │           │   │   ├── tests
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
│   │           │   │   ├── tests
│   │           │   │   │   ├── data
│   │           │   │   │   │   ├── py2-objarr.npy
│   │           │   │   │   │   ├── py2-objarr.npz
│   │           │   │   │   │   ├── py3-objarr.npy
│   │           │   │   │   │   ├── py3-objarr.npz
│   │           │   │   │   │   ├── python3.npy
│   │           │   │   │   │   └── win64python2.npy
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
│   │           │   │   ├── tests
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
│   │           │   │   ├── tests
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
│   │           │   │   ├── tests
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
│   │           │   │   ├── tests
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
│   │           │   ├── random
│   │           │   │   ├── _examples
│   │           │   │   │   ├── cffi
│   │           │   │   │   │   ├── extending.py
│   │           │   │   │   │   └── parse.py
│   │           │   │   │   ├── cython
│   │           │   │   │   │   ├── extending_distributions.pyx
│   │           │   │   │   │   ├── extending.pyx
│   │           │   │   │   │   └── setup.py
│   │           │   │   │   └── numba
│   │           │   │   │       ├── extending_distributions.py
│   │           │   │   │       └── extending.py
│   │           │   │   ├── lib
│   │           │   │   │   └── libnpyrandom.a
│   │           │   │   ├── tests
│   │           │   │   │   ├── data
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── mt19937-testset-1.csv
│   │           │   │   │   │   ├── mt19937-testset-2.csv
│   │           │   │   │   │   ├── pcg64-testset-1.csv
│   │           │   │   │   │   ├── pcg64-testset-2.csv
│   │           │   │   │   │   ├── philox-testset-1.csv
│   │           │   │   │   │   ├── philox-testset-2.csv
│   │           │   │   │   │   ├── sfc64-testset-1.csv
│   │           │   │   │   │   └── sfc64-testset-2.csv
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
│   │           │   │   │   ├── decorators.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── noseclasses.py
│   │           │   │   │   ├── nosetester.py
│   │           │   │   │   ├── parameterized.py
│   │           │   │   │   └── utils.py
│   │           │   │   ├── tests
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
│   │           │   │   ├── __init__.py
│   │           │   │   ├── test_ctypeslib.py
│   │           │   │   ├── test_matlib.py
│   │           │   │   ├── test_numpy_version.py
│   │           │   │   ├── test_public_api.py
│   │           │   │   ├── test_reloading.py
│   │           │   │   ├── test_scripts.py
│   │           │   │   └── test_warnings.py
│   │           │   ├── typing
│   │           │   │   ├── tests
│   │           │   │   │   ├── data
│   │           │   │   │   │   ├── fail
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
│   │           │   │   │   ├── base.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── installed.py
│   │           │   │   │   ├── sdist.py
│   │           │   │   │   └── wheel.py
│   │           │   │   ├── index
│   │           │   │   │   ├── collector.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── package_finder.py
│   │           │   │   │   └── sources.py
│   │           │   │   ├── locations
│   │           │   │   │   ├── base.py
│   │           │   │   │   ├── _distutils.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── _sysconfig.py
│   │           │   │   ├── metadata
│   │           │   │   │   ├── base.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── pkg_resources.py
│   │           │   │   ├── models
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
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── metadata_legacy.py
│   │           │   │   │   │   ├── metadata.py
│   │           │   │   │   │   ├── wheel_legacy.py
│   │           │   │   │   │   └── wheel.py
│   │           │   │   │   ├── install
│   │           │   │   │   │   ├── editable_legacy.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── legacy.py
│   │           │   │   │   │   └── wheel.py
│   │           │   │   │   ├── check.py
│   │           │   │   │   ├── freeze.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── prepare.py
│   │           │   │   ├── req
│   │           │   │   │   ├── constructors.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── req_file.py
│   │           │   │   │   ├── req_install.py
│   │           │   │   │   ├── req_set.py
│   │           │   │   │   ├── req_tracker.py
│   │           │   │   │   └── req_uninstall.py
│   │           │   │   ├── resolution
│   │           │   │   │   ├── legacy
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── resolver.py
│   │           │   │   │   ├── resolvelib
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
│   │           │   ├── _vendor
│   │           │   │   ├── cachecontrol
│   │           │   │   │   ├── caches
│   │           │   │   │   │   ├── file_cache.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── redis_cache.py
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
│   │           │   │   │   ├── cacert.pem
│   │           │   │   │   ├── core.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── __main__.py
│   │           │   │   ├── chardet
│   │           │   │   │   ├── cli
│   │           │   │   │   │   ├── chardetect.py
│   │           │   │   │   │   └── __init__.py
│   │           │   │   │   ├── metadata
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── languages.py
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
│   │           │   │   │   ├── ansi.py
│   │           │   │   │   ├── ansitowin32.py
│   │           │   │   │   ├── initialise.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── win32.py
│   │           │   │   │   └── winterm.py
│   │           │   │   ├── distlib
│   │           │   │   │   ├── _backport
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── misc.py
│   │           │   │   │   │   ├── shutil.py
│   │           │   │   │   │   ├── sysconfig.cfg
│   │           │   │   │   │   ├── sysconfig.py
│   │           │   │   │   │   └── tarfile.py
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
│   │           │   │   │   │   ├── alphabeticalattributes.py
│   │           │   │   │   │   ├── base.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── inject_meta_charset.py
│   │           │   │   │   │   ├── lint.py
│   │           │   │   │   │   ├── optionaltags.py
│   │           │   │   │   │   ├── sanitizer.py
│   │           │   │   │   │   └── whitespace.py
│   │           │   │   │   ├── treeadapters
│   │           │   │   │   │   ├── genshi.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── sax.py
│   │           │   │   │   ├── treebuilders
│   │           │   │   │   │   ├── base.py
│   │           │   │   │   │   ├── dom.py
│   │           │   │   │   │   ├── etree_lxml.py
│   │           │   │   │   │   ├── etree.py
│   │           │   │   │   │   └── __init__.py
│   │           │   │   │   ├── treewalkers
│   │           │   │   │   │   ├── base.py
│   │           │   │   │   │   ├── dom.py
│   │           │   │   │   │   ├── etree_lxml.py
│   │           │   │   │   │   ├── etree.py
│   │           │   │   │   │   ├── genshi.py
│   │           │   │   │   │   └── __init__.py
│   │           │   │   │   ├── _trie
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
│   │           │   │   │   ├── codec.py
│   │           │   │   │   ├── compat.py
│   │           │   │   │   ├── core.py
│   │           │   │   │   ├── idnadata.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── intranges.py
│   │           │   │   │   ├── package_data.py
│   │           │   │   │   └── uts46data.py
│   │           │   │   ├── msgpack
│   │           │   │   │   ├── exceptions.py
│   │           │   │   │   ├── ext.py
│   │           │   │   │   ├── fallback.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── _version.py
│   │           │   │   ├── packaging
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
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── _in_process.py
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
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── py31compat.py
│   │           │   │   ├── progress
│   │           │   │   │   ├── bar.py
│   │           │   │   │   ├── counter.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── spinner.py
│   │           │   │   ├── requests
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
│   │           │   │   │   │   ├── collections_abc.py
│   │           │   │   │   │   └── __init__.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── providers.py
│   │           │   │   │   ├── reporters.py
│   │           │   │   │   ├── resolvers.py
│   │           │   │   │   └── structs.py
│   │           │   │   ├── tenacity
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
│   │           │   │   │   ├── decoder.py
│   │           │   │   │   ├── encoder.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── ordered.py
│   │           │   │   │   └── tz.py
│   │           │   │   ├── urllib3
│   │           │   │   │   ├── contrib
│   │           │   │   │   │   ├── _securetransport
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
│   │           │   │   │   │   │   ├── __init__.py
│   │           │   │   │   │   │   └── makefile.py
│   │           │   │   │   │   ├── ssl_match_hostname
│   │           │   │   │   │   │   ├── _implementation.py
│   │           │   │   │   │   │   └── __init__.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── six.py
│   │           │   │   │   ├── util
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
│   │           │   │   └── __init__.py
│   │           │   ├── tests
│   │           │   │   └── data
│   │           │   │       └── my-test-package-source
│   │           │   │           └── setup.py
│   │           │   ├── _vendor
│   │           │   │   ├── packaging
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
│   │           │   │   ├── appdirs.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── pyparsing.py
│   │           │   └── __init__.py
│   │           ├── pluggy
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
│   │           │   │   ├── _assertionnew.py
│   │           │   │   ├── _assertionold.py
│   │           │   │   ├── assertion.py
│   │           │   │   ├── code.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _py2traceback.py
│   │           │   │   └── source.py
│   │           │   ├── _io
│   │           │   │   ├── capture.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── saferepr.py
│   │           │   │   └── terminalwriter.py
│   │           │   ├── _log
│   │           │   │   ├── __init__.py
│   │           │   │   ├── log.py
│   │           │   │   └── warning.py
│   │           │   ├── _path
│   │           │   │   ├── cacheutil.py
│   │           │   │   ├── common.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── local.py
│   │           │   │   ├── svnurl.py
│   │           │   │   └── svnwc.py
│   │           │   ├── _process
│   │           │   │   ├── cmdexec.py
│   │           │   │   ├── forkedfunc.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── killproc.py
│   │           │   ├── _vendored_packages
│   │           │   │   ├── apipkg
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
│   │           ├── pyparsing-2.4.7.dist-info
│   │           │   ├── INSTALLER
│   │           │   ├── LICENSE
│   │           │   ├── METADATA
│   │           │   ├── RECORD
│   │           │   ├── top_level.txt
│   │           │   └── WHEEL
│   │           ├── _pytest
│   │           │   ├── assertion
│   │           │   │   ├── __init__.py
│   │           │   │   ├── rewrite.py
│   │           │   │   ├── truncate.py
│   │           │   │   └── util.py
│   │           │   ├── _code
│   │           │   │   ├── code.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── source.py
│   │           │   ├── config
│   │           │   │   ├── argparsing.py
│   │           │   │   ├── exceptions.py
│   │           │   │   ├── findpaths.py
│   │           │   │   └── __init__.py
│   │           │   ├── _io
│   │           │   │   ├── __init__.py
│   │           │   │   ├── saferepr.py
│   │           │   │   ├── terminalwriter.py
│   │           │   │   └── wcwidth.py
│   │           │   ├── mark
│   │           │   │   ├── expression.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── structures.py
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
│   │           │   │   ├── _cwt.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _dwt.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _pywt.cpython-38-x86_64-linux-gnu.so
│   │           │   │   └── _swt.cpython-38-x86_64-linux-gnu.so
│   │           │   ├── tests
│   │           │   │   ├── data
│   │           │   │   │   ├── cwt_matlabR2015b_result.npz
│   │           │   │   │   ├── dwt_matlabR2012a_result.npz
│   │           │   │   │   ├── generate_matlab_data_cwt.py
│   │           │   │   │   ├── generate_matlab_data.py
│   │           │   │   │   └── wavelab_test_signals.npz
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
│   │           │   │   ├── tests
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── test_scipy_version.py
│   │           │   │   ├── compiler_helper.py
│   │           │   │   ├── _fortran.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── setup.py
│   │           │   │   └── system_info.py
│   │           │   ├── cluster
│   │           │   │   ├── tests
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
│   │           │   │   ├── tests
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_codata.py
│   │           │   │   │   └── test_constants.py
│   │           │   │   ├── codata.py
│   │           │   │   ├── constants.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── setup.py
│   │           │   ├── fft
│   │           │   │   ├── _pocketfft
│   │           │   │   │   ├── tests
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
│   │           │   │   ├── tests
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
│   │           │   │   ├── tests
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
│   │           │   │   │   ├── tests
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
│   │           │   │   ├── tests
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
│   │           │   │   ├── tests
│   │           │   │   │   ├── data
│   │           │   │   │   │   ├── bug-1310.npz
│   │           │   │   │   │   └── estimate_gradients_hang.npy
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
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── test_arffread.py
│   │           │   │   │   ├── arffread.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── setup.py
│   │           │   │   ├── harwell_boeing
│   │           │   │   │   ├── tests
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   ├── test_fortran_format.py
│   │           │   │   │   │   └── test_hb.py
│   │           │   │   │   ├── _fortran_format_parser.py
│   │           │   │   │   ├── hb.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── setup.py
│   │           │   │   ├── matlab
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
│   │           │   │   ├── tests
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
│   │           │   │   ├── tests
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
│   │           │   │   ├── tests
│   │           │   │   │   ├── data
│   │           │   │   │   │   ├── label_inputs.txt
│   │           │   │   │   │   ├── label_results.txt
│   │           │   │   │   │   ├── label_strels.txt
│   │           │   │   │   │   └── README.txt
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
│   │           │   │   ├── tests
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
│   │           │   │   │   ├── _highs_constants.cpython-38-x86_64-linux-gnu.so
│   │           │   │   │   ├── _highs_wrapper.cpython-38-x86_64-linux-gnu.so
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _mpswriter.cpython-38-x86_64-linux-gnu.so
│   │           │   │   │   └── setup.py
│   │           │   │   ├── lbfgsb_src
│   │           │   │   │   └── README
│   │           │   │   ├── _lsq
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
│   │           │   │   ├── _shgo_lib
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── sobol_seq.py
│   │           │   │   │   ├── sobol_vec.gz
│   │           │   │   │   └── triangulation.py
│   │           │   │   ├── tests
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
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── setup.py
│   │           │   │   │   └── _trlib.cpython-38-x86_64-linux-gnu.so
│   │           │   │   ├── _trustregion_constr
│   │           │   │   │   ├── tests
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
│   │           │   ├── signal
│   │           │   │   ├── tests
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
│   │           │   │   │   ├── tests
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
│   │           │   │   │   │   ├── SuperLU
│   │           │   │   │   │   │   └── License.txt
│   │           │   │   │   │   ├── tests
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
│   │           │   │   │   │   │   ├── tests
│   │           │   │   │   │   │   │   ├── __init__.py
│   │           │   │   │   │   │   │   └── test_arpack.py
│   │           │   │   │   │   │   ├── _arpack.cpython-38-x86_64-linux-gnu.so
│   │           │   │   │   │   │   ├── arpack.py
│   │           │   │   │   │   │   ├── __init__.py
│   │           │   │   │   │   │   └── setup.py
│   │           │   │   │   │   ├── lobpcg
│   │           │   │   │   │   │   ├── tests
│   │           │   │   │   │   │   │   ├── __init__.py
│   │           │   │   │   │   │   │   └── test_lobpcg.py
│   │           │   │   │   │   │   ├── __init__.py
│   │           │   │   │   │   │   ├── lobpcg.py
│   │           │   │   │   │   │   └── setup.py
│   │           │   │   │   │   ├── __init__.py
│   │           │   │   │   │   └── setup.py
│   │           │   │   │   ├── isolve
│   │           │   │   │   │   ├── tests
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
│   │           │   │   │   ├── tests
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
│   │           │   │   ├── tests
│   │           │   │   │   ├── data
│   │           │   │   │   │   ├── csc_py2.npz
│   │           │   │   │   │   └── csc_py3.npz
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
│   │           │   │   │   ├── tests
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
│   │           │   │   ├── tests
│   │           │   │   │   ├── data
│   │           │   │   │   │   ├── boost.npz
│   │           │   │   │   │   ├── gsl.npz
│   │           │   │   │   │   ├── local.npz
│   │           │   │   │   │   └── README
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
│   │           │   │   └── __init__.py
│   │           │   ├── _vendor
│   │           │   │   ├── more_itertools
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── more.py
│   │           │   │   │   └── recipes.py
│   │           │   │   ├── packaging
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
│   │           │   │   ├── tests
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
│   │           │   │   ├── tests
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
│   │           │   │   ├── tests
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
│   │           │   │   ├── tests
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_exposure.py
│   │           │   │   │   └── test_histogram_matching.py
│   │           │   │   ├── _adapthist.py
│   │           │   │   ├── exposure.py
│   │           │   │   ├── histogram_matching.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── setup.py
│   │           │   ├── feature
│   │           │   │   ├── tests
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
│   │           │   │   ├── rank
│   │           │   │   │   ├── tests
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
│   │           │   │   │   ├── graph_cut.py
│   │           │   │   │   ├── graph_merge.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── _ncut_cy.cpython-38-x86_64-linux-gnu.so
│   │           │   │   │   ├── _ncut.py
│   │           │   │   │   ├── rag.py
│   │           │   │   │   └── setup.py
│   │           │   │   ├── __init__.py
│   │           │   │   ├── manual_segmentation.py
│   │           │   │   ├── setup.py
│   │           │   │   └── trainable_segmentation.py
│   │           │   ├── graph
│   │           │   │   ├── tests
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
│   │           │   │   ├── tests
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
│   │           │   │   ├── tests
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
│   │           │   │   ├── tests
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
│   │           │   │   ├── tests
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
│   │           │   ├── registration
│   │           │   │   ├── __init__.py
│   │           │   │   ├── _masked_phase_cross_correlation.py
│   │           │   │   ├── _optical_flow.py
│   │           │   │   ├── _optical_flow_utils.py
│   │           │   │   └── _phase_cross_correlation.py
│   │           │   ├── restoration
│   │           │   │   ├── tests
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
│   │           │   │   ├── __init__.py
│   │           │   │   └── skivi.py
│   │           │   ├── segmentation
│   │           │   │   ├── tests
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
│   │           │   │   ├── tests
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
│   │           │   │   ├── tests
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
│   │           │   │   ├── tests
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
│   │           │   │   │   ├── base.py
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── linetool.py
│   │           │   │   │   ├── painttool.py
│   │           │   │   │   └── recttool.py
│   │           │   │   ├── plugins
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
│   │           │   │   ├── tests
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   ├── test_plugins.py
│   │           │   │   │   ├── test_tools.py
│   │           │   │   │   ├── test_utils.py
│   │           │   │   │   ├── test_viewer.py
│   │           │   │   │   └── test_widgets.py
│   │           │   │   ├── utils
│   │           │   │   │   ├── canvas.py
│   │           │   │   │   ├── core.py
│   │           │   │   │   ├── dialogs.py
│   │           │   │   │   └── __init__.py
│   │           │   │   ├── viewers
│   │           │   │   │   ├── core.py
│   │           │   │   │   └── __init__.py
│   │           │   │   ├── widgets
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
│   │           │   │   ├── _securetransport
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
│   │           │   │   │   ├── __init__.py
│   │           │   │   │   └── makefile.py
│   │           │   │   ├── ssl_match_hostname
│   │           │   │   │   ├── _implementation.py
│   │           │   │   │   └── __init__.py
│   │           │   │   ├── __init__.py
│   │           │   │   └── six.py
│   │           │   ├── util
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
│   │           │   │   ├── mayavi2_spring.py
│   │           │   │   └── README.txt
│   │           │   ├── advanced
│   │           │   │   ├── plot_eigenvalues.py
│   │           │   │   ├── plot_heavy_metal_umlaut.py
│   │           │   │   ├── plot_iterated_dynamical_systems.py
│   │           │   │   ├── plot_parallel_betweenness.py
│   │           │   │   └── README.txt
│   │           │   ├── algorithms
│   │           │   │   ├── hartford_drug.edgelist
│   │           │   │   ├── plot_beam_search.py
│   │           │   │   ├── plot_blockmodel.py
│   │           │   │   ├── plot_davis_club.py
│   │           │   │   ├── plot_decomposition.py
│   │           │   │   ├── plot_krackhardt_centrality.py
│   │           │   │   ├── plot_rcm.py
│   │           │   │   └── README.txt
│   │           │   ├── basic
│   │           │   │   ├── plot_properties.py
│   │           │   │   ├── plot_read_write.py
│   │           │   │   └── README.txt
│   │           │   ├── drawing
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
│   │           │   │   ├── force.py
│   │           │   │   └── README.txt
│   │           │   ├── jit
│   │           │   │   ├── plot_rgraph.py
│   │           │   │   └── README.txt
│   │           │   ├── pygraphviz
│   │           │   │   ├── plot_pygraphviz_attributes.py
│   │           │   │   ├── plot_pygraphviz_draw.py
│   │           │   │   ├── plot_pygraphviz_simple.py
│   │           │   │   ├── plot_write_dotfile.py
│   │           │   │   └── README.txt
│   │           │   ├── subclass
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

509 directories, 5046 files

 ```
