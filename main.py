from src.hash_algorithms import hash_password, hash_algorithms
from src.password_utils import generate_random_password
from src.file_utils import hash_file
from src.performance import compare_performance
from src.io_utils import get_user_input, save_results
import base64
import json

def main():
    while True:
        print("\n1. Hasher une chaîne")
        print("2. Vérifier un hachage")
        print("3. Générer un mot de passe aléatoire")
        print("4. Comparer les performances des algorithmes")
        print("5. Hasher un fichier")
        print("6. Quitter")
        
        choice = get_user_input("Choisissez une option : ", ["1", "2", "3", "4", "5", "6"])
        
        if choice == "1":
            password = get_user_input("Entrez la chaîne à hasher : ")
            algorithm = get_user_input("Choisissez l'algorithme de hachage : ", hash_algorithms.keys())
            hashed, salt = hash_password(password, algorithm)
            result = {
                "original": password,
                "algorithm": algorithm,
                "hashed": base64.b64encode(hashed).decode('utf-8') if algorithm in ['bcrypt', 'PBKDF2'] else hashed.hex(),
                "salt": base64.b64encode(salt).decode('utf-8') if salt else None
            }
            print(f"\nRésultat : {json.dumps(result, indent=2)}")
            save = get_user_input("Voulez-vous sauvegarder ce résultat ? (oui/non) : ").lower()
            if save == 'oui':
                save_results(result)
        
        elif choice == "2":
            # Code pour vérifier un hachage
            pass
        
        elif choice == "3":
            length = int(get_user_input("Entrez la longueur du mot de passe : "))
            password = generate_random_password(length)
            print(f"Mot de passe généré : {password}")
        
        elif choice == "4":
            results = compare_performance()
            for algo, time_taken in results.items():
                print(f"{algo}: {time_taken:.4f} secondes")
        
        elif choice == "5":
            file_path = get_user_input("Entrez le chemin du fichier à hasher : ")
            algorithm = get_user_input("Choisissez l'algorithme de hachage : ", hash_algorithms.keys())
            hashed = hash_file(file_path, algorithm)
            print(f"Hachage du fichier : {hashed.hex()}")
        
        elif choice == "6":
            break

if __name__ == "__main__":
    main()
