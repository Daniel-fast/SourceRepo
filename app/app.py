import sys
import requests

print()
print("Information")
print()
response = requests.get("https://google.com")
print(response)
print()


print()
print("Path:", sys.path)
print()
print("Versao:", sys.version_info)
print("Platform:", sys.platform)
print("Argv:", sys.argv)

print()
