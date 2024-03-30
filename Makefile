OUT_DIRECTORY = out

EXEUTABLE_NAME = wizzard

.PHONY: usage clean dev build

usage:
	echo "Usage: make [usage] [clean] [dev] [build]"

clean:
	rm -rf ${OUT_DIRECTORY}
	mkdir -p ${OUT_DIRECTORY}

dev:
	cargo run --manifest-path wizzard/Cargo.toml

build: clean
	cargo build --release --manifest-path wizzard/Cargo.toml
	cp wizzard/target/release/${EXEUTABLE_NAME} ${OUT_DIRECTORY}/${EXEUTABLE_NAME}
