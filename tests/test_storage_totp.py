"""Performs general tests."""
from storage_totp_authenticator.libs.storage_totp_authenticator import post_data
import sys

def test_storage_totp_authenticator():
    arguments = sys.argv[1:]
    resp = post_data(arguments[0], arguments[1], arguments[2], arguments[3], arguments[4])


if __name__ == "__main__":
    test_storage_totp_authenticator()


