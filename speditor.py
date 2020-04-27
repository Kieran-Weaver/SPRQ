import bimpy
import rqstate
import os
import ast
import copy
import collections
def startWindow(name, x, y, w, h, extraFlags = 0):
	bimpy.set_next_window_pos(bimpy.Vec2(x,y), int(bimpy.Condition.Once))
	bimpy.set_next_window_size(bimpy.Vec2(w, h), int(bimpy.Condition.Once))
	bimpy.begin(name, flags=bimpy.WindowFlags.NoTitleBar|bimpy.WindowFlags.NoResize|bimpy.WindowFlags.NoMove|extraFlags)

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
		while bimpy.calc_text_size(self._text, wrap_width=(W-20)).y > (H - 120):
			self.content.pop(0)
			self._text = os.linesep.join(self.content)
	
	def append(self, *args):
		if args[0]:
			self.content += [*args]

class Debugger:
	def __init__(self):
		self.menuEntries = collections.OrderedDict()
		self.currentMenuItem = ""
		self.entries = {}
	def add_menuentry(self, text):
		self.menuEntries[text] = {}
		self.currentMenuItem = text
	def add_entry(self, text, etype, callback):
		self.menuEntries[self.currentMenuItem][text] = {
			"value" : bimpy.String(),
			"type" : etype,
			"checked" : bimpy.Bool(),
			"callback" : callback
		}
	def draw(self):
		startWindow("Debugger", W, 0, 1080-W, H, bimpy.WindowFlags.MenuBar)
		bimpy.text("Debugger")
		assert(bimpy.begin_menu_bar())
		for menuitem in self.menuEntries:
			if bimpy.menu_item(menuitem, ""):
				self.entries = self.menuEntries[menuitem]
		bimpy.end_menu_bar()

		for entry in self.entries:
			bimpy.input_text(entry, self.entries[entry]["value"], 256)
			bimpy.same_line()
			if self.entries[entry]["type"] == "checkbox":
				if bimpy.checkbox(f"##{entry}_checkbox", self.entries[entry]["checked"]):
					self.entries[entry]["callback"](entry, self.entries[entry]["checked"].value, self.entries[entry]["value"].value)

W = 640
H = 480
rq = rqstate.RQState("rooms.json")
locked_fields = {}
fields = {
	"hp": int,
	"sp": int,
	"defMul": float,
	"maxSP": int,
	"maxHP": int,
	"itemCapacity": int,
	"atk": int,
	"xp": int,
	"level": int,
	"levelpoints": int,
	"money": int,
	"location": str,
	"state": str,
	"items": dict,
	"powerups": set
}

ctx = bimpy.Context()
ctx.init(1080, 480, "SPRQ Editor")
textH = bimpy.get_text_line_height_with_spacing()
name = ""
terminal = Terminal(0, 0, W, H, ["Enter your name"])
debugger = Debugger()

def lockField(field, checkValue, value):
	global locked_fields, fields
	if checkValue:
		if value:
			newValue = ast.literal_eval(value)
		else:
			newValue = fields[field]()
		if type(newValue) == fields[field]:
			locked_fields[field] = newValue
		else:
			terminal.append(f"Error: The type of {field} must be {fields[field]}") 
	elif field in locked_fields:
		del locked_fields[field]

debugger.add_menuentry("Lock Fields")
for field in fields:
	debugger.add_entry(field, "checkbox", lockField)

while not ctx.should_close():
	if name:
		for field in locked_fields:
			setattr(rq.players[name], field, copy.deepcopy(locked_fields[field]))
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
