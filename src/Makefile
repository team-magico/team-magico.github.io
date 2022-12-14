# C.A. - Inria - 2022

all: generate

generate:
	cd .. && python src/generate.py

push:
	make generate && cd .. && git add *.html && git commit -m "site update" && git push
