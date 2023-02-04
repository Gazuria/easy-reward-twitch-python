import requests
import config

# Client ID y Access Token
client_id = config.client_id
access_token = config.access_token
broadcaster_id = config.broadcaster_id

# Endpoint para obtener la lista de custom rewards
url = f"https://api.twitch.tv/helix/channel_points/custom_rewards?broadcaster_id={broadcaster_id}"
headers = {
    "Client-ID": client_id,
    "Authorization": f"Bearer {access_token}"
}

# Realizamos la petición a Twitch
response = requests.get(url, headers=headers)
data = response.json()

# print(data)

if response.status_code != 200:
    print(f"Error: {data['message']}")
else:
    # Mostramos la lista de custom rewards
    rewards = data["data"]
    for i, reward in enumerate(rewards):
        print(f"{i + 1}. {reward['title']}")

    # Pedimos al usuario que seleccione un reward
    selected_reward = int(input("Selecciona un reward: "))

    # Endpoint para obtener las custom redeemions asociadas al reward id
    url = f"https://api.twitch.tv/helix/channel_points/custom_rewards/redemptions?broadcaster_id={broadcaster_id}&reward_id={rewards[selected_reward - 1]['id']}&status=UNFULFILLED"
    
    # Realizamos la petición a Twitch
    response = requests.get(url, headers=headers)
    data = response.json()

# Verificamos si hubo un error en la petición
    if response.status_code != 200:
        print(f"Error: {data['message']}")
    else:
        # Mostramos las custom redeemions asociadas al reward id con estado UNFULFILLED
        redeemions = data["data"]      

update_url = "https://api.twitch.tv/helix/channel_points/custom_rewards/redemptions"


from datetime import datetime

today = datetime.now().strftime("%d-%m-%Y")
filename = f"redemptions_{today}.txt"


# Abrimos un archivo de texto para adjuntar los datos
with open(filename, "a") as f:
    for i, redemption in enumerate(redeemions):
        # Mostramos la información de la custom redemption
        print(f"{i + 1}. {redemption['user_input']} ({redemption['user_name']})")
        
        # Pedimos al usuario que seleccione una opción
        option = int(input("Selecciona una opción (1 para rechazar, 2 para aceptar, 3 para ignorar y continuar): "))
        
        # Actualizamos el estado de la custom redemption
        if option == 1:
            status = "CANCELED"
        elif option == 2:
            status = "FULFILLED"
            f.write(f"{redemption['user_input']} ({redemption['user_name']})\n")
        else:
            continue
        
        update_data = {
            "broadcaster_id": broadcaster_id,
		"reward_id": rewards[selected_reward - 1]['id'],
            "id": redemption["id"],
            "status": status
        }
        response = requests.patch(update_url, headers=headers, data=update_data)
        
        if response.status_code != 200:
            print(f"Error: {response.json()['message']}")
        else:
            print("Estado actualizado correctamente")