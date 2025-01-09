import socket

def start_udp_client():
    host = '127.0.0.1'
    port = 5000

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(b"Hello, UDP!", (host, port))
        data, addr = s.recvfrom(1024)
        print(f"Received {data.decode()} from {addr}")

if __name__ == "__main__":
    start_udp_client()