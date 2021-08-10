#!/usr/bin/python3

#I will maybe do a update for more filters or idk, also you can't put value like 1.3 1.4 I will do a update soon for edit it (if you want to edit it just read the src)

from PIL import Image, ImageOps, ImageEnhance, ImageDraw, ImageFilter
import os

begin = input("[1] Convert | [2] Fix Corrupted Image | [3] Edit Image\n[+] Make a choice: ")

os.system('cls' if os.name == 'nt' else 'clear')

def convert():
    filename = input("[?] Select the file: ")
    outputn = input("[?] Choose a name for the output file: ")
    choice = input("\n[1] PNG | [2] JPG | [3] WEBP | [4] GIF\n\n[+] Make a choice: ")
    if "1" in choice:
        im = Image.open(filename).convert("RGB")
        im.save(outputn, "png")
    elif "2" in choice:
        im = Image.open(filename).convert("RGB")
        im.save(outputn, "jpeg")
    elif "3" in choice:
        im = Image.open(filename).convert("RGB")
        im.save(outputn, "webp")
    elif "4" in choice:
        print("Soon")
    print("[!] Done")

if "1" in begin:
    convert()

def fci(): #https://en.wikipedia.org/wiki/List_of_file_signatures if you want to add more
    png = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])
    jpg = bytes([0xFF, 0xD8, 0xFF, 0xE0, 0x00, 0x10, 0x4A, 0x46, 0x49, 0x46, 0x00, 0X01])
    webp = bytes([0x52, 0x49, 0x46, 0x46, 0x2E, 0x7B, 0x34, 0x7D, 0x57, 0x45, 0x42, 0x50])
    gif87 = bytes([0x47, 0x49, 0x46, 0x38, 0x37, 0x61])
    gif89 = bytes([0x47, 0x49, 0x46, 0x38, 0x39, 0x61])
    mp4 = bytes([0x66, 0x74, 0x79, 0x70, 0x69, 0x73, 0x6F, 0x6D])
    filename = input("[!] Only work for bytes\n[?] Select the file: ")
    outputn = input("[?] Choose a name for the output file: ")
    choice = input("\n[1] PNG | [2] JPG | [3] WEBP | [4] GIF | [5] MP4\n\n[+] Make a choice: ")
    if "1" in choice:
        f = open(filename, "rb")
        init = f.read()
        r = open(outputn, "wb")
        r.write(png + init)
        r.close()
    elif "2" in choice:
        f = open(filename, "rb")
        init = f.read()
        r = open(outputn, "wb")
        r.write(jpg + init)
        r.close()
    elif "3" in choice:
        f = open(filename, "rb")
        init = f.read()
        r = open(outputn, "wb")
        r.write(webp + init)
        r.close()
    elif "4" in choice:
        choice2 = input("\n[1] GIF87 | [2] GIF89\n\n[?] Make a choice: ")
        if "1" in choice2:
            f = open(filename, "rb")
            init = f.read()
            r = open(outputn, "wb")
            r.write(gif87 + init)
            r.close()
        elif "2" in choice2:
            f = open(filename, "rb")
            init = f.read()
            r = open(outputn, "wb")
            r.write(gif89 + init)
            r.close()
    elif "5" in choice:
        f = open(filename, "rb")
        init = f.read()
        r = open(outputn, "wb")
        r.write(mp4 + init)
        r.close()
    print("[!] Done")

if "2" in begin:
    fci()

