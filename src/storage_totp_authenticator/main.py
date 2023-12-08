import storage_totp_authenticator.storage_totp_authenticator
# Arguments are in the following format shared_secret, timestep, root, userid, passwd, data
# Documented in storage_totp_authenticator

def main():
    arguments = sys.argv[1:]
    if(arguments.length != 5){
        print("Need Arguments in the following sequence .. shared_secret, timestep, root, userid, passwd, data")
    }
    post_data();
