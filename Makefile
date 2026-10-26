CC = gcc
CFLAGS = -Wall -Wextra -std=c99
BIN = bin

PROGS = mon_ls mon_mkdir mon_cd

.PHONY: all install clean

all: $(PROGS)

mon_ls: ls.c
	$(CC) $(CFLAGS) -o $@ $<

mon_mkdir: mkdir.c
	$(CC) $(CFLAGS) -o $@ $<

mon_cd: cd.c
	$(CC) $(CFLAGS) -o $@ $<


install: all
	@mkdir -p $(BIN)
	@cp $(PROGS) $(BIN)/
	@echo 'export PATH="'$$(pwd)'/bin:$$PATH"' > activer.sh
	@echo 'mon_cd() {' >> activer.sh
	@echo '    if [ "$$1" = "-" ]; then' >> activer.sh
	@echo '        local dir' >> activer.sh
	@echo '        dir=$$("'$$(pwd)'/bin/mon_cd" "-")' >> activer.sh
	@echo '        if [ $$? -eq 0 ] && [ -n "$$dir" ]; then' >> activer.sh
	@echo '            export OLDPWD="$$PWD"' >> activer.sh
	@echo '            builtin cd "$$dir"' >> activer.sh
	@echo '        fi' >> activer.sh
	@echo '    else' >> activer.sh
	@echo '        local dir' >> activer.sh
	@echo '        dir=$$("'$$(pwd)'/bin/mon_cd" "$$@")' >> activer.sh
	@echo '        if [ $$? -eq 0 ] && [ -n "$$dir" ]; then' >> activer.sh
	@echo '            export OLDPWD="$$PWD"' >> activer.sh
	@echo '            builtin cd "$$dir"' >> activer.sh
	@echo '        fi' >> activer.sh
	@echo '    fi' >> activer.sh
	@echo '}' >> activer.sh
	@echo 'echo "=== Émulateur activé ! Commandes globales prêtes (mon_ls, mon_mkdir, mon_cd). ==="' >> activer.sh
	@chmod +x activer.sh
	@echo "Installation terminée. Tapez 'source activer.sh' pour activer les commandes."

clean:
	rm -f $(PROGS)
	rm -rf $(BIN)
	rm -f activer.sh