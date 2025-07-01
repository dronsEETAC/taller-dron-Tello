# instalar opencv-python, numpy, ultralytics, torch y seaborn

import cv2
import torch
import time



# Cargar el modelo YOLOv5 preentrenado de Ultralytics
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
for class_id, class_name in model.names.items():
    print(f"{class_id} → {class_name}")
model.eval()

# Clase COCO para banana es la 46

BANANA_CLASS_ID = 46
CARROT_CLASS_ID = 51
DONUT_CLASS_ID = 54
FORK_CLASS_ID = 42
CLOCK_CLASS_ID = 74

# Inicializar la captura de video desde webcam (índice 0) o usa un archivo con 'video.mp4'
cap = cv2.VideoCapture(0)

end = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir frame a RGB para YOLO
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Inferencia con el modelo
    results = model(img_rgb)

    # Procesar resultados
    for *box, conf, cls in results.xyxy[0]:
        if int(cls.item()) == BANANA_CLASS_ID:
            x1, y1, x2, y2 = map(int, box)
            label = f"Banana {conf:.2f}"
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            print ("BANANA")
        elif int(cls.item()) == CLOCK_CLASS_ID:
            x1, y1, x2, y2 = map(int, box)
            label = f"Clock {conf:.2f}"
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            print ("RELOJ")
        elif int(cls.item()) == DONUT_CLASS_ID:
            x1, y1, x2, y2 = map(int, box)
            label = f"Donut {conf:.2f}"
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            print ("DONUT")
        elif int(cls.item()) == CARROT_CLASS_ID:
            x1, y1, x2, y2 = map(int, box)
            label = f"Carrot {conf:.2f}"
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            print ("Zanahoria")
        elif int(cls.item()) == FORK_CLASS_ID:
            x1, y1, x2, y2 = map(int, box)
            label = f"Fork {conf:.2f}"
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            print ("TENEDOR")
            end = True


    # Mostrar el frame con detecciones
    cv2.imshow("Detector de objetos", frame)

    # Salir con tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if end:
        break

cap.release()
cv2.destroyAllWindows()
