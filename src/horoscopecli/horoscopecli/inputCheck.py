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

def validInputDateOption(today: bool, week: bool, month: bool, year: bool):
    args = [today, week, month, year]
    labels = [("today", "daily"), ("week", "weekly"), ("month", "monthly"), ("year","yearly")]
    flags = [labels[i] for i in range(4) if args[i]]
    if len(flags) > 1:
        return (False, "ERROR: It seems you have put more than one option, chose between DAY, WEEK, MONTH or YEAR.")
    if len(flags) == 0:
        return (True, "today", "daily")
    return (True, flags[0][0], flags[0][1])


def validInputCategoryOption(love: bool, work: bool, finance: bool, self: bool, family: bool):
    args = [love, work, finance, self, family]
    labels = ["love", "work", "finance", "self", "family"]
    flags = [labels[i] for i in range(5) if args[i]]
    if len(flags) > 1:
        return (False, "ERROR: It seems you have put more than one option, chose between LOVE, WORK, FINANCE, SELF or FAMILY.")
    if len(flags) == 0:
        return (True, "self")
    return (True, flags[0])