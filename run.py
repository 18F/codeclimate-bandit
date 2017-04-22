# modified from
# https://github.com/rubik/radon/blob/b73c279acc321158c0b089b941e12a129daa9429/codeclimate-radon

import json
import os.path
import shlex
import sys

binstub = "bandit"
include_paths = ["."]

if os.path.exists("/config.json"):
    contents = open("/config.json").read()
    config = json.loads(contents)

    if config.get("config"):
        if config["config"].get("encoding"):
            encoding = config["config"].get("encoding")
            os.environ["RADONFILESENCODING"] = encoding

    if config.get("include_paths"):
        config_paths = config.get("include_paths")
        python_paths = []
        for i in config_paths:
            ext = os.path.splitext(i)[1]
            if os.path.isdir(i) or "py" in ext:
                python_paths.append(i)
        include_paths = python_paths

    include_paths = config.get("include_paths", ["."])
    include_paths = [shlex.quote(path) for path in include_paths
                     if os.path.isdir(path) or path.endswith(".py")]

if len(include_paths) > 0:
    paths = " ".join(include_paths)

    print("Running {}...".format(binstub), file = sys.stderr)
    os.system("{} -r {}".format(binstub, paths))
else:
    print("Empty workspace; skipping...", file = sys.stderr)
