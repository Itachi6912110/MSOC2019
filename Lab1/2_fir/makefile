CC = g++
CFLAGS = -std=c++11 -O3
SYSTEMC_HOME = /opt/systemc
SC_COMPILE = -I. -I$(SYSTEMC_HOME)/include
SC_LINK = -L. -L$(SYSTEMC_HOME)/lib-linux64 -Wl,-rpath=$(SYSTEMC_HOME)/lib-linux64/ -lsystemc -lm

OBJECTS = main.o FIR.o
EXECUTABLE = ex2

all: $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)
	$(CC) $(OBJECTS) -o $(EXECUTABLE) $(SC_LINK)

FIR.o: FIR.h FIR.cpp
	$(CC) $(CFLAGS) -c FIR.cpp $(SC_COMPILE)

main.o: FIR.o main.cpp
	$(CC) $(CFLAGS) -c main.cpp $(SC_COMPILE)

clean:
	rm -f *.o $(EXECUTABLE)