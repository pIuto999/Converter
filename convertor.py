####ky eshte nje konvertor i madhesive punuar nga Erdajt Sopjani######

temaall = ["1", "te gjitha", "all", "listall", "list all", "Te gjitha", "tegjitha", "Tegjitha", "krejt", "Krejt"]
temaenergy = ["2", "energy", "energji", "energi", "Energy"]
temaelectriccurrent = ["3", "Electric Current", "ElectricCurrent", "electriccurrent", "electric current", "Electric current"]
temafrequency = ["4", "Frequency", "frekuenc", "frekuencat", "frequency"]
temalength = ["5", "Length", "length", "Gjatesi", "gjatesi", "gjatesia", "gjatesine", "Gjatesine"]

madhesit = ["meter", "kilometer", "centimeter", "ampere", "miliampere", "joule", "kilojoule"]
startlist = ["m", "km", "cm", "1", "2", "3","4","5","6","7",  "meter", "kilometer", "centimeter", "ampere", "miliampere", "joule", "kilojoule"]

km = ["km", "1", "kilometer"]
cm = ["cm", "3", "centimeter"]
m = ["m", "2", "meter"]
amper = ["amper", "4", "ampere", "Ampere"]
miliamper = ["5", "Miliampere", "miliamper", "mamper", "Mamper"]
joule = ["6", "joul", "joule", "Joule", "jul", "j"]
kilojoule = ["Kilojoule", "kilojoul", "kilojoule", "7", "kilojul", "kjoule", "kjoul", "Kjoul"]
watt = ["8", "watt", "Watt", "wat", "w"]
kilowatt = ["9", "Kilowatt", "kilowat", "Kwatt", "kwat", "kwatt", "kilowatt", "Kilowat"]
hertz = ["10", "hertz", "Hertz"]
kilohertz = ["11", "Kilohertz", "kilohertz", "khertz", "Khertz"]
megahertz = ["12", "megahertz", "Megahertz", "Mhertz", "mhertz"]
gigahertz = ["13", "gigahertz", "Gigahertz", "Ghertz", "ghertz"]






tema = input("Pershendetje, nga cila nga keto lloje te madhesive doni te konvertoni?\n"
             "1.Tregomi te gjitha\n"
             "2.Energy\n"
             "3.Electric Current\n"
             "4.Frequency\n"
             "5.Length(Gjatesine)\n")





if tema in temaall:
    start = input(
        "\nKeto jane te gjitha madhesit qe ne munde te konvertojme.\n"
        "Nga cila prej ketyre madhesive doni te konvertoni?\n"
        "1.km(kilometer)""\n"
        "2.m(meter)\n"
        "3.cm(centimeter)\n"
        "4.Ampere\n"
        "5.Miliampere\n"
        "6.Joule\n"
        "7.Kilojoule\n"
        "8.Watt(hour)\n"
        "9.Kilowatt(hour)\n"
        "10.Hertz\n"
        "11.Kilohertz\n"
        "12.Megahertz\n"
        "13.Gigahertz\n")

elif tema in temaenergy:
    start = input(
        "\nKeto jane madhesite energjike qe ne munde te konvertojme.\n"
        "Nga cila prej ketyre madhesive doni te konvertoni?\n"
        "6.Joule\n"
        "7.Kilojoule\n"
        "8.Watt(hour)\n"
        "9.Kilowatt(hour)\n")


elif tema in temaelectriccurrent:
    start = input(
        "\nKeto jane madhesite elektrike qe ne munde te konvertojme.\n"
        "Nga cila prej ketyre madhesive doni te konvertoni?\n"
        "4.Ampere\n"
        "5.Miliampere\n")


elif tema in temafrequency:
    start = input(
        "\nKeto jane madhesit e frekuences qe ne munde te konvertojme.\n"
        "Nga cila prej ketyre madhesive doni te konvertoni?\n"
        "10.Hertz\n"
        "11.Kilohertz\n"
        "12.Megahertz\n"
        "13.Gigahertz\n")


elif tema in temalength:
    start = input(
        "\nKeto jane madhesit e gjatesise qe ne munde te konvertojme.\n"
        "Nga cila prej ketyre madhesive doni te konvertoni?\n"
        "1.km(kilometer)""\n"
        "2.m(meter)\n"
        "3.cm(centimeter)\n")











