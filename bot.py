# bot.py - Tu primer bot de atención en Python

print("🤖 Hola, soy tu primer bot de atención.")
nombre = input("¿Cómo te llamás? ")
print(f"Mucho gusto, {nombre}!")

mensaje = input("¿Qué querés hacer hoy? ")

if "dólar" in mensaje.lower():
    print("📈 El tipo de cambio de hoy es: 1460 ARS por USD.")
elif "saldo" in mensaje.lower():
    print("💰 Tu saldo actual es de 100 USD.")
elif "ayuda" in mensaje.lower():
    print("✅ Claro. Podés consultar cambio, saldo o pedir ayuda.")
else:
    print("🔁 Lo siento, no entendí tu consulta.")
