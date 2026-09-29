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
