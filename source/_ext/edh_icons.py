# Copyright 2026 European Union
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
from pathlib import Path

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


def write_search_icons(app, exception):
    if exception is not None or app.builder.format != "html":
        return

    icons = {}
    for docname, title in app.env.longtitles.items():
        icon = next(iter(title.findall(EdhOcticon)), None)
        if icon is not None:
            icons[docname] = icon["svg"]

    output = Path(app.outdir) / "_static" / "edh-search-icons.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(icons, sort_keys=True) + "\n", encoding="utf-8")


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
    app.connect("build-finished", write_search_icons)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
