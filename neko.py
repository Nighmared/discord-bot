import random
import logging

IMPORTS =()
logger = logging.getLogger("botlogger")


answers = (
	"nope",
	"must be hard giving in to such lowly desires",
	"what did u expect here??",
	"heck no, like come on, get your life together mate",
	"its a no from me, but I heard some of the other bots aren't so dedicated to quality",
	"fuck off mate!",
	"ETH is far more important thank looking at such disgusting imagery",
	"You should learn to pass BP, not be looking to fulfil such earthly cravings",
	"You shall not pass (BP)!",
	"Ueli doesn't like you anymore",
)

def getNeko():
	indx = int(random.random()*len(answers))
	return answers[indx]