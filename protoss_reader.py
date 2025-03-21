#!/usr/bin/env python3
"""Attempt to read a file in the current directory"""

def main():
    """Main logic"""
    with open("protoss.txt", "r") as foo:
            print(foo.read())

main()

