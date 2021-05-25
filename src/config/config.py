from os import environ

SERVICE_CONFIG = {
    'host': environ.get('SERVICE_HOST', 'localhost'),
    'port': environ.get('SERVICE_PORT', 8080)
}

DB_CONFIG = {
    'database': environ.get('DB_NAME', 'test'),
    'user': environ.get('DB_USER', 'test_user'),
    'password': environ.get('DB_PASSWORD', 'test_password'),
    'host': environ.get('DB_HOST', 'localhost')
}