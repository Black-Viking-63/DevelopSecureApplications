import socket
import numpy as np
import random
import cv2

proxy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IP, SOCK_STREAM = TCP        # создадим сокет для промежуточного сервера
proxy.bind(('localhost', 8081))                                                                     # определим адрес и порт для сокета промежуточного сервера в данном случае он будет 127.0.0.1:8081
proxy.listen()                                                                                      # поставим промежуточный сервер на прослушку
client_socket, client_address = proxy.accept()                                                      # установка параметров соединения с клиентом

file = open('image\\proxy\\recv_original_image_proxy.jpg', "wb")                                    # открываем файл для записи изображения перехваченного с клиента
image_chunk = client_socket.recv(2048)                                                              # принимаем изображение по частям
while image_chunk:
    file.write(image_chunk)
    image_chunk = client_socket.recv(2048)
    if not image_chunk:
        break
file.close()
client_socket.close()
def sp_noise(image, prob):                                                                          # нанесение шума на изображение
    output = np.zeros(image.shape, np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

image_original = cv2.imread('image\\proxy\\recv_original_image_proxy.jpg')                          # откроем полученное изображение
noise_img = sp_noise(image_original, 0.05)                                                          # произведем наложение шума на изображение
cv2.imwrite('image\\proxy\\image_noise_sp_on_proxy.jpg', noise_img)                                 # запишем полученное изображение
client_socket.close()                                                                               # закроем сокет для сообщения с клиентом
proxy2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                                          # откроем сокет для связи с основным сервером
proxy2.connect(("127.0.0.1", 8080))
file = open('image\\proxy\\recv_original_image_proxy.jpg', mode="rb")                               # считываем картинку и отправляем картинку
image_chunk = file.read(2048)
while image_chunk:
    proxy2.send(image_chunk)
    image_chunk = file.read(2048)
file.close()
proxy2.close()
