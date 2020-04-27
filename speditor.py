import bimpy
import rqstate
import os

def startWindow(name, x, y, w, h):
	bimpy.set_next_window_pos(bimpy.Vec2(x,y), int(bimpy.Condition.Once))
	bimpy.set_next_window_size(bimpy.Vec2(w, h), int(bimpy.Condition.Once))
	bimpy.begin(name, flags=bimpy.WindowFlags.NoTitleBar|bimpy.WindowFlags.NoResize|bimpy.WindowFlags.NoMove)

class Terminal:
	def __init__(self, x, y, w, h, content):
		self.dims = (x, y, w, h)
		self.content = content
		self._text = ""
		self._prompt = bimpy.String()

	def draw(self):
		startWindow("Terminal", *self.dims)
		self.fitText()
		bimpy.begin_child("Terminal", size=bimpy.Vec2(W-20, H-100), border = True, extra_flags=0)
		bimpy.text_wrapped(self._text)
		bimpy.end_child()
		bimpy.text("> ")
		bimpy.same_line()
		if bimpy.input_text(
			"Press enter to continue",
			self._prompt,
			256,
			flags = int(bimpy.InputTextFlags.EnterReturnsTrue)
		):
			self.append(prompt)
			promptvalue = str(self._prompt.value)
			self._prompt.value = ""
			bimpy.set_keyboard_focus_here(-1)
			return promptvalue
		else:
			return None

	def fitText(self):
		self._text = os.linesep.join(self.content)
		while bimpy.calc_text_size(self._text, wrap_width=(W-20)).y > (H - 100):
			self.content.pop(0)
			self._text = os.linesep.join(self.content)
	
	def append(self, *args):
		if args[0]:
			self.content += [*args]

class Debugger:
	def __init__(self):
		self.entries = {}
	def add_entry(self, text, callback):
		self.entries[text] = {
			"value" : bimpy.String(),
			"checked" : bimpy.Bool(),
			"callback" : callback
		}
	def draw(self):
		startWindow("Debugger", W, 0, 1080-W, H)
		bimpy.text("Debugger")
		for entry in self.entries:
			bimpy.input_text(entry, self.entries[entry]["value"], 256)
			bimpy.same_line()
			if bimpy.checkbox(f"##{entry}_checkbox", self.entries[entry]["checked"]):
				self.entries[entry]["callback"](self.entries[entry]["checked"].value)
W = 640
H = 480
rq = rqstate.RQState("rooms.json")
ctx = bimpy.Context()
ctx.init(1080, 480, "SPRQ Editor")
textH = bimpy.get_text_line_height_with_spacing()
name = ""
terminal = Terminal(0, 0, W, H, ["Enter your name"])
debugger = Debugger()
while not ctx.should_close():
	with ctx:
		debugger.draw()
		prompt = terminal.draw()
		if prompt:
			if not name:
				if prompt:
					name = prompt
					rq.loadPlayer(name)
			else:
				if prompt == "exit":
#				rq.savestate('rooms.json')
					break
				elif prompt:
					rq.parseMessage(name,prompt)
			rq.printState(name)
			terminal.append(*rq.getMessages(name))
