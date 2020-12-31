import amino
import getpass
import os

# Feito por Luiz Eduardo
# Amino.py criada por Slimakoi™
# Slimakoi™ todos os direitos reservados ®.

# Abaixo uma proxy japonesa.
proxies = {'http': '43.224.8.125:6666'}
client=amino.Client(proxies=proxies)

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
print( '\033[1;36mFeito por ~>\033[1;92m Luiz Eduardo')
print('\n\033[0m')             
mail = input('Seu Email:')
password = getpass.getpass('Sua Senha:')
client.login(email=mail,password=password)

# Sistema de pegar id de comunidades:
os.system("clear")
url = input('Url da Comunidade:')
obs=client.get_from_code(url)
comId=obs.path[1:obs.path.index("/")]
sclient=amino.SubClient(comId=comId,profile=client.profile)

# Sistema de pegar id de chat:
os.system("clear")
chat=input("URL do chat:")
sclient=client.get_from_code(chat).objectId

# Sistema de mandar mensagem:
os.system("clear")
message = input('Sua mensagem:')
sclient.send_message(message=message,chatId=objectId,messageType=100)
 
# -> Aqui está umas variações de mensagem.

#1 - STRIKE
#50 - UNSUPPORTED_MESSAGE
#58 - MISSED_VOICE_CHAT
#57 - REJECTED_VOICE_CHAT
#59 - CANCELED_VOICE_CHAT
#100 - DELETED_MESSAGE
#101 - JOINED_CHAT
#102 - LEFT_CHAT
#103 - STARTED_CHAT
#104 - CHANGED_BACKGROUND
#105 - EDITED_CHAT
#106 - EDITED_CHAT_ICON
#107 - STARTED_VOICE_CHAT
#109 - UNSUPPORTED_MESSAGE
#110 - ENDED_VOICE_CHAT
#113 - EDITED_CHAT_DESCRIPTION
#114 - ENABLED_LIVE_MODE
#115 - DISABLED_LIVE_MODE
#116 - NEW_CHAT_HOST
#124 - INVITE_ONLY_CHANGED
#125 - ENABLED_VIEW_ONLY
#126 - DISABLED_VIEW_ONLY