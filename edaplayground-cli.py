#!/usr/bin/env python3

import argparse
import edaplayground
import os
import sys

parser = argparse.ArgumentParser("Command line interface for edaplayground.com")
parser.add_argument("-u", help="username", required=True, type=str)
parser.add_argument("-p", help="password", required=True, type=str)
parser.add_argument("-t", help="testbench file", required=True, type=str)
parser.add_argument("-d", help="design file", required=False, type=str)
parser.add_argument("-v", help="enable verbose output", action="store_true")

args = parser.parse_args()

design = ""
testbench = ""

try:
    if args.t:
        tfile = open(args.t)
        testbench = "".join(tfile.readlines())
    if args.d:
        dfile = open(args.d)
        design = "".join(dfile.readlines())
except TypeError as e:
    import traceback

    traceback.print_exc()
    sys.exit(1)

playground = edaplayground.CLI(args.u, args.p)
playground.connect()
playground.run_simulation(design, testbench)
playground.disconnect()

sys.exit(0)
