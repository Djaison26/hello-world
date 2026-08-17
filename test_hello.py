import subprocess
import sys
import unittest

from hello import greet


class TestGreet(unittest.TestCase):
    def test_default_name(self):
        self.assertEqual(greet("World"), "Hello, World!")

    def test_custom_name(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")


class TestCli(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, "hello.py", *args],
            capture_output=True,
            text=True,
            check=True,
        )

    def test_default_output(self):
        result = self.run_cli()
        self.assertEqual(result.stdout.strip(), "Hello, World!")

    def test_name_argument(self):
        result = self.run_cli("--name", "Alice")
        self.assertEqual(result.stdout.strip(), "Hello, Alice!")


if __name__ == "__main__":
    unittest.main()
