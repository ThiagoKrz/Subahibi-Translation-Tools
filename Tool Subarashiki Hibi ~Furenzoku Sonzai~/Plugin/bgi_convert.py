# -*- coding: utf-8 -*-
import os
import codecs

startIn = os.getcwd()

print()
print("Pregledujem: " + startIn + "\\")
print("-------------------------")

for dirName, subdirList, fileList in os.walk(startIn):
  print()
  print("Trenutna mapa: " + dirName + "\\")
  for fname in fileList:
    if fname.endswith(".txt"):
      fullpath = dirName + "\\" + fname
      print("  Podnapis: " + fname )
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("à","ｧ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("À","ｱ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("ì","ｨ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("Ì","ｲ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("ù","ｩ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("Ù","ｳ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("è","ｪ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("È","ｴ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("ò","ｫ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("Ò","ｵ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("á","ｬ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("Á","ｭ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("í","ｮ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("Í","ｯ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("ú","ｶ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("Ú","ｷ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("é","ｸ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("É","ｹ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("ó","ｺ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("Ó","ｻ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("â","ｼ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("Â","ｽ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("î","ｾ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("Î","ｿ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("û","ﾀ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("Û","ﾁ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("ê","ﾂ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("Ê","ﾃ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("ô","ﾄ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("Ô","ﾅ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("ä","ﾆ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("Ä","ﾇ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("ï","ﾈ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("Ï","ﾉ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("ü","ﾊ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("Ü","ﾋ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("ë","ﾌ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("Ë","ﾍ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("ö","ﾎ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("Ö","ﾏ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("ã","ﾐ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("Ã","ﾑ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("õ","ﾒ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("Õ","ﾓ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("ç","ﾔ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("Ç","ﾕ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("ñ","ﾖ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("Ñ","ﾗ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("ý","ﾘ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("Ý","ﾙ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("®","ﾚ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("©","ﾛ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("¿","ﾜ")
        cursub.seek(0)
        cursub.write(lines)
        
      with codecs.open(fullpath, 'r+', "utf-8") as cursub:
        lines = cursub.read().replace("¡","ﾝ")
        cursub.seek(0)
        cursub.write(lines)
