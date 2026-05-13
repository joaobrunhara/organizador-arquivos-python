import os
import shutil

caminho = r"C:\Users\user\Desktop\Projeto_Organizador\Arquivos_Baguncados"
locais = {
    "Imagens":[".jpg", ".jpeg", ".png"],
    "Documentos":[".txt", ".pdf", ".docx", ".xlsx"]
    }

arquivos = os.listdir(caminho)
for arquivo in arquivos:
    nome, extensoes = os.path.splitext(arquivo)
        
for pasta, extensoes_permitidas in locais.items():
    if extensoes.lower() in extensoes_permitidas:
        pasta_destino = os.path.join(caminho, pasta)
        
        if not os.path.exists(pasta_destino):
            os.mkdir(pasta_destino)
                            
        origem = os.path.join(caminho, arquivo)
        destino = os.path.join(pasta_destino, arquivo)
                            
        shutil.move(origem, destino)
        print(f"Sucesso: {arquivo} movido para {pasta}!")