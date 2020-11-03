old_version = "".join(map(str, input().split(".")))

new_version = ".".join(str(int(old_version) + 1))

print(new_version)