import requests
import config

# Variables para autenticación
client_id = config.client_id
access_token = config.access_token

# Endpoint para obtener información de un usuario de Twitch
user_url = "https://api.twitch.tv/helix/users"
 
# Pedimos al usuario que ingrese el nombre de usuario
username = input("Ingresa el nombre de usuario: ")
 
# Hacemos la petición para obtener la información del usuario
response = requests.get(f"https://api.twitch.tv/helix/users?login={username}", headers={
    "Client-ID": client_id,
    "Authorization": f"Bearer {access_token}"
})
 
# verificamos que la respuesta sea exitosa
if response.status_code == 200:
    # obtenemos el broadcaster_id
    data = response.json()["data"]
    if len(data) > 0:
        broadcaster_id = data[0]["id"]
        print(f"{username} tiene el broadcaster id = {broadcaster_id}")

        # actualizamos el archivo de configuración
        with open("config.py", "r") as f:
            lines = f.readlines()
        
        with open("config.py", "w") as f:
            for line in lines:
                if line.startswith("broadcaster_id"):
                    f.write(f"broadcaster_id = {broadcaster_id}\n")
                else:
                    f.write(line)

else:
    print("No se pudo obtener el broadcaster_id")
