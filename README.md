# Simple password generator

After a long conversation at work, people mentioned the new
dice password list created by EFF. So since I am without dice
right now, I made this small script that pulls the list and
generates random numbers as dice rolls.

## Getting it working
Tested with Python 3.6.3

Random.org requires an API key to call their API for truely random number
generation, get one from there website and create a text file with the key
at config/api.key.

Install the dependent python modules:
	Requests

This can also be done with the command:
	pip -r requirements.txt

Then just run the script!

	python password_gen.py

