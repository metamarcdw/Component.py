clean:
	rm -rf src/__javascript__/ src/components/__javascript__/

cleanjs:
	rm -rf node_modules/ package-lock.json

compile:
	transcrypt -nab -ds --parent=.none src/index.py

watch:
	npx nodemon -e py --watch src --exec "make compile"

server:
	npx webpack-dev-server

go:
	npx concurrently --kill-others "make watch" "make server"

.PHONY: clean cleanjs compile watch server go
