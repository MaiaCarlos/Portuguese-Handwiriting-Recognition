def draw():
    import tkinter
    from PIL import Image, ImageTk, ImageDraw
    import PIL
    
    width=500
    height=500
    white = (255, 255, 255)

    def save_picture():
        filename ="image.png"
        image1.save(filename)

    def paint(event):
        x1,y1=(event.x-6),(event.y-6)
        x2,y2 = (event.x+6), (event.y+6)
        canvas.create_oval(x1,y1,x2,y2, fill='red', width=25)
        draw.line([x1,y1,x2,y2], fill='black',width=25)


    app = tkinter.Tk()
    canvas = tkinter.Canvas(app, width=width, height=height, bg='white')
    canvas.pack()



    image1=PIL.Image.new('RGB', (width, height), white)
    draw=ImageDraw.Draw(image1)

    canvas.pack(expand=tkinter.YES, fill=tkinter.BOTH)

    canvas.bind("<B1-Motion>", paint)


    button = tkinter.Button(
        text="Save Picture!",
        width=25,
        height=5,
        bg="blue",
        fg="yellow",
        command=save_picture
    )
    
    button.pack()
    app.mainloop()
    
def image_treat():
    from PIL import Image, ImageTk, ImageDraw, ImageOps, ImageEnhance
    import PIL
    import numpy as np 
    import matplotlib.pyplot as plt
    
    img = Image.open('image.png').convert('L')  # convert image to 8-bit grayscale
    img=ImageEnhance.Sharpness(img).enhance(30)
    img=ImageEnhance.Brightness(img).enhance(0.9)
    img=ImageEnhance.Contrast(img).enhance(20)
    #img=ImageEnhance.Sharpness(img).enhance(0)
    img=ImageOps.invert(img)

    img=img.resize((28,28))

    WIDTH, HEIGHT = img.size

    newdata = list(img.getdata()) # convert image data to a list of integers
    # convert that to 2D list (list of lists of integers)
    newdata = [newdata[offset:offset+WIDTH]for offset in range(0, WIDTH*HEIGHT, WIDTH)]
    newdata=np.array(newdata)
    plt.imshow(newdata.reshape(28,28))