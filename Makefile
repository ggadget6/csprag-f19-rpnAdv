test:
	#python3 -m unittest
	coverage run --omit test_rpn.py -m unittest
.PHONY: test