if start in gigahertz:
    sasia = input("\nNe cilen mase doni te konvertoni Gigahertz?\n10.Hertz\n11.Kilohertz\n12.Megahertz\n")

    if sasia in hertz:
        convert = input("Sa Gigahertz doni te konvertoni ne Hertz\n")
        sasiahertz = float(convert)*1000000000
        print(f"\n{convert} Gigahertz jane {sasiahertz} Hertz!!")

    if sasia in kilohertz:
        convert = input("Sa Gigahertz doni te konvertoni ne Kilohertz\n")
        sasiakilohz = float(convert)*1000000
        print(f"\n{convert} Gigahertz jane {sasiakilohz} Kilohertz!!")

    if sasia in megahertz:
        convert = input("Sa Gigahertz doni te konvertoni ne Megahertz\n")
        sasiamegahz = float(convert)*1000
        print(f"\n{convert} Gigahertz jane {sasiamegahz} Megahertz!!")

    elif sasia not in hertz and sasia not in megahertz and sasia not in kilohertz:
        print("Ajo nuk eshte mase valide e konvertimit!!\n Ju lutemi hapeni programin perseri!!!\n")
        sasia = input("Ne cilen mase doni te konvertoni Megahertz?\n10.Hertz\n11.Kilohertz\n13.Gigahertz\n")

if start in megahertz:
    sasia = input("\nNe cilen mase doni te konvertoni Megahertz?\n10.Hertz\n11.Kilohertz\n13.Gigahertz\n")

    if sasia in hertz:
        convert = input("Sa Megahertz doni te konvertoni ne Hertz\n")
        sasiahertz = float(convert)*1000000
        print(f"\n{convert} Megahertz jane {sasiahertz} Hertz!!")

    if sasia in kilohertz:
        convert = input("Sa Megahertz doni te konvertoni ne Kilohertz\n")
        sasiakilohz = float(convert)*1000
        print(f"\n{convert} Megahertz jane {sasiakilohz} Kilohertz!!")

    if sasia in gigahertz:
        convert = input("Sa Megahertz doni te konvertoni ne Gigahertz\n")
        sasiagigahz = float(convert)/1000
        print(f"\n{convert} Megahertz jane {sasiagigahz} Gigahertz!!")

    elif sasia not in hertz and sasia not in gigahertz and sasia not in kilohertz:
        print("Ajo nuk eshte mase valide e konvertimit!!\n Ju lutemi hapeni programin perseri!!!\n")
        sasia = input("Ne cilen mase doni te konvertoni Megahertz?\n10.Hertz\n11.Kilohertz\n13.Gigahertz\n")


if start in kilohertz:
    sasia = input("\nNe cilen mase doni te konvertoni Kilohertz?\n10.Hertz\n12.Megahertz\n13.Gigahertz\n")

    if sasia in hertz:
        convert = input("Sa Kilohertz doni te konvertoni ne Hertz\n")
        sasiahertz = float(convert)*1000
        print(f"\n{convert} Kilohertz jane {sasiahertz} Hertz!!")

    if sasia in megahertz:
        convert = input("Sa Kilohertz doni te konvertoni ne Megahertz\n")
        sasiamegahertz = float(convert)/1000
        print(f"\n{convert} Kilohertz jane {sasiamegahertz} Megahertz!!")

    if sasia in gigahertz:
        convert = input("Sa Kilohertz doni te konvertoni ne Gigahertz\n")
        sasiagigahz = float(convert)/1000000
        print(f"\n{convert} Hertz jane {sasiagigahz} Gigahertz!!")

    elif sasia not in hertz and sasia not in gigahertz and sasia not in megahertz:
        print("Ajo nuk eshte mase valide e konvertimit!!\n Ju lutemi hapeni programin perseri!!!\n")
        sasia = input("Ne cilen mase doni te konvertoni Hertz?\n11.Kilohertz\n12.Megahertz\n13.Gigahertz\n")

if start in hertz:
    sasia = input("\nNe cilen mase doni te konvertoni Hertz?\n11.Kilohertz\n12.Megahertz\n13.Gigahertz\n")

    if sasia in kilohertz:
        convert = input("Sa Hertz doni te konvertoni ne Kilohertz\n")
        sasiakilohertz = float(convert)/1000
        print(f"\n{convert} Hertz jane {sasiakilohertz} Kilohertz!!")

    if sasia in megahertz:
        convert = input("Sa Hertz doni te konvertoni ne Megahertz\n")
        sasiamegahertz = float(convert)/1000000
        print(f"\n{convert} Hertz jane {sasiamegahertz} Megahertz!!")

    if sasia in gigahertz:
        convert = input("Sa Hertz doni te konvertoni ne Gigahertz\n")
        sasiagigahz = float(convert)/1000000000
        print(f"\n{convert} Hertz jane {sasiagigahz} Gigahertz!!")

    elif sasia not in kilohertz and sasia not in gigahertz and sasia not in megahertz:
        print("Ajo nuk eshte mase valide e konvertimit!!\n Ju lutemi hapeni programin perseri!!!\n")
        sasia = input("Ne cilen mase doni te konvertoni Hertz?\n11.Kilohertz\n12.Megahertz\n13.Gigahertz\n")


