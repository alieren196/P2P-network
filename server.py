import socket

def start_server(buffer_size):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 12345

    try:
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Sunucu {host}:{port} üzerinde dinleniyor...")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"{client_address} adresinden bir istemci bağlandı.")

            # İstemciye hoş geldin mesajı gönder
            welcome_message = "Bağlantı başarıyla kuruldu. Hoş geldin!"
            client_socket.send(welcome_message.encode())

            # Büyük veri gönderimi
            with open("large_file.txt", "rb") as file:
                data = file.read(buffer_size)
                while data:
                    client_socket.send(data)
                    data = file.read(buffer_size)

    except Exception as e:
        print(f"Hata oluştu: {e}")

    finally:
        server_socket.close()

if __name__ == "__main__":
    buffer_size = int(input("Sunucu buffer boyutunu girin: "))
    start_server(buffer_size)
