### РЕЖИМ а
colors = ['red', 'green', 'blue']
data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
data.writelines(colors) # разделителей не будет
data.close()

# data.close() — используется для закрытия файла, чтобы разорвать
# подключение файловой переменной с файлом на диске.
# ● exit() — позволяет не выполнять код, прописанный после этой команды в
# скрипте.
# ● В итоге создаётся текстовый файл с текстом внутри: redbluedreen.
# ● При повторном выполнении скрипта redbluedreenredbluedreen — добавление
# в существующий файл, а не перезапись файлов.

with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')

### РЕЖИМ r
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()

### РЕЖИМ w
colors = ['red', 'green', 'blue']
data = open('file.txt', 'w')
data.writelines(colors) # разделителей не будет
data.close()
# ● В итоге создаётся текстовый файл с текстом внутри: ‘redbluedreen’.
# ● В случае перезаписи новые данные записываются, а старые удаляются.
