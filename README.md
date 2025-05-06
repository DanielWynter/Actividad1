# 📷 Detección de Texto en Placas Vehiculares

Este proyecto utiliza **OpenCV** y **EasyOCR** para procesar imágenes de placas vehiculares, aplicar filtros para aislar el texto y extraerlo utilizando reconocimiento óptico de caracteres (OCR).

## 🚀 Tecnologías utilizadas

- Python 3
- OpenCV (`cv2`)
- EasyOCR
- NumPy

## 🖼️ Funcionalidad

1. Carga imágenes de placas (`placa.jpg`, `placa2.jpg`).
2. Convierte las imágenes al espacio de color HSV.
3. Filtra el color negro mediante máscaras HSV.
4. Aplica filtro de mediana para suavizar la imagen.
5. Guarda imágenes filtradas (`placa_filtrada.jpg`, `placa_filtrada2.jpg`).
6. Utiliza EasyOCR para extraer texto de las imágenes filtradas.
7. Dibuja los resultados sobre las imágenes originales y los muestra en pantalla.

## 🗂️ Estructura de archivos

