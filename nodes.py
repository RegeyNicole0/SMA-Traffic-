landmarks = {
    #Petron Sabayle to Wet Market
    "petron": [("coop_fuel", 140), ("uncle_brew", 170)],
    "coop_fuel": [("daily", 190), ("octagon", 160 ), ("petron", 140)],
    # "octagon": [("coop_fuel", 160)], one way
    "octagon": [("coop_fuel", 160), ("fire_safe", 95), ("abest", 50)], 
    # "abest": [("octagon", 50)], one way
    "abest": [("octagon", 50), ("techtalk", 56)],
    # "techtalk": [("abest", 56)], one way
    "techtalk": [("abest", 56), ("frapella", 32)],
    # "IS_Rep": ["fire_safe", "octagon"],
    # "fire_safe": [("daily", 117), ("rcbc", 45), ("pnb", 87)], one way
    "fire_safe": [("daily", 117), ("rcbc", 45), ("pnb", 87), ("octagon", 95)],
    "daily": [("tc_circle", 261), ("coop_fuel", 190) ("fire_safe",117)],
    "tc_circle": [("iligan_pier", 113), ("daily", 261), ("gaisano_old", 193)],
    "iligan_pier":[("tc_circle", 113), ("coast_guard", 110)],
    "coast_guard": [("nehal_arc", 141)],
    # "Ludo": ["tc_circle", "gaisano_old"],
    "nehal_arc": [("wet_market", 37), ("gaisano_old", 50)],
    "gaisano_old": [("nehal_arc", 50), ("ukay_market", 105), ("halal_meat", 114)],
    "wet_market": [("pub_market", 112)],
    "pub_market": [("ukay_market", 80)],
    "ukay_market": [("dunkin", 113)],
    "halal_meat": [("gaisano_old", 144), ("dunkin", 97), ("dnp", 99)],
    "dnp": [("halal_meat", 99), ("rcbc", 45), ("bike_ent", 88)],
    "rcbc": [("dnp", 45), ("fire_safe", 89), ("penshoppe", 103)],
    # "agr_pharm": ["novo", "ukay_market", "dunkin"],
    # "novo": ["halal_meat", "gaisano_old", "agr_pharm"],
    # "Rojon": ["RCBC_PNB", "Penshoppe"], 
    "dunkin": [("bike_ent", 96)],
    "bike_ent": [("pulis_agu", 39)],
    "pulis_agu": [("pera_mpc", 40),("mc_hotel", 63)],
    "mc_hotel": [("pater", 46), ("learnfast", 47)],
    "pater": [("glo_flash", 47), ("penshoppe", 85), ("mot_race", 46)],
    "penshoppe": [("rcbc", 103), ("galaxy_mart", 46), ("pater", 85), ("octagon", 91)],
    "galaxy_mart": [("penshoppe", 46), ("unitop", 46)],   
    "learnfast": [("glo_flash", 46), ("tambacan", 78)],
    "glo_flash": [("learnfast", 46), ("tambacan", 43), ("red_carp", 48), ("pater", 47)],
    "red_carp": [("ilaya", 36), ("fount_acad", 44) ("mot_race", 47)],
    "ilaya": [("ortiz", 36), ("gsis", 40)],
    "gsis": [("fount_acad", 37), ("new_flash", 70)],
    "zoey": [("shoppe_24", 36), ("ilaya", 45)],
    "mot_race": [("red_carp", 47), ("zoey", 39)],
    "tambacan": [("glo_flash", 43), ("fount_acad", 48)],
    "fount_acad": [("red_carp", 44), ("tambacan", 48), ("gsis", 37)],
    "unitop": [("galaxy_mart", 46) ,("watsons", 33) , ("zoey", 85)],
    "pnb": [("dnp", 45), ("Pulis_Agu", 89), ("penshoppe", 102), ("fire_safe", 87)],
    "pera_mpc": [("learnfast", 59)],

    # Purok Concepcion
    "cq_print": [("coast_wat", 58), ("deja_teu", 37)],
    "ziga_teck": [("deja_teu", 58), ("sapp_ara", 44), ("pondoc", 59)],
    "deja_teu": [("ziga_teck", 58), ("icnhs", 45), ("cq_print", 37)],
    "coast_wat": [("cq_print", 58), ("ziga_teck", 40),("new_flash",58)],
    "new_flash": [("gsis", 70), ("coast_wat", 58), ("pondoc", 41)],
    "waynsee": [("pondoc", 48), ("orix", 46), ("pop_rock", 48)],
    "pondoc": [("new_flash", 41), ("ziga_teck", 59), ("mayo_dia", 47), ("waynsee", 48)],
    "mayo_dia": [("pondoc", 47), ("lanastida", 53), ("pop_rock", 45), ("sapp_ara", 64)],
    "sapp_ara": [("mayo_dia", 64), ("tomntoms", 57), ("icnhs", 60)],
    "icnhs": [("sapp_ara", 60), ("deja_teu", 45), ("des_wing", 58)],
    "ortiz": [("dexter", 36), ("shoppe_24", 48)],
    "dexter": [("news_flash", 47), ("waynsee", 40)],
    "shoppe_24": [("ball_4k", 38)],
    "ball_4k": [("dexter", 46), ("orix", 40)],
    "orix": [("waynsee", 46), ("crown", 47)],
    "crown": [("pop_rock", 46), ("mejia_bldg", 60), ("st_michaels", 37)],
    "pop_rock": [("doc_uy", 58), ("mayo_dia", 45), ("crown", 46)],
    "st_michaels": [("crown", 37), ("mshoes", 57), ("bpi", 47)],
    "bpi": [("st_michaels", 47), ("sec_bank", 88), ("ncip", 59), ("epson", 51)],
    "sec_bank": [("bpi", 88), ("ball_4k", 85), ("watsons", 40)],
    "watsons": [("sec_bank", 40), ("unitop", 33)],
    "epson": [("bpi", 51), ("mackis", 50), ("post_off", 58)],
    # "mackis": [("tita_fan", 40), ("epson", 50), ("uncle_brew", 50)], one way
    "mackis": [("tita_fan", 40), ("epson", 50), ("uncle_brew", 50), ("desmark", 60)],
    "uncle_brew": [("mackis", 50), ("emcor", 61), ("petron", 170)],
    # "tita_fan": [("avila_learn", 45)],
    "tita_fan": [("mackis", 40), ("avila_learn", 45)],
    # "avila_learn": [("sec_bank", 94), ("frapella", 40)], one way
    "avila_learn": [("tita_fan", 45),("sec_bank", 94), ("frapella", 40)],
    # "frapella": [("techtalk", 32)], one way
    "frapella": [("avila_learn", 40), ("techtalk", 32)],
    # "cathedral": [("sec_bank", ), ("avila_learn", )],
    
    # National Road (ICNHS to GMALL)
    "des_wing": [("icnhs", 58), ("tomntoms", 59)],
    "tomntoms": [("des_wing", 59), ("sapp_ara", 57), ("lanastida", 63)],
    "lanastida": [("tomntoms", 63), ("mayo_dia", 53), ("phoenix_gas", 218), ("doc_uy", 46)],
    "doc_uy": [("lanastida", 46), ("pop_rock", 58), ("mejia_bldg", 46)],
    "mejia_bldg": [("doc_uy", 46), ("crown", 60), ("coinsaver", 208), ("mshoes", 37)],
    "mshoes": [("mejia_bldg", 37), ("st_michaels", 57), ("ncip", 47)],
    "ncip": [("mshoes", 47), ("bpi", 59), ("mottrad_villa", 292), ("post_off", 51)],
    "post_off": [("ncip", 51), ("epson", 58), ("desmark", 52)],
    "desmark": [("post_off", 52),("mackis", 60), ("emcor", 50)],
    "emcor": [("desmark", 50), ("uncle_brew", 61), ("gaisano_mall", 124)],
    "gaisano_mall": [("emcor", 124)],

    # Palao Market
    # "pbb": ["ncip", "kylas"],
    # "kylas": ["pbb", "Alemania"],
    # "Alemania": ["kylas", "mottrad_villa", "Bam_Doc"],
    "mottrad_villa": [("ncip", 292), ("chandis", 94), ("min_burger", 94)],
    "chandis": [("mottrad_villa", 94), ("meat_shop", 121)],
    "min_burger": [("meat_shop", 94), ("landbank", 116)],
    "coinsaver": [("chandis", 75), ("phoenix_gas", 99)],
    "phoenix_gas": [("coinsaver", 99), ("lanastida", 218), ("palao_mrkt", 67)],
    "palao_mrkt": [("chandis", 102), ("iligan_deal", 83), ("puregold", 60)],
    "iligan_deal": [("palao_mrkt", 83), ("comelec", 64)],
    "comelec": [("iligan_deal", 64), ("puregold", 82), ("megatech", 62)],
    "puregold": [("comelec", 82), ("palao_mrkt", 60), ("coco_pet", 63)],
    "megatech": [("phoenix_lpg", 57), ("comelec", 62), ("coco_pet", 80)],
    "coco_pet": [("megatech", 80), ("meat_shop", 106), ("pc_ilgn", 60), ("puregold", 63)],
    "meat_shop": [("coco_pet", 106), ("sym", 118)],
    "sym": [("bdo_network", 109), ("landbank", 100)],
    "bdo_network": [("sym", 109), ("pc_ilgn", 61)],
    "pc_ilgn": [("bdo_network", 61), ("coco_pet", 60), ("phoenix_lpg", 85)],
    "phoenix_lpg": [("megatech", 57), ("pc_ilgn", 85)],
    "landbank": [("min_burger", 116), ("sym", 100)],
    # "colorchart": ["landbank", "sym"]
}

# 3+ Lanes Roads (two-way)
    # Gaisano Mall to NCIP (6-lanes)
    # TC- Circle to Gaisano Old (6-lanes)
    # Co-op Fuel to TC-Circle (4-lanes)
    # NCIP to ICNHS (4-lanes)
    # Petron to Co-op Fuel (3-lanes)
    
# Two-Lane Roads
   
# Single-Lane Roads
    # Gaisano Mall to 