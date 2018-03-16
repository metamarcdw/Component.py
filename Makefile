clean:
	rm -rf __javascript__/ components/__javascript__/

cleanjs:
	rm -rf node_modules/ package-lock.json

compile:
	transcrypt -nab -ds --parent=.none index.py

bundle:
	npx webpack __javascript__/index.js --output __javascript__/bundle.js

.PHONY: clean cleanjs compile bundle
