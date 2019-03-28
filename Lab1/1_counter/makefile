CC = g++
CFLAGS = -std=c++11
SYSTEMC_HOME = /opt/systemc
SC_COMPILE = -I$(SYSTEMC_HOME)/include
SC_LINK = -lsystemc -L$(SYSTEMC_HOME)/lib-linux64

OBJECTS = main.o Counter.o Display.o TestDriver.o
EXECUTABLE = ex1

all: $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)
	$(CC) $(OBJECTS) -o $(EXECUTABLE) $(SC_LINK)

Counter.o: Counter.h Counter.cpp
	$(CC) $(CFLAGS) -c Counter.cpp $(SC_COMPILE)

Display.o: Display.h Display.cpp
	$(CC) $(CFLAGS) -c Display.cpp $(SC_COMPILE)

TestDriver.o: TestDriver.h TestDriver.cpp
	$(CC) $(CFLAGS) -c TestDriver.cpp $(SC_COMPILE)

main.o: Counter.o Display.o TestDriver.o main.cpp
	$(CC) $(CFLAGS) -c main.cpp $(SC_COMPILE)

clean:
	rm -f *.o $(EXECUTABLE)