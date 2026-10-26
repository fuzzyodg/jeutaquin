CC = gcc
CFLAGS = -Wall -Wextra -std=c99
BIN = bin

PROGS = mon_ls mon_mkdir mon_cd

.PHONY: all install shell clean

.DEFAULT_GOAL := shell

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
	@echo '#!/usr/bin/env bash' > activer.sh
	@echo 'if [ -z "$$_EMULATEUR_ACTIVATED" ]; then' >> activer.sh
	@echo '    export _EMULATEUR_ACTIVATED=1' >> activer.sh
	@echo '    if [ -f "$$HOME/.bashrc" ]; then' >> activer.sh
	@echo '        . "$$HOME/.bashrc"' >> activer.sh
	@echo '    fi' >> activer.sh
	@echo 'fi' >> activer.sh
	@echo 'DIR="$$( cd -- "$$( dirname -- "$${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"' >> activer.sh
	@echo 'export PATH="$$DIR/bin:$$PATH"' >> activer.sh
	@echo 'mon_cd() {' >> activer.sh
	@echo '    local dir' >> activer.sh
	@echo '    dir="$$("$$DIR/bin/mon_cd" "$$@")"' >> activer.sh
	@echo '    if [ $$? -eq 0 ] && [ -n "$$dir" ]; then' >> activer.sh
	@echo '        export OLDPWD="$$PWD"' >> activer.sh
	@echo '        builtin cd "$$dir"' >> activer.sh
	@echo '    fi' >> activer.sh
	@echo '}' >> activer.sh
	@echo 'export PS1="(emulateur) $$PS1"' >> activer.sh
	@echo 'echo "=== Émulateur activé dans un shell temporaire ! ==="' >> activer.sh
	@echo 'echo "Commandes disponibles : mon_ls, mon_mkdir, mon_cd"' >> activer.sh
	@echo 'echo "Tapez '\''exit'\'' pour quitter l'\''émulateur."' >> activer.sh
	@chmod +x activer.sh

shell: install
	@bash --rcfile activer.sh -i

clean:
	rm -f $(PROGS)
	rm -rf $(BIN)
	rm -f activer.sh
