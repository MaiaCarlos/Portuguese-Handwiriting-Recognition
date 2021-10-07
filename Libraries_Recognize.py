def draw():
    import tkinter
    from pil import Image, ImageTk, ImageDraw
    import pil
    
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



    image1=pil.Image.new('RGB', (width, height), white)
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
    from pil import Image, ImageTk, ImageDraw, ImageOps, ImageEnhance
    import pil
    import numpy as np 
    import matplotlib.pyplot as plt
    global newdata
    #Tratamento de imagem
    img = Image.open('image.png').convert('L')  # convert image to 8-bit grayscale
    img=ImageEnhance.Sharpness(img).enhance(30)
    img=ImageEnhance.Brightness(img).enhance(0.9)
    img=ImageEnhance.Contrast(img).enhance(20)
    #img=ImageEnhance.Sharpness(img).enhance(0)
    img=ImageOps.invert(img)
    #alterar tamanho da imagem
    img=img.resize((28,28))

    WIDTH, HEIGHT = img.size
    

    newdata = list(img.getdata()) # convert image data to a list of integers
    # convert that to 2D list (list of lists of integers)
    newdata = [newdata[offset:offset+WIDTH]for offset in range(0, WIDTH*HEIGHT, WIDTH)]
    newdata=np.array(newdata)

    plt.imshow(newdata.reshape(28,28))
    return newdata
   

def import_models():
    import joblib
    from keras.models import model_from_json
    #Importar Modelo LGBM
    
    lgb=joblib.load('lgbm.pkl')
    
    #Importar modelo CNN 
    json_file = open ('model.json', 'r')
    loaded_model_json= json_file.read()
    json_file.close()

    cnn= model_from_json(loaded_model_json)
    cnn.load_weights('letter.h5')
    cnn.compile(optimizer='adam', loss='categorical_crossentropy', metrics='accuracy')

    return lgb, cnn

def models_predict():
    
    lgb, cnn = import_models()
    newdata= image_treat()
    word_dict = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X', 24:'Y',25:'Z'}
    # LGBM- Predict
    newdata=newdata.reshape(1,784)
    predict=lgb.predict_proba(newdata)
    letter=predict.argmax()
    print('LGBM: Letra que foi escrita é: ',word_dict[letter], 'com probabilidade de acertar de: ',"%.2f" % (predict[0][letter]*100),"%")
    
    # CNN - Predict
    newdata=newdata/255
    newdata=newdata.reshape(1,28,28,1)
    predict=cnn.predict(newdata)
    letter=predict.argmax()
    print('CNN: Letra que foi escrita é: ',word_dict[letter], 'com probabilidade de acertar de: ',"%.2f" % (predict[0][letter]*100),"%")
    
def models_predict_(caminho):
    
    lgb, cnn = import_models()
    newdata= image_treat2(caminho)
    word_dict = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X', 24:'Y',25:'Z'}
    # LGBM- Predict
    newdata=newdata.reshape(1,784)
    predict=lgb.predict_proba(newdata)
    letter=predict.argmax()
    print('LGBM: Letra que foi escrita é: ',word_dict[letter], 'com probabilidade de acertar de: ',"%.2f" % (predict[0][letter]*100),"%")
    
    # CNN - Predict
    newdata=newdata/255
    newdata=newdata.reshape(1,28,28,1)
    predict=cnn.predict(newdata)
    letter=predict.argmax()
    print('CNN: Letra que foi escrita é: ',word_dict[letter], 'com probabilidade de acertar de: ',"%.2f" % (predict[0][letter]*100),"%")    
    
def image_treat2(caminho):
    from pil import Image, ImageTk, ImageDraw, ImageOps, ImageEnhance
    import pil
    import numpy as np 
    import matplotlib.pyplot as plt
    global newdata
  
    #Tratamento de imagem
    img = Image.open(caminho).convert('L')  # convert image to 8-bit grayscale
    img=ImageEnhance.Brightness(img).enhance(2)
    #img=ImageEnhance.Sharpness(img).enhance(0)
    img=ImageEnhance.Contrast(img).enhance(10)
    img=ImageEnhance.Sharpness(img).enhance(10)
    img=ImageOps.invert(img)

    img=img.resize((28,28))

    WIDTH, HEIGHT = img.size

    newdata = list(img.getdata()) # convert image data to a list of integers
    # convert that to 2D list (list of lists of integers)
    newdata = [newdata[offset:offset+WIDTH]for offset in range(0, WIDTH*HEIGHT, WIDTH)]
    newdata=np.array(newdata)

    plt.imshow(newdata.reshape(28,28))
    return newdata   

def import_image(caminho):
   
    import matplotlib.image as mpimg
    import matplotlib.pyplot as plt
    

    img = mpimg.imread(caminho)
    plt.imshow(img)
    return caminho

    
    
    