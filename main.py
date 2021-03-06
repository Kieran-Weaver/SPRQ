import backend.rqstate as rqstate
import os
if __name__ == '__main__':
	rq = rqstate.RQState("resources/rooms.json")
	name = ''
	if rq.players == {}:
		while not name:
			print("Enter your name")
			name = input("> ")
		rq.loadPlayer(name)
	elif len(rq.players.keys()) == 1:
		name = list(rq.players.keys())[0]
	else:
		print(len(rq.players.keys()))
		while name not in rq.players.keys():
			print("Choose your name: ")
			print(" ".join(rq.players.keys()))
			name = input("> ")
	while True:
		rq.printState(name)
		print(os.linesep.join(rq.getMessages(name)))
		prompt = input("> ")
		if prompt == "exit":
			rq.savestate('rooms.json')
			break
		elif prompt:
			rq.parseMessage(name,prompt)
