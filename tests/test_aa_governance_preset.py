"""Tests for the bundled ``aa-governance`` preset."""

from __future__ import annotations

import json
from pathlib import Path

import yaml

from specify_cli import _locate_bundled_preset


PROJECT_ROOT = Path(__file__).resolve().parent.parent
PRESET_DIR = PROJECT_ROOT / "presets" / "aa-governance"


class TestPresetLayout:
    def test_preset_yml_exists(self):
        assert (PRESET_DIR / "preset.yml").is_file()

    def test_preset_manifest_has_required_fields(self):
        manifest = yaml.safe_load(
            (PRESET_DIR / "preset.yml").read_text(encoding="utf-8")
        )
        assert manifest["preset"]["id"] == "aa-governance"
        assert manifest["preset"]["name"] == "Advanced Analytica Governance"
        assert manifest["preset"]["author"] == "Advanced Analytica"
        template = manifest["provides"]["templates"][0]
        assert template["name"] == "constitution-template"
        assert template["strategy"] == "append"

    def test_template_and_readme_exist(self):
        assert (PRESET_DIR / "templates" / "constitution-template.md").is_file()
        assert (PRESET_DIR / "README.md").is_file()


class TestCatalogEntry:
    def test_catalog_lists_preset_as_bundled(self):
        catalog = json.loads(
            (PROJECT_ROOT / "presets" / "catalog.json").read_text(encoding="utf-8")
        )
        entry = catalog["presets"]["aa-governance"]
        assert entry["bundled"] is True
        assert entry["id"] == "aa-governance"
        assert entry["author"] == "Advanced Analytica"


class TestBundleResolution:
    def test_locate_bundled_preset_finds_bundle(self):
        located = _locate_bundled_preset("aa-governance")
        assert located is not None
        assert (located / "preset.yml").is_file()


class TestPresetInstall:
    def test_install_from_directory(self, tmp_path: Path):
        from specify_cli.presets import PresetManager

        (tmp_path / ".specify").mkdir()
        manager = PresetManager(tmp_path)
        manifest = manager.install_from_directory(PRESET_DIR, "0.9.0")

        assert manifest.id == "aa-governance"
        assert manager.registry.is_installed("aa-governance")

        installed = tmp_path / ".specify" / "presets" / "aa-governance"
        assert (installed / "preset.yml").is_file()
        assert (installed / "templates" / "constitution-template.md").is_file()
