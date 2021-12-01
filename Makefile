format:
	python -m black 2021/

run:
	python $(year)/day$(day)/main.py

create:
	mkdir $(year)/day$(day)
	touch $(year)/day$(day)/input.txt
	printf "with open('$(year)/day$(day)/input.txt') as f:\nDATA = [int(x) for x in f.readlines()]\n\ndef part_one():\n    return -1\n\ndef part_two():\n    return -1\n" >> $(year)/day$(day)/main.py
