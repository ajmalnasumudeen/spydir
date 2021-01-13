#!/usr/bin/env python
     
import scanner
import time     
target_url = "http://examplewebsite.com/"  #your testing application address 
target_list = []
print( " ")
print("                      __Spy Dir__")
print("_____________________                              _____________________")
print("`-._:  .:'   `:::  .:\           |\__/|           /::  .:'   `:::  .:.-'")
print("    \      :          \          |:   |          /         :       /    ")
print("     \     ::    .     `-_______/ ::   \_______-'   .      ::   . /      ")
print("      |  :   :: ::'  :   :: ::'  :   :: ::'      :: ::'  :   :: :|       ")
print("      |  .:'   `:::  .:'   `:::  .:'   `:::  .:'   `:::  .:'   `:|       ")
print("      /     :           :           :           :           :    \       ")
print("     /______::_____     ::    .     ::    .     ::   _____._::____\      ")
print("                   `----._:: ::'  :   :: ::'  _.----'                    ")
print("                          `--.       ;::  .--'                           ")
print("                                 \    /                                  ")
print("                                  \  / Created by                        ") 
print("                                   \/            __:AJMAL:") 
print("\n")
print("\n")
#Don't test web without owner's/Organization's permission 
#Don't Test with public website, 
#Test it on your own website
packet = 0
x = 1
while x < 5:
	x = 1 + x
	time.sleep(1)
	packet = packet + 1
	print("\r[+] Program starts in  " + str(packet), end="")
	
	
print("\n ")
ignored_links = [""]
data_dict = {"username": "admin", "password": "password", "Login": "submit"}
     
vuln_scanner = scanner.Scanner(target_url, ignored_links)
vuln_scanner.session.post("http://example.com/login", data=data_dict) #Login Creds the web if any,
     
vuln_scanner.crawl()
vuln_scanner.run()