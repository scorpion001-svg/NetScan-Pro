from colors import SUCCESS_COLOR,ERROR_COLOR, RESET_COLOR
def display_results(target, resolved_ip, open_ports):
    header = """
    ==================================================
                NetScan Pro Results
    ==================================================
    """
    print(header)
   
    print("Target      :", target)
    print("Resolved IP :", resolved_ip)
    
    
    print("\nOpen Ports")
    print("-" * 30)
    
    if len(open_ports) == 0: #if not open_ports:
        print(f"{ERROR_COLOR}No open ports found.{RESET_COLOR}")
     
    else:   
        for port in open_ports:
            print(f"{SUCCESS_COLOR}[+] Port {port} OPEN{RESET_COLOR}")
    
    
    print("=" * 50)
    print(f"{SUCCESS_COLOR}Scan Completed.{RESET_COLOR}")
 