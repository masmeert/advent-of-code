start:
	aoc -d $(d) -f $(y)/inputs/day$(d).txt -y $(y) download
	python template.py $(y) $(d)