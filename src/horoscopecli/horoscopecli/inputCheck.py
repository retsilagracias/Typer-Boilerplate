def validInputSign(sign: str):
    """
    Take a sign as argument
    If sign is valid, returns a tuple: (True, 'sign in english', 'sign in french')
    If sign is not valid, returns a tuple: (False, 'Error message', '')
    """
    if sign == "bélier":
        sign = "belier"
    if sign == "gémeaux":
        sign = "gemeaux"
    signsEn = ["aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces"]
    signsFr = ["belier", "taureau", "gemeaux", "cancer", "lion", "vierge", "balance", "scorpion", "sagittaire", "capricorne", "verseau", "poissons"]
    if sign.lower() in signsEn:
        return (True, sign.lower(), signsFr[signsEn.index(sign.lower())])
    elif sign.lower() in signsFr:
        return (True, signsEn[signsFr.index(sign.lower())], sign.lower())
    return (False, "ERROR: It seems you have entered a wrong astrological sign.", "")