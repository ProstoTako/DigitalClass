from re import match


def check_string(string: str) -> bool:
    regular_number = (r'(((\+?7|8)?(\(\d{3}\)|(\d{3}))\d{7})|'
                      r'(((\+?7|8)-)?\d{3}-\d{3}-\d{2}-\d{2})|'
                      r'(((\+?7|8)\ )?\(\d{3}\)\ \d{3}-\d{2}-\d{2})|'
                      r'(((\+?7|8))?\(\d{3}\)\d{3}-\d{2}-\d{2}))$')
    regular_email = r'\w(\w|\.\w\w)*@\w+(\.\w\w)+(\w|\.\w\w)*$'
    is_phone_number = match(regular_number, string)
    is_email = match(regular_email, string)
    if is_phone_number or is_email:
        return True
    else:
        return False
