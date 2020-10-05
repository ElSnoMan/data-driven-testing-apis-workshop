
def test_login_without_seam(py, credentials, new_unauthorized_user):
    user = new_unauthorized_user
    py.visit('https://demoqa.com/login')
    py.get('#userName').type(credentials.get('username'))
    py.get('#password').type(credentials.get('password'))
    py.get('#login').click()
    assert py.contains(user.username)


def test_login_with_seam(py, login_seam):
    user, _ = login_seam('/profile')
    assert py.contains(user.username)


def test_login_with_seam_land_on_books(py, login_seam):
    user, _ = login_seam('/books')
    assert py.contains('Git Pocket Guide')
