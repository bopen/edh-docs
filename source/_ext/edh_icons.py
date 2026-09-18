from docutils import nodes
from sphinx.util.docutils import SphinxRole
from sphinx_design.icons import get_octicon

# TODO: Remove after sphinx-design releases the fix from
# https://github.com/executablebooks/sphinx-design/pull/279.


class EdhOcticon(nodes.inline, nodes.General):
    """Render an Octicon without adding its SVG to extracted text."""


def visit_edh_octicon_html(translator, node):
    translator.body.append(node["svg"])
    raise nodes.SkipNode


def skip_edh_octicon(translator, node):
    raise nodes.SkipNode


class EdhOcticonRole(SphinxRole):
    def run(self):
        values = self.text.split(";") if ";" in self.text else [self.text]
        icon = values[0]
        height = "1em" if len(values) < 2 else values[1]
        classes = "" if len(values) < 3 else values[2]
        icon = icon.strip()
        try:
            svg = get_octicon(icon, height=height, classes=classes.split())
        except (KeyError, ValueError) as exc:
            message = self.inliner.reporter.error(
                f"Invalid octicon content: {exc}",
                line=self.lineno,
            )
            problematic = self.inliner.problematic(
                self.rawtext,
                self.rawtext,
                message,
            )
            return [problematic], [message]

        node = EdhOcticon("", svg=svg)
        self.set_source_info(node)
        return [node], []


def setup(app):
    app.add_node(
        EdhOcticon,
        html=(visit_edh_octicon_html, None),
        latex=(skip_edh_octicon, None),
        man=(skip_edh_octicon, None),
        texinfo=(skip_edh_octicon, None),
        text=(skip_edh_octicon, None),
    )
    app.add_role("edh-octicon", EdhOcticonRole())

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
