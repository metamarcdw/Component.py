clean:
	rm -rf src/__javascript__/ src/components/__javascript__/

cleanjs:
	rm -rf node_modules/ package-lock.json

compile:
	transcrypt -nab -ds --parent=.none src/index.py

server:
	npx webpack-dev-server

.PHONY: clean cleanjs compile server
