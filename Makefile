PREFIX ?= /usr/local

all:
install:
	systemctl disable thermostat --now
	mkdir -p ${DESTDIR}${PREFIX}/bin
	cp thermostat.py ${DESTDIR}${PREFIX}/bin
	cp silverpm.py ${DESTDIR}${PREFIX}/bin
	cp thermostat.service ${DESTDIR}/lib/systemd/system
	systemctl daemon-reload	
	systemctl enable thermostat --now
	
