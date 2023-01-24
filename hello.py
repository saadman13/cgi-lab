#!/usr/bin/env python3

import os
import json

print("Content-Type: application/json")
print(os.environ)
print(f"<p> HTTP_USER_AGENT = {os.environ} HTTP_USER_AGENT</p>")