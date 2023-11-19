
# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)

from user import username, password

# InstaPy session
session = InstaPy(username=username, password=password, want_check_browser=False, headless_browser=False)
# Login
session.browser.get('https://instagram.com/accounts/login')
session.browser.implicitly_wait(5)

try:
    # Finde das Cookie-Popup-Element
    popup_buttons = session.browser.find_elements_by_xpath("//button[contains(text(),'Alle akzeptieren')]")

    # Überprüfe, ob das Element vorhanden ist
    if popup_buttons:
        # Klicke auf den Cookie-Popup-Button
        popup_buttons[0].click()
        print("Cookie-Popup geschlossen.")
    else:
        print("Cookie-Popup-Button nicht gefunden.")
except Exception as e:
    print(f'Fehler beim Schließen des Cookie-Popups: {e}')

# Führe den Login durch
session.login()

# Führe InstaPy-Aktionen durch (z.B., Likes nach Tags)
session.like_by_tags(["bananabread"], amount=5)

# Weitere InstaPy-Aktionen hier...

# Beende die InstaPy-Sitzung
session.end()
