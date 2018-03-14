compile:
	transcrypt -nab --parent=.none index.py

bundle:
	npx webpack __javascript__/index.js --output __javascript__/bundle.js

.PHONY: compile bundle
