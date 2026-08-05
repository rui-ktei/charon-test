# What CI runs, in one target, so anything that checks this repository checks the same thing.
.PHONY: test

test:
	uvx ruff check .
	uv run --with httpx python smoke.py
