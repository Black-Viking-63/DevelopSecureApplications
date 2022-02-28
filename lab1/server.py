import socket
import cv2
import logging
                                                            # basicConfig выполняет базовую настройку системы ведения журнала
logging.basicConfig(filename="logs\\server.log", level=logging.DEBUG, format="%(asctime)s - %(message)s")
                                                            # создадим сокет для сервера
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IP, SOCK_STREAM = TCP
server.bind(('localhost', 8080))                            # 127.0.0.1:8080
server.listen(10)                                           # поставим сервер на прослушку
logging.info("Ожидаем подключение...")                      # запишем лог-сообщение в файл с логами и одновременно выведем в консоль


def recChunk(namefile):
    file = open(namefile, "wb")
    image_chunk1 = client_socket.recv(2048)  # stream-based protocol
    # запись получаемых фрагментов изображения
    while image_chunk1:
        file.write(image_chunk1)
        image_chunk1 = client_socket.recv(2048)
        if not image_chunk1:
            break
    # по окончании записи изображения закроем файл
    file.close()

# В цикле будем производить обработку файла
while True:

    client_socket, client_address = server.accept()
    recChunk('image\\server\\recv_image_noise_on_server.jpg')                              # получение оригинального изображения


    logging.info("Изображения получены")                                                # сообщение о получении изображений

    image_with_noise = cv2.imread('image\\server\\recv_image_noise_on_server.jpg')

    logging.info("Идет восстановление изображения...")                                  # запишем лог-сообщение в файл с логами

    denoised_image = cv2.medianBlur(image_with_noise, 5)                                # для восстановления испорченного изображения используем медианный фильтр


    cv2.imwrite('image\\server\\denoised_on_server.jpg', denoised_image)                # запись восстановленного изображения


    logging.info("Изображение восстановлено")                                           # запишем лог-сообщение в файл с логами

client_socket.close()