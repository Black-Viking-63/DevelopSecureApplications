# Лабораторная работа по курсу<br>"Проектирование распределенных защищенных приложений"
 Лабораторная работа №1: "Клиент серверная архитектура"

Лабораторная работа содержит 3 файла скрипта:<br>
client.py - клиент, который производит отправку изображения.<br>
proxy.py - промежуточный клиент-сервер, осуществялющй "перехват изображения" и его искажение при помощи шума Salt & Paper.<br>
server.py - основной сервер, осуществляющий прием изображения и его восстановление.<br>


# Изображения, полученные в результате работы программы
| Original Image |  Noise on Proxy_Server | Denoise on Server | 
|:----:|:----:|:----:|
|![Screenshot](image/original.jpg) | ![Screenshot](image/proxy/image_noise_sp_on_proxy.jpg) | ![Screenshot](image/server/denoised_on_server.jpg) | 
|![Screenshot](image/original1.jpg) | ![Screenshot](image/proxy/image_noise_sp_on_proxy1.jpg) | ![Screenshot](image/server/denoised_on_server1.jpg) | 
|![Screenshot](image/original2.jpg) | ![Screenshot](image/proxy/image_noise_sp_on_proxy2.jpg) | ![Screenshot](image/server/denoised_on_server2.jpg) | 
|![Screenshot](image/original3.jpg) | ![Screenshot](image/proxy/image_noise_sp_on_proxy3.jpg) | ![Screenshot](image/server/denoised_on_server3.jpg) | 


# Результаты
В результате работы программы, испорченное изображение промежуточным сервером, было частично восстановлено основным.
