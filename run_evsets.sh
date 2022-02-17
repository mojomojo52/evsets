#!/bin/bash
rm output.log
touch output.log

for i in {1..100}
do
    echo "$i"
    ./evsets --verify --retry --backtracking --nohugepages >> output.log
done

#echo "Run: $i"
