import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IP, SOCK_STREAM = TCP
client.connect(('localhost', 8081))                                                                 # 127.0.0.1:8081
file = open('image\\original.jpg', 'rb')                                                            # открытие файла для отправки
image_chunk = file.read(2048)
while image_chunk:
    client.send(image_chunk)
    image_chunk = file.read(2048)
file.close()                                                                                        # закрытие файла
client.close()                                                                                      # закрытие сокета