if start in watt:
    sasia = input("\nNe cilen mase doni te konvertoni watt?\n6.Joule\n7.Kiljoule\n9.Kilowatt(hour)\n")

    if sasia in joule:
        convert = input("Sa Watt doni te konvertoni ne Joule\n")
        sasiakilojoule = float(convert)*3600
        print(f"\n{convert} Kilowatt jane {sasiakilojoule} Joule!!")

    if sasia in kilowatt:
        convert = input("Sa Watt doni te konvertoni ne Kilowatt\n")
        sasiakilowatt = float(convert)/1000
        print(f"\n{convert} Watt jane {sasiakilowatt} Kilowatt!!")

    if sasia in kilojoule:
        convert = input("Sa Watt doni te konvertoni ne Kilojoule\n")
        sasiakilojoule = float(convert)*3.6
        print(f"\n{convert} Watt jane {sasiakilojoule} Kilojoule!!")

    elif sasia not in joule and sasia not in kilowatt and sasia not in kilojoule:
        print("Ajo nuk eshte mase valide e konvertimit!!\n Ju lutemi hapeni programin perseri!!!\n")
        sasia = input("Ne cilen mase doni te konvertoni watt?\n6.Joule\n7.Kiljoule\n9.Kilowatt(hour)\n")

if start in kilowatt:
    sasia = input("\nNe cilen mase doni te konvertoni Kilowatt?\n6.Joule\n7.Kiljoule\n8.Watt(hour)\n")

    if sasia in joule:
        convert = input("Sa Kilowatt doni te konvertoni ne Joule\n")
        sasiakilojoule = float(convert)*3600000
        print(f"\n{convert} Kilowatt jane {sasiakilojoule} Joule!!")

    if sasia in watt:
        convert = input("Sa Kilowatt doni te konvertoni ne Watt\n")
        sasiawatt = float(convert)*1000
        print(f"\n{convert} Kilowatt jane {sasiawatt} Watt!!")

    if sasia in kilojoule:
        convert = input("Sa Kilowatt doni te konvertoni ne Kilojoule\n")
        sasiakilojoule = float(convert)*3600
        print(f"\n{convert} Kilowatt jane {sasiakilojoule} Kilojoule!!")

    elif sasia not in joule and sasia not in watt and sasia not in kilojoule:
        print("Ajo nuk eshte mase valide e konvertimit!!\n Ju lutemi hapeni programin perseri!!!\n")
        sasia = input("Ne cilen mase doni te konvertoni Kilowatt?\n6.Joule\n7.Kiljoule\n8.Watt(hour)\n")

if start in kilojoule:
    sasia = input("\nNe cilen mase doni te konvertoni Kilojoule?\n6.Joule\n8.Watt(hour)\n9.Kilowatt(hour)\n")

    if sasia in joule:
        convert = input("Sa Kilojoule doni te konvertoni ne Joule\n")
        sasiakilojoule = float(convert)*1000
        print(f"\n{convert} Kilojoule jane {sasiakilojoule} Joule!!")

    if sasia in kilowatt:
        convert = input("Sa Kilojoule doni te konvertoni ne Kilowatt\n")
        sasiakilowatt = float(convert)/3600
        print(f"\n{convert} Kilojoule jane {sasiakilowatt} Kilowatt!!")

    if sasia in watt:
        convert = input("Sa Kilojoule doni te konvertoni ne Watt\n")
        sasiawatt = float(convert)/3.6
        print(f"\n{convert} Kilojoule jane {sasiawatt} Watt!!")

    elif sasia not in joule and sasia not in watt and sasia not in kilowatt:
        print("Ajo nuk eshte mase valide e konvertimit!!\n Ju lutemi hapeni programin perseri!!!\n")
        sasia = input("Ne cilen mase doni te konvertoni Kilojoule?\n6.Joule\n8.Watt(hour)\n9.Kilowatt(hour)\n")

