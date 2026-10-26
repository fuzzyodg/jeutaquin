CC = gcc
CFLAGS = -Wall -Wextra -std=c99
BIN_DIR = bin

TARGETS = ls mkdir cd manuel

.PHONY: all install clean

all: $(TARGETS)

ls: ls.c
	$(CC) $(CFLAGS) -o $@ $<

mkdir: mkdir.c
	$(CC) $(CFLAGS) -o $@ $<

cd: cd.c
	$(CC) $(CFLAGS) -o $@ $<

manuel: manuel.c
	$(CC) $(CFLAGS) -o $@ $<

install: all
	@mkdir -p $(BIN_DIR)
	@cp $(TARGETS) $(BIN_DIR)/
	@echo 'export PATH="'$$(pwd)'/bin:$$PATH"' > activer.sh
	@echo 'cd() {' >> activer.sh
	@echo '    if [ "$$1" = "-" ]; then' >> activer.sh
	@echo '        local target_dir' >> activer.sh
	@echo '        target_dir=$$("'$$(pwd)'/bin/cd" "-")' >> activer.sh
	@echo '        if [ $$? -eq 0 ] && [ -n "$$target_dir" ]; then' >> activer.sh
	@echo '            export OLDPWD="$$PWD"' >> activer.sh
	@echo '            builtin cd "$$target_dir"' >> activer.sh
	@echo '        fi' >> activer.sh
	@echo '    else' >> activer.sh
	@echo '        local target_dir' >> activer.sh
	@echo '        target_dir=$$("'$$(pwd)'/bin/cd" "$$@")' >> activer.sh
	@echo '        if [ $$? -eq 0 ] && [ -n "$$target_dir" ]; then' >> activer.sh
	@echo '            export OLDPWD="$$PWD"' >> activer.sh
	@echo '            builtin cd "$$target_dir"' >> activer.sh
	@echo '        fi' >> activer.sh
	@echo '    fi' >> activer.sh
	@echo '}' >> activer.sh
	@echo 'echo "=== Émulateur activé ! Commandes globales prêtes (ls, mkdir, cd, manuel). ==="' >> activer.sh
	@chmod +x activer.sh
	@echo "Installation terminée. Pour activer l'environnement, exécutez :"
	@echo "source activer.sh"

clean:
	rm -f $(TARGETS)
	rm -rf $(BIN_DIR)
	rm -f activer.sh
