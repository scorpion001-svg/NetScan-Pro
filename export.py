from colors import SUCCESS_COLOR,ERROR_COLOR, RESET_COLOR


def export_results(target, resolved_ip, scan_results):
    with open("results.txt", "w") as file:
        file.write("=" * 50 + "\n")
        file.write("NetScan Pro Results\n")
        file.write("=" * 50 + "\n\n")
        file.write(f"Target      : {target}\n")
        file.write(f"Resolved IP : {resolved_ip}\n\n")
        file.write("Open Ports\n")
        file.write("-" * 30 + "\n")
        
        if not scan_results:
            file.write("No open ports found.\n")
        
        else:
            for result in scan_results:
                port = result["port"]
                state = result["state"]
                service = result["service"]
                    
                file.write(f"[+] Port {port}\n")
                file.write(f"    State   : {state}\n")
                file.write(f"    Service : {service}\n")

                if result["server"] is not None:
                    file.write(f"    Server  : {result['server']}\n")

                file.write("\n")
                

                    
    return "results.txt"