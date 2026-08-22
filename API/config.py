"""Configuration for the demoblaze API suite.

Values come from the environment so the same tests can be pointed at another
host without a code change.  The defaults are a public demo account, which is
why they can sit in the repo.
"""
import os

BASE_URL = os.getenv("DEMOBLAZE_URL", "https://api.demoblaze.com")
USERNAME = os.getenv("DEMOBLAZE_USER", "Shahrukh")
PASSWORD = os.getenv("DEMOBLAZE_PASS", "12345")
