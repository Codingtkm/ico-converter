from PIL import Image
png = Image.open("icon.png")
size = png.size
ico = Image.new(mode="RGBA", size=(max(size), max(size)), color=(0, 0, 0, 0))
ico.paste(png, (int((max(size)-size[0])/2), int((max(size)-size[1])/2)))
ico.save("icon.ico", format='ICO', quality=100)