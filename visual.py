import tkinter as tk
from PIL import Image, ImageTk
import cv2
import imutils
from PIL import Image as Img
from PIL import ImageTk
import os 
import subprocess



print("Libreria Leidas...")
## Detección de emociones en tiempo real ##
## SISTEMAS INTELIGENTES ##
## https://www.youtube.com/channel/UCr_dJOULDvSXMHA1PSHy2rg
## David Revelo Luna

# Import de librerias
from tensorflow.keras.applications.imagenet_utils import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import imutils
import cv2
import time


# Tipos de emociones del detector
classes = ['concentrado','dormido','disgustado','dormido','enojado','feliz','triste']
# Cargamos el  modelo de detección de rostros
prototxtPath = r"face_detector\deploy.prototxt"
weightsPath = r"face_detector\res10_300x300_ssd_iter_140000.caffemodel"
faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)

# Carga el detector de clasificación de emociones
emotionModel = load_model("modelFEC.h5")
# Variables para calcular FPS
time_actualframe = 0
time_prevframe = 0


#Colores
fondo_entrar = "#7952B3"
fondo_salir = "#FF1616"
fondo_correcto = "#8C52FF"
fondo_incorrecto = "#FF5757"
fondo_entrada = "#FFFFFF"

ventana = tk.Tk()
ventana.title("MENU")
ventana. geometry("1000x680+200+10")
ventana.resizable(width=False, height=False)
fondo = tk.PhotoImage(file="fondito.png")
fondo1 = tk.Label(ventana, image=fondo).place(x=0, y=0, relwidth=1, relheight=1)
video = None
def video_stream():
        global video
        video = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        iniciar()

        




def iniciar():
         subprocess.call(["python",r"C:\Users\50766\Desktop\FaceEmotionVideo.py"])   
         subprocess.release()
            



def quitar():

 iniciar()

          



       
# creating a button instance 




 #botones
boton = tk.Button(ventana, text="Iniciar Video", bg=fondo_entrar,relief="flat", cursor="hand2",command=video_stream,width=15, height=2, font=("Calisco MT", 12, "bold"))

boton.place(x=200, y=590)

boton2 = tk.Button(ventana, text="Quitar Video", bg=fondo_entrar,relief="flat", cursor="hand2",command=quitar,width=15, height=2, font=("Calisco MT", 12, "bold"))

boton2.place(x=640, y=590)


#Etiqueta
etiq_de_video = tk.Label(ventana, bg="black")
etiq_de_video.place(x=187, y=75)


ventana.mainloop()

    
