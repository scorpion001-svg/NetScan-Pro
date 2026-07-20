from utils import show_banner
from utils import get_target
from utils import validate_target
from utils import resolve_target
from scanner import scan_ports
from scanner import get_scan_mode
from display import display_results
from colorama import init
from colors import ERROR_COLOR, RESET_COLOR, SUCCESS_COLOR
import time
from export import export_results
from analyzer import grab_banner



def main():
    init()
    
    show_banner()

    target = get_target()

    target_type = validate_target(target)

    if target_type is None:
        print(f"{ERROR_COLOR}[ERROR] Invalid target.{RESET_COLOR}")
        return
    
    resolved_ip = resolve_target(target, target_type)
    if resolved_ip is None:
        print(f"{ERROR_COLOR}[ERROR] Unable to resolve target.{RESET_COLOR}")
        return 
    
    
    start_port, end_port = get_scan_mode()

    start_time = time.time()
    scan_results = scan_ports(resolved_ip, start_port, end_port)
    end_time = time.time()
    scan_time = end_time - start_time
    
    for result in scan_results:
        banner = grab_banner(target, resolved_ip, result["port"])
        result["server"] = banner

    display_results(target, resolved_ip, scan_results, scan_time, start_port,end_port)
     

    
    saved_file = export_results(target, resolved_ip, scan_results)
    print(f"{SUCCESS_COLOR}Results saved to {saved_file}{RESET_COLOR}")


if __name__ == "__main__":
    main()