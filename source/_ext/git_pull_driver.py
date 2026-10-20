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

# See: https://github.com/useblocks/sphinx-collections/pull/61

from git import InvalidGitRepositoryError, NoSuchPathError, Repo
from sphinx_collections.drivers.git import GitDriver


class GitPullDriver(GitDriver):
    def _clone(self):
        self.info("Cloning git repository...")
        try:
            Repo.clone_from(self.config["source"], self.config["target"], depth=1)
        except Exception as e:  # noqa: BLE001
            self.error("Problems during cloning repository.", e)

    def run(self):
        target = self.get_path(self.config["target"])
        self.create_target_dir(target)

        try:
            repo = Repo(target)
            self.info("Pulling git repository...")
            repo.remotes.origin.pull()
        except InvalidGitRepositoryError, NoSuchPathError:
            self._clone()
        except Exception as e:  # noqa: BLE001
            self.error("Problems during repository pull.", e)
