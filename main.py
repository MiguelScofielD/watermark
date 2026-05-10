from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

window = Tk()
window.title("Watermark")
window.minsize(width=400, height=200)

filename = ""
watermark_filename = ""

label = Label(text="Adicione a sua marca d'água", font=("Arial", 12, "bold"))
label.pack()

image_label = Label()
image_label.pack()

image_watermark_label = Label()
image_watermark_label.pack(pady=5)


def upload_image():
    global filename

    filename = askopenfilename()

    if not filename:
        return

    image = Image.open(filename)

    image.thumbnail((300, 300))

    image_tk = ImageTk.PhotoImage(image)

    image_label.config(image=image_tk)
    image_label.image = image_tk


def upload_watermark():
    global watermark_filename

    watermark_filename = askopenfilename()

    if not watermark_filename:
        return

    watermark = Image.open(watermark_filename)

    watermark.thumbnail((300, 300))

    watermark_tk = ImageTk.PhotoImage(watermark)

    image_watermark_label.config(image=watermark_tk)
    image_watermark_label.image = watermark_tk


def add_watermark():
    if filename and watermark_filename:

        image = Image.open(filename).convert("RGBA")

        watermark = Image.open(watermark_filename).convert("RGBA")

        # tamanho proporcional
        new_width = int(image.width * 0.30)

        ratio = new_width / watermark.width

        new_height = int(watermark.height * ratio)

        watermark = watermark.resize((new_width, new_height))

        # posição inferior direita
        x = image.width - watermark.width - 10
        y = image.height - watermark.height - 10

        image.paste(watermark, (x, y), watermark)

        output_filename = f"watermarked_{filename.split('/')[-1]}"

        if output_filename.endswith(".jpg") or output_filename.endswith(".jpeg"):
            image = image.convert("RGB")  # Converter para RGB antes de salvar como JPEG

        image.save(output_filename)

        label.config(text="Marca d'água adicionada com sucesso!")

        # abre a imagem automaticamente
        image.show()

    else:
        label.config(text="Por favor, faça upload de uma imagem primeiro.")


button = Button(text="Upload Image", command=upload_image)
button.pack()

watermark_button = Button(text="Upload Watermark", command=upload_watermark)
watermark_button.pack(pady=10)

execute_button = Button(text="Add Watermark", command=add_watermark)
execute_button.pack()

window.mainloop()
