'''
getapp.py

logs in to amazon.com and "buys" the free-app of the day

Created on Oct 16, 2011

@author: Chad Blomquist <chad.blomquist@gmail.com>

Requires mechanize. set your amazon.com username and password and run it. Enjoy.


As is, no warranty.

'''
import mechanize



amazon_username = ""
amazon_password = ""



def get_browser():
    br = mechanize.Browser()
    cj = mechanize.CookieJar()
    br.set_cookiejar(cj)
    
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    
    # debugging messages?
    #br.set_debug_http(True)
    #br.set_debug_redirects(True)
    #br.set_debug_responses(True)
    
    br.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 7.0b;Windows NT 5.1)')]
    
    br.clear_history()
    return br


if __name__ == "__main__":
    login_url = "https://www.amazon.com/ap/signin?_encoding=UTF8&openid.assoc_handle=usflex&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fmobile-apps%2Fb%3Fie%3DUTF8%26node%3D2350149011%26path%3D%252Fgp%252Fbrowse.html%26useRedirectOnSuccess%3D1%26ref%3Dmas_faad&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.pape.max_auth_age=0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select"

    br = get_browser()
    page = br.open(login_url)

    # the page has a couple \" that broke mechanize's parser, so git rid of them
    login_html = page.read().replace("\\", "")
    f = open("login.html", "w")
    f.write(login_html)
    f.close()

    br.open_local_file("login.html")
    br.select_form(name="signIn")
    br["email"] = amazon_username
    br["password"] = amazon_password
    br.method = "POST"

    response = br.submit()

    br.select_form(name="handleBuy")
    buy_response = br.submit();



