# 🎙️ Transcriptor de Audio con Whisper (Interfaz Gráfica en Python)

> [!WARNING]  
> Chat GPT hizo esto, lo publico por que es bastante útil, pero yo sólo comprobé que funcionara cómo debía. No me responsabilizo de NADA ni me acredito su creación (la idea mía, el código de chat).

Este es un transcriptor de audio basado en [Whisper](https://github.com/openai/whisper), con una interfaz gráfica en Python usando `tkinter`. Permite seleccionar un archivo de audio, transcribirlo automáticamente y exportar el resultado como `.txt`, con o sin marcas de tiempo estilo YouTube.

---

## 🚀 Características

- Selección de archivos `.mp3`, `.wav`, `.ogg`, `.flac`, `.m4a`
- Transcripción automática usando el modelo Whisper de OpenAI
- Exportación opcional a `.txt`
- Inclusión opcional de timestamps (`[HH:MM:SS]`)
- Interfaz gráfica amigable
- Sin bloqueos ("not responding") gracias a ejecución en segundo plano

---

## 📸 Captura de pantalla

> *(Puedes incluir una imagen aquí de la GUI si quieres)*

---

## 🧰 Requisitos

- Python 3.8 o superior
- [FFmpeg](https://ffmpeg.org/)
- Conexión a internet (para descargar el modelo)

---

## 🔧 Instalación

### 1. Instalar Python

Descarga e instala Python desde [https://www.python.org/downloads/](https://www.python.org/downloads/), marcando la opción **"Add Python to PATH"** durante la instalación.

---

### 2. Instalar FFmpeg

Whisper depende de FFmpeg para leer y convertir archivos de audio.

#### Pasos:

1. Ve a [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
2. Descarga `ffmpeg-release-essentials.zip`
3. Extrae el contenido en `C:\ffmpeg`
4. Agrega `C:\ffmpeg\bin` a tu variable de entorno `PATH`:
   - Busca “Editar las variables de entorno del sistema”
   - Haz clic en “Variables de entorno”
   - Edita `Path` en Variables del sistema
   - Agrega: `C:\ffmpeg\bin`
   - Acepta y reinicia tu PC o consola

Para verificar:

```bash
ffmpeg -version
```

---

### 3. Instalar las dependencias en Python

Si vas a ejecutar el script directamente con Python, asegúrate de instalar también los siguientes paquetes necesarios:

```bash
pip install git+https://github.com/openai/whisper.git
pip install torch
pip install numpy
pip install tqdm
```

```bash
pip install git+https://github.com/openai/whisper.git
```

> `tkinter` ya viene con la mayoría de instalaciones de Python. Si no, instala con:

```bash
pip install tk
```

---

## ▶️ Uso

Guarda el script como `transcriptor_gui.py` y ejecútalo desde la terminal:

```bash
python transcriptor_gui.py
```

### Funcionalidades:

1. Selecciona uno o más archivos de audio.
2. Elige el idioma o deja la opción en “auto”.
3. (Opcional) Activa “Exportar a archivo .txt”.
4. (Opcional) Marca “Incluir timestamps” para subtítulos o sincronización estilo YouTube.
5. Elige carpeta de salida si vas a exportar.
6. Haz clic en “Iniciar transcripción”.
7. La transcripción aparecerá en la ventana y, si lo elegiste, se guardará en la carpeta seleccionada.

---

## ⌛ Ejemplo de salida con timestamps

```
[00:00:01] Hola, esta es una prueba de transcripción.
[00:00:05] Continuamos con el siguiente segmento.
```

---

## ❓ Preguntas frecuentes

### ¿Siempre usa español?

Por defecto, no. Puedes dejar el idioma en “auto” para detección automática o elegir el idioma deseado manualmente desde la interfaz.

---

### ¿Puedo usar otros idiomas?

Sí, Whisper soporta más de 90 idiomas. Puedes seleccionar el idioma desde el menú desplegable de la aplicación.

---

## 🛠️ Solución de problemas

| Problema                         | Solución                                                                 |
|----------------------------------|--------------------------------------------------------------------------|
| La ventana dice *"not responding"* | Usa la versión con `threading`, ya incluida.                            |
| Error de FFmpeg                  | Asegúrate de haber agregado `C:\ffmpeg\bin` al PATH del sistema.       |
| No se abre la app                | Verifica que tengas Python instalado y ejecuta desde terminal con `python`. |
| Transcripción vacía              | Usa un audio claro, sin silencios, y de buena calidad.                   |

---

## ✨ Créditos

Desarrollado completamente por **ChatGPT de OpenAI** a solicitud del usuario.

El modelo de transcripción de voz es proporcionado por **[OpenAI Whisper](https://github.com/openai/whisper)**.
