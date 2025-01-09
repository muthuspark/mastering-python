import socket

def start_server():
    host = '127.0.0.1'  # localhost
    port = 65432        # Port to listen on (non-privileged ports are > 1023)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print('Received:', data.decode())
                conn.sendall(b'Message received')

if __name__ == "__main__":
    start_server()
