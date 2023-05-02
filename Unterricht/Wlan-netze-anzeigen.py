import network

# WLAN-Verbindung herstellen
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Verfügbare WLAN-Netzwerke scannen
nets = wlan.scan()

# SSIDs der verfügbaren WLAN-Netzwerke ausgeben
for net in nets:
    print(net[0].decode())