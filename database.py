import os
from sqlalchemy import create_engine, text


# Connection URL (ensure special characters in the password are URL-encoded)
DATABASE_URL = os.environ['DB_CONNECTION_STRING']

# SSL/TLS configuration (corrected file paths)
connect_args = {
    "ssl": {
        "ca": "ssl/server-ca.pem",  # Path to the CA certificate
        "cert": "ssl/client-cert.pem",  # Path to the client certificate
        "key": "ssl/client-key.pem",  # Path to the client private key
         "check_hostname": False  # Disable hostname verification
    }
}

# print("Current working directory:", os.getcwd())
# print("SSL CA file exists:", os.path.exists("ssl/server-ca.pem"))
# print("SSL cert file exists:", os.path.exists("ssl/client-cert.pem"))
# print("SSL key file exists:", os.path.exists("ssl/client-key.pem"))
# Create an engine with connect_args
engine = create_engine(DATABASE_URL, connect_args=connect_args)

def load_jobs_from_db():
  with engine.connect() as connection:
    result = connection.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
        jobs.append(row._asdict())

    return jobs
    # print("type(result):", type(result))
    # result_all = result.all()
    # print("type(result_all):", type(result_all))
    # first_result = result_all[0]
    # first_result_dict = first_result._asdict()
    # print("first_result_dict:", first_result_dict)