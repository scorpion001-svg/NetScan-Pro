from colors import SUCCESS_COLOR,ERROR_COLOR, RESET_COLOR, INFO_COLOR, VALUE_COLOR, WARNING_COLOR


def display_results(target, resolved_ip, scan_results, scan_time, start_port, end_port):
    print(f"{INFO_COLOR}{'='*50}")
    print("              NetScan Pro Results")
    print(f"{'='*50}{RESET_COLOR}\n")
   
    print(f"{INFO_COLOR}Target      : {VALUE_COLOR}{target}{RESET_COLOR}")
    print(f"{INFO_COLOR}Resolved IP : {VALUE_COLOR}{resolved_ip}{RESET_COLOR}")
    
    
    print(f"\n{INFO_COLOR}Open Ports ({len(scan_results)}){RESET_COLOR}")
    print("-"*50)
    
    if len(scan_results) == 0: #if not open_ports:
        print(f"{WARNING_COLOR}No open ports were detected.{RESET_COLOR}")
     
    else:   
        for result in scan_results:
            port = result["port"]
            state = result["state"]
            service = result["service"]

            print(f"{SUCCESS_COLOR}[+] Port {port}{RESET_COLOR}")

            print(f"    State   : {state}")
            print(f"    Service : {service}")

            if result["server"]:
                print(f"    Server  : {result['server']}")

            print()
            
    
    
    print("=" * 50)
    print(f"{SUCCESS_COLOR}Scan completed in {scan_time:.2f} seconds.{RESET_COLOR}")
    
    print(f"{INFO_COLOR}{'='*50}")

    print("Scan Summary")

    print(f"{'='*50}{RESET_COLOR}")

    print(f"Ports Scanned : {start_port} - {end_port}")
    print(f"Open Ports    : {len(scan_results)}")
    print(f"Scan Time     : {scan_time:.2f} sec\n")
 