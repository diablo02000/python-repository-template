"""Tests for {{ project_name }} main module."""

import pytest
from {{ project_name }}.main import main


class TestMain:
    """Test cases for the main module."""

    def test_main_returns_zero(self) -> None:
        """Test that main function returns 0 (success)."""
        result = main([])
        assert result == 0

    def test_main_with_help_flag(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Test that main function shows help when requested."""
        with pytest.raises(SystemExit) as exc_info:
            main(["--help"])
        assert exc_info.value.code == 0
        captured = capsys.readouterr()
        assert "{{ project_name }}" in captured.out or "{{ project_description|default('') }}" in captured.out

    def test_main_with_version_flag(self, capsys: pytest.CaptureFixture[str]) -> None:
        """Test that main function shows version when requested."""
        with pytest.raises(SystemExit) as exc_info:
            main(["--version"])
        assert exc_info.value.code == 0
        captured = capsys.readouterr()
        assert "0.0.1" in captured.out