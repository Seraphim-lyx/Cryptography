

#prime number
p = 327454814830879107005084559983937540620999771927590724375920536641886208384200886100832287233189957813210371270334671807234945559603670066271190686868192951585598967591659932386815068908731683296587391491576094005762186571748971597872804471563462770253729404898993052640639229265746366764575629356117212612483
#generator
g = 3
#server public key
y_s = 270777412149929484001863390556812437650217372623256964473786247790081116293039231848340961609598350528119104342594404900999835706426623129587174483358517841533822239955333174228907887738542205020781526770060608262671493559426323466156179373688123191174601830514438528672878353156049874045807463762362474446252

pri_c = 250941525

pul_c = (g**pri_c)%p

print(pul_c)


