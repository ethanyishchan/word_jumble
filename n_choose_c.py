# return permute it
# slice off accordingly

# n choose c
#




def n_choose_c(s, c):


	def n_choose_c_help(s, n, i, c, memo = {}, output = ''):
		'''
		s - given a string s
		n - given the length of s
		i - index of current char
		c - given number of characters we want to select
		'''
		output += s[i]
		#add this char in, or skip to the next char
		n_choose_c_help (s, n, i+1, c, memo, output)



		return 0

	n = len(s)

	for x in range(0, c):
		n_choose_c_help(s, n , c)











