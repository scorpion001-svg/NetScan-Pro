from services import get_service_name
from colors import SUCCESS_COLOR,ERROR_COLOR, RESET_COLOR


def export_results(target, resolved_ip, open_ports):
    with open("results.txt", "w") as file:
        file.write("=" * 50 + "\n")
        file.write("NetScan Pro Results\n")
        file.write("=" * 50 + "\n\n")
        file.write(f"Target      : {target}\n")
        file.write(f"Resolved IP : {resolved_ip}\n\n")
        file.write("Open Ports\n")
        file.write("-" * 30 + "\n")
        
        if not open_ports:
            file.write("No open ports found.\n")
        
        else:
            for port in open_ports:
                service = get_service_name(port)
                file.write(f"[+] Port {port:<5} OPEN   {service}\n")
                    
    return "results.txt"