import discord
import curses
from discord.channel import TextChannel
import discord.ext.commands
import threading
from curses import wrapper
from queue import Queue
from discord.ext.commands import Bot
from discord.ext import tasks
import asyncio

#TODO:
#	- curses func for recording keyboard input
#	- curses func for displaying incoming msgs
#	- discord.py handling to fetch incoming msgs
#	- asyncio thingy to catch incoming keystrokes

class InputHandler(discord.ext.commands.Cog):
	def __init__(self,client:discord.ext.commands.Bot,msgq:Queue,coutwin:curses.window,status):
		with open("client_debug.log","a") as f:
			f.write("instance got created\n")
		self.client = client
		self.msgq = msgq
		self.coutwin = coutwin
		self.chosen_channel = None
		self.server = None 
		self.status =status
		self.consume_messages_to_send.start()

	@tasks.loop(seconds=0.5)
	async def consume_messages_to_send(self):
		with open("client_debug.log","a") as f:
			f.write("henlo lol\n")
		self.server = await self.client.fetch_guild(SERVER_ID)
		self.coutwin.refresh()
		COMMANDS = (
			"help",
			"channels",
			"servers",
			"setserver",
			"setchannel",
			"quit",

		)
		PREFIX = "%"

		while self.msgq.not_empty:
			next_inp = self.msgq.get()
			if next_inp.startswith(PREFIX): #client command
				self.coutwin.erase()
				self.coutwin.refresh()
				space_split = next_inp[1:].split(" ")
				cmd = space_split[0]
				args = ()
				if len(space_split)>1:
					args = space_split[1:]
				if cmd == "channels":
					chan_list = list(filter(lambda x : isinstance(x, discord.TextChannel),self.server.channels))
					indx = 0
					for channel in chan_list:
						self.coutwin.addstr(indx,0,f"{indx} {channel.name[:17]}")
						indx+=1
				elif cmd == "servers":
					guild_list = self.client.guilds
					indx = 0
					for guild in guild_list:
						self.coutwin.addstr(indx,0,f"{indx} {guild.name[:17]}")
						indx+=1
				elif cmd == "help":
					indx = 0
					for command in COMMANDS:
						self.coutwin.addstr(indx,0,f"{PREFIX}{command}")
						indx+=1
				elif cmd == "setchannel":
					self.chosen_channel = (await self.server.fetch_channels())[int(args[0])]
				elif cmd == "setserver":
					self.server = self.client.guilds[int(args[0])]
					self.coutwin.erase()
					self.coutwin.refresh()
					self.coutwin.addstr(0,0,f"Set server to {self.server.name}",curses.A_BLINK)
					self.coutwin.refresh()
				elif cmd == "quit":
					stdscr.clear()
					curses.echo()
					stdscr.keypad(False)
					curses.nocbreak()
					curses.endwin()
					status.run = False
					
					exit()
				else:
					continue # TODO show invalid cmd msg
				self.coutwin.refresh()
			else: #is message to be sent
				if self.chosen_channel != None:
					try:
						await self.chosen_channel.send(content=next_inp)
					except Exception as e:
						continue
				pass # TODO implement



stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

class Status:
	def __init__(self):
		self.run = True


status = Status()


msgq = Queue()
client = Bot("·")

with open(".token.txt","r") as f:
	TOKEN = f.read()


L_PAD = 0
line_n = 1
T_PAD = 0
WIN_HEIGHT, WIN_WIDTH = stdscr.getmaxyx()
INPUT_HEIGHT = 4
CMD_OUT_WIDTH = 50
OUTPUT_HEIGHT = WIN_HEIGHT-INPUT_HEIGHT-1
CMD_OUT_HEIGHT = WIN_HEIGHT
CMD_OUT_STARTX = WIN_WIDTH-CMD_OUT_WIDTH
OUTPUT_WIDTH = INPUT_WIDTH = WIN_WIDTH-CMD_OUT_WIDTH-1
LINE_LIM = OUTPUT_HEIGHT

SERVER_ID = 695246759382745108

outwin = curses.newwin(OUTPUT_HEIGHT,OUTPUT_WIDTH,0,0)
inpwin = curses.newwin(INPUT_HEIGHT,INPUT_WIDTH,OUTPUT_HEIGHT+2,0)
cmdoutwin = curses.newwin(CMD_OUT_HEIGHT,CMD_OUT_WIDTH,0,CMD_OUT_STARTX)

