index = 0
while True:

    line = input()
    if line == "end of comments":
        break

    index += 1

    if index == 1:
        print("<h1>")
        print(f"    {line}")
        print("</h1>")

    elif index == 2:
        print("<article>")
        print(f"    {line}")
        print("</article>")

    else:
        print("<div>")
        print(f"    {line}")
        print("</div>")