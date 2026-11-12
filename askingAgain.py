good_answers = ["yes", "yup", "ok", "fine" , "whatever", "sure", "allright"]

answered_right = False
while not answered_right:
    your_answer = input("Can I eat my candy now?")
    answer = your_answer.lower()
    if answer in good_answers:
        break
    print("No realllllllllly........................")
print("Finally you said the right thing")