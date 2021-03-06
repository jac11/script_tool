#!/usr/bin/env python

import string  
import random
import argparse
import sys
import os 
import re
import subprocess
class Tools :
   
    def __init__(self):

	parser = argparse.ArgumentParser( description="Usage: [OPtion] [arguments]  [length]  [arguments] Example: -c a -l 300")
	parser.add_argument( '-c',"--char"     , metavar='' , action=None  ,help ="to generate  A or B..etc char " "Example : -c a -l 220")
	parser.add_argument( '-r',"--random"   , metavar='' , action =None ,help ="to generate  random pattern " "Example : -r r -l 200", type = str)
	parser.add_argument( '-a',"--alfa"     , metavar='' , action =None ,help ="to generate AAAAtoZZZZ 32bit " "Example : -a x86 -l 26 ")
	parser.add_argument( '-A',"--alfa_64"  , metavar='' , action =None,help ="generate AAAAAAAAtoZZZZZZZZ 64bit ""Example :-A x64 -l 26")
	parser.add_argument( '-H',"--Hexdecode", metavar='' , action =None ,help ="to decode hex address ""Exampel: -H 0x00000000", type =str)
	parser.add_argument( '-l',"--length"   , metavar='' , action =None,help ="to give length of the pattern ", type = int)
	parser.add_argument( '-s',"--L_endian", metavar='' , action =None ,help ="to little-endian struct " "EExample: -s 0x0876bf67") 
        parser .add_argument( '-g',"--libc"    , metavar='' , action =None ,help ="to grep from libc Library x86" " Example -g /bin/sh") 
        parser.add_argument( '-G',"--libc64"    , metavar='' , action =None ,help ="to grep from libc Library x86-64 " "Example -G /bin/sh") 
        parser.add_argument( '-F',"--object"  , metavar='' , action =None ,help ="Select  program  dump " "Example: -F program.o -D ret") 
        parser.add_argument( '-D',"--dump"  , metavar='' , action =None ,help ="grep program addresses " " Example: -F Program -D pop")
	parser.add_argument( '-R',"--reverse" , metavar='' , action=None  ,help ="check payload  length" "Example : -R AAASsscc@@@ ")
        parser.add_argument( '-E',"--encode" , metavar='' , action =None ,help ="encode the address from gdb " "Example : --R AAASsscc@@@ -E sss" , type = str)

	self.args = parser.parse_args()
	if len(sys.argv)!=1:
           pass
        else:
           parser.print_help()
	   exit()	
	self.Main()
	
    def ALFA__(self):
        try: 
            argv = sys.argv[2]  
            if self.args.char and len(argv) ==1 and sys.argv[1]=="-c" :             
                 char = self.args.char.upper()           
                 len_long = self.args.length
                 result = char*len_long
                 print result 
                 exit()
            else:
                 print"Usege : [Option] -c [arguments] a [OPtion] -l [arguments] Number of length."        
        except UnboundLocalError:
                 print"Usege : [Option] -c [arguments] a [OPtion] -l [arguments] Number of length."
                 print"Example: -c a -l 200"  
                 exit()
    def ran(self):        
            argv = sys.argv[2]                  
            if self.args.random and argv =="r": 
                 len_long_1 = self.args.length                                     
                 result = "".join(random.choice(string.ascii_letters)for i in range(len_long_1)).lower() 
                 print result 
                 with open("./.data",'w')as data:
                    self.dataW = data.write(result)
                 exit()
            else:
                 print"Usege : [Option] -r [arguments] r [OPtion] -l [arguments] Number of length."
                 print"Example: -r  r -l 100" 
                 exit()
    def AAAA(self): 
        try:    
            argv = sys.argv[2]
            if self.args.alfa and argv =="x86": 
                 len_alfa= self.args.length 
            if len_alfa == 1 or len_alfa < 27:                    
                 ALfa = ''.join((string.ascii_uppercase[i:i+1]*4)for i in range(len_alfa)) 
                 print ALfa
                 with open("./.data",'w')as data:
                    self.dataW =  data.write(ALfa)
                 exit()    
            else:
                 print"Usege : [Option] -a [arguments] x86 [OPtion] -l [arguments] Number of length."
                 print "minimum  '1' maximum '26'"
                 print"Example: -a  x86 -l 26"           
        except UnboundLocalError:
                 print"Usege : [Option] -a[arguments] x86 [OPtion] -l [arguments] Number of length."
                 print"Example: -a  x86 -l 26"      
                            
    def x86_64(self):
        try:    
            argv_1 = sys.argv[2]
            if self.args.alfa_64 and argv_1 =="x64": 
                 len_alfa_1= self.args.length 
            if len_alfa_1 == 1 or len_alfa_1 < 27:                    
                 ALfa_1 = ''.join((string.ascii_uppercase[i:i+1]*8)for i in range(len_alfa_1)) 
                 print ALfa_1
                 with open("./.data",'w')as data:
                     self.dataW = data.write(ALfa_1)
                 exit()
            else:
                 print"Usege : [Option] -A [arguments] x64 [OPtion] -l [arguments] Number of length."
                 print "minimum  '1' maximum '26'"
                 print"Example: -A  x64 -l 26"            
        except UnboundLocalError:
                 print"Usege : [Option] -A [arguments] x64 [OPtion] -l [arguments] Number of length."
                 print"Example: -A  x64 -l 26"                           
   
    def decode(self):
        try:
            if self.args.Hexdecode  :
                 hexdecode = self.args.Hexdecode
                 hexdecode = hexdecode.replace("0x","")
                 hexdecode ="".join(reversed([hexdecode[i:i+2] for i in range(0,len( hexdecode), 2)]))
                 hexdecode = hexdecode.decode("hex")
                 print"decode HEX is : ", hexdecode                
                 with open("./.data",'r')as data:
                     find = data.read()                    
                 located = find.find( hexdecode)
                 if hexdecode in find  :
                    print "Offset Found at  : ",located      
                    if os.path.isfile("./.data"):
                       os.remove("./.data")
                    else:
                        pass                        
                 else:
                       print "No Offset Found "
            else:
                 print"Usege : [Option] -H [arguments]  HexNumber "
                 print"Example: -H 0x00000000 "
        except IOError:
                pass                                            
        except Exception :
            print "[IndexError]-[TypeError]"
            exit()               
            
    def little_endian1(self):
       
            if self.args.L_endian:
               little_endian =  self.args.L_endian
               little_endian1  =   little_endian.replace("0x","")
               little_endian = "".join(reversed([little_endian1  [i:i+2] for i in range(0, len(little_endian1  ), 2)]))
               little_endian = "".join('\\x%s'% little_endian[i:i+2] for i in range(0, len( little_endian), 2))
               little_endian = "".join('"\\x%s"'% little_endian[i:i+32] for i in range(0, len( little_endian), 32))
               little_endian.replace(" ","")
               little_endian.replace(" ","")
               little_endian= little_endian.replace('"\\x','"')               
               print "little_endian is : ",little_endian
               print "struck mode :","struct.pack","('I',",'{}'.format(self.args.L_endian),")".strip()
            else:
               print"Usege : [Option] -s [arguments]  Hexaddress "
               print"Example: -s 0x0876bf67 "                
    
    def libc_Library(self):
            if self.args.libc:  
               Libc_libc = self.args.libc     
               process = subprocess.Popen(['strings', '-a', '-t','x','/lib/i386-linux-gnu/libc.so.6'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
               stdout, stderr = process.communicate()
               stdout_libc =stdout
               get_gerp= re.findall("......."+'{}'.format(Libc_libc),stdout_libc) 
               if Libc_libc in stdout_libc:   
                  print"grep _from _libc: ", '\n'.join(get_gerp)                    
               else:
                  print "[Error][NotFound] "
            else:
               print "[Error][/lib/i386-linux-gnu/libc.so.6]"
    
    def libc_Library_64(self):
            if self.args.libc64:  
               Libc_libc = self.args.libc64   
               process = subprocess.Popen(['strings', '-a', '-t','x','/lib/x86_64-linux-gnu/libc-2.30.so'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
               stdout, stderr = process.communicate()
               stdout_libc =stdout
               get_gerp= re.findall("......."+'{}'.format(Libc_libc),stdout_libc) 
               if Libc_libc in stdout_libc:   
                  print"grep _from _libc: ", '\n'.join(get_gerp)                    
               else:
                  print "[Error][NotFound] "
            else:
               print "[Error][/lib/x86_64-linux-gnu/libc-2.30.so]"   
    
    def objdump_file(self):  
                 
            if self.args.object and sys.argv[1] == "-F" and sys.argv[3]=="-D":
               FileName = self.args.object
               FileDump = self.args.dump
               with open('./.file_1','w')as file:                 
                   stdout = subprocess.call(['objdump','-d','{}'.format(FileName)], stdout=file, stderr=file)                         
               process = subprocess.Popen(['grep','{}'.format(FileDump), './.file_1'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
               stdout, stderr = process.communicate()
               print stdout
               if os.path.isfile("./.file_1"):
                     os.remove("./.file_1")
               else:
                  pass      
            else:
               print"Usege : [Option] -F [arguments] filename [OPtion] -D [arguments] grep txt ."
               print"Example -F  Objectfile -D pop"  
    def DE_CODE(self):
	try :
	        if self.args.reverse:
	            rev=self.args.reverse
	            en_code= self.args.encode
	            en_code = en_code.replace("0x","")
	            en_code = "".join(reversed([en_code[i:i+2] for i in range(0,len( en_code), 2)])) 
	            en_code = en_code.replace("00","")
	            rev= rev.encode("hex")
	            with open("./.encode",'wb') as encode :
		        rev_1 = encode.write(rev)                   
	            with open("./.encode",'rb') as encode :
		        read= encode.read() 
	        if en_code in  read:                
		        find_1 = read.find(en_code)
		        find = find_1/2
		        if find > 0 :
		                  print"length of payload is |",len(rev)/2,"|"
		                  print"the address start at |",find,"|"
	                          print"the address end at   |" ,find+len(en_code)/2 ,'|'
	                          
	                else:
	                    print "[Error]-[indexError]"     
		        if os.path.isfile("./.encode"):
		            os.remove("./.encode")    
	                else: 
	                     pass
	        elif en_code not in  read:
	              re_code = en_code.encode("hex")
	              find_1 = read.find(re_code)
	              find = find_1/2
	              if find > 0 :
	                         print"length of payload is |",len(rev)/2 ,"|"
		                 print"the address start at |",find,"|"
	                         print"the address end at |" ,find+len(en_code)/2 ,'|'
	              else:
	                    print "[Error]-[indexError]"   
	              if os.path.isfile("./.encode"):
		            os.remove("./.encode")    
	              else: 
	                 pass
	        else:
	             print"Usege : [Option] -R [arguments]  payload [Option] -E [arguments] "
                     print"Example: -R AAAAAAAAAAAAAAAAAAAAAAAAAA@@@ -E 0x4040bdbfef4067 "
                               	            	    
	except IOError:
		   pass                                            
        except Exception :
	      print "[OPtion] -R [arguments] the payload  [OPtion] -E [arguments] Example:-R AAAAAAAAAAAAAAAAAAAAAAAAAAg@@@ -E 0x4040bdbfef4067 "  
     
    def Main(self):
        if self.args.char :       
             self.ALFA__()  
        if self.args.random :
             self.ran()   
        if self.args.alfa:      
             self.AAAA()    
        if self.args.alfa_64:
             self.x86_64()
        if self.args.Hexdecode:
             self.decode()
        if self.args.L_endian:
             self.little_endian1()
        if self.args.libc:
             self.libc_Library()
	if self.args.libc64:
             self.libc_Library_64()
        if self.args.object:
             self.objdump_file() 
	if self.args.reverse:
             self.DE_CODE() 
                                  
if __name__=="__main__":
    Tools()
    
        


