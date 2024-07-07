import json

def get_user_input(prompt, valid_options=None):
    while True:
        user_input = input(prompt).strip()
        if valid_options is None or user_input in valid_options:
            return user_input
        print(f"Entrée invalide. Veuillez choisir parmi : {', '.join(valid_options)}")

def save_results(data):
    with open('hash_results.json', 'w') as f:
        json.dump(data, f, indent=4)
    print("Résultats sauvegardés dans hash_results.json")
