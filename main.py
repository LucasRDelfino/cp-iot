import cv2
import mediapipe as mp
import math
import serial
import time

# Inicializa o MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_draw = mp.solutions.drawing_utils

# Configura a comunicação serial com o Arduino
# Substitua 'COM3' pela porta correta do seu Arduino
try:
    arduino = serial.Serial('COM3', 9600, timeout=1)
    time.sleep(2)  # Aguarda a conexão ser estabelecida
except serial.SerialException as e:
    print(f"Erro ao conectar ao Arduino: {e}")
    exit()

cap = cv2.VideoCapture("video.mp4")

frames_queda = 0
LIMIAR_QUEDA = 20  # Número de frames consecutivos para confirmar queda

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    altura_frame, largura_frame = frame.shape[:2]
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultados = pose.process(rgb)

    if resultados.pose_landmarks:
        mp_draw.draw_landmarks(frame, resultados.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        pontos = resultados.pose_landmarks.landmark

        ombro = pontos[mp_pose.PoseLandmark.LEFT_SHOULDER]
        quadril = pontos[mp_pose.PoseLandmark.LEFT_HIP]

        # Posição em pixels
        pos_y_quadril_px = quadril.y * altura_frame
        pos_y_ombro_px = ombro.y * altura_frame

        # Mostrar os valores
        cv2.putText(frame, f"Y Quadril: {int(pos_y_quadril_px)}", (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)
        cv2.putText(frame, f"Y Ombro: {int(pos_y_ombro_px)}", (10, 90),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)

        # Critério baseado no ombro
        if pos_y_ombro_px > 500:  # Ombro abaixo de 500 pixels indica queda
            frames_queda += 1
            if frames_queda > LIMIAR_QUEDA:
                cv2.putText(frame, "QUEDA DETECTADA!", (10, 130),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
                arduino.write(b'1')  # Envia 1 para o Arduino
            else:
                arduino.write(b'0')  # Envia 0 enquanto não confirma a queda
        else:
            frames_queda = 0
            arduino.write(b'0')  # Envia 0 quando não há queda

    cv2.imshow("Detecção de Queda", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Fecha a conexão com o Arduino e a captura de vídeo
arduino.close()
cap.release()
cv2.destroyAllWindows()