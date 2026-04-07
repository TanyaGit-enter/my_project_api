import pytest
from endpoints.create_token import CreateToken
from endpoints.get_token import GetToken
from endpoints.create_meme import CreateMeme
from endpoints.get_meme import GetMeme
from endpoints.put_meme import PutMeme
from endpoints.delete_meme import DeleteMeme


@pytest.fixture(scope="session")
def auth_token():
    return CreateToken()


@pytest.fixture()
def get_auth_token():
    return GetToken()


@pytest.fixture()
def create_meme(auth_token):
    return CreateMeme()


@pytest.fixture()
def get_meme():
    return GetMeme()


@pytest.fixture()
def put_meme():
    return PutMeme()


@pytest.fixture()
def delete_meme():
    return DeleteMeme()


@pytest.fixture()
def auth_header(auth_token):
    return {"Authorization": f'{auth_token.get_token()}'}


@pytest.fixture()
def meme_id(auth_token, create_meme, get_meme, delete_meme):
    headers_auth = {"Authorization": f'{auth_token.get_token()}'}
    payload = {
        "text": "love memes",
        "url": "https://miro.medium.com/v2/resize:fit:1100/format:webp/1*OkVxoXBTygSKB8K-zbB7uQ.jpeg",
        "tags": ["love", "memes", "favorite"],
        "info": {"text1": "love memes", "text2": "memes are my favorite"}
    }
    create_meme.create_new_meme(payload, headers_auth)
    yield create_meme.meme_id
    meme = get_meme.get_meme_id(create_meme.meme_id)
    if meme:
        print('\ndeleting object')
        delete_meme.delete_meme_id(create_meme.meme_id)
