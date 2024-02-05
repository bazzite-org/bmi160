obj-m += bmi160_core.o
obj-m += bmi160_i2c.o
obj-m += bmi160_spi.o

KERNEL_SRC ?= /lib/modules/$(shell uname -r)/build

all default: modules
install: modules_install

modules modules_install help clean:
	$(MAKE) -C $(KERNEL_SRC) M=$(shell pwd) $@
