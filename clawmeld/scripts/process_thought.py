#!/usr/bin/env python3
import sys
import os
import re

def process_thought(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return

    with open(file_path, 'r') as f:
        content = f.read()

    # Simple parsing
    thought = re.search(r"Thought: (.*)", content)
    context = re.search(r"Context: (.*)", content)
    metadata = re.search(r"Metadata: (.*)", content)
    timestamp = re.search(r"Timestamp: (.*)", content)

    print("--- PROCESSED THOUGHT ---")
    print(f"TEXT: {thought.group(1) if thought else 'N/A'}")
    print(f"CONTEXT: {context.group(1) if context else 'N/A'}")
    print(f"METADATA: {metadata.group(1) if metadata else 'N/A'}")
    print(f"TIME: {timestamp.group(1) if timestamp else 'N/A'}")
    print("-------------------------")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: process_thought.py <path_to_file>")
    else:
        process_thought(sys.argv[1])
