# Target di default
all:
	gcc main.c src/example.c -o main

build:
	gcc -shared -o local_lib.so -fPIC src/example.c

# Dichiarazione dei target fittizi
.PHONY: all build
