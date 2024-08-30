# Primeira parte
def formatterNumber (numero):
    DDI = "+55"
    DDD = [
        {"BA": ["71", "73", "74", "75", "77"]},
        {"SP": ["11", "12", "13", "14", "15", "16", "17", "18", "19"]},
        {"MG": ["31", "32", "33", "34", "35", "37", "38"]},
        {"ES": ["27", "28"]},
        {"RJ": ["21", "22", "24"]}
    ]

    # Verificar se o numero tem o DDI
    if not numero.startswith(DDI):
        numero = DDI + numero

    # Retira o prefixo DDD e o resto do número
    prefixo = numero[3:5]
    resto = numero[5:]

    # Verifica o estado e o DDD
    estado = None
    for item in DDD:
        for est, codigo in item.items():
            if prefixo in codigo: # verifia se o prefixo retirado está presente no codigo
                estado = est
                break
        if estado:
            break
            
    if not estado:
        print("DDD não Encontrado")

    if estado == "BA":
        if "9" in "BA":
            if resto.index('9') >= len(resto) - 8: #Verifica se o 9 estiver entre os 8 números"
                return numero
            else:
                resto = resto.replace('9', '', 1)
        return DDI + prefixo + resto

    else:
        # se for qualquer outro estado
        if resto.index('9') != len(resto) - 9:
            resto = '9' + resto
        return DDI + prefixo + resto



# Escopo Principal
numero = ["11923456789", "71923456789", "+5573923456798", "7123456798", "1123456689"]
for num in numero:
    funcao = formatterNumber(num)
    print(f"CADASTRADO: {num} | Formatado: {funcao}")