TEMPLATE = "with open('$(year)/inputs/day$(day)') as f:\n    DATA = [int(x) for x in f.readlines()]\n\ndef part_one():\n    return -1\n\ndef part_two():\n    return -1\n\nprint(part_one())\nprint(part_two())\n"

format:
	python -m black $(year)/

run:
	python $(year)/day$(day).py

create:
	aoc -d $(day) -f $(year)/inputs/day$(day) -y $(year) download
	printf $(TEMPLATE) >> $(year)/day$(day).py

submit:
	aoc -d $(day) -y $(year) submit $(part) $(result)
