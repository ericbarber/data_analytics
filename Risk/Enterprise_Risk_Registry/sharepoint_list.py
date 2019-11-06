from shareplum import Site, Office365
from bs4 import BeautifulSoup

from _secret import Secrets

def sharepoint_list(Secrets):
    """
    Connection to SharePoint API with password authentication
    """
    username = Secrets['sharepoint']['user_name']
    password = Secrets['sharepoint']['password']
    web_site = Secrets['sharepoint']['web_site']
    my_site = Secrets['sharepoint']['my_site']

    authcookie = Office365(
        my_site,
        username=username,
        password=password
    ).GetCookies()

    site = Site(
        web_site,
        authcookie=authcookie
    )

    result = site.List('Risk Registry').GetListItems()

    return result


def fix_html():
    """
    Utilizes beautifulSoup to extract comment from HTML format.
    returns list of dicts.
    """
    change_keys = {
    '2. Risk Statement', '11. Controls in Place', '17. Response Status Notes'
}

    return [{k: BeautifulSoup(v, 'html.parser').get_text() if k in change_keys else v for k,
      v in item.items()} for item in sharepoint_list(Secrets)]

def main():
    fix_html()

if __name__ == '__main__':
    main()