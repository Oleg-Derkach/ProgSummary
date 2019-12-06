#!/bin/bash

file1="./test_file1"
file2="./test_file2"

if [ -e "$file1" ]; then
	echo "file1 exists"

	if [ -f "$file1" ];then 
		echo "file1 is normal file"
	fi
	if [ -r "$file1" ];then 
		echo "file1 is readable" 
	fi
	if [ -w "$file1" ];then 
		echo "file1 is writable"
	fi
	if [ -x "$file1" ];then 
		echo "file1 is executable"
	fi
	if [ -d "$file1" ];then 
		echo "file1 is dirrectory"
	fi
	if [ -L "$file1" ];then 
		echo "file1 is symbolic linc"
	fi
	if [ -p "$file1" ];then 
		echo "file1 is named pipe"
	fi
	if [ -S "$file1" ];then 
		echo "file1 is network socket"
	fi
	if [ -G "$file1" ];then 
		echo "file1 is owned by the group"
	fi
	if [ -O "$file1" ];then 
		echo "file1 is owned by the user"
	fi
fi










