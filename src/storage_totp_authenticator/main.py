import sys
from libs.storage_totp_authenticator import post_data

# Arguments are in the following format shared_secret, timestep, root, userid, passwd, data
# Documented in storage_totp_authenticator

def main():
    arguments = sys.argv[1:]
    print("Arguments to the Program are : ", *arguments)
   
    if(len(arguments) != 5) :
        print("Need Arguments in the following sequence .. shared_secret, root, userid, passwd, data")
        sys.exit()

    post_data(arguments[0], arguments[1], arguments[2], arguments[3], arguments[4])


if __name__ == "__main__":
    main()
