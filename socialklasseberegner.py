import os
import time
import sys

print("Velkommen til dette socialklasseberegner.")
time.sleep(2)
print("Den fungere ved at du indtaster dine oplysninger, hvorefter du vil blive placeret i en af de fem socialklasser.")
time.sleep(4)
print("Du vil også få en lille beskrivelse af den klasse du tilhører, samt kan du trkke på Y for at få mere information om den socialklasse du tilhører.")
time.sleep(4)

indkomst = int(input("Indkomst årligt (før skat): "))

time.sleep(3)
print(f"Du har nu indtastet din årlige indkomst før skat: {indkomst}.")
time.sleep(2)
print("Herunder skal du skrive hvor lang tid din videreuddanelse er i år. HUSK at folkeskolen ikke gælder. ")
time.sleep(2)
print("Har du ingen videreuddanelse skal du skrive 0.")

uddanelse = input("Hvor mange år er din videreuddanelse?: ")
uddanelse = int(uddanelse)

time.sleep(3)
print(f"Du har nu indtastet hvor mange år din videreuddanelse har taget: {uddanelse}.")
time.sleep(2)
print("Herunder skal du skrive hvilken socialklasse du er født/opvokset i.")
time.sleep(2)
print("Der er en kort beskrivelse omkring socialklasserne du kan bruge. Du skal skrive tallet ud for den socialklasse du er fra.")
time.sleep(4)

samfundsklasser = ["overklassen", "den højere middelklasse", "middelklassen", "arbejderklassen", "uden for arbejde"]

print("Herunder er en kort beskrivelse af de forskellige socialklasser:")
time.sleep(2)
print("1. Overklassen: Personer med en årlig indkomst over 1.2 millioner kroner før skat. Du har typisk en høj stilling som topleder, selvstændig eller noget ligende.")
time.sleep(4)
print("2. Den højere middelklasse: Personer med en årlig indkomst mellem 785.000 kroner før skat. Du har typisk en lang videreuddanelse som akademiker, læge, advokat eller noget ligende.")
time.sleep(4)
print("3. Middelklassen: Personer med en årlig indkomst mellem 484.000 kroner før skat. Du har typisk en kort eller mellemlang videreuddanelse som pædagog, folkeskolelærer, eller noget ligende.")
time.sleep(4)
print("4. Arbejderklassen: Personer med en årlig indkomst mellem 220.000 kroner før skat. Du har typisk en faglært eller ufaglært uddannelse som håndværker eller noget ligende.")
time.sleep(4)
print("5. Uden for arbejde: Personer med en årlig indkomst under 219.999 kroner før skat. Dette kan være pga psygiske sygdomme eller fysiske skader/sygdomme.")
time.sleep(4)

for i, klasse in enumerate(samfundsklasser, start=1):
    print(f"{i}. {klasse}")

valg = int(input("Skriv nummeret på din klasse: "))

valgt_klasse = samfundsklasser[valg - 1] 

overklassen = indkomst >= 1200000
højere_middelklasse = indkomst >= 785000 and uddanelse >= 8
middelklassen = indkomst >= 484000 and uddanelse >= 5
arbejderklassen = indkomst >= 220000 and uddanelse >= 1
uden_arbejde = indkomst >= 0 and uddanelse >= 0


if indkomst >= 1200000:
    print("Du er en del af overklassen, du udgør 45.600 personer. Det svarer til 1,8 procent af den 18-59 årlige befolkning i Danmark.")
    print("Vil du vide mere? tryk Y for ja og N for nej.")
    if indkomst >= 1200000 and valgt_klasse in ["den højere middelklasse", "middelklassen", "arbejderklassen", "uden for arbejde"]:
        print("Du er mønsterbryder!")
    svar = input("Skriv Y eller N: ")
    if svar == "Y":
        print("Overklassen udgør omkring 45.600 personer. Det svarer til 1,8 procent af den 18-59-årige befolkning i Danmark. En person i overklassen tjener i gennemsnit 2,9 millioner kroner om året før skat. Mange er selvstændigt erhvervsdrivende, topledere eller højtlønnede specialister. Det forudsætter nemlig en indkomst på over 1,2 millioner kroner at være med i den eksklusive klub, vi kalder overklassen. Overklassen er vokset kraftigt over de seneste årtier i takt med, at indkomstuligheden er steget. Deres familier udgør nu 3,6 procent af familierne i det danske klassesamfund. Børn, der fødes ind i overklassen, har samtidig de bedste kort på hånden helt fra livets start. De har en højere fødselsvægt, og de trives i skolen blandt klassekammerater, der ligner dem selv. De får de højeste afgangskarakterer, og de ender langt oftere selv i overklassen som voksne, end deres jævnaldrende.")
    else:
        print("Tak for din tid.")
        time.sleep(2)
        sys.exit()
elif indkomst >= 785000 and uddanelse >= 8:
    print("Du er en del af den højere middelklasse, du udgør 382.000 personer. Du har en lang videruddanelse og er særdeles højtlønet.")
    print("Vil du vide mere? tryk Y for ja og N for nej.")
    if indkomst >= 785000 and valgt_klasse in ["middelklassen", "arbejderklassen", "uden for arbejde"]:
        print("Du er mønsterbryder!")
    svar = input("Skriv Y eller N: ")
    if svar == "Y":
        print("Den højere middelklasse består af akademikere og højtlønnede specialister. I alt består klassen af 382.000 personer. Det er den klasse, der har oplevet den kraftigste vækst over de seneste årtier som følge af, at flere og flere tager en lang videregående uddannelse, mens stigende indkomstulighed også har betydet en stigning i antallet af personer tilhørende den højere middelklasse. Den højere middelklasse ligner på en række områder overklassen. De to klasser udgør tilsammen eliten. Sammenlignet med overklassen har den højere middelklasse ikke de samme økonomiske muskler og samme økonomisk kapital. Til gengæld har den kulturel kapital, som tydeligt kommer til udtryk, når man betragter børnenes skolegang. Deres trivsel, testresultater og afgangskarakterer peger i samme retning. Halvdelen af børnene fra den højere middelklasse gennemfører en lang videregående uddannelse som voksne.")
    else:
        print("Tak for din tid.")
        time.sleep(2)
        sys.exit()
