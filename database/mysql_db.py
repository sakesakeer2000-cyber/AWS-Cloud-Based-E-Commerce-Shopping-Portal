import os,hashlib,pymysql
def conn():
    if not os.getenv("MYSQL_HOST") or not os.getenv("MYSQL_USER"): raise RuntimeError("MYSQL_HOST and MYSQL_USER are not configured")
    return pymysql.connect(host=os.getenv("MYSQL_HOST"),user=os.getenv("MYSQL_USER"),password=os.getenv("MYSQL_PASSWORD",""),database=os.getenv("MYSQL_DATABASE","shopping_portal"),port=int(os.getenv("MYSQL_PORT","3306")),autocommit=True,connect_timeout=5)
def init_db():
    c=conn()
    try:
        with c.cursor() as x: x.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(120) NOT NULL,email VARCHAR(255) UNIQUE NOT NULL,password_hash VARCHAR(64) NOT NULL,created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
    finally: c.close()
def create_user(name,email,password):
    c=conn()
    try:
        with c.cursor() as x: x.execute("INSERT INTO users(name,email,password_hash) VALUES(%s,%s,%s)",(name,email,hashlib.sha256(password.encode()).hexdigest()))
    finally: c.close()
