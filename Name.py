def send_email(message, recipient, sender = "universiti.help@gmail.com"):
    if '@' not in recipient or not recipient.endswith(('.ru', '.com' 'net')):
        print(f'Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>')
    elif '@' not in sender or not sender.endswith(('.ru', '.com', '.net')):
        print(f'Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>')
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "universiti.help@gmail.com":
        print("Письмо успешно отправлено")
    else:
        print(f"НЕСТАНЛАРТЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <{sender}> на адрес <{recipient}>")


send_email('Это сообщение для проверки в связи','vasyok1337@.gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!','urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправтье задание', 'urban.student@mail.ru', sender ='urban.teacher@mail.uk')
send_email("Напоминаю самому себе о вебинаре", 'urban.teasher@mail.ru', sender='urban.teasher@mail.ru')