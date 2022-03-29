import argparse
import sys
import time
import subprocess as sp
import os

from click import command

parser = argparse.ArgumentParser(description="sdasdas")

parser.add_argument("-c", "--command", type=str, required=True, help="string")
parser.add_argument("-f", "--outputfile", type=str, required=True, help="string")
parser.add_argument("-l", "--logfile", type=str, required=True, help="string")
args = parser.parse_args()

print('Command: %s' % args.command.split())
print('Output File: %s' % args.outputfile)
print('Log File: %s' % args.logfile)

with open(args.outputfile, "ab") as outputfile:
    process = sp.Popen(args.command.split(), stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = process.communicate()
    process2 = sp.Popen("date", stdout=sp.PIPE, stderr=sp.PIPE)
    stdout2, stderr2 = process2.communicate()
    outputfile.write(stdout)

with open(args.logfile, "ab") as logfile:
    if stderr == b'':
        logfile.write(stdout2[:-2] + b': Comando ' + bytes(args.command, encoding = "utf-8") + b' ejecutado correctamente.\n')
    else:
        logfile.write(stdout2[:-2] + b' ' + stderr)