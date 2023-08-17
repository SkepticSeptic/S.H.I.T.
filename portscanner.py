import sys
import socket
from datetime import datetime
from multiprocessing import Pool, cpu_count
import color

def scan(target_port):
    target, port = target_port
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(color.success("PORT {} IS OPEN".format(port)))
        else:
            print(color.error("no response from port " + str(port)))
        s.close()
    except Exception as e:
        print(f"Error: {e}")

def main():
    first = 20 #port range to scan from 20
    last = 1023 #to 1023, which are the most common-ish ports

    target = socket.gethostbyname(input(color.progress("IP to scan: ")))
    specifyports = input(color.warning("Specify ports? (y/n)"))
    if specifyports.lower() == "y":
        rangeOrSpecific = input(color.warning("Specify port range or list of ports to try? (r or l)"))
        
        if rangeOrSpecific.lower() == "r":
            first = int(input("check from port: "))
            last = int(input("to port: "))
        elif rangeOrSpecific.lower() == "l":
            print("Feature not implemented yet")

    print("-" * 50)
    print("Scanning Target: " + target)
    print("Scanning started at:" + str(datetime.now()))
    print("-" * 50)

    try:
        # Utilize all available CPUs
        pool = Pool(processes=cpu_count())
        # Create target-port pairs for each port in the range and scan
        target_ports = [(target, port) for port in range(first, last+1)]
        pool.map(scan, target_ports)

    except KeyboardInterrupt:
        print("\n Exiting Program !!!!")
        sys.exit()
    except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
    except socket.error:
        print("\ Server not responding !!!!")
        sys.exit()

if __name__ == '__main__':
    main()
