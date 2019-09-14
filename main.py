import rqstate
if __name__ == '__main__':
	rq = rqstate.RQState("rooms.json")
	while True:
		rq.printRoom("testplayer")
		rq.oqlock.acquire()
		for message in rq.outqueue:
			print(message)
		rq.outqueue.clear()
		rq.oqlock.release()
		prompt = input("> ")
		if prompt == "exit":
			rq.savestate('rooms.json')
			break
		else:
			rq.parseMessage("testplayer",prompt)
