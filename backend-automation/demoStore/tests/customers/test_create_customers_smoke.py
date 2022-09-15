import pytest
import logging as logger
from demoStore.src.utilities import genericUtilities

@pytest.mark.tcid29
def test_create_customer_only_email_password():
    random_email = genericUtilities.generate_random_email()
    random_password = genericUtilities.generate_random_password()
    # logger.info(f'{random_email} / {random_password}')

    # create payload
    payload = {'email': random_email, 'password': random_password}

    # make the call

    # verify status code of the call

    # verify email in the response

    # verify customer is created in database