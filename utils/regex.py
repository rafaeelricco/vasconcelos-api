# some regexs I used for data validation and parsing

text_regex = r"^[!?a-zA-Zà-úÀ-Ú0-9\s\,\.\-\_]+$"
link_regex = r"^(http|https)://"
year_regex = r"^[0-9]{4}$"
code_regex = r"^[0-9]+$"
price_regex = r"^R\$\d{1,4}(\.\d{3})*,\d{2}$"
email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
phone_regex = r"^\d{2}\d{4,5}\d{4}$"
city_regex = r"^[a-zA-Zà-úÀ-Ú\s]+$"
state_regex = r"^[a-zA-Zà-úÀ-Ú\s]+$"
parts_regex = r"^[/\"'a-zA-Zà-úÀ-Ú0-9\s\,\.\-\_]+$"
