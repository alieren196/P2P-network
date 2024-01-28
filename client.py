import socket

def start_client(buffer_size):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 12345

    try:
        client_socket.connect((host, port))
        print(f"Sunucuya bağlandı: {host}:{port}")


        welcome_message = client_socket.recv(1024).decode()
        print(f"Sunucudan gelen mesaj: {welcome_message}")

        client_socket.send(str(buffer_size).encode())

        with open("received_large_file.txt", "wb") as file:
            data = client_socket.recv(buffer_size)
            while data:
                file.write(data)
                data = client_socket.recv(buffer_size)

    except Exception as e:
        print(f"Hata oluştu: {e}")

    finally:
        client_socket.close()

if __name__ == "__main__":
    buffer_size = int(input("İstemci buffer boyutunu girin: "))
    start_client(buffer_size)
