#!/bin/sh -l

cd /home/test/
python3 -m test.test
res=$?

if [ $res -ne 0 ]; then
    echo -e "Build Failed\nNum Test Cases failed = "$res
    exit $res
else
    echo "Build Passed"
fi
