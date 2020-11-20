def is_valid(username: str) -> bool:
    return (
            (3 <= len(username) <= 16) and
            ((username.isalnum()) or
             ("_" in username) or
             ("-" in username))

    )


[print(username) for username in input().split(", ") if is_valid(username)]


# ===============================================================

# from re import match
#
# usernames = input().split(", ")
#
# for username in usernames:
#     if (
#             (3 <= len(username) <= 16) and
#             (match("^[A-Za-z0-9_-]*$", username))
#     ):
#         print(username)
#
# ===============================================================
#
#
# usernames = input().split(", ")
#
# for username in usernames:
#     if (
#             (3 <= len(username) <= 16) and
#             ((username.isalnum()) or
#              ("_" in username) or
#              ("-" in username))
#
#     ):
#         print(username)
