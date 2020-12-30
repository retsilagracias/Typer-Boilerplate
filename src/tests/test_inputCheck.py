from horoscopecli.inputCheck import validInputCategoryOption, validInputSign, validInputDateOption

def test_belier_validInputSign():
    resultWithoutAccent = validInputSign("belier")
    resultWithAccent = validInputSign("bélier")
    assert resultWithAccent[0] == True
    assert resultWithAccent[1] == "aries"
    assert resultWithAccent[2] == "belier"
    assert resultWithoutAccent[0] == True
    assert resultWithoutAccent[1] == "aries"
    assert resultWithoutAccent[2] == "belier"

def test_Taureau_validInputSign():
    result = validInputSign("Taureau")
    assert result[0] == True
    assert result[1] == "taurus"
    assert result[2] == "taureau"

def test_gemeaux_validInputSign():
    resultWithoutAccent = validInputSign("gemeaux")
    resultWithAccent = validInputSign("gémeaux")
    assert resultWithAccent[0] == True
    assert resultWithAccent[1] == "gemini"
    assert resultWithAccent[2] == "gemeaux"
    assert resultWithoutAccent[0] == True
    assert resultWithoutAccent[1] == "gemini"
    assert resultWithoutAccent[2] == "gemeaux"

def test_CaNcer_validInputSign():
    result = validInputSign("CaNcer")
    assert result[0] == True
    assert result[1] == "cancer"
    assert result[2] == "cancer"

def test_lion_validInputSign():
    result = validInputSign("lion")
    assert result[0] == True
    assert result[1] == "leo"
    assert result[2] == "lion"

def test_viergE_validInputSign():
    result = validInputSign("viergE")
    assert result[0] == True
    assert result[1] == "virgo"
    assert result[2] == "vierge"

def test_balance_validInputSign():
    result = validInputSign("balance")
    assert result[0] == True
    assert result[1] == "libra"
    assert result[2] == "balance"

def test_Scorpion_validInputSign():
    result = validInputSign("Scorpion")
    assert result[0] == True
    assert result[1] == "scorpio"
    assert result[2] == "scorpion"

def test_sagiTtaire_validInputSign():
    result = validInputSign("sagiTtaire")
    assert result[0] == True
    assert result[1] == "sagittarius"
    assert result[2] == "sagittaire"

def test_capricorne_validInputSign():
    result = validInputSign("capricorne")
    assert result[0] == True
    assert result[1] == "capricorn"
    assert result[2] == "capricorne"

def test_Verseau_validInputSign():
    result = validInputSign("Verseau")
    assert result[0] == True
    assert result[1] == "aquarius"
    assert result[2] == "verseau"

def test_PoIsSoNs_validInputSign():
    result = validInputSign("PoIsSoNs")
    assert result[0] == True
    assert result[1] == "pisces"
    assert result[2] == "poissons"

def test_Aries_validInputSign():
    result = validInputSign("Aries")
    assert result[0] == True
    assert result[1] == ("aries")
    assert result[2] == ("belier")

def test_taurus_validInputSign():
    result = validInputSign("taurus")
    assert result[0] == True
    assert result[1] == ("taurus")
    assert result[2] == ("taureau")

def test_GeMiNi_validInputSign():
    result = validInputSign("GeMiNi")
    assert result[0] == True
    assert result[1] == ("gemini")
    assert result[2] == ("gemeaux")

def test_cancer_validInputSign():
    result = validInputSign("cancer")
    assert result[0] == True
    assert result[1] == ("cancer")
    assert result[2] == ("cancer")

def test_leo_validInputSign():
    result = validInputSign("leo")
    assert result[0] == True
    assert result[1] == ("leo")
    assert result[2] == ("lion")

def test_viergO_validInputSign():
    result = validInputSign("virgO")
    assert result[0] == True
    assert result[1] == ("virgo")
    assert result[2] == ("vierge")

def test_libra_validInputSign():
    result = validInputSign("libra")
    assert result[0] == True
    assert result[1] == ("libra")
    assert result[2] == ("balance")

def test_Scorpio_validInputSign():
    result = validInputSign("scorpio")
    assert result[0] == True
    assert result[1] == ("scorpio")
    assert result[2] == ("scorpion")

def test_sagittarius_validInputSign():
    result = validInputSign("sagittarius")
    assert result[0] == True
    assert result[1] == ("sagittarius")
    assert result[2] == ("sagittaire")

def test_CapriCorn_validInputSign():
    result = validInputSign("CapriCorn")
    assert result[0] == True
    assert result[1] == ("capricorn")
    assert result[2] == ("capricorne")

def test_aquarius_validInputSign():
    result = validInputSign("aquarius")
    assert result[0] == True
    assert result[1] == ("aquarius")
    assert result[2] == ("verseau")

def test_Pisces_validInputSign():
    result = validInputSign("Pisces")
    assert result[0] == True
    assert result[1] == ("pisces")
    assert result[2] == ("poissons")

def test_InvalidSign_validInputSign():
    result = validInputSign("InvalidSign")
    assert result[0] == False

def test_gemeau_validInputSign():
    result = validInputSign("gemeau")
    assert result[0] == False

def test_noOption_validInputDateOption():
    result = validInputDateOption(False, False, False, False)
    assert result[0] == True
    assert result[1] == "today"

def test_today_validInputDateOption():
    result = validInputDateOption(True, False, False, False)
    assert result[0] == True
    assert result[1] == "today"

def test_week_validInputDateOption():
    result = validInputDateOption(False, True, False, False)
    assert result[0] == True
    assert result[1] == "week"

def test_month_validInputDateOption():
    result = validInputDateOption(False, False, True, False)
    assert result[0] == True
    assert result[1] == "month"

def test_year_validInputDateOption():
    result = validInputDateOption(False, False, False, True)
    assert result[0] == True
    assert result[1] == "year"


