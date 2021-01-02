import amino
import getpass
import os

# Feito por Luiz Eduardo
# Amino.py criada por Slimakoi™
# Slimakoi™ todos os direitos reservados ®.

# Abaixo uma proxy japonesa.
proxies = {'http': '43.224.8.125:6666'}
client = amino.Client(proxies=proxies)

# Sistema login amino:
os.system('clear')
print("""
╭━━━┳╮╱╱╱╱╭╮
┃╭━╮┃┃╱╱╱╭╯╰╮
┃┃╱╰┫╰━┳━┻╮╭╯
┃┃╱╭┫╭╮┃╭╮┃┃
┃╰━╯┃┃┃┃╭╮┃╰╮
╰━━━┻╯╰┻╯╰┻━╯
╭━━━╮╱╱╱╱╱╱╱╱╭╮
┃╭━╮┃╱╱╱╱╱╱╱╭╯╰╮
┃╰━━┳━━┳━┳┳━┻╮╭╯
╰━━╮┃╭━┫╭╋┫╭╮┃┃
┃╰━╯┃╰━┫┃┃┃╰╯┃╰╮
╰━━━┻━━┻╯╰┫╭━┻━╯
╱╱╱╱╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╱╱╱╱╰╯
""")
print('\033[1;36mFeito por ~>\033[1;92m Luiz Eduardo')
print('\n\033[0m')
mail = input('Seu Email:')
password = getpass.getpass('Sua Senha:')
client.login(email=mail, password=password)

# Sistema de pegar id de comunidades:
os.system("clear")
url = input('Url da Comunidade:')
obs = client.get_from_code(url)
comId = obs.path[1:obs.path.index("/")]
sclient = amino.SubClient(comId=comId,profile=client.profile)

# Sistema de pegar id de chat:
os.system("clear")
chat = input("URL do chat:")
chatId = client.get_from_code(chat).objectId

# Sistema de mandar mensagem:
os.system("clear")
message = input('Sua mensagem:')
os.system("clear")
print('\033[1;36m ◈ ━━━━━━━━━ \033[1;31m◆\033[1;92m ━━━━━━━━━ ◈')
print('\033[1;36m #1 - STRIKE')
print('\033[1;92m #50 - UNSUPPORTED_MESSAGE')
print('\033[1;36m #58 - MISSED_VOICE_CHAT')
print('\033[1;92m #57 - REJECTED_VOICE_CHAT')
print('\033[1;36m #59 - CANCELED_VOICE_CHAT')
print('\033[1;92m #100 - DELETED_MESSAGE')
print('\033[1;36m #101 - JOINED_CHAT')
print('\033[1;92m #102 - LEFT_CHAT')
print('\033[1;36m #103 - STARTED_CHAT')
print('\033[1;92m #104 - CHANGED_BACKGROUND')
print('\033[1;36m #105 - EDITED_CHAT')
print('\033[1;92m #106 - EDITED_CHAT_ICON')
print('\033[1;36m #107 - STARTED_VOICE_CHAT')
print('\033[1;92m #109 - UNSUPPORTED_MESSAGE')
print('\033[1;36m #110 - ENDED_VOICE_CHAT')
print('\033[1;92m #113 - EDITED_CHAT_DESCRIPTION')
print('\033[1;36m #114 - ENABLED_LIVE_MODE')
print('\033[1;92m #115 - DISABLED_LIVE_MODE')
print('\033[1;36m #116 - NEW_CHAT_HOST')
print('\033[1;92m #124 - INVITE_ONLY_CHANGED')
print('\033[1;36m #125 - ENABLED_VIEW_ONLY')
print('\033[1;92m #126 - DISABLED_VIEW_ONLY ')
print('\033[1;36m ◈ ━━━━━━━━━ \033[1;31m◆\033[1;92m ━━━━━━━━━ ◈')
messageType = input('Qual id de mensagem você vai colocar?:')
sclient.send_message(message=message,chatId=chatId,messageType=messageType)