horiz_sep_win = curses.newwin(1,OUTPUT_WIDTH-1,OUTPUT_HEIGHT+1,0)
verti_sep_win = curses.newwin(WIN_HEIGHT,1,0,OUTPUT_WIDTH)
horiz_sep_win.erase()
verti_sep_win.erase()
horiz_sep_win.addstr(0,0,"-"*(OUTPUT_WIDTH-2))
verti_sep_win.addstr(0,0,"|"*(WIN_HEIGHT-1))
horiz_sep_win.refresh()
verti_sep_win.refresh()


with open("curses_metrics.log", "w") as f:
	f.write(f"height:\t{WIN_HEIGHT}\n")
	f.write(f"width:\t{WIN_WIDTH}\n")
	f.write(f"chat height:\t{OUTPUT_HEIGHT}\n")
	f.write(f"chat width:\t {OUTPUT_WIDTH}\n")
	f.write(f"input height:\t{INPUT_HEIGHT}\n")
	f.write(f"input start at y:\t{OUTPUT_HEIGHT+2}\n")
	f.write(f"horiz_zep y starts at: \t {OUTPUT_HEIGHT+1}\n")



msgs =[]
msg_zero = 0
focussing_channel = False
chan_id = 0


@client.event
async def on_message(message:discord.Message):
	if message.channel.id == 819966095070330950: #eth place
		return
	if message.channel.id==chan_id or not focussing_channel:
		curses_print_msg(message)
	else:
		return

@client.event
async def on_ready():
	global msgq
	outwin.erase()
	#print("test")
	outwin.addstr(0,L_PAD,"--READY--")
	outwin.refresh()
	client.add_cog(InputHandler(client,coutwin=cmdoutwin,msgq=msgq,status=status))


def curses_print_msg(message:discord.Message):
	global line_n
	global msgs
	global msg_zero
	md = message.created_at
	nice_date = f"{md.day}.{md.month}.{md.year}-{md.hour}:{md.minute}"
	msg_string = f"{nice_date} | {message.channel.name[:10].rjust(10)} <{message.author.name[:10].center(11)}> : {message.content}"
	msgs.append(msg_string)
	outwin.addstr(line_n,L_PAD,msg_string)
	line_n+=1
	if line_n  > LINE_LIM:
		outwin.erase()
		line_n=0
		msg_zero+=1
		for s in msgs[msg_zero:]:
			outwin.addstr(line_n+T_PAD,L_PAD,s)
			line_n+=1
		#	outwin.refresh()

	outwin.refresh()


def curses_get_input(stdscr:curses.window,inputwin:curses.window,msgqueue:Queue,status):
	to_send = ""
	next_char_x = 2
	next_char_y = 0
	inputwin.addstr(0,0,">>")
	inputwin.refresh()
	while status.run:
		curr_in = inputwin.getkey()	
		with open("keys.log","a") as f:
			f.write(f"got {curr_in}")
		if curr_in == "\n":
			msgqueue.put(to_send)
			to_send = ""
			inputwin.erase()
			next_char_x = next_char_y = 0
			inputwin.addstr(next_char_y,next_char_x,">>")
			next_char_x += 2
		elif curr_in == 'KEY_BACKSPACE' or curr_in == curses.KEY_BACKSPACE or curr_in == "^?" or curr_in=="\b" or curr_in == '\x7f':
			with open("clientdebug.log","a") as f:
				f.write(f"got key {curr_in} went into backspace case\n")
			if next_char_x == 2 and next_char_y == 0:
				continue #nothing to delete
			if next_char_x == 0 and next_char_y>0: # at the start of a new line
				next_char_y -=1
				next_char_x = INPUT_WIDTH-1
			elif (next_char_x > 0 and next_char_y>0) or next_char_x>2:
				next_char_x -= 1

			inputwin.addstr(next_char_y,next_char_x," ")
			inputwin.move(next_char_y,next_char_x)
			to_send = to_send[:-1]
		else:
			to_send += curr_in
			inputwin.addstr(next_char_y,next_char_x,curr_in)
			next_char_x+=1
			if next_char_x==INPUT_WIDTH:
				next_char_x = 0
				next_char_y += 1
		
		inputwin.refresh()




reader_thread = threading.Thread(target=curses_get_input,args=(stdscr,inpwin,msgq,status))
reader_thread.start()




try:
	client.run(TOKEN)
except Exception as e:
	status.run = False
	log = open("client_log.log","a")
	for s in msgs:
		log.write(s+"\n")
	log.write("PROPERLY EXITED!!\n")
	log.close()
	stdscr.clear()
	curses.echo()
	stdscr.keypad(False)
	curses.nocbreak()
	curses.endwin()
	print("!!!!",str(e))
	exit()
exit()