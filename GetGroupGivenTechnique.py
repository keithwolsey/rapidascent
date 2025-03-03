from pyattck import Attck

# Initialize MITRE ATT&CK framework
attack = Attck()

# Specify the T code
t_code = "T1059"

# Loop through techniques and find the groups using the specified T code
for technique in attack.enterprise.techniques:
    if technique.technique_id == t_code:
        print(f"Groups using {technique.name} ({technique.technique_id}):")
        for group in technique.actors:
            print(f"  - {group.name}")