'''
create a trie, if we want to be more efficient, we can create a DAWG instead. Directed Acyclic Word Graph.
'''
import time

class trie:
	def __init__(self, root):
		self.rootnode = root

class node:
	def __init__(self, c):
		self.letter = c
		self.memo = {}
		self.terminal = False

	def input_word(self, s, index = 0):
			if index == len(s):
				return
			#if it already exists in the trie
			if s[index] in self.memo:
				self.memo[s[index]].input_word(s, index+1)
			#else add it to a chain
			else:
				self.memo[s[index]] = node(s[index])
				#if this is the last letter of a word, mark it as a terminal point
				if index == len(s)-1:
					print s[index]
					self.terminal = True
				self.memo[s[index]].input_word(s, index+1)

	def print_node(self):
		if len(self.memo) == 0:
			return
		else:
			print self.letter
			print self.memo
			for e in self.memo:
				self.memo[e].print_node()	

def create_trie(word_list, eng_trie):
	for word in word_list:
		print word
		eng_trie.rootnode.input_word(word)

def delete_char(word, char):
	word_list = list(word)
	index = word_list.index(char)
	del(word_list[index])
	output = ''.join(word_list)
	return output

def jumble(s, trie_root, output_memo= set()):

	def jumblebee(word, curr_node, output_memo, path = ''):
		for letter in word:
			#if letter exists in memo of node
			if letter in curr_node.memo:
				newpath = path + letter
				if curr_node.memo[letter].terminal == True:
					output_memo.add(newpath)
				#double check this removing indice, and the bottom return value
				truncated_word = delete_char(word, letter)
				if len(truncated_word) == 0:
					return
				jumblebee(truncated_word, curr_node.memo[letter], output_memo, newpath)
			else:
				return
		return

	#input becoes a list of sorted letters, O(N Lg N)
	s = sorted(s)
	jumblebee (s, trie_root, output_memo)
	return output_memo



#initialize the trie
word_list = open('englishwordlist.txt', 'r')
eng_trie = trie(node('rootnode'))
create_trie(word_list,eng_trie)

#take note that most of the time is to create the trie in the cache. Cheers!
#start time clock	
input_word = "cathy"			
start = time.clock()
print "Output Here: ", jumble (input_word, eng_trie.rootnode)

#end time clock
print time.clock() - start