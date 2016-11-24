import json
import pdb

"""Returns a map with a list of character objects in map['characters'] 
	and the max character's Primary Key in map['max_pk']"""
def get_characters(session):
	players_chars = None
	if 'username' not in session.keys():
		return None #TODO: raise not_logged_in_Exception
	uname = session['username']
	filepath = "users/%s/charfile.json" % uname #TODO: encrypt this
	with open(filepath, 'r') as charfile:
		play_string = charfile.read()
		json_blob = json.loads(play_string)
		parsed_list = []
		for charstring in json_blob['characters']:
			new_character = from_string(charstring)
			parsed_list.append(new_character)
		json_blob['characters'] = parsed_list
		players_chars = json_blob
	return players_chars

class Character:
	
	def __init__(self):
		self.pk = 0
		self.name = "Sam Vaughn"
		self.level = 1
		self.money = 0
		self.mission = "Mercenaries"
		self.my_class = "Preist"
		self.race = "Human"
		self.weapons = []
		self.armor = []
		self.items = []
		self.feats = []
		self.skills = {}
	
	def __str__(self):
		returnMe = "%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s" % (self.name,self.level,self.money,self.mission,self.my_class,self.race,str(self.weapons),str(self.armor),str(self.items),str(self.feats),str(self.skills))
		
		return returnMe
	
	def __cmp__(self,other):
		if self.level != other.level:
			return self.level - other.level
		elif self.name > other.name:
			return 1
		elif self.name < other.name:
			return -1
		else:
			return 0
	
def from_string(a_string):
	if a_string.count('|') != 10:
		raise ValueError("Not a valid character string, wrong number of pipe characters.")
	bits = a_string.split('|')
	newbie = Character()
	newbie.name = bits[0]
	newbie.level = int(bits[1])
	newbie.money = int(bits[2])
	newbie.race = bits[3]
	newbie.my_class = bits[4]
	newbie.race = bits[5]
	newbie.weapons = parse_list(bits[6])
	newbie.armor = parse_list(bits[7])
	newbie.items = parse_list(bits[8])
	newbie.feats = parse_list(bits[9])
	newbie.skills = {}
	return newbie
	
def parse_list(list_string):
	if list_string == '[]':
		return []
	items = list_string[1:-1].split(',')
	final = []
	for item in items:
		f_item = item.strip()
		if f_item[0] == f_item[-1:]:
			f_item = f_item[1:-1]
		final.append(f_item)
	return final