include settings.mk

BASEDIR=$(PWD)
OUTPUTDIR=$(BASEDIR)/output

minimal:
	yasb --ignore static --ignore theme --ignore pyscss --silent

minimal-verbose:
	yasb --ignore static --ignore theme --ignore pyscss

autobuild:
	yasb-monitor --ignore static --ignore theme --ignore pyscss --silent

help:
	@echo '                                '
	@echo 'Usage:                          '
	@echo '   make minimal                 '
	@echo '   make minimal-verbose         '
	@echo '   make autobuild               '
	@echo '   make full	                   '
	@echo '   make clean                   '
	@echo '   make rsync	               '
	@echo '                                '

full:
	yasb

clean:
	rm -rf $(OUTPUTDIR)
	mkdir $(OUTPUTDIR)

rsync:
	rsync -acvzh --no-perms --no-owner --no-group --exclude '.diff_build_db' --exclude '.lastbuild' --delete -e "ssh -p $(SSH_PORT)" $(OUTPUTDIR)/ $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)

.PHONY: help clean minimal minimal-verbose autobuild full rsync
