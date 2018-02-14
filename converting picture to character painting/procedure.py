from PIL import Image

def get_char(r,g,b,alpha): 
    if alpha == 0:
        return ' '
    grey = 0.2126*r + 0.7152*g + 0.0722*b
    char = 'qwertyuiop[]{}\|asdfghjkl;:zxcvbnm,.<>?/!@#$%^&*()_+-='
    greytochar = int((grey/(256+1.0))*len(char))
    return char[greytochar]

def output(outputname,content):
    with open(outputname,'w') as f:
        f.write(content)

def get_picture(file_name,width=80,height=80):
    image = Image.open(file_name)
    image = image.resize((width,height))
    text = ''
    for i in range(width):
        for j in range(height):
            content = image.getpixel((j,i))
            text += get_char(*content)
        text += '\n'
    print (text)
    output('a.txt',text)
    
get_picture('wm.png')
            
    
