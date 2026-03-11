import allure


def configure_data(text, url, tags, info):
    with allure.step('Prepare test data for creating'):
        body = {
            "text": text,
            "url": url,
            "tags": tags,
            "info": info
        }
    return body


def configure_data_with_meme_id(meme_id, text, url, tags, info):
    with allure.step('Prepare test data for creating'):
        body = {
            "id": meme_id,
            "text": text,
            "url": url,
            "tags": tags,
            "info": info
        }
    return body