import ipaddress
import socket
def show_banner():
    """
    Display the NetScan Pro application banner.

    Parameters:
        None.

    Returns:
        None.
    """

    banner = r"""
    _   __     __  _____                     ____
   / | / /__  / /_/ ___/_________ _____     / __ \_________
  /  |/ / _ \/ __/\__ \/ ___/ __ `/ __ \   / /_/ / ___/ __ \
 / /|  /  __/ /_ ___/ / /__/ /_/ / / / /  / ____/ /  / /_/ /
/_/ |_/\___/\__//____/\___/\__,_/_/ /_/  /_/   /_/   \____/

────────────────────────────────────────────────────────────
                Scan Smart. Discover More.
                      Version 1.0.0
────────────────────────────────────────────────────────────
"""

    print(banner)


#multi-line string



def get_target():
    while True:
        target = input("Target (IP / Domain): ").strip()
        
        if target : #!= ""
            return target
        else:
            print("[ERROR] Target cannot be empty.")
            print()


            
def validate_target(target):
    try :
        ipaddress.ip_address(target)
        return "ip"
        
    except ValueError:
        if(
            "." in target  
            and not target.startswith(".")
            and not target.endswith(".") 
            and " " not in target
            and ".." not in target
           
        ):
            return "domain"
    
        return None
    
    
def resolve_target(target, target_type):
    #resolve_target(target, target_type)
    if target_type == "ip" :
        return target
    try:
        resolved_ip = socket.gethostbyname(target)
        return resolved_ip
            
            
    except socket.gaierror:  #Get Address Info Error
        return None