from pathlib import Path

import yaml


class ConfigManager:
    def __init__(self, folder="config"):
        self.data = {}
        p = Path(folder)
        if p.exists():
            for f in p.glob("*.yaml"):
                self.data[f.stem] = yaml.safe_load(f.read_text()) or {}

    def get(self, path, default=None):
        cur = self.data
        for part in path.split("."):
            if isinstance(cur, dict) and part in cur:
                cur = cur[part]
            else:
                return default
        return cur
