#!/usr/bin/python3

import os
import sys
import json

CONFIG_PATH = "/usr/local/climate/CLImate_mocks.json"
OUTPUT_LOG_STREAM = sys.stderr

def normalizePath(path):
    if path.startswith("./"):
        return path[2:]
    else:
        return path

print(f"Reading mock configuration from: {CONFIG_PATH}", file=OUTPUT_LOG_STREAM)
with open(CONFIG_PATH) as f:
    config = json.load(f)

print(f"Argument list {str(sys.argv)}", file=OUTPUT_LOG_STREAM)
application_name = os.path.basename(sys.argv[0])

if application_name in config:
    print(f"Mock configuration found for {application_name}, checking parameters {sys.argv[1:]}", file=OUTPUT_LOG_STREAM)
    for mock_inputs in config[application_name]:
        if mock_inputs["input"] == sys.argv[1:]:
            print("Found matching mock configuration, returning mocked result", file=OUTPUT_LOG_STREAM)
            print(mock_inputs["output"])
