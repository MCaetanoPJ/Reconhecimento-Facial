# Reconhecimento-Facial
Reconhecimento Facial usando OpenCV e Haar Cascade

Notas Importantes a respeito da lógica e funcionamento desse reconhecedor Facial:

Este Documento se refere a Pasta Versão_0.2

Siga as etapas na ordem sendo:
(1)Detector_Facial.py
(2)Treinamento.py
(3)Reconhecimento_Facial.py


#(1)Detector_Facial.py
Esse arquivo é responsável por detectar que existe uma face no frame capturado do video
e aplicar a escala de cinza, logo após redimensionar para salvar apenas a imagem dentro do
Baunding Box

-No total são capturadas 100 imagens, que são salvas dentro da pasta "Faces_Usuario", com o
nome "User...", todas as 100 imagem pertencem a um mesmo usuário, que é reconhecido por um Id
definido dentro do código pela váriavel "face_id"

- A variavel "face_detector" é responsável por informar o modelo de reconhecimento Haarcascade
será usado, sendo que atualmente está definido como um reconhecedor de faces, onde qualquer rosto
dentro do frame será capturado

#(2)Treinamento.py
Esse arquivo possui a função de mapear todos as faces dos usuários cadastrados anteriormente
, o arquivo gerado possui a extensão ".yml", com o nome de "trainer" e se envontra dentro
da pasta "Arquivo_Treinado", apenas é necessário executar este arquivo para iniciar o treinamento


#(3)Reconhecimento_Facial.py
Esse arquivo é considerado o principal, pois é onde de fato ocorre o reconhecimento facial,
a váriavel "recognizer" com o método "read", fazem a leitura do arquivo com o treinamento realizado
na etapa anterior

            recognizer.read('Arquivo_Treinado/trainer.yml')

-a váriavel "cascadePath" recebe o arquivo XML com o modelo para detecção de faces dentro do frame
que já está treinado

            cascadePath = "Modelo_XML/haarcascade_frontalface_default.xml"

-A váriavel "Id" possui o id do usuário que foi atribuida uma por usuário na primeira etapa,

-A váriavel "conf" possui a confiança de que o usuário cadastrado e o usuário detectado são os mesmos

            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])

-O método criado "Bauding_Box()" é chamado somente dentro do IF ao detectar algum rosto cadastrado, sua função é gerar um retangulo ao redor do rosto na cor Verde e gerar um segundo retangulo acima deste para inserir o nome desete usuário identificado, esse nome foi definido dentro do IF com a variavel "Nome"

            def Bauding_Box(): #Metodo responsavel por gerar os retangulos ao encontrar um usuario
                cv2.rectangle(im, (x - 20, y - 20), (x + w + 20, y + h + 20), (0, 255, 0), 4)  # Retangulo do nome Verde
                cv2.rectangle(im, (x - 22, y - 90), (x + w + 22, y - 22), (0, 255, 0), -1)  # Retangulo do rosto verde

-A váriavel "nvl_conf_min" informa a confiança minima para entrar dentro do IF
Obs: Recomendo deixar a confiança em 70

-Note que da linha 56 até a linha 73 existem alguns IFs, eles são necessário para validar a
confiança, e validar o Id recebido com o nome do Usuário que será exibido na tela, ao ser detectado,

-O nome do rosto detectado deve ser inserido dentro do IF, da seguinte forma

            elif (Id == 2):
                Nome = "Pai"
                Id = "{} {:.2f}".format(Nome, conf)
                print("Bem vindo", Nome)
                Bauding_Box()


Obs: caso nenhum rosto seja reconhecido, terá a palavra "Desconhecido", acima do baunding box (Retângulo)
inserida com o nivel de confiança na frente do nome, neste caso o baunding box terá a cor vermelha com as letras brancas do nome e confiança

Nome = "Desconhecido"
            Id = "{} {:.2f}".format(Nome, conf)
            print("Invasor", Id)
            cv2.rectangle(im, (x - 20, y - 20), (x + w + 20, y + h + 20), (0, 0, 255), 4)  # Retangulo do rosto Vermelho
            cv2.rectangle(im, (x - 22, y - 90), (x + w + 22, y - 22), (0, 0, 255), -1)  # Retangulo do nome Vermelho

Outra função caso não identifique a pessoa, é tirar prints (capturas de tela) do momento em que detectou o rosto desconhecido, essas imagens capturadas são armazenadas no diretório "Faces_Anonimas\Print_Frame"

	cv2.imwrite("Faces_Anonimas/Print_Frame/Usuario." + str(date.today()) + '.' + str(count) + ".jpg", im)

além de tirar os prints, também é capturado somente o rosto não conhecido que foi capturado dentro do bauding box (Retangulo), para que o dono do sistema possa  analisar posteriormente, esses rostos estão no diretorio "Faces_Anonimas\Capturas_Faciais"

	cv2.imwrite("Faces_Anonimas/Capturas_Faciais/Usuario." + str(date.today()) + '.' + str(count) + ".jpg", im[y:y+h, x:x+w])

Ambas imagens capturadas são salvas com o formato "JPG" sendo o formato do nome "Usuario" seguido da data que foi capturada e o número do frame onde foi capturada
exemplo: Usuario.08-11-2019.25.jpg
Onde 25 é o número do frame





