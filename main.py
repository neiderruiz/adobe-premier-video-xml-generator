import tkinter as tk
from tkinter import ttk, filedialog as fd, messagebox
import threading
from modules import actions
import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Convert Premier')
        self.iconbitmap('./assets/icon.ico')

        self.frm = ttk.Frame(self, padding=10, width=300, height=400)
        self.frm.grid()

        self.setup_styles()
        self.setup_widgets()

    def setup_styles(self):
        self.style = ttk.Style()
        self.style.configure(
            'TEntry',
            padding=[5, 2],
            font=('Arial', 12),
            fieldbackground='white',
            foreground='black',
            borderwidth=2,
            relief='solid',
            bordercolor='#ccc'
        )
        self.style.configure(
            'TButton',
            padding=[5, 5],
            font=('Arial', 12),
            relief='raised',
            borderwidth=2,
        )
        self.style.configure(
            'TLabel',
            font=('Arial', 12),
        )
        self.style.configure(
            'TLabelFrame',
            font=('Arial', 12, 'bold'),
            borderwidth=2,
            relief='solid',
        )

    def setup_widgets(self):
        self.nameProject_entry, _ = self.create_entry(
            self.frm, "Nombre del proyecto", 0, 0)
        self.select_file_btn = self.create_button(
            self.frm, "Select File", self.select_file, 2, 0)

        self.process_video_btn = self.create_button(
            self.frm, "Procesar Video", self.process_video, 3, 0)

        # Crear un LabelFrame para el grupo Miniatura
        self.miniature_frame = ttk.LabelFrame(
            self.frm, text="Miniatura", padding=(10, 5))
        self.miniature_frame.grid(
            column=0, row=4, padx=10, pady=10, sticky=(tk.W, tk.E))

        # Crear las entradas para el grupo Miniatura
        self.scale_var = tk.StringVar(value='25')
        self.scale_entry, self.scale_label = self.create_entry(
            self.miniature_frame, "Escala", 0, 0, validate=True, textvariable=self.scale_var)

        self.right_cut_percentage_var = tk.StringVar(value='0')
        self.right_cut_percentage_entry, _ = self.create_entry(
            self.miniature_frame, "Porcentaje de corte a la derecha", 1, 0, textvariable=self.right_cut_percentage_var)

        self.left_cut_percentage_var = tk.StringVar(value='50')
        self.left_cut_percentage_entry, _ = self.create_entry(
            self.miniature_frame, "Porcentaje de corte a la izquierda", 1, 1, textvariable=self.left_cut_percentage_var)

        self.vertical_position_var = tk.StringVar(value='0.354622')
        self.vertical_position_entry, _ = self.create_entry(
            self.miniature_frame, "Posición vertical miniatura", 2, 0, textvariable=self.vertical_position_var)

        self.horizontal_position_var = tk.StringVar(value='0.119977')
        self.horizontal_position_entry, _ = self.create_entry(
            self.miniature_frame, "Posición horizontal miniatura", 2, 1, textvariable=self.horizontal_position_var)

        self.hide_miniature_frame_and_button()

        self.file_label = ttk.Label(self.frm, text="")
        self.file_label.grid(column=0, row=5)

    def create_entry(self, parent, label_text, row, column, validate=False, textvariable=None):
        label = ttk.Label(parent, text=label_text)
        label.grid(column=column, row=row * 2)

        if validate:
            validate_command = self.register(self.validate_input)
            entry = ttk.Entry(parent, width=40, validate='key', validatecommand=(
                validate_command, '%P'), textvariable=textvariable)  # Cambié width a 40
        else:
            # Cambié width a 40
            entry = ttk.Entry(parent, width=40, textvariable=textvariable)

        entry.grid(column=column, row=row * 2 + 1)
        return entry, label  # Devuelve tanto la entrada como la etiqueta

    def create_button(self, parent, text, command, row, column):
        btn = ttk.Button(parent, text=text, command=command)
        btn.grid(column=column, row=row)
        return btn

    def select_file(self):
        filename = fd.askopenfilename(
            filetypes=[('videos', '*.mp4'), ('All files', '*.*')])
        if filename:  # Si un archivo fue seleccionado
            self.file_label.config(text=filename)
            self.show_miniature_frame_and_button()
        else:  # Si no se seleccionó ningún archivo (se presionó 'Cancelar')
            self.hide_miniature_frame_and_button()

    def process_video(self):
        new_video = self.file_label.cget("text")
        name_project = self.nameProject_entry.get()
        # Suponiendo que quieres mostrar el estado en la interfaz, podrías necesitar una etiqueta para mostrar esto
        loading = tk.StringVar()

        # Puedes crear una etiqueta para mostrar el estado de 'loading' si lo deseas
        loading_label = ttk.Label(self.frm, textvariable=loading)
        # Ajusta la fila y columna como necesites
        loading_label.grid(column=0, row=6)

        run_translate(
            new_video,
            name_project,
            loading,
            miniature={
                'scale': self.scale_var.get(),
                'right_cut_percentage': self.right_cut_percentage_var.get(),
                'left_cut_percentage': self.left_cut_percentage_var.get(),
                'vertical_position': self.vertical_position_var.get(),
                'horizontal_position': self.horizontal_position_var.get(),
            }
        )

    def validate_input(self, value_if_allowed):
        if value_if_allowed == '' or value_if_allowed.isdigit():
            return True
        return False

    def show_miniature_frame_and_button(self):
        self.miniature_frame.grid(
            column=0, row=4, padx=10, pady=10, sticky=(tk.W, tk.E))
        self.process_video_btn.grid(column=0, row=3)  # Muestra el botón

    def hide_miniature_frame_and_button(self):
        self.miniature_frame.grid_remove()
        self.process_video_btn.grid_remove()  # Oculta el botón


def run_translate(new_video: str, name_project: str, loading, miniature: dict = None):
    print(miniature)
    t = threading.Thread(target=actions.edit_video, args=(
        new_video,
        name_project,
        loading,
        miniature
    ))
    t.start()




if __name__ == "__main__":
    app = App()
    app.mainloop()
