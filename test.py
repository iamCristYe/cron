def dec_to_hex(decimal_value):
    """
    Convert a decimal integer to a hexadecimal string.
    """
    try:
        decimal_value = int(decimal_value)  # Ensure input is an integer
        hex_value = hex(decimal_value).replace("0x", "").lower()
        return hex_value
    except ValueError:
        return "Invalid decimal value!"


def hex_to_dec(hex_value):
    """
    Convert a hexadecimal string to a decimal integer.
    """
    try:
        decimal_value = int(hex_value, 16)
        return decimal_value
    except ValueError:
        return "Invalid hexadecimal value!"


def gen_str(code):
    hex_value = dec_to_hex(code)
    url = f"https://img.lemino.docomo.ne.jp/cms/{hex_value}/{hex_value}_h1.jpg"
    crid = "crid://plala.iptvf.jp/group/" + hex_value
    json_url = "https://if.lemino.docomo.ne.jp/v1/meta/contents?crid" + crid
    lemino_url = (
        "https://lemino.docomo.ne.jp/contents/"
        + base64.b64encode(crid.encode()).decode()
    )
    res_str = url + "\n" + json_url + "\n" + lemino_url + "\n" + str(code) + "\n"
    print(lemino_url)


import base64

with open("test.txt") as f:
    lines = f.readlines()
    #print(lines)
    for line in lines:
        if line.startswith("https://img.lemino.docomo.ne.jp/cms/"):
            #print(line.split("/")[4])
            gen_str(hex_to_dec(line.split("/")[4]))
