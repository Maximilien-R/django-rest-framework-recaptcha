SHELL = /bin/sh

COMPOSE = docker-compose -p rest_framework_recaptcha

.PHONY: check-format
check-format:
	$(COMPOSE) build check-format-imports
	$(COMPOSE) build check-format-imports
	$(COMPOSE) build check-format
	$(COMPOSE) run check-format

.PHONY: format
format:
	$(COMPOSE) build format-imports
	$(COMPOSE) run format-imports
	$(COMPOSE) build format
	$(COMPOSE) run format

.PHONY: style
style: check-format
	$(COMPOSE) build style
	$(COMPOSE) run style

.PHONY: complexity
complexity:
	$(COMPOSE) build complexity
	$(COMPOSE) run complexity

.PHONY: test-unit
test-unit:
	$(COMPOSE) build test-unit
	$(COMPOSE) run test-unit

.PHONY: test
test: test-unit

.PHONY: test-all
test-all:
	$(COMPOSE) build test-all
	$(COMPOSE) run test-all

.PHONY: security-sast
security-sast:
	$(COMPOSE) build security-sast
	$(COMPOSE) run security-sast

.PHONY: security-dependency-scan
security-dependency-scan:
	$(COMPOSE) build security-dependency-scan
	$(COMPOSE) run security-dependency-scan

.PHONY: security
security: security-sast security-dependency-scan

.PHONY: down
down:
	$(COMPOSE) down --volumes --rmi=local

.PHONY: clean-docs
clean-docs:
	@rm -f docs/rest_framework_recaptcha.rst
	@rm -f docs/modules.rst
	@rm -rf docs/_build

.PHONY: docs
docs: clean-docs
	$(COMPOSE) build build-docs
	$(COMPOSE) run build-docs

.PHONY: get-version
get-version:
	@bash -c "cat rest_framework_recaptcha/__init__.py | grep \"__version__ = \" | egrep -o \"([0-9]+\\.[0-9]+\\.[0-9]+)\""

.PHONY: bumpversion
bumpversion:
	$(COMPOSE) build bumpversion-package
	$(COMPOSE) run bumpversion-package

.PHONY: clean-pyc
clean-pyc:
	@find . -name "*.pyc" -exec rm -f {} +
	@find . -name "*.pyo" -exec rm -f {} +
	@find . -name "*~" -exec rm -f {} +
	@find . -name __pycache__ -exec rm -rf {} +

.PHONY: clean-build
clean-build:
	@rm -rf build/
	@rm -rf dist/
	@rm -rf .eggs/
	@find . -name "*.egg-info" -exec rm -fr {} +
	@find . -name "*.egg" -exec rm -f {} +

.PHONY: clean
clean: clean-pyc clean-build

.PHONY: build
build: clean compile-translations
	$(COMPOSE) build build-package
	$(COMPOSE) run build-package

.PHONY: publish-test
publish-test: build
	$(COMPOSE) build publish-test-package
	$(COMPOSE) run publish-test-package

.PHONY: publish
publish: build
	$(COMPOSE) build publish-package
	$(COMPOSE) run publish-package

.PHONY: generate-translations
generate-translations:
ifndef LOCALE
	$(error LOCALE is undefined)
endif
	$(COMPOSE) build generate-translations
	$(COMPOSE) run generate-translations

.PHONY: update-translations
update-translations:
	$(COMPOSE) build update-translations
	$(COMPOSE) run update-translations

.PHONY: compile-translations
compile-translations:
	$(COMPOSE) build compile-translations
	$(COMPOSE) run compile-translations
