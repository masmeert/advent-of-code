TEMPLATE = "with open('$(y)/inputs/day$(d)') as f:\n    DATA = [int(x) for x in f.readlines()]\n\ndef part_one():\n    return -1\n\ndef part_two():\n    return -1\n\nprint(part_one())\nprint(part_two())\n"

format:
	python -m black $(y)/

run:
	python $(y)/day$(d).py

create:
	aoc -d $(d) -f $(y)/inputs/day$(d) -y $(y) download
	printf $(TEMPLATE) >> $(y)/day$(d).py

submit:
	aoc -d $(d) -y $(y) submit $(p) $(r)

read:
	aoc -d $(d) -y $(y) read
