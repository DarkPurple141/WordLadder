#!/usr/local/bin/python3.5

import os, sys, queue, cgitb, cgi

queue = queue.Queue()
seen = set()
parent = {}

def find_neighbours(curr, alphabet, words, word_length):
	# iterate through word
	for indx, char in enumerate(curr):
		for c in alphabet:
			copy = list(curr)
			copy[indx] = c
			copy = "".join(copy)
			if (copy in words) and (copy not in seen):
				parent[copy] = curr
				queue.put(copy)
				seen.add(copy)

def prog (word1,word2):

	# intialise the dictionary
	result = ""
	words = {}
	start = word1.strip()
	start = start.lower()
	end = word2.strip()
	end = end.lower()
	word_length = len(start)
	alphabet = 'abcdefghijklmnopqrstuvwxyz'

	with open ("lcwords_new", 'r') as fo:
		# read words into dict, strip \n
		for line in fo:
			word = line.rstrip('\n')
			if len(word) == word_length and word not in words:
				words[word] = 1
			else:
				continue

	# initialise queue and set
	queue.put(start)
	curr = start
	seen.add(start)

	while (curr != end) and not queue.empty():
		curr = queue.get()
		find_neighbours(curr,alphabet,words,word_length)

	if curr == end:
		counter = 0;
		result += """<table id="answer"><th style="width:30%;"">Origin</th><th style="width:20px; margin-right:40px"></th><th style="padding-left:50px;">Alter</th>"""
		curr = end
		while curr is not start:
			counter+=1
			result += """<tr>"""
			result += """<td>%s</td><td><i style="font-size:30px;" class="glyphicon glyphicon-arrow-right"></i></td>""" % (curr)
			curr = parent[curr]
			result += """<td style="padding-left:50px;">%s</td></tr>\n""" % (curr)
		result += """</table>"""
		result = """<p>A word-ladder is possible with %d moves. 
		<a onclick="clickfunction('answer')">Click here</a> to reveal the answer.</p>%s""" % (counter, result)
	else:
		result = "No word-ladder found!"

	return result

def main ():
	cgitb.enable()
	parameters = cgi.FieldStorage()
	print_header()
	#error = parameters.getvalue('error') or check_valid(parameters) or 0
	word1 = parameters.getvalue('word1') or 0
	word2 = parameters.getvalue('word2') or 0

	if word1 and word2:
		result = prog(word1,word2)
		page_authenticate(result)
	else:
		print(form())

def form ():
	return """
    <div class="container">
      <form action="" method="post">
      
        <h1>Word Ladder</h1>
        
        <fieldset>
          <legend>Given any two words of the same length we can sometimes find what's known as a 'word ladder'...</legend>
          <p>Word ladders (also known as doublets, word-links, change-the-word puzzles, paragrams, laddergrams,
           or Word golf) are a sequence of words linked by similar word 'rungs'.</p>
		<p>Each rung can only differ to its parent by a single character. Eg. Bar->Bat->Cat is a legal three-rung ladder. 
		It must also be a real English word. There's no limit to the amount of rungs you can make use of as long as each rung is legal. The game was first invented by Lewis Carroll.</p>
		  <p><em>Note by definition words must be of the same length!</em></p>
		  <p>Type two words below and we'll determine if a word ladder exists.</p>
          <label for="name">Word:</label>
          <input type="text" id="word1" name="word1" placeholder="enter a word..">
 
          <label for="word2">Word:</label>
          <input type="text" id="word2" name="word2" placeholder="enter another word..">
          <br><br>
        </fieldset>
        <legend></legend>
        <button type="submit" onclick="return value_check();">Submit</button>
      </form>
      </div>
    </body>
</html>

"""

def page_authenticate (result):
	string = """
	<div class="container">
	<h1>Word Ladder</h1>
	<legend>The result was..</legend>
	<p>%s</p>
	<form action="" method="post">
		<button type="submit">Reset</button>
	</form>
	</div>

	""" % (result)
	print (string)

def print_header ():
	string = """Content-Type: text/html;charset=utf-8

<!DOCTYPE html>
<html lang=\"en\">
	<head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Word Ladder</title>
        <link href='http://fonts.googleapis.com/css?family=Nunito:400,300' rel='stylesheet' type='text/css'>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <link rel="stylesheet" href="css/style.css">
        <script type='text/javascript' src="scripts/myjs.js"></script>
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
	</head>
<body>
	"""
	print(string)

if __name__ == '__main__':
	main()



