"""Tests for the bundled ``aa-governance`` extension."""

from __future__ import annotations

import json
from pathlib import Path

import yaml

from specify_cli import _locate_bundled_extension


PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
EXT_DIR = PROJECT_ROOT / "extensions" / "aa-governance"

EXPECTED_COMMANDS = {
    "speckit.aa-governance.name-repo",
    "speckit.aa-governance.label-repo",
}


class TestExtensionLayout:
    def test_extension_yml_exists(self):
        assert (EXT_DIR / "extension.yml").is_file()

    def test_extension_yml_has_required_fields(self):
        manifest = yaml.safe_load(
            (EXT_DIR / "extension.yml").read_text(encoding="utf-8")
        )
        assert manifest["extension"]["id"] == "aa-governance"
        assert manifest["extension"]["name"] == "Advanced Analytica Governance"
        assert manifest["extension"]["author"] == "Advanced Analytica"
        commands = {c["name"] for c in manifest["provides"]["commands"]}
        assert commands == EXPECTED_COMMANDS

    def test_extension_declares_after_tasks_hook(self):
        manifest = yaml.safe_load(
            (EXT_DIR / "extension.yml").read_text(encoding="utf-8")
        )
        after_tasks = manifest["hooks"]["after_tasks"]
        assert after_tasks["command"] == "speckit.aa-governance.label-repo"
        assert after_tasks["optional"] is True

    def test_readme_exists(self):
        readme = EXT_DIR / "README.md"
        assert readme.is_file()
        text = readme.read_text(encoding="utf-8")
        assert "Advanced Analytica Governance Extension" in text

    def test_command_files_exist(self):
        for name in EXPECTED_COMMANDS:
            cmd = EXT_DIR / "commands" / f"{name}.md"
            assert cmd.is_file(), f"Missing command file: {cmd}"

    def test_config_template_exists(self):
        assert (EXT_DIR / "config-template.yml").is_file()


class TestCatalogEntry:
    def test_catalog_lists_extension_as_bundled(self):
        catalog = json.loads(
            (PROJECT_ROOT / "extensions" / "catalog.json").read_text(encoding="utf-8")
        )
        entry = catalog["extensions"]["aa-governance"]
        assert entry["bundled"] is True
        assert entry["id"] == "aa-governance"
        assert entry["author"] == "Advanced Analytica"


class TestBundleResolution:
    def test_locate_bundled_extension_finds_bundle(self):
        located = _locate_bundled_extension("aa-governance")
        assert located is not None
        assert (located / "extension.yml").is_file()


class TestExtensionInstall:
    def test_install_from_directory(self, tmp_path: Path):
        from specify_cli.extensions import ExtensionManager

        (tmp_path / ".specify").mkdir()
        manager = ExtensionManager(tmp_path)
        manifest = manager.install_from_directory(
            EXT_DIR, "0.9.0", register_commands=False
        )

        assert manifest.id == "aa-governance"
        assert manager.registry.is_installed("aa-governance")

        installed = tmp_path / ".specify" / "extensions" / "aa-governance"
        for name in EXPECTED_COMMANDS:
            assert (installed / "commands" / f"{name}.md").is_file()
        assert (installed / "config-template.yml").is_file()

    def test_install_command_names(self, tmp_path: Path):
        from specify_cli.extensions import ExtensionManager

        (tmp_path / ".specify").mkdir()
        manager = ExtensionManager(tmp_path)
        manifest = manager.install_from_directory(
            EXT_DIR, "0.9.0", register_commands=False
        )

        names = {c["name"] for c in manifest.commands}
        assert names == EXPECTED_COMMANDS
