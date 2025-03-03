from pyattck import Attck

# Initialize MITRE ATT&CK framework
attack = Attck()

# Specify the threat group
group_name = "APT29"

# Loop through the group and retrieve TTPs
for actor in attack.enterprise.actors:
    if actor.name == group_name:
        print(f"Techniques for {actor.name}:")
        for technique in actor.techniques:
            print(f"{technique.technique_id} - {technique.name}")