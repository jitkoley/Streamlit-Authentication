import yaml
import streamlit_authenticator as stauth
from yaml.loader import SafeLoader
import streamlit as st

# Load the configuration file
# with open('config.yaml', 'r') as file:
#     config = yaml.safe_load(file)
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
# Generate hashed passwords
hashed_passwords = stauth.Hasher(['abc', 'def']).generate()

# Replace plain text passwords with hashed passwords
for user, password in zip(config['credentials']['usernames'].keys(), hashed_passwords):
    config['credentials']['usernames'][user]['password'] = password

# Save the updated configuration file
with open('config.yaml', 'w') as file:
    yaml.safe_dump(config, file)

name, authentication_status, username = authenticator.login('Login', 'main')


if authentication_status:
    authenticator.logout('Logout', 'main', key='unique_key')
    st.write(f'Welcome *{name}*')
    st.title('Some content')
elif authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')








