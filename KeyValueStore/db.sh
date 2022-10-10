#!/bin/bash

create(){
    if [ ! -f data ]; then
        touch data
    fi
    r=$(read $1)
    # echo $r
    if [[ "$r" == "" ]]; then
        echo $1 $2 >> data
        exit 0
    else
        exit 3
    fi
}

read() {
    cat "data" | grep -e $1 | awk '{print $2}'
    exit 0
}

update(){
    r=$(read $1)
    if [[ "$r" == "" ]]; then
        exit 2
    else
        sed -ir "s/$1\ .*/$1\ $2/g" data
        exit 0
    fi
}

delete(){
    r=$(read $1)
    if [[ "$r" == "" ]]; then
        exit 2
    else
        sed -ir "/$1\ .*/d" data
        exit 0
    fi
}

$@