import sys
import requests
import re


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    # stáhneme stránku
    response = requests.get(url)

    # kontrola navratoveho kodu
    if response.status_code != 200:
        raise RuntimeError(f"Chyba stahovani, status code: {response.status_code}")

    # text stránky (jako string)
    html = response.text

    # najdeme všechny odkazy v <a href="...">
    hrefs = re.findall(r'<a\s+[^>]*href="([^"]+)"', html)

    return hrefs


if __name__ == "__main__":
    try:
        # načtení URL z příkazové řádky
        url = sys.argv[1]
        hrefs = download_url_and_get_all_hrefs(url)

        # vypíšeme nalezené odkazy (každý na nový řádek)
        for h in hrefs:
            print(h)

    # osetrete potencialni chyby pomoci vetve except
    except Exception as e:
        print(f"Program skoncil chybou: {e}")
