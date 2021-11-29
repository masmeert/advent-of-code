run:
	python $(year)/day$(day)/main.py

create:
	mkdir $(year)/day$(day)
	touch $(year)/day$(day)/input.txt
	printf "data = [int(x) for x in open('$(year)/day$(day)/input.txt').readlines()]\n\ndef part_one():\n    return -1\n\ndef part_two():\n    return -1\n" >> $(year)/day$(day)/main.py
