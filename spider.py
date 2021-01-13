import requests, re, time, sys 
import urllib.parse as urlparse



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
target_url = "example.com /" #your testing application address 

packet = 0
x = 1
while x < 5:
	x = 1 + x
	time.sleep(1)
	packet = packet + 1
	print("\r[+] Program starts in  " + str(packet), end="")
	
time.sleep(1)
def extract_url(url):
	responce = requests.get(url)
	return re.findall('(?:href=")(.*?)"', responce.content.decode(errors="ignore"))

def crawl(url):
	
			webs_link = extract_url(url)
			for link in webs_link:
				link = urlparse.urljoin(url, link)

				if "#" in link:
					link = link.split("#")[0]

				if target_url in link and link not in target_list:
					target_list.append(link)
					print("\n")
					print(link)
					crawl(link)

crawl(target_url)

