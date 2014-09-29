#high level thinking
#find all the subsets of a word
#--> O(2^N)
#for each word in the subset
	#permute it, and check if it is a valid english word
	#O(N!)
#output all of them

#Final runtime O((2^N) * N!)


#pyenchant import
#instructions to download: pip install pyenchant
import enchant

def permute (s, memo = set(), permute_step = 0):
	'''
	this function permutes a word recursively
	'''
	def permute_help(s, memo, permute_step):
		if s in memo or s == " ":
			return
		else:
			#uses pyenchant library to see if it is valid word
			d = enchant.Dict("en_US")
			if d.check(s) and len(s)>1:
				memo.add(s)
			#pyenchant takes every valid alphabet as an english word, this is to fix that.
			elif s == "i" or s == "a":
				memo.add(s)
		for i in xrange(permute_step,len(s)):
			s_copy = [c for c in s]
			s_copy[0],s_copy[i] = s_copy[i],s_copy[0]
			permute_help (''.join(s_copy), memo, permute_step +1)

	permute_help(s,memo, permute_step)		
	return memo

def subset (s, memo = set()):
	'''
	this function uses bit manipulation to find all the possible subsets of a word a.k.a. powerset
	2^n number of subsets, each one can be represented by a binary representation, 
	where the 1's and 0's correspond to whether it belongs in the set or not.
	'''
	no_of_subsets = 2 ** len(s)
	for i in range (0, no_of_subsets):
		formatting_string = "{0:0" + str(len(s)) + "b}"
		binary_rep = formatting_string.format(i)
		string_rep = ""
		for index in range (0, len(binary_rep)):
			if int(binary_rep[index]) == 1:
				string_rep += s[index]
		#only if string has a length > 0
		if len(string_rep):
			memo.add(string_rep)

	return memo

def jumble (s):
	'''
	finds the correct english subwords given a word s
	'''
	subsets = subset(s)
	print subsets
	output_set = set()
	for word in subsets:
		permute (word, output_set, 0)
	return output_set

output = jumble("hippo")
print output


