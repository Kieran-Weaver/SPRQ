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
		self.etype = ""
		self.combo_text = ""

	def add_menuentry(self, condition, text, etype):
		self.menuEntries[text] = {"condition" : condition, "type" : etype, "entries" : {}}
		self.currentMenuItem = text
	
	def set_menuentry(self, text):
		self.currentMenuItem = text

	def set_attr(self, entry, attr, value):
		self.menuEntries.get(entry, {})[attr] = value

	def add_entry(self, text, etype, callback, defValue=""):
		self.menuEntries[self.currentMenuItem]["entries"][text] = {
			"value" : bimpy.String(),
			"type" : etype,
			"checked" : bimpy.Bool(),
			"callback" : callback
		}
		self.menuEntries[self.currentMenuItem]["entries"][text]["value"].value = str(defValue)

	def draw(self):
		startWindow("Debugger", W, 0, 1080-W, H, bimpy.WindowFlags.MenuBar)
		bimpy.text("Debugger")
		assert(bimpy.begin_menu_bar())
		for menuitem in self.menuEntries:
			if self.menuEntries[menuitem]["condition"]:
				if bimpy.menu_item(menuitem, ""):
					self.entries = self.menuEntries[menuitem]["entries"].copy()
					self.etype = self.menuEntries[menuitem]["type"]
					if self.etype == "combo" and not self.combo_text:
						self.combo_text = [*self.entries.keys()][0]
		bimpy.end_menu_bar()

		if self.entries:
			shouldend = False
			if self.etype == "combo" and bimpy.begin_combo("##Combo", self.combo_text):
				shouldend = True
			for entry in self.entries:
				if self.etype == "combo":
					is_selected = bimpy.Bool()
					if bimpy.selectable(f"{entry}##_combo", selected=is_selected):
						self.entries[entry]["callback"](entry, self.entries)
					elif is_selected.value:
						self.combo_text = entry
						print(self.combo_text)
				elif self.entries[entry]["type"] == "button":
					if bimpy.button(f"{entry}##_button") and self.entries[entry]["callback"]:
						self.entries[entry]["callback"](entry, self.entries)
				elif self.entries[entry]["type"] == "text":
					bimpy.text_wrapped(f"{entry}")
				else:
					bimpy.input_text(f"{entry}##_input", self.entries[entry]["value"], 256)
					if self.entries[entry]["callback"]:
						if self.entries[entry]["type"] == "checkbox":
							bimpy.same_line()
							if bimpy.checkbox(f"##{entry}_checkbox", self.entries[entry]["checked"]):
								self.entries[entry]["callback"](entry, self.entries)
			if shouldend:
				bimpy.end_combo()

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

def lockField(field, entries):
	global locked_fields, fields
	value = entries[field]["value"].value
	checkValue = entries[field]["checked"].value
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

debugger.add_menuentry(True, "Lock Fields", "default")
for field in fields:
	debugger.add_entry(field, "checkbox", lockField)

def saveItem(field, entries):
	item = ''
	for val in entries:
		if entries[val]["type"] == "text":
			item = val
	fields = [val for val in entries if entries[val]["type"] == "default"]
	itemData = rq.savedData["items"][item]
	for field in fields:
		itemData[field] = ast.literal_eval(entries[field]["value"].value)

def editItem(item, entries):
	itemData = rq.savedData["items"][item]
	debugger.add_menuentry(True, "Edit Item", "default")
	debugger.add_entry(item, "text", None)
	for key in itemData:
		debugger.add_entry(key, "default", None, repr(itemData[key]))
	debugger.add_entry("Save", "button", saveItem)

debugger.add_menuentry(True, "Edit Item Data", "combo")
for item in rq.savedData["items"]:
	debugger.add_entry(item, "combo", editItem)
debugger.add_menuentry(True, "Edit Room", "default")
debugger.add_menuentry(False, "Edit Item", "default")
debugger.add_menuentry(False, "Edit NPC", "default")

while not ctx.should_close():
	if name:
		for field in locked_fields:
			setattr(rq.players[name], field, copy.deepcopy(locked_fields[field]))
	with ctx:
		debugger.draw()
		prompt = terminal.draw()
		if prompt:
			if not name:
				name = prompt
				rq.loadPlayer(name)
				debugger.set_menuentry("Lock Fields")
				for field in fields:
					debugger.add_entry(field, "checkbox", lockField, repr(getattr(rq.players[name], field)))
			else:
				if prompt == "exit":
#				rq.savestate('rooms.json')
					break
				else:
					rq.parseMessage(name,prompt)
			rq.printState(name)
			terminal.append(*rq.getMessages(name))
