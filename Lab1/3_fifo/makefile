CC = g++
CFLAGS = -std=c++11 -O3
SYSTEMC_HOME = /opt/systemc
SC_COMPILE = -I. -I$(SYSTEMC_HOME)/include
SC_LINK = -L. -L$(SYSTEMC_HOME)/lib-linux64 -Wl,-rpath=$(SYSTEMC_HOME)/lib-linux64/ -lsystemc -lm

OBJECTS = main.o Consumer.o Fifo.o Producer.o
EXECUTABLE = ex3

all: $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)
	$(CC) $(OBJECTS) -o $(EXECUTABLE) $(SC_LINK)

Consumer.o: Interface.h Consumer.h Consumer.cpp
	$(CC) $(CFLAGS) -c Consumer.cpp $(SC_COMPILE)

Fifo.o: Interface.h Fifo.h Fifo.cpp
	$(CC) $(CFLAGS) -c Fifo.cpp $(SC_COMPILE)

Producer.o: Interface.h Producer.h Producer.cpp
	$(CC) $(CFLAGS) -c Producer.cpp $(SC_COMPILE)

main.o: Consumer.o Fifo.o Producer.o main.cpp
	$(CC) $(CFLAGS) -c main.cpp $(SC_COMPILE)

clean:
	rm -f *.o $(EXECUTABLE)