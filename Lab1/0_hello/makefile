CC = g++
CFLAGS = --std=c++11 -O3
SYSTEMC_HOME = /opt/systemc
SC_COMPILE = -I. -I$(SYSTEMC_HOME)/include
SC_LINK = -L. -L$(SYSTEMC_HOME)/lib-linux64 -Wl,-rpath=$(SYSTEMC_HOME)/lib-linux64/ -lsystemc -lm

OBJECTS = main.o Hello_SystemC.o
EXECUTABLE = ex0

all: $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)
	$(CC) $(OBJECTS) -o $(EXECUTABLE) $(SC_LINK)

Hello_SystemC.o: Hello_SystemC.h Hello_SystemC.cpp
	$(CC) $(CFLAGS) -c Hello_SystemC.cpp $(SC_COMPILE)

main.o: Hello_SystemC.o main.cpp
	$(CC) $(CFLAGS) -c main.cpp $(SC_COMPILE)

clean:
	rm -f *.o $(EXECUTABLE)