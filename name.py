name = "ada lovelace"
print(name.title())

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print (full_name)
# print(f"{"Hello"} {full_name.title()}")
print(f"Hello, How are you! {first_name}")
print(f"Hello,{full_name.title()}!")

message = f"Hello, {full_name.title()}!"
print(message)

print("\tPython")
print("\nPython")
print("Langurages:\n\tPython\n\tC\n\tJavaScript")

favorite_langurage = ' python '
print(favorite_langurage)
favorite_langurage = favorite_langurage.rstrip()
print(favorite_langurage)
favorite_langurage = favorite_langurage.lstrip()
print(favorite_langurage)
favorite_langurage = favorite_langurage.strip()
print(favorite_langurage)

nostarch_url = 'https://nostarch.com'
nostarch_url = nostarch_url.removeprefix('https://')
print(nostarch_url)