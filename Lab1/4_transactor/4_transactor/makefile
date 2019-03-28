CC = g++
CFLAGS = -std=c++11 -O3
SYSTEMC_HOME = /opt/systemc
SC_COMPILE = -I. -I$(SYSTEMC_HOME)/include
SC_LINK = -L. -L$(SYSTEMC_HOME)/lib-linux64 -Wl,-rpath=$(SYSTEMC_HOME)/lib-linux64/ -lsystemc -lm

OBJECTS = main.o Interchange.o Memory.o Transactor.o
EXECUTABLE = ex4

all: $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)
	$(CC) $(OBJECTS) -o $(EXECUTABLE) $(SC_LINK)

Interchange.o: Interchange.h Interchange.cpp Mem_if.h
	$(CC) $(CFLAGS) -c Interchange.cpp $(SC_COMPILE)

Memory.o: Memory.h Memory.cpp Mem_if.h
	$(CC) $(CFLAGS) -c Memory.cpp $(SC_COMPILE)

Transactor.o: Transactor.h Transactor.cpp Mem_if.h
	$(CC) $(CFLAGS) -c Transactor.cpp $(SC_COMPILE)

main.o: Interchange.o Memory.o Transactor.o main.cpp
	$(CC) $(CFLAGS) -c main.cpp $(SC_COMPILE)

clean:
	rm -f *.o $(EXECUTABLE)