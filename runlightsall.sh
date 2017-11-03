#!/bin/bash
echo "Running Pi-Stop Traffic Lights as background process..."
cmd="python3 Pi-Stop/python_source/trafficlightsall.py"
eval "${cmd}" &>/dev/null &disown
echo PID: $!+1