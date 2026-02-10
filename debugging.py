def divide_numbers(num1, num2):
    try:
        with num1/num2 as result:
            return result
    except ZeroDivisionError:
        print('Cannot divide by zero.')

class EmailMissingAtsignError(Exception):
    def __init__(self, email, message="either has too many, is missing, or starts with an atsign ('@')."):
        self.email = email
        self.message = f"'{email}' {message}"
        super().__init__(self.message)
class InvalidEmailDomainError(Exception):
    def __init__(self, email, message='has a malformed [mailserver].[domain] format.'):
        self.email = email
        self.message = f"'{email}' {message}"
        super().__init__(self.message)

def email_validation(e):
    print()
    email=str(e)
    try:
        if email.count('@')!=1 or email.startswith('@'):
            raise EmailMissingAtsignError(email)
        mailserver_domain=email.split('@')[1]
        MD = mailserver_domain
        if MD.endswith('.') or MD.count('.')!=1:
            raise InvalidEmailDomainError(email)
        print(f'{email} is a valid email.')
        return True
    except EmailMissingAtsignError as Err:
        print(f'Validation failed: {Err}')
    except InvalidEmailDomainError as Err:
        print(f'Validation failed: {Err}')
    return False

print(f'Email is valid: {email_validation('wavedash.ledgegrab@gmail.com')}')
print(f'Email is valid: {email_validation('wavedash.ledgegrabgmail.com')}')
print(f'Email is valid: {email_validation('wavedash.ledgegrab@gmailcom')}')
print(f'Email is valid: {email_validation('wavedash.ledgegrabgmailcom')}')
