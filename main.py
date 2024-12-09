#Generate Password

import random
import string

def generate_password(length=12):
  """Génère un mot de passe aléatoire de longueur spécifiée."""
  characters = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choice(characters) for _ in range(length))
  return password

# Exemple d'utilisation :
password = generate_password(16)
print(password)