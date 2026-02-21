# Email processing

## Setup exercise (What I still remember)

Idea is to generate code that does email parsing and analyses to practice with understanding code and functionalities. The analysis was whether specific key words (in this case "fraud") ocurred in the email. In that case, the sender email address was logged. In the end, both the total number of occurences was printed, and each sender was printed on a separate line.

From previous interview had a few files:
* app.py 
* configation file
* parser.py
* helper.py
* ... ?

## Finding the mistake in the code (what I still remember)

Part of the exercise was to look at the output, and interpret what went wrong. In this case: Email addresses where printed multiple times because the analysis was done on line level in the email. This had the implication that when the word "fraud" occurred multiple times in the email, the sender was printed for multiple times. This was due to some for loop where the logging on the sender's email address was done within the for loop on each line instead of on message level.