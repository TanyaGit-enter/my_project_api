from http import HTTPStatus
from utils.data import configure_data, configure_data_with_meme_id

import allure
import pytest

false_meme_id = '567k'


@allure.feature("Test API token")
@allure.story("Create token")
def test_create_token(auth_token):
    auth_token.create_new_token()
    auth_token.check_that_status(HTTPStatus.OK)


@allure.feature("Test API token")
@allure.story("Create negative token")
def test_create_negative_name_token(auth_token):
    auth_token.create_new_token(payload={"name": 1111})
    auth_token.check_that_status(HTTPStatus.BAD_REQUEST)


@allure.feature("Test API token")
@allure.story("Create session Token")
def test_api_token_is_alive(auth_token, get_auth_token):
    get_auth_token.get_token(auth_token.get_token())
    get_auth_token.check_that_status(HTTPStatus.OK)
    get_auth_token.check_response_token_is_alive()


@allure.feature("Test API token")
@allure.story("Create session token 404")
def test_api_token_is_alive_not_found(auth_token, get_auth_token):
    get_auth_token.get_token(token_id='c2Fcb02vuV01111')
    get_auth_token.check_that_status(HTTPStatus.NOT_FOUND)


test_data = [
    ("Good brains", "https://miro.medium.com/v2/resize:fit:1100/format:webp/1*8sxdEUQBS6qXrx5Ya2OMeQ.jpeg",
     ["humor", "good", "brain"], {"text1": "false sense", "text2": "good head"}),
    ("", "", [], {})
]


@allure.feature("Test API")
@allure.story("Create memes")
@allure.title("Create memes positive")
@pytest.mark.parametrize("text, url, tags, info", test_data)
def test_create_meme_positive(auth_header, create_meme, text, url, tags, info):
    create_meme.create_new_meme(payload=configure_data(text, url, tags, info), headers=auth_header)
    create_meme.check_that_status(HTTPStatus.OK)
    create_meme.check_response_data_is_correct("text", text)
    create_meme.check_response_data_is_correct("url", url)
    create_meme.check_response_data_is_correct("tags", tags)
    create_meme.check_response_data_is_correct("info", info)


test_data_negative = [
    ("Good brains", "https://miro.medium.com/v2/resize:fit:1100/format:webp/1*8sxdEUQBS6qXrx5Ya2OMeQ.jpeg",
     ["humor", "good", "brain"], None),
    (None, None, None, None),
    (25, "https://miro.medium.com/v2/resize:fit:1100/format:webp/1*8sxdEUQBS6qXrx5Ya2OMeQ.jpeg",
     ["humor", "good", "brain"], {"text1": "false sense", "text2": "good head"}),
    ("Good head", "https://miro.medium.com/v2/resize:fit:1100/format:webp/1*8sxdEUQBS6qXrx5Ya2OMeQ.jpeg",
     ["humor", "good", "brain"], []),
    ("Good head", "https://miro.medium.com/v2/resize:fit:1100/format:webp/1*8sxdEUQBS6qXrx5Ya2OMeQ.jpeg",
     {}, {"text1": "false sense", "text2": "good head"}),

]


@allure.feature("Test API")
@allure.story("Create memes")
@allure.title("Create memes negative")
@pytest.mark.parametrize("text, url, tags, info", test_data_negative)
def test_create_meme_bad_request(auth_header, create_meme, text, url, tags, info):
    create_meme.create_new_meme(payload=configure_data(text, url, tags, info), headers=auth_header)
    create_meme.check_that_status(HTTPStatus.BAD_REQUEST)


test_data_1 = [
    ("Good brains", "https://miro.medium.com/v2/resize:fit:1100/format:webp/1*8sxdEUQBS6qXrx5Ya2OMeQ.jpeg",
     ["humor", "good", "brain"], {"text1": "false sense", "text2": "good head"})
]


@allure.feature("Test API")
@allure.story("Create memes")
@allure.title("Create memes for unauthorized user")
@pytest.mark.parametrize("text, url, tags, info", test_data_1)
def test_create_meme_unauthorized(create_meme, text, url, tags, info):
    create_meme.create_new_meme(payload=configure_data(text, url, tags, info))
    create_meme.check_that_status(HTTPStatus.UNAUTHORIZED)


@allure.feature("Test API")
@allure.story("Get memes")
@allure.title("Get all memes")
def test_get_all_memes(auth_header, get_meme):
    get_meme.get_all_memes(auth_header)
    get_meme.check_that_status(HTTPStatus.OK)
    get_meme.check_response_data_is_not_empty()


@allure.feature("Test API")
@allure.story("Get memes")
@allure.title("Get memes for unauthorized user")
def test_get_all_memes_unauthorized(get_meme):
    get_meme.get_all_memes()
    get_meme.check_that_status(HTTPStatus.UNAUTHORIZED)


