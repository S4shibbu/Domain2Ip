import pyfiglet 
import socket
from termcolor import colored

#banner
banner = colored(pyfiglet.figlet_format("DOMAIN2IP"),'magenta')
print(banner)

user = colored("*************** github.com/S4shibbu ***************",'red')

print(user)

#domain converting
domain_name = input(colored("Enter your target Domain : ",'green'))

#ip convert
ip = socket.gethostbyname(domain_name)
print(colored("Ip for {} : {} ".format(domain_name,ip),'green'))