# Given a list of URLs, try to fetch content from
# each URL until the content returned is valid
def get_content_first_url(url_list, get_url_method):
    if len(url_list) <= 0:
        return False

    content = get_url_method(url_list[0])
    if content != False:
        # The request was successful
        return content
    else:
        del url_list[0]
        return get_content_first_url(url_list, get_url_method)
