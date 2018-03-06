"""
	Storage class to handle data using data structures
"""


class store():
    """Main store  for storing data"""
    users = []
    businesses = []
    reviews = []
    auth_tokens = []

    def save_user(self, data):
        """Save user method"""
        self.users.append(data)

    def save_token(self, token):
        """Save token method"""
        self.auth_tokens.append(token)