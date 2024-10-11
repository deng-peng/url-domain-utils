import re

def get_domain_from_url(url: str) -> str:
    # Handle empty or None input
    if not url:
        return ''

    # Convert to string, trim whitespace, and convert to lowercase
    url = str(url).strip().lower()

    # Replace commas with dots
    url = url.replace(',', '.')

    # Fix malformed URLs with triple slashes
    url = url.replace('///', '//')

    # Remove protocol prefix (http://, https://, etc.)
    url = re.sub(r'.+?//', '', url)

    # Remove path components after domain
    url = re.sub(r'/.*$', '', url)

    # Remove query string
    url = url.split('?')[0]

    # Handle email-style URLs (extract domain after @)
    if '@' in url:
        url = url.split('@')[1]

    # Remove www prefix and similar variations
    url = re.sub(r'[:.\/]*w{2,}[-\d]?\.+', '', url)

    return url