def edit():
    filename = input("[?] Select the file: ")
    outputn = input("[?] Choose a name for the output file: ")
    choice = input("\n[1] Mirror | [2] Flip | [3] Rotate | [4] Crop | [5] Resize | [6] Filters | [7] Image to ASCII | [8] Split\n\n[+] Make a choice: ")
    if "1" in choice: #mirror
        im1 = Image.open(filename)
        im2 = ImageOps.mirror(im1)
        im2.save(outputn)
    elif "2" in choice: #flip
        im1 = Image.open(filename)
        im2 = ImageOps.flip(im1)
        im2.save(outputn)
    elif "3" in choice: #rotate
        choice2 = input("[1] Rotate Left | [2] Rotate Right | [3] Own value\n\n[?] Make a choice: ")
        if "1" in choice2:
            im1 = Image.open(filename)
            im1 = im1.rotate(-90, expand=1) #expand=1 will make no black lines
            im1.save(outputn)
        elif "2" in choice2:
            im1 = Image.open(filename)
            im1 = im1.rotate(90, expand=1)
            im1.save(outputn)
        elif "3" in choice2:
            im1 = Image.open(filename)
            rotationv = int(input("Enter a value (max 180, -180): "))
            im1 = im1.rotate(rotationv, expand=1)
            im1.save(outputn)
    elif "4" in choice: #crop
        im1 = Image.open(filename)
        w, h = im1.size
        print("[!] Width:", w)
        print("[!] Height:", h)
        left = int(input("\n[?] Left: "))
        top = int(input("[?] Top: "))
        right = int(input("[?] Right: "))
        bottom = int(input("[?] Bottom: "))
        im2 = im1.crop((left, top, right, bottom))
        im2.save(outputn)
    elif "5" in choice:#resize
        im1 = Image.open(filename)
        w, h = im1.size
        print("[!] Width:", w)
        print("[!] Height:", h)
        width = int(input("\n[?] Width: "))
        height = int(input("[?] Height: "))
        im2 = im1.resize((width, height))
        im2.save(outputn)
    elif "6" in choice: #filters
        choice2 = input("[1] Autocontrast | [2] Black And White | [3] Invert | [4] Tint | [5] Saturation | [6] Blur | [7] Brightness | [8] Contrast | [9] Merge\n\n[+] Make a choice: ")
        if "1" in choice2:
            im1 = Image.open(filename).convert("RGB")
            value = int(input("[?] Enter a value (max 2): "))
            im2 = ImageOps.autocontrast(im1, cutoff = value, ignore = value)
            im2.save(outputn)
        elif "2" in choice2:
            im1 = Image.open(filename).convert("RGB")
            im2 = ImageOps.grayscale(im1)
            im2.save(outputn)
        elif "3" in choice2:
            im1 = Image.open(filename).convert("RGB")
            im2 = ImageOps.invert(im1)
            im2.save(outputn)
        elif "4" in choice2:
            im1 = Image.open(filename).convert("RGB")
            red = int(input("[?] Red value: "))
            green = int(input("[?] Green value: "))
            blue = int(input("[?] Blue value: "))
            tint = Image.new("RGB", (im1.size), color=(red,green,blue))
            out = Image.blend(im1, tint, 0.4) #0.4 is the opacity edit it if you want to change the opacity, I will do a update soon for edit the opacity
            out.save(outputn)
        elif "5" in choice2:
            im1 = Image.open(filename)
            value = int(input("[?] Enter a value of saturation (default 2, 3): "))
            saturation = ImageEnhance.Color(im1)
            im2 = saturation.enhance(value)
            im2.save(outputn)
        elif "6" in choice2:
            im1 = Image.open(filename)
            value = int(input("[?] Enter a value for blur (default 5): "))
            im2 = im1.filter(ImageFilter.GaussianBlur(value))
            im2.save(outputn)
        elif "7" in choice2:
            im1 = Image.open(filename)
            value = int(input("[?] Enter a value for brightness (default 1): "))
            bright = ImageEnhance.Brightness(im1)
            im2 = bright.enhance(value)
            im2.save(outputn)
        elif "8" in choice2:
            im1 = Image.open(filename)
            value = int(input("[?] Enter a value for contrast (default 2): "))
            contrast = ImageEnhance.Contrast(im1)
            im2 = contrast.enhance(value)
            im2.save(outputn)
        elif "9" in choice2:
            im1 = Image.open(filename)
            print("[!] This can have a error on big file")
            red, green, blue = im1.split()
            im2 = Image.merge("RGB", (green, red, blue))
            im2.save(outputn)
    elif "7" in choice:
        print("Soon")
    elif "8" in choice:
        print("Soon")

if "3" in begin:
    edit()
