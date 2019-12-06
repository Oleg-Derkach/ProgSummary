# ------------------------------
# Conditional information

read -p "How old are you? " age

if [ $age -ge 16 ]
then
	echo "You can drive"
elif [ $age -eq 15 ]
then
	echo "You can drive nex year"
else
	echo "You can't drive"
fi

read -p "Enter a number : " num

if ((num == 10 )); then
	echo "Your number equals 10"
fi

if((num > 10)); then
	echo "It is greater then 10"
else
	echo "It is less then 10"
fi

if (( ((num % 2)) == 0)); then
	echo "It is even"
else
	echo "its odd"
fi

# ---------------------------
# Logical operators

if (( ((num > 0)) && ((num < 11)) ));
then
	echo "$num is between 1 and 10"
fi

touch samp_file && vim samp_file

[ -d samp_dir ] || mkdir samp_dir
