from os import getenv

print("TYPE:", getenv("TYPE"))
print("PROJECT_ID:", getenv("PROJECT_ID"))
print("PRIVATE_KEY_ID:", getenv("PRIVATE_KEY_ID"))
print("PRIVATE_KEY:", getenv("PRIVATE_KEY"))
print("CLIENT_EMAIL:", getenv("CLIENT_EMAIL"))
print("CLIENT_ID:", getenv("CLIENT_ID"))
print("AUTH_URI:", getenv("AUTH_URI"))
print("TOKEN_URI:", getenv("TOKEN_URI"))
print("AUTH_PROVIDER_x509_CERT_URL:", getenv("AUTH_PROVIDER_x509_CERT_URL"))
print("CLIENT_x509_CERT_URL:", getenv("CLIENT_x509_CERT_URL"))
print("UNIVERSE_DOMAIN:", getenv("UNIVERSE_DOMAIN"))


fbk_dict = {
  "type": getenv("TYPE"),
  "project_id": getenv("PROJECT_ID"),
  "private_key_id": getenv("PRIVATE_KEY_ID"),
  "private_key": getenv("PRIVATE_KEY"),
  "client_email": getenv("CLIENT_EMAIL"),
  "client_id": getenv("CLIENT_ID"),
  "auth_uri": getenv("AUTH_URI"),
  "token_uri": getenv("TOKEN_URI"),
  "auth_provider_x509_cert_url": getenv("AUTH_PROVIDER_x509_CERT_URL"),
  "client_x509_cert_url": getenv("CLIENT_x509_CERT_URL"),
  "universe_domain": getenv("UNIVERSE_DOMAIN")
}