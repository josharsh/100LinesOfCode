CC = g++
CFLAGS = -g -Wall -std=c++2a
TARGET = compute
INCLUDES = -Iinclude/


.PHONY: 
	echo "Do nothing" 

all: build/$(TARGET)
build/$(TARGET): src/$(TARGET).cpp
	echo "Compiling....\n"
	mkdir -p build
	$(CC) $(CFLAGS) -o build/$(TARGET) $(INCLUDES) src/$(TARGET).cpp

clean: 
	rm -rf build/

