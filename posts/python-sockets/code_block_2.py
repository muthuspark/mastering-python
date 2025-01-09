import socket

def start_udp_server():
    host = '127.0.0.1'
    port = 5000

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        while True:
            data, addr = s.recvfrom(1024)
            print(f"Received {data.decode()} from {addr}")
            s.sendto(b"UDP Message Received", addr)

if __name__ == "__main__":
    start_udp_server()