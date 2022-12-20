from maestro import Maestro

maestro = Maestro.get_one()

print("Maestro:", maestro)
print("Channel count:", maestro.channel_count)
