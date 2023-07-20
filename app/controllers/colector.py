import re

class get_autor():
    def __init__(self):
        pass
    def get_name_text(self,content):
        """
        Extrai o nome do autor de um texto.

        Parâmetros:
            content (str): O texto de onde o nome do autor será extraído.

        Retorna:
            str or bool: O nome do autor se encontrado no texto, caso contrário, False.
        """
        
        vals = []
        for pattern in pattern_name:
            val = re.findall(pattern,content)
            if val != []:
                nome = str(val[0]).strip()
                nome = nome.replace('e outro','')
                if "e herdeiro" in nome:
                    continue
                nome = nome.split(",")[0]
                nome = nome.upper()
                name_ = nome.split(" ")
                nome = " ".join([name for i,name in enumerate(name_) if not len(name) == 1])
                vals.append(nome)
                

        vals = list(dict.fromkeys(vals)) 
        if len(vals) == 0:
            return False
        else:
            return vals[0]