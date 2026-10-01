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

.PHONY: help Makefile qa serve clean

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Extend 'clean' to remove the downloaded collections and the copied notebooks
clean:
	@$(SPHINXBUILD) -M clean "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@echo "Removing '$(SOURCEDIR)/_collections' and the copied notebooks..."
	@rm -rf $(SOURCEDIR)/_collections $(SOURCEDIR)/notebooks/edh-learning $(SOURCEDIR)/notebooks/insula-code-lab

# Run quality assurance checks (pre-commit)
qa:
	@uv run pre-commit run --all

# Start a local HTTP server at http://localhost:8000
serve:
	@uv run python -m http.server $(PORT) --directory build/html
