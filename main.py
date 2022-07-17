def sentence_maker(text):

    questions1 = ("what", "why", "when", "where", "how", "can")
    caps = text.capitalize()
    if text.startswith(questions1):
        return "{}?".format(caps)
    else:
        return "{}.".format(caps)


restults = []
while True:
    u_input = input("Say something: ")
    if u_input == "done":
        break
    else:
        restults.append(sentence_maker(u_input))
