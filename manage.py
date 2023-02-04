import requests
import json
import config

# Variables de autenticación y URL
access_token = config.access_token
client_id = config.client_id
broadcaster_id = config.broadcaster_id
custom_rewards_url = "https://api.twitch.tv/helix/channel_points/custom_rewards"

# Función para hacer una solicitud GET
def get_custom_rewards():
    headers = {
        "Authorization": "Bearer " + access_token,
        "Client-ID": client_id
    }
    params = {
        "broadcaster_id": broadcaster_id,
        "only_manageable_rewards": True
    }
    response = requests.get(custom_rewards_url, headers=headers, params=params)
    return response.json()

# Función para hacer una solicitud POST
def create_custom_reward(title, prompt, cost, user_input_required, max_per_user_per_stream):
    headers = {
        "Authorization": "Bearer " + access_token,
        "Client-ID": client_id
    }
    data = {
        "broadcaster_id": broadcaster_id,
        "title": title,
        "prompt": prompt,
        "cost": cost,
        "user_input_required": user_input_required,
        "max_per_user_per_stream": max_per_user_per_stream
    }
    response = requests.post(custom_rewards_url, headers=headers, data=data)
    return response.json()

# Función para imprimir la lista de recompensas personalizadas
def print_custom_rewards(rewards):
    for i, reward in enumerate(rewards["data"]):
        print(f"{i+1}. {reward['title']} (costo:{reward['cost']}) (activo:{reward['is_enabled']})")

    print(f"----------------------------------------------------")

# Función para crear una recompensa personalizada
def create_reward():
    title = input("Cual es el titulo del reward? ")
    prompt = input("Cual es el prompt del reward? ")
    cost = input("Cual es el Costo? ")
    user_input_required = input("Si requiere input del usuario? (para activar el is_user_input_required) ")
    max_per_user_per_stream = input("Cuantas veces puede el usuario redimir este reward? (max_per_user_per_stream) ")
    create_custom_reward(title, prompt, cost, user_input_required, max_per_user_per_stream)

# Función para modificar una recompensa personalizada
def modify_reward(reward):
    print(f"Recompensa seleccionada: {reward['title']} {reward['cost']} {reward['is_enabled']}")
    print("1. Modificar titulo")
    print("2. Modificar costo")
    print("3. Desactivar")
    print("4. Borrar recompensa")
    print("5. Volver a la lista de recompensas")
    choice = int(input("Que deseas hacer? "))
    if choice == 1:
        new_title = input("Nuevo título: ")
        reward["title"] = new_title
    elif choice == 2:
        new_cost = input("Nuevo costo: ")
        reward["cost"] = new_cost
    elif choice == 3:
        reward["is_enabled"] = False
    elif choice == 4:
        # Borrar recompensa
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Client-ID": client_id,
            "Content-Type": "application/json"
        }
        url = f"https://api.twitch.tv/helix/channel_points/custom_rewards?broadcaster_id={broadcaster_id}&id={reward['id']}"
        response = requests.delete(url, headers=headers)
        print("Recompensa borrada exitosamente")
        return

    else:
        return

    # Realizar la llamada PATCH a la API de Twitch
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Client-ID": client_id,
        "Content-Type": "application/json"
    }
    url = f"https://api.twitch.tv/helix/channel_points/custom_rewards?id={reward['id']}"
    response = requests.patch(url, headers=headers, json=reward)
    if response.status_code == 200:
        print("Recompensa modificada exitosamente")
    else:
        print(f"Error al modificar recompensa: {response.text}")


# Main loop
while True:
    rewards = get_custom_rewards()
    print_custom_rewards(rewards)
    choice = int(input("1. Crear recompensa\n2. Modificar recompensa\n3. Salir\nSelecciona una opción: "))
    if choice == 1:
        create_reward()
    elif choice == 2:
        reward_index = int(input("Que recompensa deseas modificar? ")) - 1
        modify_reward(rewards["data"][reward_index])
    else:
        break



