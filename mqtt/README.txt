SERVIDOR MQTT COM PYTHON
Utilizando um programa externo para enviar mensagens via MQTT para essa aplicação. Ela por sua vez converte a mensagem em voz e a executa. Existem duas threads aí. Uma para ouvir o canal e converter o texto e outra para ficar executando o arquivo de mp3. 

Programa cliente utilizado: MQTTlens
Connection name: Eclipse MQTT
hostname: mqtt.eclipse.org
tópico: pythonTodoDia

**Cuidado com o nome do tópico. Se for igual ao de outra aplicação em alguma parte do mundo, significa que você vai mandar mensagens para ela.

BIBLIOTECAS:
pip install paho-mqtt
pip install gTTS
