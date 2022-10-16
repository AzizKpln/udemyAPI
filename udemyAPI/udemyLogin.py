class login:
    """
    This function is used to login Udemy.
    
    note: if you don't wanna show your mail and password in your script,
    you can simply create an enviroment and use it
    like:
    touch .bash_profile && echo "export 'MAIL' = YOURMAIL >>.bash_profile && echo "export 'PASSWORD' = YOURPASSWORD">>.bash_profile
    python side -> import os;os.getenv("EMAIL");os.getenv("PASSWORD")
    """
    def __init__(self,page,email,password) -> None:
        self.page=page
        self.page.goto("https://www.udemy.com/join/login-popup")
        self.page.locator("#email--1").fill(email)
        self.page.locator("#id_password").fill(password)
        self.page.click("#submit-id-submit")
    