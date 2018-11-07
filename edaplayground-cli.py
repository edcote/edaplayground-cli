#!/usr/bin/env python3

import argparse
import edaplayground

parser = argparse.ArgumentParser("Command line interface for edaplayground.com")
parser.add_argument("-u", help="username", required=True, type=str)
parser.add_argument("-p", help="password", required=True, type=str)
parser.add_argument("-v", help="enable verbose output", action="store_true")
args = parser.parse_args()

playground = edaplayground.CLI(args.u, args.p)
playground.connect()
