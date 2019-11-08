# Importa o OpenCV2
import cv2

# Define qual webcam será usada
vid_cam = cv2.VideoCapture(0)

# Informa o que deve ser procurado na tela usando o Haarcascade
face_detector = cv2.CascadeClassifier('Modelo_XML/haarcascade_frontalface_default.xml')

# Para cada rosto crie um novo ID
face_id = 4

# Contador de rostos
count = 0

# Inicia o looping infinito para capturar frames
while(True):

    # Captura o frame do video
    _, image_frame = vid_cam.read()

    # Converte o frame do video em escala de cinza
    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

    # Detecta os frames de diferentes tamanhos, list of faces rectangles
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    # Looping para cada rosto detectado
    for (x, y, w, h) in faces:

        # Incrementa +1 no contador de frames
        count += 1

        # Gera um Baunding Box ao redor da face
        cv2.rectangle(image_frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        Texto = 'Analisando', count, '%'
        print(Texto)
        cv2.putText(image_frame, str(Texto), (x, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 2)
        
        # Incrementa +1 no contador de frames
        #count += 1

        # Salva o frame com rosto detectado dentro da pasta Faces_Usuario
        cv2.imwrite("Faces_Usuario/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        # Display the video frame, with bounded rectangle on the person's face
        cv2.imshow('Cadastrando Rosto', image_frame)

    # Para encerrar o detector apertar q
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

    # Quando 99 frames forem salvos o programa é encerrado
    elif count > 99:
        break

# Encerra o video
vid_cam.release()

# Encerra todas as janelas criadas
cv2.destroyAllWindows()
