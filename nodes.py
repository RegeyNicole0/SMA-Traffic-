landmarks = {
    "TC_Circle": ["Ludo", "Daily"],
    #PPA # Phil. Port Authority
    #PCG # Coast Guard
    "Ludo": ["TC_Circle", "Gaisano_Old", "Mon_Print"],
    "Mon_Print": ["Halal_Meat", "Ludo"],
    "Nehal_Arc": ["Wet_Market", "Gaisano_Old"],
    "Gaisano_Old": ["Ukay_Market", "Novo", "Nehal_Arc", "Ludo"],
    "Pub_Market": ["Wet_Market", "Ukay_Market"],
    "Wet_Market": ["Pub_Market", "Nehal_Arc"],
    "Ukay_Market": ["Gaisano_Old", "Pub_Market", "AGR_Pharm"],
    "Daily": ["TC_Circle", "COOP_Fuel", "Fire_Safe"],
    "AGR_Pharm": ["Novo", "Ukay_Market", "Dunkin"],
    "Novo": ["Halal_Meat", "Gaisano_Old", "AGR_Pharm"],
    "Halal_Meat": ["Dunkin", "DNP", "Novo", "Mon_Print"],
    "Dunkin": ["AGR_Pharm", "Bike_Ent", "Halal_Meat"],
    "Bike_Ent": ["DNP", "Dunkin", "Pulis_Agu"],
    "DNP": ["Hala_Meat", "Bike_Ent", "RCBC_PNB"],
    "Fire_Safe": ["Daily"],
    "RCBC_PNB": ["DNP", "Rojon"],
    "Pulis_Agu": ["Bike_Ent", "Learnfast", "MC_Hotel"],
    "Learnfast": ["MC_Hotel", "Pulis_Agu", "Glo_Flash", "Tambacan"],
    "MC_Hotel": ["Pulis_Agu", "Pater", "Learnfast"],
    "Rojon": ["RCBC_PNB", "Penshoppe"],
    "IS_Rep": ["Fire_Safe", "Octagon"],
    "Tambacan": ["Learnfast", "Glo_Flash", "Fount_Acad"],
    "Glo_Fash": ["Learnfast", "Tambacan", "Red_Carp", "Pater"],
    "Pater": ["Glo_Flash", "MC_Hotel", "Mot_Race"],
    "Penshoppe": ["Galaxy_Mart", "Rojon"],
    "Octagon": ["COOP_Fuel", "IS_Rep", "ABest"],
    "COOP_Fuel": ["Daily", "Octagon", "Petron"],
    "Petron": ["COOP_Fuel", "Uncle_Brew"],
    "Fount_Acad": ["Red_Carp", "Tambacan", "GSIS"],
    "Red_Carp": ["Ilaya", "Fount_Acad", "Glo_Fash", "Mot_Race"],
    "Mot_Race": ["Red_Carp", "Pater", "Zoey"],
    "Galaxy_Mart": ["Penshoppe", "Unitop"],
    "ABest": ["Octagon", "TechTalk"],
    "TechTalk": ["ABest", "Frappella"],
    "Unitop": ["Galaxy_Mart", "Watsons"],
    "Zoey": ["Mot_Race", "Shoppe_24", "Ilaya"],
    "Ilaya": ["Zoey", "Ortiz", "GSIS", "Red_Carp"],
    "GSIS": ["Fount_Acad", "Ilaya"],
    #Concepcion # Purok Concepcion
    "CQ_Print": ["Coast_Wat", "Deja_Teu"],
    "Coast_Wat": ["CQ_Print", "Ziga_Teck", "New_Fash"],
    "New_Fash": ["Coast_Wat", "Pondoc", "Dexter"],
    "Dexter": ["New_Fash", "Ball_4k", "Waynsee", "Ortiz"],
    "Ball_4k": ["Dexter", "Orix", "Shoppe_24"],
    "Ortiz": ["Dexter", "Ilaya", "Shoppe_24"],
    "Shoppe_24": ["Ball_4k", "Zoey", "Ortiz"],
    "Watsons": ["Sec_Bank", "Unitop"],
    "Frappella": ["TechTalk", "Avila_Learn"],
    "Avila_Learn": ["Frappella", "Cathedral", "Tita_Fan"],
    "Cathedral": ["Sec_Bank", "Avila_Learn"],
    "Sec_Bank": ["BPI", "Watsons", "Cathedral"],
    "Deja_Teu": ["Ziga_Teck", "ICNHS", "CQ_Print"],
    "ICNHS": ["Sapp_Ara", "Deja_Teu", "Des_Wing"],
    "Ziga_Teck": ["Deja_Teu", "Sapp_Ara", "Pondoc", "Coast_Wat"],
    "Pondoc": ["Ziga_Teck", "New_Fash", "Mayo_Dia", "Waynsee"],
    "Waynsee": ["Pondoc", "Orix", "Pop_Rock", "Dexter"],
    "Orix": ["Ball_4k", "Waynsee", "Crown"],
    "Tita_Fan": ["Avila_Learn", "Mackis"],
    "Uncle_Brew": ["Emcor", "Petron", "Mackis"],
    "Mackis": ["Tita_Fan", "Epson", "Uncle_Brew", "Desmark"],
    "Epson": ["Mackis", "BPI", "Post_Off"],
    "BPI": ["St_Michaels", "Sec_Bank", "NCIP", "Epson"],
    "St_Michaels": ["Crown", "MShoes", "BPI"],
    "Crown": ["Pop_Rock", "Orix", "Mejia_Bldg", "St_Michaels"],
    "Pop_Rock": ["Doc_Uy", "Mayo_Dia", "Waynsee", "Crown"],
    "Mayo_Dia": ["Pondoc", "Lanastida", "Pop_Rock", "Sapp_Ara"],
    "Sapp_Ara": ["Mayo_Dia", "TomNToms", "Ziga_Teck", "ICNHS"],
    "Des_Wing": ["ICNHS", "TomNToms"],
    "TomNToms": ["Des_Wing", "Lanastida", "Sapp_Ara"],
    "Lanastida": ["TomNToms", "Mayo_Dia", "Doc_Uy"],
    "Doc_Uy": ["Mejia_Bldg", "Lanastida", "Pop_Rock"],
    "Mejia_Bldg": ["MShoes", "Crown", "Doc_Uy"],
    "MShoes": ["NCIP", "St_Michaels", "Mejia_Bldg"],
    "NCIP": ["Post_Off", "BPI", "PBB", "MShoes"],
    "Post_Off": ["Epson", "Desmark", "NCIP"],
    "Desmark": ["Post_Off", "Mackis", "Emcor"],
    "Emcor": ["Desmark", "Uncle_Brew"], 
    #Gaisano_Mall
    "PBB": ["NCIP", "Kylas"],
    "Phoenix_Gas": ["Palao_Mrkt", "Lanastida", "CoinSaver"],
    "CoinSaver": ["Chandis"],
    "Kylas": ["PBB", "Alemania"],
    "Alemania": ["Kylas", "MotTrad_Villa", "Bam_Doc"],
    "Chandis": ["MotTrad_Villa", "Meat_Shop", "Palao_Mrkt", "CoinSaver"],
    "MotTrad_Villa": ["Alemania", "Chandis", "Landbank"],
    "Bam_Doc": ["MercJupi_St", "Abund_Life"],
    "Palao_Mrkt": ["Chandis", "Ilgn_Deal", "Puregold"],
    "Ilgn_Deal": ["Palao_Mrkt", "COMELEC"],
    "COMELEC": ["Ilgn_Deal", "Puregold", "Megatech"],
    "Puregold": ["Palao_Mrkt", "Coco_Pet", "COMELEC"],
    "Megatech": ["Phoenix_LPG", "COMELEC", "Coco_Pet"],
    "Coco_Pet": ["Megatech", "Meat_Shop", "PC_Ilgn", "Puregold"],
    "Meat_Shop": ["Coco_Pet", "SYM", "Chandis"],
    "Landbank": ["MotTrad_Villa", "ColorChart"],
    "ColorChart": ["Landbank", "SYM"],
    "SYM": ["ColorChart", "Meat_Shop", "BDO_Network"],
    "BDO_Network": ["SYM", "PC_Ilgn"],
    "PC_Ilgn": ["BDO_Network", "Coco_Pet", "Phoenix_LPG"],
    "Phoenix_LPG": ["Megatech", "PC_Ilgn"]
}