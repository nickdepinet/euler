"""
	Project Euler #17:
	If the numbers 1 to 5 are written out in words: one, two, three, four, 
	five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
	If all the numbers from 1 to 1000 (one thousand) inclusive were written 
	out in words, how many letters would be used?
	NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
	contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
	The use of "and" when writing out numbers is in compliance with British usage.
	
	Author: Nick Depinet
"""
a = 'and'
digits = {
	'0': '',
	'1': 'one',
	'2': 'two',
	'3': 'three',
	'4': 'four',
	'5': 'five',
	'6': 'six',
	'7': 'seven',
	'8': 'eight',
	'9': 'nine',
	'10': 'ten',
	'11': 'eleven',
	'12': 'twelve',
	'13': 'thirteen',
	'14': 'fourteen',
	'15': 'fifteen',
	'16': 'sixteen',
	'17': 'seventeen',
	'18': 'eighteen',
	'19': 'nineteen'
	}

tens = {
	'0': '',
	'1': 'ten',
	'2': 'twenty',
	'3': 'thirty',
	'4': 'forty',
	'5': 'fifty',
	'6': 'sixty',
	'7': 'seventy',
	'8': 'eighty',
	'9': 'ninety',
	}
	

big = {
	'4': 'thousand',
	'3': 'hundred',
	}

def wordify(i, outStr = ''):
	if len(i) < 3:
		if i[0] == '0' and len(i) == 2:
			i = i[1:]
		if i in digits:
			outStr = ''.join([outStr, digits[i]])
		else:
			outStr = ''.join([outStr, tens[i[0]], digits[i[1]]])
		return outStr
	elif len(i) == 3:
		if i[0] == '0':
			return wordify(i[1:], outStr)
		outStr = ''.join([outStr, digits[i[0]], big['3']])
		if i[1] == '0' and i[2] == '0':
			return outStr
		else:
			outStr = ''.join([outStr, a])
			return wordify(i[1:], outStr)
	elif len(i) == 4:
		if i[0] == '0':
			return wordify(i[1:], outStr)
		outStr = ''.join([outStr, digits[i[0]], big['4']])
		return wordify(i[1:], outStr)

done = ''
for i in xrange(1,1001):
	done = ''.join([done, wordify(str(i))])
print len(done)
