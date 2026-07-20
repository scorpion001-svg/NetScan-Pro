from colors import SUCCESS_COLOR,ERROR_COLOR, RESET_COLOR
from services import get_service_name

def display_results(target, resolved_ip, scan_results, scan_time):
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
    
    if len(scan_results) == 0: #if not open_ports:
        print(f"{ERROR_COLOR}No open ports found.{RESET_COLOR}")
     
    else:   
        for result in scan_results:
            port = result["port"]
            state = result["state"]
            service = result["service"]

            print(f"{SUCCESS_COLOR}[+] Port {port:<5} {state:<6} {service}{RESET_COLOR}")
            
            if result["banner"] is not None:
                print(f"    Banner : {result['banner']}")
            
            print()
            
    
    
    print("=" * 50)
    print(f"{SUCCESS_COLOR}Scan completed in {scan_time:.2f} seconds.{RESET_COLOR}")
 