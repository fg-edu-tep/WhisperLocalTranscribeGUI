import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
import whisper
import os
import threading

class WhisperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Transcriptor de Audio con Whisper")

        self.audio_paths = []
        self.output_path = ""
        self.languages = ["auto", "Spanish", "English", "French", "German", "Portuguese", "Italian", "Dutch", "Russian", "Japanese", "Korean"]

        # Archivo de audio
        self.audio_button = tk.Button(root, text="Seleccionar audio(s)", command=self.select_audio)
        self.audio_button.pack(pady=5)

        self.audio_label = tk.Label(root, text="Ningún archivo seleccionado")
        self.audio_label.pack()

        # Idioma
        tk.Label(root, text="Idioma de transcripción:").pack()
        self.language_var = tk.StringVar(value="auto")
        self.language_menu = ttk.Combobox(root, textvariable=self.language_var, values=self.languages, state="readonly")
        self.language_menu.pack()

        # Exportar y timestamps
        self.export_var = tk.BooleanVar()
        self.export_check = tk.Checkbutton(root, text="Exportar a archivo .txt", variable=self.export_var, command=self.toggle_output_path)
        self.export_check.pack()

        self.timestamps_var = tk.BooleanVar()
        self.timestamps_check = tk.Checkbutton(root, text="Incluir timestamps (estilo YouTube)", variable=self.timestamps_var)
        self.timestamps_check.pack()

        self.output_button = tk.Button(root, text="Seleccionar carpeta de salida", command=self.select_output, state="disabled")
        self.output_button.pack()

        self.output_label = tk.Label(root, text="Ruta de salida no seleccionada", fg="gray")
        self.output_label.pack()

        # Transcribir
        self.transcribe_button = tk.Button(root, text="Iniciar transcripción", command=self.start_transcription_thread)
        self.transcribe_button.pack(pady=10)

        # Salida
        self.output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=15, width=80)
        self.output_text.pack(padx=10, pady=10)

    def select_audio(self):
        paths = filedialog.askopenfilenames(filetypes=[("Audio Files", "*.mp3 *.wav *.ogg *.m4a *.flac")])
        if paths:
            self.audio_paths = paths
            self.audio_label.config(text=f"{len(paths)} archivo(s) seleccionado(s)")

    def toggle_output_path(self):
        if self.export_var.get():
            self.output_button.config(state="normal")
            self.output_label.config(fg="black")
        else:
            self.output_button.config(state="disabled")
            self.output_label.config(fg="gray")

    def select_output(self):
        path = filedialog.askdirectory()
        if path:
            self.output_path = path
            self.output_label.config(text=f"Salida: {path}")

    def start_transcription_thread(self):
        thread = threading.Thread(target=self.transcribe)
        thread.start()

    def transcribe(self):
        if not self.audio_paths:
            messagebox.showerror("Error", "Selecciona al menos un archivo de audio.")
            return

        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, "Transcribiendo...\n")
        self.transcribe_button.config(state="disabled")
        self.root.update()

        try:
            model = whisper.load_model("base")
            lang = self.language_var.get()
            lang_arg = None if lang == "auto" else lang.lower()

            for audio_path in self.audio_paths:
                self.output_text.insert(tk.END, f"Procesando: {os.path.basename(audio_path)}\n")
                result = model.transcribe(audio_path, language=lang_arg, verbose=False)
                transcription = ""

                if self.timestamps_var.get():
                    for seg in result['segments']:
                        start = self.format_time(seg['start'])
                        transcription += f"[{start}] {seg['text'].strip()}\n"
                else:
                    transcription = result["text"]

                self.output_text.insert(tk.END, transcription + "\n")

                if self.export_var.get() and self.output_path:
                    filename_base = os.path.splitext(os.path.basename(audio_path))[0]
                    suffix = "_timestamps" if self.timestamps_var.get() else ""
                    file_name = f"{filename_base}{suffix}.txt"
                    full_path = os.path.join(self.output_path, file_name)
                    with open(full_path, "w", encoding="utf-8") as f:
                        f.write(transcription)

            if self.export_var.get():
                messagebox.showinfo("Éxito", "Todos los archivos han sido exportados.")

        except Exception as e:
            self.output_text.insert(tk.END, f"{str(e)}\n")

        self.transcribe_button.config(state="normal")

    def format_time(self, seconds):
        h = int(seconds // 3600)
        m = int((seconds % 3600) // 60)
        s = int(seconds % 60)
        return f"{h:02}:{m:02}:{s:02}"

if __name__ == "__main__":
    root = tk.Tk()
    app = WhisperApp(root)
    root.mainloop()
