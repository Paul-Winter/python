def generate_secure_query(user_login, user_pass):
    safe_login = user_login.replace("'", "''")
    safe_pass = user_pass.replace("'", "''")
    query = f"SELECT * FROM users WHERE login = '{safe_login}' AND password = '{safe_pass}';"
    return query
