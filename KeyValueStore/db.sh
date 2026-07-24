#!/bin/bash

create(){
    if [ ! -f data ]; then
        touch data
    fi
    r=$(read "$1")
    # echo $r
    if [[ "$r" == "" ]]; then
        printf '%s %s\n' "$1" "$2" >> data
        exit 0
    else
        exit 3
    fi
}

read() {
    [ -f data ] || exit 0
    awk -v key="$1" '$1 == key { print $2 }' data
    exit 0
}

update(){
    r=$(read "$1")
    if [[ "$r" == "" ]]; then
        exit 2
    else
        awk -v key="$1" -v val="$2" '$1 == key { $2 = val } { print }' data > data.tmp && mv data.tmp data
        exit 0
    fi
}

delete(){
    r=$(read "$1")
    if [[ "$r" == "" ]]; then
        exit 2
    else
        awk -v key="$1" '$1 != key { print }' data > data.tmp && mv data.tmp data
        exit 0
    fi
}

cmd="$1"
shift
case "$cmd" in
    create) create "$@" ;;
    read)   read "$@" ;;
    update) update "$@" ;;
    delete) delete "$@" ;;
    *)
        echo "Usage: $0 {create|read|update|delete} key [value]" >&2
        exit 1
        ;;
esac
