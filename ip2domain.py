import socket

def get_domain_name():
    try:
        # Take user input for the IP address
        ip_address = input("Enter the IP address: ")
        
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout for the socket connection
        sock.settimeout(2)
        
        # Reverse the IP address and append ".in-addr.arpa" to form the PTR record
        reversed_ip = ".".join(reversed(ip_address.split(".")))
        ptr_record = f"{reversed_ip}.in-addr.arpa"
        
        # Use the socket object to establish a connection with the DNS server
        sock.connect(('8.8.8.8', 53))
        
        # Send a DNS request for PTR record to the DNS server
        sock.sendall(bytes(f"PTR {ptr_record}\r\n", 'utf-8'))
        
        # Receive the response from the DNS server
        response = sock.recv(4096).decode('utf-8')
        
        # Parse the response to extract the domain name
        domain_name = response.split()[-1].strip('.')
        
        return domain_name
    except socket.timeout:
        return "Timeout occurred while connecting to DNS server"
    except socket.error as e:
        return f"Socket error: {e}"
      
domain_name = get_domain_name()
print(f"The domain name is: {domain_name}")
