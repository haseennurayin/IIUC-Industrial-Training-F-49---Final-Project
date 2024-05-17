import os
from requests_html import HTMLSession

# Set the path to the Chromium executable
os.environ['PYTHON_CHROMIUM_EXECUTABLE_PATH'] = r'C:\path\to\your\chromium\chrome.exe'

def render_javascript(url):
    """
    Demonstrates how to render JavaScript using the `requests-html` library.
    This function fetches the page content after JavaScript has been executed.

    Parameters:
    url : str
        The URL of the website to scrape.

    Returns:
    None
    """
    session = HTMLSession()
    try:
        response = session.get(url)
        response.html.render()  # This will use the specified Chromium executable
        print("Rendered web page:", response.html.html)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()

def extract_information(url):
    """
    Extracts and prints specific information from a webpage using CSS selectors.

    Parameters:
    url : str
        The URL of the website to scrape.

    Returns:
    None
    """
    session = HTMLSession()
    try:
        response = session.get(url)
        response.html.render()  # Render JavaScript content if necessary

        # Extracting the first <h1> tag text
        title_tag = response.html.find('h1', first=True)
        if title_tag:
            print("Title: ", title_tag.text)
        else:
            print("No <h1> tag found.")

        # Extracting the datetime attribute from the first <time> tag
        datetime_element = response.html.find('time', first=True)
        if datetime_element and 'datetime' in datetime_element.attrs:
            datetime = datetime_element.attrs['datetime']
            print("Datetime attribute: ", datetime)
        else:
            print("No <time> tag with datetime attribute found.")

        # Advanced extraction using XPath (adjust the XPath as needed)
        temp = response.html.xpath('//div[contains(@class, "time-social-share-wrapper")]/div/time', first=True)
        if temp and 'datetime' in temp.attrs:
            datetime = temp.attrs['datetime']
            print("Advanced extraction datetime: ", datetime)
        else:
            print("No advanced datetime element found.")
        
        # Example: Extracting all links
        links = response.html.find('a')
        print(len(links), "links found:")
        for link in links:
            print("Link Text: ", link.text, "Link href: ", link.attrs['href'])

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()

def main():
    """
    Main function to execute the web scraping examples.
    """
    # Uncomment to test rendering JavaScript
    # print("Rendering JavaScript on a web page...")
    # render_javascript('https://example.com')

    print("\nExtracting information from a web page...")
    extract_information('https://www.prothomalo.com/world/usa/xnjy4uqwpv')

if __name__ == "__main__":
    main()
