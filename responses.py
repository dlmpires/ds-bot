from random import choice, randint

def GetResponse(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return "No lower-case allowed, sorry :P"
    elif 'hello' in lowered:
        return "Hey :P"
    elif 'escolha' in lowered:
        return f'1- Sim, 2- Não: \n {randint(1,2)}'
    else:
        return choice(['Nao sei'])