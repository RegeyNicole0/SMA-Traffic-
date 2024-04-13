#akong pag assign sa distance is from starting point(0) + d from sp to one node
# gibase nako ang distance from the node system
routes = {
# Tambo-Gerona
    "tambo_ger": [("emcor", 0), ("desmark", 50), ("mackis", 60), ("tita_fan", 40), ("avila_learn", 45), ("frappella", 40), 
                ("techtalk", 32), ("abest", 56), ("octagon", 50), ("coop_fuel", 160), ("daily", 190), ("tc_circle", 261), 
                ("gaisano_old", 193), ("ukay_market", 105), ("dunkin", 113), ("bike_ent", 96), ("pulis_agu", 39), ("mc_hotel", 63), 
                ("pater", 46), ("mot_race", 46), ("zoey", 39), ("shoppe_24", 36), ("ball_4k", 38), ("orix", 40), ("crown", 47), 
                ("mejia_bldg", 60), ("coinsaver", 208), ("chandis", 75), ("mottrad_Villa", 94), #("alemania", 0), ("kylas", 0), ("pbb", 0), 
                ("ncip", 292), ("post_off", 51), ("desmark", 52), ("emcor", 50)],


# Fuentes - buruun
    "fuentes": [("des_wing", 0), ("tomntoms", 59), ("lanastida", 63), ("phoenix_gas", 218), ("palao_mrkt", 67), ("puregold", 60), ("coco_pet", 63),
                ("pc_ilgn", 60), ("bdo_network", 61), ("sym", 109), #("colorchart", 0), 
                ("landbank", 100), ("min_burger", 116), ("mottrad_villa", 94), #("alemania", 0), ("kylas", 0), ("pbb", 0), 
                ("ncip", 292), ("bpi", 59), ("sec_bank", 88), ("watsons", 40), ("unitop", 33), ("galaxy_mart", 46),    
                ("penshoppe", 46), ("pnb", 102), ("fire_safe", 87), ("daily", 117), ("tc_circle", 261), ("iligan_pier", 113), ("coast_guard", 110),
                ("nehal_arc", 141), ("wet_market", 37), ("pub_market", 112), ("ukay_market", 80), ("dunkin", 113), ("bike_ent", 96), 
                ("pulis_agu", 39), ("mc_hotel", 63), ("pater", 46), ("mot_race", 46), ("zoey", 39), ("ilaya", 45), ("gsis", 40), ("new_flash", 70),
                ("pondoc", 41), ("ziga_teck", 59), ("sapp_ara", 44), ("tomntoms", 57), ("des_wing", 59)],



# Ditucalan
    "ditucalan": [("des_wing", 0), ("tomntoms", 59), ("lanastida", 63), ("phoenix_gas", 218), ("palao_mrkt", 67), ("puregold", 60), ("coco_pet", 63),
                ("pc_ilgn", 60), ("bdo_network", 61), ("sym", 109), #("colorchart", 0), 
                ("landbank", 100), ("min_burger", 116), ("mottrad_villa", 94), #("alemania", 0), ("kylas", 0), ("pbb", 0), 
                ("ncip", 292), ("bpi", 59), ("sec_bank", 88), ("watsons", 40), ("unitop", 33), ("galaxy_mart", 46),    
                ("penshoppe", 46), ("pnb", 102), ("fire_safe", 87), ("daily", 117), ("tc_circle", 261), ("iligan_pier", 113), ("coast_guard", 110),
                ("nehal_arc", 141), ("wet_market", 37), ("pub_market", 112), ("ukay_market", 80), ("dunkin", 113), ("bike_ent", 96), 
                ("pulis_agu", 39), ("pera_mpc", 40), ("learnfast", 59), ("tambacan", 78), ("celdran", 1180), ("macapagal", 543), ("ditucalan", 13900), 
                ("des_wing", 15200)],


# Canaway-Santiago-Bayug
    "canaway": [("h30", 0), ("rmn_dxic", 701), ("crossing", 700), ("petron", 2600), ("coop_fuel", 140), ("daily", 190), ("tc_circle", 261), ("iligan_pier", 113),
                ("coast_guard", 110), ("nehal_arc", 141), ("wet_market", 37), ("pub_market", 112), ("ukay_market", 80), ("dunkin", 113), 
                ("bike_ent", 96), ("pulis_agu", 39), ("mc_hotel", 63), ("pater", 46), ("mot_race", 46), ("zoey", 39), ("unitop", 85), 
                ("techtalk", 93), ("frapella", 32), ("avila_learn", 40), ("tita_fan", 45), ("mackis", 40), ("desmark", 60), ("emcor", 50), ("inc", 0), ("paseo", 0)
                ("h30", 0), ("rmn_dxic", 0)],


# Tambo-Hinaplanon-San Roque-Gerona (and -Gerona-SanRoque)
    "tambo-hinaplanon": [("vanitea", 0), ("petron", 0), ("coop_fuel", 140), ("daily", 190), ("tc_circle", 261), ("iligan_pier", 113),
                ("coast_guard", 110), ("nehal_arc", 141), ("wet_market", 37), ("pub_market", 112), ("ukay_market", 80), ("dunkin", 113), 
                ("bike_ent", 96), ("pulis_agu", 39), ("mc_hotel", 63), ("pater", 46), ("mot_race", 46), ("zoey", 39), ("unitop", 85), 
                ("techtalk", 93), ("frapella", 32), ("avila_learn", 40), ("tita_fan", 45), ("mackis", 40), ("desmark", 60), ("emcor", 50), ("vanitea", 0)],



# Hinaplanon-Cabaro
    "hinaplanon-cabaro": [("vanitea", 0), ("petron", 0), ("coop_fuel", 140), ("daily", 190), ("tc_circle", 261), ("iligan_pier", 113),
                ("coast_guard", 110), ("nehal_arc", 141), ("wet_market", 37), ("pub_market", 112), ("ukay_market", 80), ("dunkin", 113), 
                ("bike_ent", 96), ("pulis_agu", 39), ("mc_hotel", 63), ("pater", 46), ("mot_race", 46), ("zoey", 39), ("unitop", 85), 
                ("techtalk", 93), ("frapella", 32), ("avila_learn", 40), ("tita_fan", 45), ("mackis", 40), ("desmark", 60), ("emcor", 50), ("vanitea", 0)],


# Bayug-Santiago-IBJT
    "bayug-santiago": [("vanitea", 0), ("petron", 0), ("coop_fuel", 140), ("daily", 190), ("tc_circle", 261), ("iligan_pier", 113),
                ("coast_guard", 110), ("nehal_arc", 141), ("wet_market", 37), ("pub_market", 112), ("ukay_market", 80), ("dunkin", 113), 
                ("bike_ent", 96), ("pulis_agu", 39), ("mc_hotel", 63), ("pater", 46), ("mot_race", 46), ("zoey", 39), ("unitop", 85), 
                ("techtalk", 93), ("frapella", 32), ("avila_learn", 40), ("tita_fan", 45), ("mackis", 40), ("desmark", 60), ("emcor", 50), ("vanitea", 0)],


# Luinab-Bahayan-Manrique
    "luinab": [("vanitea", 0), ("petron", 0), ("coop_fuel", 140), ("daily", 190), ("tc_circle", 261), ("iligan_pier", 113),
                ("coast_guard", 110), ("nehal_arc", 141), ("wet_market", 37), ("pub_market", 112), ("ukay_market", 80), ("dunkin", 113), 
                ("bike_ent", 96), ("pulis_agu", 39), ("mc_hotel", 63), ("pater", 46), ("mot_race", 46), ("zoey", 39), ("unitop", 85), 
                ("techtalk", 93), ("frapella", 32), ("avila_learn", 40), ("tita_fan", 45), ("mackis", 40), ("desmark", 60), ("emcor", 50), ("vanitea", 0)],


# Bagong Silang
    "bagong_silang": [("vanitea", 0), ("petron", 0), ("coop_fuel", 140), ("daily", 190), ("tc_circle", 261), ("iligan_pier", 113),
                ("coast_guard", 110), ("nehal_arc", 141), ("wet_market", 37), ("pub_market", 112), ("ukay_market", 80), ("dunkin", 113), 
                ("bike_ent", 96), ("pulis_agu", 39), ("mc_hotel", 63), ("pater", 46), ("mot_race", 46), ("zoey", 39), ("unitop", 85), 
                ("techtalk", 93), ("frapella", 32), ("avila_learn", 40), ("tita_fan", 45), ("mackis", 40), ("desmark", 60), ("emcor", 50), ("vanitea", 0)],

 
# Sta. Filomena-Dalipuga-Centennial
#vanitea, petron, coop_fuel, daily, tc_circle, gaisano_old, halal_meat, dnp, pnb, penshoppe, galaxy_mart, unitop, techtalk, frapella, avila_learn, tita_fan, mackis, desmark,   emcor, vanitea
    "sta_dalipuga": [("vanitea", 0), ("petron", 0), ("coop_fuel", 140), ("daily", 190), ("tc_circle", 261), ("gaisano", 193), ("halal_meat", 114),
                     ("dnp", 99), ("pnb", 45), ("penshoppe", 102), ("galaxy_mart", 46), ("unitop", 46), ("tecktalk", 93), ("frapella", 32), 
                     ("avila_learn", 40), ("tita_fan", 45), ("mackis", 40), ("desmark", 60), ("emcor", 50), ("vanitea", 0)],



}
