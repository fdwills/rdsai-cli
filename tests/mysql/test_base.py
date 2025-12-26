"""Tests for MySQL base tool version detection."""

import pytest
from unittest.mock import MagicMock, patch

from tools.mysql.base import MySQLToolBase
from loop.runtime import BuiltinSystemPromptArgs


class MockMySQLTool(MySQLToolBase):
    """Mock MySQL tool for testing."""

    async def _execute_tool(self, params):
        """Mock implementation."""
        return {}


class TestVersionDetection:
    """Test MySQL version detection methods."""

    @pytest.fixture
    def tool(self):
        """Create a mock MySQL tool instance."""
        builtin_args = BuiltinSystemPromptArgs()
        return MockMySQLTool(builtin_args=builtin_args)

    @pytest.mark.parametrize(
        "version_str,expected",
        [
            ("8.0.22", True),
            ("8.0.23", True),
            ("8.1.0", True),
            ("9.0.0", True),
            ("8.0.21", False),
            ("8.0.0", False),
            ("7.9.9", False),
            ("5.7.40", False),
        ],
    )
    def test_is_mysql_version_at_least_8_0_22(self, tool, version_str, expected):
        """Test version comparison for MySQL 8.0.22."""
        with patch.object(tool, "_get_mysql_version", return_value=version_str):
            result = tool._is_mysql_version_at_least(8, 0, 22)
            assert result == expected, f"Version {version_str} should return {expected}"

    @pytest.mark.parametrize(
        "version_str,expected",
        [
            ("8.0.22-0ubuntu0.20.04.1", True),  # Version with suffix
            ("8.0.22-log", True),  # Version with log suffix
            ("8.0.22-debug", True),  # Version with debug suffix
            ("8.0.21-0ubuntu0.20.04.1", False),
        ],
    )
    def test_version_with_suffix(self, tool, version_str, expected):
        """Test version parsing with suffix."""
        with patch.object(tool, "_get_mysql_version", return_value=version_str):
            result = tool._is_mysql_version_at_least(8, 0, 22)
            assert result == expected, f"Version {version_str} should return {expected}"

    def test_version_none(self, tool):
        """Test when version cannot be determined."""
        with patch.object(tool, "_get_mysql_version", return_value=None):
            result = tool._is_mysql_version_at_least(8, 0, 22)
            assert result is False, "Should return False when version is None"

    def test_version_invalid_format(self, tool):
        """Test with invalid version format."""
        with patch.object(tool, "_get_mysql_version", return_value="invalid"):
            result = tool._is_mysql_version_at_least(8, 0, 22)
            assert result is False, "Should return False for invalid version format"

    def test_version_empty_string(self, tool):
        """Test with empty version string."""
        with patch.object(tool, "_get_mysql_version", return_value=""):
            result = tool._is_mysql_version_at_least(8, 0, 22)
            assert result is False, "Should return False for empty version string"

    @pytest.mark.parametrize(
        "major,minor,patch,version_str,expected",
        [
            (8, 0, 22, "8.0.22", True),
            (8, 0, 22, "8.0.21", False),
            (8, 0, 22, "8.0.23", True),
            (5, 7, 40, "5.7.40", True),
            (5, 7, 40, "5.7.39", False),
            (5, 7, 40, "5.8.0", True),
            (5, 7, 40, "5.6.0", False),
        ],
    )
    def test_various_version_checks(self, tool, major, minor, patch, version_str, expected):
        """Test various version comparison scenarios."""
        with patch.object(tool, "_get_mysql_version", return_value=version_str):
            result = tool._is_mysql_version_at_least(major, minor, patch)
            assert result == expected, (
                f"Version {version_str} >= {major}.{minor}.{patch} should be {expected}"
            )

