import socket

def port_scan(host, start_port, end_port):
    print(f"Scanning {host} from port {start_port} to {end_port}...\n")
    
    for port in range(start_port, end_port + 1):
        try:
            # Create a socket object
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Set a timeout for the connection attempt
            
            # Attempt to connect to the port
            result = sock.connect_ex((host, port))
            
            if result == 0:
                print(f"Port {port}: Open")
            else:
                print(f"Port {port}: Closed")
            
            # Close the socket
            sock.close()
        
        except KeyboardInterrupt:
            print("\nScan interrupted by user.")
            break
        except socket.error:
            print(f"Could not connect to {host}:{port}")

if __name__ == "__main__":
    target_host = input("Enter the target host (e.g., '127.0.0.1'): ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))

    port_scan(target_host, start_port, end_port)
