all: build

build: ../venv/bin/activate build-subdirs

build-subdirs:
	for d in * ; do [ -d "$$d" ] && make -C "$$d" $* ; done

clean: clean-subdirs

clean-subdirs:
	for d in * ; do [ -d "$$d" ] && make -C "$$d" clean $* ; done
