from pyattck import Attck

# Initialize MITRE ATT&CK freamework
attack = Attck()

# Specify the threat groups
group_names = ["APT28", "APT41"]


# Find the groups and list their malware and associated tools
for group in attack.enterprise.actors:
    if group.name in group_names:
        print(f"\nMalware used by {group.name}:")
        for malware in group.malwares:
            print(f"  -{malware.name}")
            for technique in malware.techniques:
                print(f"    {technique.technique_id} - {technique.name}")
        print(f"\nTools used by {group.name}:")
        for tool in group.tools:
            print(f"  -{tool.name}")
            for technique in tool.techniques:
                print(f"    {technique.technique_id} - {technique.name}")