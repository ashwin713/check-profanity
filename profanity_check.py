import urllib

def read_txt():
	input_txt = open("input.txt")
	contents_txt = input_txt.read()
	input_txt.close()
	check_for_profanity(contents_txt)


def check_for_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
	output_txt = connection.read()
	if output_txt == "true":
		print "You are using curse words, please edit your text."
	else:
		print "Your text is clean."
	connection.close()

read_txt()