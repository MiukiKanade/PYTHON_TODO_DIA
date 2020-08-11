#!/usr/bin/env python
# coding: utf-8

# In[2]:


#https://pypi.org/project/face-recognition/
#pip install pip install face-recognition
import face_recognition
import cv2
import numpy as np

# captura vídeo pela webcam
cap = cv2.VideoCapture(0)

# imagem com a face frontal de quem quer reconhecer
obama_image = face_recognition.load_image_file("obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# imagem com a face frontal de quem quer reconhecer
biden_image = face_recognition.load_image_file("biden.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

# lista com os códigos das faces
known_face_encodings = [
    obama_face_encoding,
    biden_face_encoding
]
# lista com o nome das faces
known_face_names = [
    "obama",
    "biden"
]

# algumas variáveis
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while cap.isOpened():
    # frame é a captura da webcam
    ret, frame = cap.read()
    # diminui o tamanho do vídeo para 1/4 para aumentar a velocidade de reconhecimento
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # converte a imagem rgb da opencv em rbg da face_recognition
    rgb_small_frame = small_frame[:, :, ::-1]

    # processa frame a frame da captura da web cam
    if process_this_frame:
        # encontra todas as faces do frame (e seus códigos)
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        #para cada face que está nas faces encontradas
        for face_encoding in face_encodings:
            # verifica se essa face é igual a que queremos achar
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            #Se uma correspondência foi encontrada em known_face_encodings, basta usar o primeiro.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Ou, em vez disso, use o rosto conhecido com a menor distância para o novo rosto
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    # mostra o resultado
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # dimensiona os frames
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # desenha um retângulo ao redor do rosto
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # desenha a caixa com legenda do nome da pessoa
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # mostra os resultados
    cv2.imshow('Video', frame)

    # pressione 'q' para parar o programa
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()


# In[ ]:




