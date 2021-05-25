#!/bin/bash
#Converts Dotted Decimal IP Notation to standard int [Ping works with integers too!]

dotted2int(){
  temp1=0
  result=0

  declare -a temp_arr=$( echo $1 | tr . ' ' )
  ctr=3
  for i in ${temp_arr[*]}; do
   temp1=$( echo "ibase=10; $i*(256^$ctr)" | bc )
   result=$((result + temp1))
   ((ctr--))
 done
  echo $result
}
