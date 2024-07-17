


docs-build:
	quartodoc build --config docs/_quarto.yml --verbose
	quarto render docs/
	open docs/_build/index.html

docs-preview:
	quartodoc build --config docs/_quarto.yml
	quarto preview docs/
