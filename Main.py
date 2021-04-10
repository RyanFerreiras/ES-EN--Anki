import sys
Dictionary = {}
Key = 0
words = []
dictionary_file = str(sys.argv[1])
words_file = str(sys.argv[2])
output_name = str(sys.argv[3]) 
with open(dictionary_file,'r',encoding = 'UTF-8') as file:
    for line in file:
        if ('<c>' in line):
            word = ""
            for letter in line:
                if (letter not in "</>"):
                    word += letter

            Key = word.strip()
        if ('<d>' in line):
            word = ""
            for letter in line:
                if (letter not in "</>"):
                    word += letter
            word = word.strip()
            if Key[1:-1] not in Dictionary:
                Dictionary[Key[1:-1]] = word[1:-1]
            elif(Key[1:-1] in Dictionary):
                Dictionary[Key[1:-1]] += ' Alternate Defintion: ' + word[1:-1]
with open(words_file,'r', encoding = 'UTF-8') as file:
    for line in file:
        if len(line.split()) > 1:
            for word in line.split():
                words.append(word.strip().lower())
        else:
            words.append(line.strip().lower())
with open(output_name + '.txt','w', encoding= 'UTF-8') as file:
    i = 0
    while(i < len(words)):
        file.write(words[i] + ";" + Dictionary[words[i]] + '\n')
        i += 1








