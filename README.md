index-duplicates-python
=======================

Benchmark of algorithms to find indexes of duplicate items.

The problem
-----------------------
The question raised here: http://stackoverflow.com/questions/5419204/index-of-duplicates-items-in-a-python-list

Having a dict with items search for a duplicates and return the dict containing indexes of duplicates.

Example: List = ['A', 'B', 'A', 'C', 'E']
Return: {A: [0, 2]}

Benchmarking
-----------------------
To do a benchmark, download both testdupl.py and timetestdupl.py and run `python timetestdupl.py`
The algorithms in testdupl.py are the ones mentioned in [the question on the Stackoverflow](http://stackoverflow.com/questions/5419204/index-of-duplicates-items-in-a-python-list)

You can change various commandline options. Check the comment in the beginning of the script