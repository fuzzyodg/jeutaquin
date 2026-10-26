CC = gcc
CFLAGS = -Wall -Wextra -std=c99
BIN_DIR = bin

TARGETS = mon_ls mon_mkdir mon_cd mon_manuel

.PHONY: all install clean

all: $(TARGETS)

mon_ls: ls.c
	$(CC) $(CFLAGS) -o $@ $<

mon_mkdir: mkdir.c
	$(CC) $(CFLAGS) -o $@ $<

mon_cd: cd.c
	$(CC) $(CFLAGS) -o $@ $<

mon_manuel: manuel.c
	$(CC) $(CFLAGS) -o $@ $<

install: all
	@mkdir -p $(BIN_DIR)
	@cp $(TARGETS) $(BIN_DIR)/
	@echo 'export PATH="'$$(pwd)'/bin:$$PATH"' > activer.sh
	@echo 'mon_cd() {' >> activer.sh
	@echo '    if [ "$$1" = "-" ]; then' >> activer.sh
	@echo '        local target_dir' >> activer.sh
	@echo '        target_dir=$$("'$$(pwd)'/bin/mon_cd" "-")' >> activer.sh
	@echo '        if [ $$? -eq 0 ] && [ -n "$$target_dir" ]; then' >> activer.sh
	@echo '            export OLDPWD="$$PWD"' >> activer.sh
	@echo '            builtin cd "$$target_dir"' >> activer.sh
	@echo '        fi' >> activer.sh
	@echo '    else' >> activer.sh
	@echo '        local target_dir' >> activer.sh
	@echo '        target_dir=$$("'$$(pwd)'/bin/mon_cd" "$$@")' >> activer.sh
	@echo '        if [ $$? -eq 0 ] && [ -n "$$target_dir" ]; then' >> activer.sh
	@echo '            export OLDPWD="$$PWD"' >> activer.sh
	@echo '            builtin cd "$$target_dir"' >> activer.sh
	@echo '        fi' >> activer.sh
	@echo '    fi' >> activer.sh
	@echo '}' >> activer.sh
	@echo 'echo "=== Émulateur activé ! Commandes globales prêtes (mon_ls, mon_mkdir, mon_cd, mon_manuel). ==="' >> activer.sh
	@chmod +x activer.sh
	@echo "Installation terminée. Pour activer l'environnement, exécutez :"
	@echo "source activer.sh"

clean:
	rm -f $(TARGETS)
	rm -rf $(BIN_DIR)
	rm -f activer.sh
