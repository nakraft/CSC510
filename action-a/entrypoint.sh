#!/bin/sh -l

cd /home/test/
python3 -m test.test
if python3 -m test.test | grep -i "fail"; then
    echo "Build Failed"
    exit 1
else
    echo "Build Passed"
fi

