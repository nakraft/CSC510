#!/bin/sh -l

cd /home/test/
python3 -m test.test
res=$?

if [ $res -ne 2 ]; then
    echo -e "Build Failed\nNum Test Cases failed = "$res
    echo "Expected 2 failed test"
    exit $res
else
    echo "Build Passed"
fi