if start in joule:
    sasia = input("\nNe cilen mase doni te konvertoni Joule?\n7.Kilojoule\n8.Watt(hour)\n9.Kilowatt(hour)\n")

    if sasia in kilojoule:
        convert = input("Sa Joule doni te konvertoni ne Kilojoule?\n")
        sasiajoul = float(convert)/1000
        print(f"\n{convert} Joule jane {sasiajoul} Kilojoule!!")

    if sasia in kilowatt:
        convert = input("Sa Joule doni te konvertoni ne Kilowatt\n")
        sasiakilowatt = float(convert)/3600000
        print(f"\n{convert} Joule jane {sasiakilowatt} Kilowatt!!")

    if sasia in watt:
        convert = input("Sa Joule doni te konvertoni ne Watt\n")
        sasiawatt = float(convert)/3600
        print(f"\n{convert} Joule jane {sasiawatt} Watt!!")

    elif sasia not in kilojoule and sasia not in watt and sasia not in kilowatt:
        print("Ajo nuk eshte mase valide e konvertimit!!\n Ju lutemi hapeni programin perseri!!!\n")
        sasia = input("Ne cilen mase doni te konvertoni Joule?\n7.Kilojoule\n8.Watt(hour)\n9.Kilowatt(hour)\n")

if start in miliamper:
    sasia = input("\nNe cilen mase doni te konvertoni miliamper?\n4.Ampere\n")

    if sasia in amper:
        convert = input("Sa Miliampere doni te konvertoni ne Ampere?\n")
        sasiamiliamper = float(convert)/1000
        print(f"\n{convert} Miliampere jane {sasiamiliamper} Ampere!!")

    elif sasia not in amper:
        print("Ajo nuk eshte mase valide e konvertimit!!\n Ju lutemi hapeni programin perseri!!!\n")
        sasia = input("Ne cilen mase doni te konvertoni miliamper?\n4.Ampere\n")

if start in amper:
    sasia = input("Ne cilen mase doni te konvertoni amper?\n5.Miliampere\n")

    if sasia in miliamper:
        convert = input("Sa ampere doni te konvertoni ne miliampere?\n")
        sasiaamper = float(convert)*1000
        print(f"\n{convert} Ampere jane {sasiaamper} Miliampere!!")

    elif sasia not in miliamper:
        print("Ajo nuk eshte mase valide e konvertimit!!\n Ju lutemi hapeni programin perseri!!!\n")
        sasia = input("Ne cilen mase doni te konvertoni amper?\n5.Miliampere\n")

if start in cm:
    sasia = input("\nNe cilen mase doni te konvertoni centimetrin?\n2.m(meter)\n1.km(kilomter)\n")

    if sasia in m:
        convert = input("Sa centimetra doni te konvertoni ne meter?\n")
        sasiacm = int(convert)/100
        print(f"\n{convert} centimetra jane {sasiacm} metra!!")

    elif sasia in km:
        convert = input("Sa centimetra doni te konvertoni ne kilomter?\n")
        sasiakm = float(convert)/100000
        print(f"\n{convert} centimetra jane {sasiakm} kilometra")

    elif sasia not in km and sasia not in m:
        print("Ajo nuk eshte mase valide e konvertimit!!\n Ju lutemi hapeni programin perseri!!!\n")
        sasia = input("Ne cilen mase doni te konvertoni centimetrin?\n2.m(meter)\n1.km(kilomter)\n")

if start in km:
    sasia = input("\nNe cilen mase doni te konvertoni kilometrin?\n2.m(meter)\n3.cm(centimeter)\n")

    if sasia in cm:
        convert = input("Sa kilometra doni te konvertoni ne centimeter?\n")
        sasiacm = float(convert)*100000
        print(f"\n{convert} kilometra jane {sasiacm} centimetra!!")

    elif sasia in m:
        convert = input("Sa kilometra doni te konvertoni ne meter?\n")
        sasiam = int(convert)*1000
        print(f"\n{convert} kilometra jane {sasiam} metra")

    elif sasia not in m and sasia not in cm:
        print("Ajo nuk eshte mase valide e konvertimit!!\n Ju lutemi hapeni programin perseri!!!\n")
        sasia = input("Ne cilen mase doni te konvertoni kilometrin?\n2.m(meter)\n3.cm(centimeter)\n")

if start in m:
    sasia = input("\nNe cilen mase doni te konvertoni metrin?\n3.cm(centimeter)\n1.km(kilomter)\n")

    if sasia in cm:
        convert = input("Sa metra doni te konvertoni ne centimeter?\n")
        sasiacm = int(convert)*100
        print(f"\n{convert} metra jane {sasiacm} centimetra!!")

    elif sasia in km:
        convert = input("Sa metra doni te konvertoni ne kilomter?\n")
        sasiakm = float(convert)/1000
        print(f"\n{convert} metra jane {sasiakm} kilometra")

    elif sasia not in km and sasia not in cm:
        print("Ajo nuk eshte mase valide e konvertimit!!\n Ju lutemi hapeni programin perseri!!!\n")
        sasia = input("Ne cilen mase doni te konvertoni metrin?\n3.cm(centimeter)\n1.km(kilomter)\n")

input("")
