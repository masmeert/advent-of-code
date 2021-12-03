format:
	python -m black $(year)/

run:
	python $(year)/day$(day)/main.py

create:
	mkdir $(year)/day$(day)
	touch $(year)/day$(day)/input
	printf "with open('$(year)/day$(day)/input.txt') as f:\n    DATA = [int(x) for x in f.readlines()]\n\ndef part_one():\n    return -1\n\ndef part_two():\n    return -1\n\nprint(part_one())\nprint(part_two())\n" >> $(year)/day$(day)/main.py
