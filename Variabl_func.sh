#!/bin/bash

declare -r NUM1=5

num2=4

num3=$((NUM1+num2))
num4=$((NUM1-num2))
num5=$((NUM1*num2))
num6=$((NUM1/num2))


echo "5 + 4 = $num3"	# 5 + 4 = 9
echo "5 - 4 = $num4"	# 5 - 4 = 1
echo "5 * 4 = $num5"	# 5 * 4 = 20
echo "5 / 4 = $num6"	# 5 / 4 = 1

echo $((5**2))	# 25
echo $((5%4))	# 1

rand=5
let rand+=4
echo "$rand"  # 9

echo "rand++ = $(( rand++ ))" # 9
echo "$rand"   # 10
echo "++rand = $(( ++rand ))" # 11
echo "$rand"   # 11
echo "rand-- = $(( rand-- ))" # 11
echo "$rand"   # 10
echo "--rand = $(( --rand ))" # 9

num7=1.2
num8=3.4
num9=$(python -c "print $num7+$num8")
echo $num9

cat<< END
this text
prints on 
many lines
END
echo " ===================== "

getDate(){
	date
	return
}
getDate

name="Derek"


# =================================
# Functions

demLocal(){
	local name="Paul"  #available only
	return             #inside of this function
}

echo "$name" # Derek

# =================================
# Variables
getSum(){
	local num3=$1
	local num4=$2

	local sum=$((num3+num4))
	echo $sum
}

sum=$(getSum 4 3)  
echo "the sum of variables num1 and num2 is $sum"    # 7
# the sum of variables num1 and num2 is 7

num1=13
num2=42
sum=$(getSum num1 num2)
echo "the sum of $num1 and $num2 is $sum"   # 55
# the sum of 13 and 42 is 55



