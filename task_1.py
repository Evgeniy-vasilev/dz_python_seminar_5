# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

string = 'Напишите программуабв, удаляющуюабв изабв текстаабв всеабв слова, содержащиеабв "абв"'.split()

print(' '.join(x for x in string if 'абв' not in x))
