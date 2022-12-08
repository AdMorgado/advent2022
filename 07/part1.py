
filename = "example.txt"

PREFIX_DIR = "dir"
PREFIX_COMMAND = "$"

COMMAND_LS = "ls"
COMMAND_CD = "cd"

with open(filename, "r") as f:
    lines = f.read().split("\n")

def createFolder(name, parent) -> dict:
    return {
        "name": name,
        "dirs": [],
        "size": 0,
        "parent": parent
    }

root = createFolder("/", None)

current_dir = root

for line in lines[1:]: 
    match line.split(" "):
        case "$", "ls":
            pass
        case "$", "cd", "..":
            current_dir = current_dir["parent"]
        case "$", "cd", dirName:
            current_dir = next((dir for dir in current_dir["dirs"] if dir["name"] == dirName))
        case "dir", dir: root["dirs"].append(createFolder(dir, root))
        case size, _: current_dir["size"] += int(size) 


#getSize(root, accum)


