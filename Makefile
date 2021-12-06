format:
	python -m black ./

create:
	aoc -d $(d) -f $(y)/inputs/day$(d).txt -y $(y) download
	python template.py $(y) $(d)

submit:
	aoc -d $(d) -y $(y) submit $(p) $(r)

read:
	aoc -d $(d) -y $(y) read
