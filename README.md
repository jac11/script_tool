# script_tool
* script tool python 2.7 
* script take input as option and arguments
## how to use 
* git clone https://github.com/jac11/script_tool.git
* chmod +x script.py
* to check all  option open help menu by typing ./script.py -h or --help
* follow the help menu to use option 
##  [ help menu overview ]
```
usage: script.py [-h] [-c] [-r] [-a] [-A] [-H] [-l] [-s] [-G] [-F] [-D]

Usage: [OPtion] [arguments] [length] [arguments] Example: -c a -l 300

optional arguments:
  -h, --help         show this help message and exit
  -c , --char        to generate  A or B..etc char Example : -c a -l 220
  -r , --random      to generate random pattern Example : -r r -l 200
  -a , --alfa        to generate  AAAAtoZZZZ 32bit Example : -a x86 -l 26
  -A , --alfa_64     generate  AAAAAAAAtoZZZZZZZZ 64bit Example :-A x64 -l 26
  -H , --Hexdecode   to decode hex address Exampel: -H 0x00000000
  -l , --length      to give length of the pattern
  -s , --L_endian    to little-endian struct Example: -s 0x0876bf67
  -G , --libc        to grep from libc Library Example -G /bin/sh
  -F , --object      Select program dump Example: -F program.o -D ret
  -D , --dump        grep program addresses Example: -F Program -D pop

```

### [ Pattern ]

* wtih scripy.py can generate  different kind of strings pattren 
*  option -r  r to give random pattern -l to give length for the pattren 
```
 ~/script_tool# ./script.py  -r r -l 60
xvwbcigltvzcyrynipadtsjuukqlczgczwoxwjulmaidhijnveusieyfgzqz
```
* wtih -c can generate  char from a to b or any string like %
```
~/script_tool# ./script.py  -c a -l 50
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
~/script_tool# ./script.py  -c b  -l 70
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
~/script_tool# ./script.py  -c %  -l 70
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
```
* with  -a x86 or -A  x64 can generate English alphabet AAAA to ZZZZ or AAAAAAAA to ZZZZZZZZ 
* minimum  '1' maximum '26' 
```
~/script_tool# ./script.py  -a x86 -l 26
AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ
~/script_tool# ./script.py  -A x64 -l 26
AAAAAAAABBBBBBBBCCCCCCCCDDDDDDDDEEEEEEEEFFFFFFFFGGGGGGGGHHHHHHHHIIIIIIIIJJJJJJJJKKKKKKKKLLLLLLLLMMMMMMMMNNNNNNNNOOOOOOOOPPPPPPPPQQQQQQQQRRRRRRRRSSSSSSSSTTTTTTTTUUUUUUUUVVVVVVVVWWWWWWWWXXXXXXXXYYYYYYYYZZZZZZZZ
```
### [ option -H ]
* -H option to conver decode hex 
* and search for offset in pattren generate  by script.py
```
~/script_tool# ./script.py  -H 0x6d7a7463

decode HEX is :  ctzm
Offset Found at  :  140
```
### [ struck address ]
* with option -s can convert address to little-endian 
* address will convert to array and as struct mode
``` 
~/script_tool# ./script.py  -s 0x6d7a7463
little_endian is :  "\x63\x74\x7a\x6d"
struck mode : struct.pack ('I', 0x6d7a7463 )
```
### [ Return-to-libc ]
* to grep from libc library use ./script.py -G /bin/sh # -G option grep folow with the string 
* ```~/script_tool# ./script.py -G /bin/sh```
* ```grep _from _libc:  188406 /bin/sh```
### [ Return-oriented programming ROP ]
* to grep pop ,ret from the program use -F and - D

``` 
~/script_tool# ./script.py  -F stack7 -D ret

 8048383:	c3                   	ret    
 8048494:	c3                   	ret    
 80484c2:	c3                   	ret    
 8048544:	c3                   	ret    
 8048553:	c3                   	ret    
 8048564:	c3                   	ret    
 80485c9:	c3                   	ret    
 80485cd:	c3                   	ret    
 80485f9:	c3                   	ret    
 8048617:	c3                   	ret    
```

### [for connect]

* administrator@jacstory.tech
* thank you 
