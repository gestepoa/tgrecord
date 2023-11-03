class DevConfig:
    SQLALCHEMY_DATABASE_URI = "mysql://root:zhrmghgws2@192.168.50.199/TGRecord"
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True
    UPLOAD_FOLDER = './static/profile_photo'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