elif indkomst >= 484000 and uddanelse >= 5:
    print("Du er en del af middelklassen, du udgør 644.000 personer. Dermed udgør du hver fjerde person i klasserne. Du placere dig på midten af klassesamfundet.")
    print("Vil du vide mere? tryk Y for ja og N for nej.")
    if indkomst >= 484000 and valgt_klasse in ["arbejderklassen", "uden for arbejde"]:
        print("Du er mønsterbryder!")
    svar = input("Skriv Y eller N: ")
    if svar == "Y":
        print("Middelklassen består af beskæftigede, der har en mere almindelig indkomst og oftest en kort eller mellemlang videregående uddannelse. Det gælder for eksempel pædagoger, folkeskolelærere, sygeplejersker, selvstændige og personer med ledelsesansvar. Middelklassen består af 644.000 personer. Dermed udgør de hver fjerde person i klasserne. Middelklassen placerer sig på en lang række socioøkonomiske markører midt i klassesamfundet, hvad enten det gælder indkomst, formue, børnenes skolepræstationer,  social arv, sundhedstilstand eller bolig. Middelklassen skiller sig dog ud i forhold til de andre klasser målt på beskæftigelse. 41 procent af middelklassen er offentligt ansat. Det er den højeste andel blandt klasserne. Her arbejder middelklassen typisk inden for undervisning, sundhed og sociale institutioner.")
    else:
        print("Tak for din tid.")
        time.sleep(2)
        sys.exit()
elif indkomst >= 220000 and uddanelse >= 1:
    print("Du er en del af arbejderklassen, du udgør fire ud af ti af danskerne. Dog førhen udgjorde du seks ud af 10 af danskerne.")
    print("Vil du vide mere? tryk Y for ja og N for nej.")
    if indkomst >= 220000 and valgt_klasse in ["uden for arbejde"]:
        print("Du er mønsterbryder!")
    svar = input("Skriv Y eller N: ")
    if svar == "Y":
        print("I arbejderklassen indgår de faglærte og ufaglærte arbejdere. De er den suverænt største gruppe i det danske klassesamfund, hvor fire ud af ti er i arbejderklassen. Men det er faktisk langt færre end før i tiden. Skruer vi tiden tre årtier tilbage var det seks ud af ti, der tilhørte arbejderklassen. I kraft af sin størrelse favner arbejderklassen bredt på tværs af arbejdsmarkedet. Det er industriteknikeren, håndværkeren, social- og sundhedsassistenten, chaufføren, butiks- eller rengøringsassistenten - for bare at nævne et par stykker. Arbejderklassen indeholder derfor også store forskelle, da spændet mellem faglærte og ufaglærte arbejdere målt på indkomst og jobsikkerhed er blevet større med tiden. Hvor arbejderklassen tidligere var bredt repræsenteret på tværs af landet og særligt vest for København, er arbejderne nu kommet i mindretal i og omkring de store byer.")
    else:
        print("Tak for din tid.")
        time.sleep(2)
        sys.exit()
elif indkomst >= 219999 and uddanelse >= 0:
    print("Du er en del af klassen uden for arbejde. Dette kan være pga psygiske psygdomme eller fysiske skader/sygdomme.")
    print("Vil du vide mere? tryk Y for ja og N for nej.")
    svar = input("Skriv Y eller N: ")
    if svar == "Y":
        print("Der er en gruppe af mennesker, der befinder sig langvarigt uden for arbejdsmarkedet, og som derfor hverken indgår i overklassen, den højere middelklasse, middelklassen eller arbejderklassen. I dag er hver femte i den arbejdsdygtige alder uden for arbejdsmarkedet i størstedelen af året og er samtidig ikke under uddannelse. Det svarer til omkring en halv million personer. Gruppens størrelse svinger i høj grad med udviklingen i de økonomiske konjunkturer. I opgangstider bliver der færre, der befinder sig langvarigt uden for arbejdsmarkedet, mens antallet stiger i nedgangstider. Det så man for eksempel i kølvandet på finanskrisen. Opgjort på familier er det 12 procent, der befinder sig langvarigt uden for arbejdsmarkedet. For børnene i disse familier, er der tale om svære opvækstvilkår. Det kan ses på præstationerne i skolen og senere i voksenlivet. Knap hver tredje af børnene ender selv langvarigt uden for arbejdsmarkedet.")
    else:
        print("Tak for din tid.")
        time.sleep(2)
        sys.exit()
else:
    print("Desværre kunne vi ikke placere dig i en af de fem socialklasser. Prøv igen og indtast dine oplysninger korrekt.")
    time.sleep(2)
    print("Har du gjort det korrekt bedes du kontakte udvikleren af dette program.")
    time.sleep(2)
    fejl = input("Skriv fejl herunder for at få en fejlkode: ")
    fejl = str.lower(fejl)
    if fejl == "fejl":
       print("[FEJL] Syntax fejl.")
       time.sleep(10)
       print("Tak for din tid. Lukker programmet om 2 minutter.")
       time.sleep(120)
       sys.exit()
    else:
        print(f"[FEJL] Ukendt kommando. {fejl} er ikke en gyldig kommando.")
        time.sleep(60)
        sys.exit()