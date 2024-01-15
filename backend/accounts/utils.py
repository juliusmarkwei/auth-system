from django.core.mail import send_mail


def send_confirmation_email(email, token_id, user_id):
    data = {
        "token_id": str(token_id),
        "user_id": str(user_id)
    }
    
    message = f"Hello {user_id}, your confirmation token is {token_id}"
    send_mail(
        subject="Email Confirmation Testing",
        message=message,
        from_email="juliusmarkwei2000@gmail.com",
        recipient_list=[email],
        fail_silently=True
    )
    print("Email confirmation sent!")
    