@allure.feature("Test API")
@allure.story("Get meme")
@allure.title("Get meme id")
def test_get_meme_id(auth_header, get_meme, meme_id):
    get_meme.get_meme_id(meme_id, auth_header)
    get_meme.check_that_status(HTTPStatus.OK)
    get_meme.check_response_data_is_correct('id', meme_id)


@allure.feature("Test API")
@allure.story("Get meme")
@allure.title("Get non-existent meme ")
def test_get_meme_false_id(auth_header, get_meme):
    get_meme.get_meme_id(false_meme_id, auth_header)
    get_meme.check_that_status(HTTPStatus.NOT_FOUND)


@allure.feature("Test API")
@allure.story("Get meme")
@allure.title("Get meme for unauthorized user")
def test_get_meme_unauthorized(get_meme, meme_id):
    get_meme.get_meme_id(meme_id)
    get_meme.check_that_status(HTTPStatus.UNAUTHORIZED)


test_data_2 = [
    ("love memes changed", "https://miro.medium.com/v2/resize:fit:1100/format:webp/1*OkVxoXBTygSKB8K-zbB7uQ.jpeg",
     ["love", "memes", "favorite", "change"], {"text1": "love memes", "text2": "memes are my favorite"})
]


@allure.feature("Test API")
@allure.story("Put meme")
@allure.title("Put positive meme")
@pytest.mark.parametrize("text, url, tags, info", test_data_2)
def test_put_meme(auth_header, meme_id, put_meme, text, url, tags, info):
    put_meme.put_meme_id(meme_id, payload=configure_data_with_meme_id(meme_id, text, url, tags, info),
                         headers=auth_header)
    put_meme.check_that_status(HTTPStatus.OK)
    put_meme.check_response_data_is_correct("text", text)
    put_meme.check_response_data_is_correct("url", url)
    put_meme.check_response_data_is_correct("tags", tags)
    put_meme.check_response_data_is_correct("info", info)


@allure.feature("Test API")
@allure.story("Put meme")
@allure.title("Put positive meme")
@pytest.mark.parametrize("text, url, tags, info", test_data_2)
def test_put_false_meme_id(auth_header, meme_id, put_meme, text, url, tags, info):
    put_meme.put_meme_id(false_meme_id, payload=configure_data_with_meme_id(meme_id, text, url, tags, info),
                         headers=auth_header)
    put_meme.check_that_status(HTTPStatus.NOT_FOUND)


test_data_negative_2 = [
    ("love memes changed", None, ["love", "memes", "favorite", "change"],
     {"text1": "love memes", "text2": "memes are my favorite"}),
    ("love memes changed 2", "https://miro.medium.com/v2/resize:fit:1100/format:webp/1*OkVxoXBTygSKB8K-zbB7uQ.jpeg",
     ["love", "memes", "favorite", "change"], None)
]


@allure.feature("Test API")
@allure.story("Put meme")
@allure.title("Put negative meme")
@pytest.mark.parametrize("text, url, tags, info", test_data_negative_2)
def test_put_meme_false_parameters(auth_header, meme_id, put_meme, text, url, tags, info):
    memes_id = ["680K", None, meme_id]
    for meme in memes_id:
        put_meme.put_meme_id(meme_id, payload=configure_data_with_meme_id(meme, text, url, tags, info),
                             headers=auth_header)
    put_meme.check_that_status(HTTPStatus.BAD_REQUEST)


@allure.feature("Test API")
@allure.story("Put meme")
@allure.title("Put meme for unauthorized user")
def test_put_meme_unauthorized(meme_id, put_meme):
    body = {
        "text": "love memes changed"
    }
    put_meme.put_meme_id(meme_id, payload=body)
    put_meme.check_that_status(HTTPStatus.UNAUTHORIZED)


@allure.feature("Test API")
@allure.story("Delete meme")
@allure.title("Delete existing meme")
def test_delete_meme_id(auth_header, delete_meme, get_meme, meme_id):
    delete_meme.delete_meme_id(meme_id, auth_header)
    delete_meme.check_that_status(HTTPStatus.OK)
    delete_meme.check_meme_deleted(meme_id)
    get_meme.get_meme_id(meme_id, auth_header)
    get_meme.check_that_status(HTTPStatus.NOT_FOUND)


@allure.feature("Test API")
@allure.story("Delete false meme")
@allure.title("Delete not existing meme")
def test_delete_false_meme_id(auth_header, delete_meme):
    delete_meme.delete_meme_id(false_meme_id, auth_header)
    delete_meme.check_that_status(HTTPStatus.NOT_FOUND)


@allure.feature("Test API")
@allure.story("Delete meme")
@allure.title("Delete meme for unauthorized user")
def test_delete_meme_unauthorized(delete_meme, meme_id):
    delete_meme.delete_meme_id(meme_id)
    delete_meme.check_that_status(HTTPStatus.UNAUTHORIZED)
