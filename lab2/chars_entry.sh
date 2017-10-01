#!/bin/bash

echo "Hi!"


cat text/LNT_WaP.txt | sed 's/\(.\)/\L\1\n/g' | sort | uniq -c > RUSout

awk -v s=100 '{print $1/s " "  $2}' RUSout > RUSfreq



cat text/Mary.txt | sed 's/\(.\)/\L\1\n/g' | sort | uniq -c > ENGout

awk -v s=100 '{print $1/s " "  $2}' ENGout > ENGfreq




