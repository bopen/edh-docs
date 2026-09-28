# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= uv run sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
PORT          ?= 8000

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@echo ""
	@echo "Custom targets:"
	@echo "  qa          to run quality assurance checks (pre-commit)"
	@echo "  serve       to start a local HTTP server at http://localhost:8000"

.PHONY: help Makefile qa serve clean prod-serve

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Extend 'clean' to remove source/_collections
clean:
	@$(SPHINXBUILD) -M clean "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@echo "Removing everything under '$(SOURCEDIR)/_collections'..."
	@rm -rf $(SOURCEDIR)/_collections

# Run quality assurance checks (pre-commit)
qa:
	@uv run pre-commit run --all

# Start a local HTTP server at http://localhost:8000
serve:
	@uv run python -m http.server $(PORT) --directory build/html

# Robust serve
prod-serve: html
	@uv run uvicorn --host 0.0.0.0 'edh_docs:app'
