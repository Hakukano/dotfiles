DISTRO := $(shell bin/distro.sh)

OUT_DIRECTORY = bin

EXEUTABLE_NAME = wizard

.PHONY: usage clean dev build

usage:
	echo "Usage: make [usage] [clean] [lint] [dev] [build]"

clean:
	rm -rf ${OUT_DIRECTORY}
	mkdir -p ${OUT_DIRECTORY}

lint:
	cargo clippy --manifest-path wizard/Cargo.toml

dev:
	cargo run --manifest-path wizard/Cargo.toml

build:
	cargo build --release --manifest-path wizard/Cargo.toml
	cp wizard/target/release/${EXEUTABLE_NAME} ${OUT_DIRECTORY}/${EXEUTABLE_NAME}-${DISTRO}
