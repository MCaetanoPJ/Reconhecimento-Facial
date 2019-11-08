# Importa o OpenCV2
import cv2

from datetime import date

# Numpy é usado em calculos
import numpy as np

# Gera um padrão binário para reconhecimento facial
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Carrega o treinamento facial
recognizer.read('Arquivo_Treinado/trainer.yml')

# Carrega o modelo de reconhecimento de face
cascadePath = "Modelo_XML/haarcascade_frontalface_default.xml"

# Inicia um classificado baseado em um modelo pronto
faceCascade = cv2.CascadeClassifier(cascadePath);

# Informa o estilo da fonte
font = cv2.FONT_HERSHEY_SIMPLEX

# Define a webcam que será usada
cam = cv2.VideoCapture(0)

count = 0

# Loop
while True:
    # Ler o frame do video
    ret, im =cam.read()

    # Converte o frame para escala de cinza
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    # Captura todas as faces dentro de um frame
    faces = faceCascade.detectMultiScale(gray, 1.2, 5)

    # Percorre todas as face dentro do frame
    for (x, y, w, h) in faces:

        count += 1

        # Reconhece o Rosto usando o Id deninido no inicio
        Id, conf = recognizer.predict(gray[y:y + h, x:x + w])

        def Bauding_Box(): #Metodo responsavel por gerar os retangulos ao encontrar um usuario
            cv2.rectangle(im, (x - 20, y - 20), (x + w + 20, y + h + 20), (0, 255, 0), 4)  # Retangulo do nome Verde
            cv2.rectangle(im, (x - 22, y - 90), (x + w + 22, y - 22), (0, 255, 0), -1)  # Retangulo do rosto verde

        #Define o nivel de confiança para informar o nome do rosto
        nvl_conf_min = 70

        #Verifica se a confiança é suficiente
        if(conf < nvl_conf_min):
            if (Id == 1 or Id == 4):
                Nome = "Marcos"
                Id = "{} {:.2f}".format(Nome, conf)
                print("Bem vindo", Nome)
                Bauding_Box()

            elif (Id == 2):
                Nome = "Pai"
                Id = "{} {:.2f}".format(Nome, conf)
                print("Bem vindo", Nome)
                Bauding_Box()

            elif (Id == 3):
                Nome = "Sarah"
                Id = "{} {:.2f}".format(Nome, conf)
                print("Bem vindo", Nome)
                Bauding_Box()
        else:
            Nome = "Desconhecido"
            Id = "{} {:.2f}".format(Nome, conf)
            print("Invasor", Id)
            cv2.rectangle(im, (x - 20, y - 20), (x + w + 20, y + h + 20), (0, 0, 255), 4)  # Retangulo do rosto Vermelho
            #cv2.rectangle(im, (x - 22, y - 90), (x + w + 22, y - 22), (0, 0, 255), -1)  # Retangulo do nome Vermelho
            Texto = 'Capturas Faciais esta em', count, '%'
            print(Texto)

            #Capturas de tela feita dos rostos não reconhecidos
            cv2.imwrite("Faces_Anonimas/Capturas_Faciais/Usuario." + str(date.today()) + '.' + str(count) + ".jpg", im[y:y+h, x:x+w])
            cv2.imwrite("Faces_Anonimas/Print_Frame/Usuario." + str(date.today()) + '.' + str(count) + ".jpg", im)

        # Insere um texto na descrição ao redor do baunding box
        cv2.putText(im, str(Id), (x, y - 40), font, 1, (255, 255, 255), 2)

    # Mostra o video com o reconhimento ativado
    cv2.imshow('Reconhecimento Facial Ativado', im)

    # Se q for pressionado o sistema fecha
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Encerra a camera
cam.release()

# Fecha todas as janelas
cv2.destroyAllWindows()
