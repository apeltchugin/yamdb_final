import os
import re

from django.conf import settings


class TestDockerfileCompose:

    def test_dockerfile_compose(self):
        try:
            with open(f'{os.path.join(settings.BASE_DIR, "docker-compose.yaml")}', 'r') as f:
                docker_compose = f.read()
        except FileNotFoundError:
            assert False, 'Проверьте, что добавили файл docker-compose.yaml'

        assert re.search(r'image:\s+postgres:', docker_compose), (
            'Проверьте, что добавили образ postgres:latest в файл docker-compose.yaml'
        )
        assert re.search(r'image:\s+([a-zA-Z0-9]+)\/([a-zA-Z0-9_\.])+(\:[a-zA-Z0-9_-]+)?', docker_compose), (
            'Проверьте, что добавили сборку контейнера из образа на вашем DockerHub в файл docker-compose.yaml'
        )
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# PEP 582; used by e.g. github.com/David-OConnor/pyflow
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# Папки, создаваемые средой разработки
.idea
.DS_Store
.AppleDouble
.LSOverride

*.sublime-project
*.sublime-workspace

.vscode/
*.code-workspace

# Local History for Visual Studio Code
.history/

.mypy_cache

# папки со статикой и медиа
media/