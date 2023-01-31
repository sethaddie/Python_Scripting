from platform import platform, machine, processor, system

print(platform())
print(platform(1))
print(platform(0, 1))
print(platform(aliased = True, terse= False))


print(machine())
print(processor())
print(system())
