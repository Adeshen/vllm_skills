PYTHON ?= python3
TARGET ?= build/upstream_skills
MODE ?= symlink

.PHONY: install manifest list

install:
	$(PYTHON) scripts/install_upstream_skills.py --target "$(TARGET)" --mode "$(MODE)"

manifest:
	$(PYTHON) scripts/install_upstream_skills.py --target "$(TARGET)" --mode manifest

list:
	$(PYTHON) scripts/install_upstream_skills.py --list
