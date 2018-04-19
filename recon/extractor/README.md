# Extractor : An HTML Sources Recon Tool

Extractor is a simple tool to retrieve interesting parts of an HTML source code during recon.

Currently retrieved informations are the following :

* `<a>` tags href attributes values
* `<img>` tags src attributes values
* `<script>` tags src attributes values
* Comments


## Usage

```
usage: extractor.py [-h] -u URLS [URLS ...] [-c COOKIES]

optional arguments:
  -h, --help            show this help message and exit
  -u URLS [URLS ...], --urls URLS [URLS ...]
                        <Required> Set URLs to check
  -c COOKIES, --cookies COOKIES
```

## Example

```
python3 extractor.py -u google.com
```

Output : 

```
====================================================================================
[+] Summary for target google.com
====================================================================================


[+] Found 24 <a> tags with href attribute from google.com

[+] https://www.google.ch/imghp?hl=de&tab=wi
[+] https://maps.google.ch/maps?hl=de&tab=wl
[+] https://play.google.com/?hl=de&tab=w8
[+] https://www.youtube.com/?gl=CH&tab=w1
[+] https://news.google.ch/nwshp?hl=de&tab=wn
[+] https://mail.google.com/mail/?tab=wm
[+] https://drive.google.com/?tab=wo
[+] https://www.google.ch/intl/de/options/
[+] http://www.google.ch/history/optout?hl=de
[+] /preferences?hl=de
[+] https://accounts.google.com/ServiceLogin?hl=de&passive=true&continue=https://www.google.com/
[+] /advanced_search?hl=de-CH&authuser=0
[+] /language_tools?hl=de-CH&authuser=0
[+] https://www.google.com/setprefs?sig=0_sOwq5agenZzDxLz-OMgqYL8pi2Q%3D&hl=en&source=homepage&sa=X&ved=0ahUKEwjvosnwysbaAhXC66QKHVhZB2sQ2ZgBCAU
[+] https://www.google.com/setprefs?sig=0_sOwq5agenZzDxLz-OMgqYL8pi2Q%3D&hl=fr&source=homepage&sa=X&ved=0ahUKEwjvosnwysbaAhXC66QKHVhZB2sQ2ZgBCAY
[+] https://www.google.com/setprefs?sig=0_sOwq5agenZzDxLz-OMgqYL8pi2Q%3D&hl=it&source=homepage&sa=X&ved=0ahUKEwjvosnwysbaAhXC66QKHVhZB2sQ2ZgBCAc
[+] https://www.google.com/setprefs?sig=0_sOwq5agenZzDxLz-OMgqYL8pi2Q%3D&hl=rm&source=homepage&sa=X&ved=0ahUKEwjvosnwysbaAhXC66QKHVhZB2sQ2ZgBCAg
[+] /intl/de/ads/
[+] http://www.google.ch/intl/de/services/
[+] https://plus.google.com/105772902399567012021
[+] /intl/de/about.html
[+] https://www.google.com/setprefdomain?prefdom=CH&prev=https://www.google.ch/&sig=__RWPeqtfqsgy0iG8fztnERhtfu6Y%3D
[+] /intl/de/policies/privacy/
[+] /intl/de/policies/terms/


[+] Found 1 <img> tags with src attribute from google.com

[+] /images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png


[-] No <script> tag with src attribute found in google.com HTML Sources !


[-] No comment tag found in google.com HTML Sources !

```

Extractor can also be used with authentication :

```
python3 extractor.py -u example.com mydomain.com -c '{"sessionID":"sessiontoken"}'
```