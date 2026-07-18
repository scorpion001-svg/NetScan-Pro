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
        print("No open ports found.")
     
    else:   
        for port in open_ports:
            print(f"[+] Port {port} OPEN")
    
    
    print("=" * 50)
    print("Scan Completed.")