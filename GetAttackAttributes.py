from pyattck import Attck

# Initialize MITRE ATT&CK framework
attack = Attck()

# Get the first actor, technique, malware, tool, and mitigation to inspect their attributes
first_actor = attack.enterprise.actors[0]
first_technique = attack.enterprise.techniques[0]
first_malware = attack.enterprise.malwares[0]
first_tool = attack.enterprise.tools[0]
first_mitigation = attack.enterprise.mitigations[0]

# Print the attributes of each individual object
print("Actor Attributes:")
print(dir(first_actor))

print("\nTechnique Attributes:")
print(dir(first_technique))

print("\nMalware Attributes:")
print(dir(first_malware))

print("\nTool Attributes:")
print(dir(first_tool))

print("\nMitigation Attributes:")
print(dir(first_mitigation))