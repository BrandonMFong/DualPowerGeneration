from django.contrib.auth import get_user_model
# ^ instead of 'from django.contrib.auth.models import User'
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()  # <- function that will go out find
        # the actual class that is the user model and give me that back.

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"
