from docutils import nodes
from sphinx.util.docutils import SphinxRole


class EdhBadgeRole(SphinxRole):
    def run(self):
        variant = self.name.removeprefix("bdg-")
        node = nodes.inline(
            self.rawtext,
            self.text,
            classes=[
                "sd-sphinx-override",
                "sd-badge",
                "edh-badge",
                f"edh-badge--{variant}",
            ],
        )
        self.set_source_info(node)
        return [node], []


def setup(app):
    for variant in (
        "restricted",
        "edh-keyword",
        "draft",
        "deprecated",
        "geobrowser",
    ):
        app.add_role(f"bdg-{variant}", EdhBadgeRole())

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
