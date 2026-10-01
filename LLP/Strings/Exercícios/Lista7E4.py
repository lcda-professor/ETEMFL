"""Peça o nome de uma instituição (ex: “Universidade Federal do Rio de 
Janeiro”) e gere sua sigla automaticamente (UFRJ).
Ignore palavras curtas como “de”, “da”, “do”, “das”, “dos”.

Dica: split(), upper(), laços for."""

nome = input("Digite o nome completo da instituição: ").upper().strip()
sigla = ""
forma = ["DO","DA","DE","NO","NA","NE","EM"]

for palavra in nome.split():
    if palavra not in forma:
        sigla = sigla + palavra[0]

print(f"A sigla de {nome} é {sigla}")