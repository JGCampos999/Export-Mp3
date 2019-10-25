from gtts import gTTS
language = 'pt'
bicho = ['pintinho', 'galinha', 'galo', 'perú', 'capote', 'gato',
         'cachorro', 'cabra', 'bode','vaca','boi']
som = ['piu', 'có', 'corócocó', 'gulu gulu', 'tô fraco', 'miau',
        'áu áu', 'mééé', 'bééé', 'móóh', 'múúh']
letra = ''
c = 0
for i in range(len(bicho)):
    s = bicho[i]
    if (s[len(s)-1:] == 'a'):
        s = 'uma'
    else:
        s = 'um'
    letra+= ('Lá em casa tinha {} {}\nLá em casa tinha {} {}\n'.format(s, bicho[i],s, bicho[i]))
    for j in range(c, 0, -1):
        s = bicho[j]
        if (s[len(s)-1:] == 'a'):
            s = 'a'
        else:
            s = 'o'
        letra+= ('E {} {} {}\n' .format(s, bicho[j], som[j]))
    for x in range(2):
        letra+= ('E o pintinho piu\n')
    c-= -1
    
output = gTTS(text=letra,lang=language,slow=False)
output.save('output.mp3')
