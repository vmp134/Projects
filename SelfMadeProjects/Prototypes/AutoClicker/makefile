CC     = gcc
CFLAGS = -Wall -Wextra -g
TARGET = AutoClick

.PHONY: all clean

all: $(TARGET)

$(TARGET): AutoClick.c AutoClick.h
	$(CC) $(CFLAGS) -o $@ AutoClick.c

clean: 
	rm -f $(TARGET)