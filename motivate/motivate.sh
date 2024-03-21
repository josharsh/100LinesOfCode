#!/bin/bash


function main {
    motivate="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )/motivate.txt"
    ignore_lines=2
    index=$(grep -Eo -m 2 "[0-9]+[0-9]+" $motivate)
    rand=$(( ($RANDOM % $index) + $ignore_lines))

    while IFS= read -r line
    do
        let rand=$rand-1
        if [[ $rand -eq 0 ]]
        then
            echo $line
            break
        fi
done < $motivate
}

main "$@"