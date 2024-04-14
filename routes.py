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
                ("e_fix", 50), ("landbank", 50), ("min_burger", 116), ("mottrad_villa", 94), #("alemania", 0), ("kylas", 0), ("pbb", 0), 
                ("ncip", 292), ("bpi", 59), ("sec_bank", 88), ("watsons", 40), ("unitop", 33), ("galaxy_mart", 46),    
                ("penshoppe", 46), ("pnb", 103), ("fire_safe", 89), ("daily", 117), ("tc_circle", 261), ("iligan_pier", 113), ("coast_guard", 110),
                ("nehal_arc", 141), ("wet_market", 37), ("pub_market", 112), ("ukay_market", 80), ("dunkin", 113), ("bike_ent", 96), 
                ("pulis_agu", 39), ("mc_hotel", 63), ("pater", 46), ("mot_race", 46), ("zoey", 39), ("ilaya", 45), ("gsis", 40), ("new_flash", 70),
                ("pondoc", 41), ("ziga_teck", 59), ("sapp_ara", 44), ("tomntoms", 57), ("des_wing", 59)],



# Ditucalan
    "ditucalan": [("des_wing", 0), ("tomntoms", 59), ("lanastida", 63), ("phoenix_gas", 218), ("palao_mrkt", 67), ("puregold", 60), ("coco_pet", 63),
                ("pc_ilgn", 60), ("bdo_network", 61), ("sym", 109), #("colorchart", 0), 
                ("e_fix", 50), ("landbank", 50), ("min_burger", 116), ("mottrad_villa", 94), #("alemania", 0), ("kylas", 0), ("pbb", 0), 
                ("ncip", 292), ("bpi", 59), ("sec_bank", 88), ("watsons", 40), ("unitop", 33), ("galaxy_mart", 46),    
                ("penshoppe", 46), ("pnb", 102), ("fire_safe", 87), ("daily", 117), ("tc_circle", 261), ("iligan_pier", 113), ("coast_guard", 110),
                ("nehal_arc", 141), ("wet_market", 37), ("pub_market", 112), ("ukay_market", 80), ("dunkin", 113), ("bike_ent", 96), 
                ("pulis_agu", 39), ("pera_mpc", 40), ("learnfast", 59), ("tambacan", 78)],


# Canaway-Santiago-Bayug
    "canaway": [("vanitea", 0), ("petron", 243), ("coop_fuel", 140), ("daily", 190), ("tc_circle", 261), ("iligan_pier", 113),
                ("coast_guard", 110), ("nehal_arc", 141), ("wet_market", 37), ("pub_market", 112), ("ukay_market", 80), ("dunkin", 113), 
                ("bike_ent", 96), ("pulis_agu", 39), ("mc_hotel", 63), ("pater", 46), ("mot_race", 46), ("zoey", 39), ("unitop", 85), 
                ("techtalk", 93), ("frapella", 32), ("avila_learn", 40), ("tita_fan", 45), ("mackis", 40), ("desmark", 60), ("emcor", 50),
                ("gaisano_mall", 124), ("vanitea", 192)],


# Tambo-Hinaplanon-San Roque-Gerona (and -Gerona-SanRoque)
    "tambo-hinaplanon": [("vanitea", 0), ("petron", 243), ("coop_fuel", 140), ("daily", 190), ("tc_circle", 261), ("iligan_pier", 113),
                ("coast_guard", 110), ("nehal_arc", 141), ("wet_market", 37), ("pub_market", 112), ("ukay_market", 80), ("dunkin", 113), 
                ("bike_ent", 96), ("pulis_agu", 39), ("mc_hotel", 63), ("pater", 46), ("mot_race", 46), ("zoey", 39), ("unitop", 85), 
                ("techtalk", 93), ("frapella", 32), ("avila_learn", 40), ("tita_fan", 45), ("mackis", 40), ("desmark", 60), ("emcor", 50), 
                ("gaisano_mall", 124), ("vanitea", 192)],



# Hinaplanon-Cabaro
    "hinaplanon-cabaro": [("vanitea", 0), ("petron", 243), ("coop_fuel", 140), ("daily", 190), ("tc_circle", 261), ("iligan_pier", 113),
                ("coast_guard", 110), ("nehal_arc", 141), ("wet_market", 37), ("pub_market", 112), ("ukay_market", 80), ("dunkin", 113), 
                ("bike_ent", 96), ("pulis_agu", 39), ("mc_hotel", 63), ("pater", 46), ("mot_race", 46), ("zoey", 39), ("unitop", 85), 
                ("techtalk", 93), ("frapella", 32), ("avila_learn", 40), ("tita_fan", 45), ("mackis", 40), ("desmark", 60), ("emcor", 50), 
                ("gaisano_mall", 124), ("vanitea", 192)],


# Bayug-Santiago-IBJT
    "bayug-santiago": [("vanitea", 0), ("petron", 243), ("coop_fuel", 140), ("daily", 190), ("tc_circle", 261), ("iligan_pier", 113),
                ("coast_guard", 110), ("nehal_arc", 141), ("wet_market", 37), ("pub_market", 112), ("ukay_market", 80), ("dunkin", 113), 
                ("bike_ent", 96), ("pulis_agu", 39), ("mc_hotel", 63), ("pater", 46), ("mot_race", 46), ("zoey", 39), ("unitop", 85), 
                ("techtalk", 93), ("frapella", 32), ("avila_learn", 40), ("tita_fan", 45), ("mackis", 40), ("desmark", 60), ("emcor", 50), 
                ("gaisano_mall", 124), ("vanitea", 192)],


# Luinab-Bahayan-Manrique
    "luinab": [("vanitea", 0), ("petron", 243), ("coop_fuel", 140), ("daily", 190), ("tc_circle", 261), ("iligan_pier", 113),
                ("coast_guard", 110), ("nehal_arc", 141), ("wet_market", 37), ("pub_market", 112), ("ukay_market", 80), ("dunkin", 113), 
                ("bike_ent", 96), ("pulis_agu", 39), ("mc_hotel", 63), ("pater", 46), ("mot_race", 46), ("zoey", 39), ("unitop", 85), 
                ("techtalk", 93), ("frapella", 32), ("avila_learn", 40), ("tita_fan", 45), ("mackis", 40), ("desmark", 60), ("emcor", 50), 
                ("gaisano_mall", 124), ("vanitea", 192)],

# Bagong Silang
    "bagong_silang": [("vanitea", 0), ("petron", 243), ("coop_fuel", 140), ("daily", 190), ("tc_circle", 261), ("iligan_pier", 113),
                ("coast_guard", 110), ("nehal_arc", 141), ("wet_market", 37), ("pub_market", 112), ("ukay_market", 80), ("dunkin", 113), 
                ("bike_ent", 96), ("pulis_agu", 39), ("mc_hotel", 63), ("pater", 46), ("mot_race", 46), ("zoey", 39), ("unitop", 85), 
                ("techtalk", 93), ("frapella", 32), ("avila_learn", 40), ("tita_fan", 45), ("mackis", 40), ("desmark", 60), ("emcor", 50), 
                ("gaisano_mall", 124), ("vanitea", 192)],
 
# Sta. Filomena-Dalipuga-Centennial
    "sta_dalipuga": [("vanitea", 0), ("petron", 243), ("coop_fuel", 140), ("daily", 190), ("tc_circle", 261), ("gaisano_old", 193), ("halal_meat", 114),
                     ("dnp", 99), ("pnb", 45), ("penshoppe", 102), ("galaxy_mart", 46), ("unitop", 46), ("tecktalk", 93), ("frapella", 32), 
                     ("avila_learn", 40), ("tita_fan", 45), ("mackis", 40), ("desmark", 60), ("emcor", 50), ("gaisano_mall", 124), ("vanitea", 192)],



# Dalipuga - Vista Village
    "dalipuga-vista": [("vanitea", 0), ("petron", 243), ("coop_fuel", 140), ("daily", 190), ("tc_circle", 261), ("gaisano_old", 193), ("halal_meat", 114),
                     ("dnp", 99), ("pnb", 45), ("penshoppe", 102), ("galaxy_mart", 46), ("unitop", 46), ("tecktalk", 93), ("frapella", 32), 
                     ("avila_learn", 40), ("tita_fan", 45), ("mackis", 40), ("desmark", 60), ("emcor", 50), ("gaisano_mall", 124), ("vanitea", 192)],


# Kalubihon
    "kalubihon": [("vanitea", 0), ("petron", 243), ("coop_fuel", 140), ("daily", 190), ("tc_circle", 261), ("gaisano_old", 193), ("halal_meat", 114),
                     ("dnp", 99), ("pnb", 45), ("penshoppe", 102), ("galaxy_mart", 46), ("unitop", 46), ("tecktalk", 93), ("frapella", 32), 
                     ("avila_learn", 40), ("tita_fan", 45), ("mackis", 40), ("desmark", 60), ("emcor", 50), ("gaisano_mall", 124), ("vanitea", 192)],



# San Roque - Lambaguhon
    "san_lambaguhon": [("vanitea", 0), ("petron", 243), ("coop_fuel", 140), ("daily", 190), ("tc_circle", 261), ("gaisano_old", 193), ("halal_meat", 114),
                     ("dnp", 99), ("pnb", 45), ("penshoppe", 102), ("galaxy_mart", 46), ("unitop", 46), ("tecktalk", 93), ("frapella", 32), 
                     ("avila_learn", 40), ("tita_fan", 45), ("mackis", 40), ("desmark", 60), ("emcor", 50), ("gaisano_mall", 124), ("vanitea", 192)],


# Tambacan
    "tambacan": [("tambacan", 0), ("fount_acad", 48), ("gsis", 37), ("new_flash", 70), ("pondoc", 41), ("mayo_dia", 47), ("lanastida", 53),
                 ("phoenix_gas", 218), ("palao_mrkt", 67), ("puregold", 60), ("coco_pet", 63), ("meat_shop", 106), ("pugaan_term", 50), ("min_burger", 45), ("mottrad_villa", 94),
                 ("ncip", 292), ("bpi", 59), ("sec_bank", 88), ("watsons", 40), ("shoppe_24", 85), ("ortiz", 45), ("qa_plaza", 43), ("citi_alley", 65),
                 ("coast_wat", 35), ("ziga_teck", 40), ("sapp_ara", 44), ("tomntoms", 57), ("des_wing", 59)],


# Tubod-Rosario Heights
    "tubod_rosario": [("des_wing", 0), ("tomntoms", 59), ("lanastida", 63), ("doc_uy", 46), ("mejia_bldg", 46), ("coinsaver", 208), ("chandis", 75),
              ("mottrad_villa", 94), ("ncip", 292), ("bpi", 59), ("sec_bank", 88), ("watsons", 40), ("shoppe_24", 85), ("ortiz", 45), 
              ("qa_plaza", 43), ("citi_alley", 65), ("coast_wat", 35), ("ziga_teck", 40), ("sapp_ara", 44), ("tomntoms", 57), ("des_wing", 59)],


# Tubod-Carbide Village
    "tubod_carbide": [("des_wing", 0), ("tomntoms", 59), ("lanastida", 63), ("doc_uy", 46), ("mejia_bldg", 46), ("coinsaver", 208), ("chandis", 75),
                    ("mottrad_villa", 94), ("ncip", 292), ("bpi", 59), ("sec_bank", 88), ("watsons", 40), ("shoppe_24", 85), ("ortiz", 45), 
                    ("qa_plaza", 43), ("citi_alley", 65), ("coast_wat", 35), ("ziga_teck", 40), ("sapp_ara", 44), ("tomntoms", 57), ("des_wing", 59)],        


# Tubod-Orellana-C3
    "tubod_orellana": [("des_wing", 0), ("tomntoms", 59), ("lanastida", 63), ("doc_uy", 46), ("mejia_bldg", 46), ("coinsaver", 208), ("chandis", 75),
                    ("mottrad_villa", 94), ("ncip", 292), ("bpi", 59), ("sec_bank", 88), ("watsons", 40), ("shoppe_24", 85), ("ortiz", 45), 
                    ("qa_plaza", 43), ("citi_alley", 65), ("coast_wat", 35), ("ziga_teck", 40), ("sapp_ara", 44), ("tomntoms", 57), ("des_wing", 59)],                        


# Baraas-Dona Maria
    "baraas": [("des_wing", 0), ("tomntoms", 59), ("lanastida", 63), ("doc_uy", 46), ("mejia_bldg", 46), ("coinsaver", 208), ("chandis", 75),
                ("mottrad_villa", 94), ("ncip", 292), ("bpi", 59), ("sec_bank", 88), ("watsons", 40), ("shoppe_24", 85), ("ortiz", 45),
                ("qa_plaza", 43), ("citi_alley", 65), ("coast_wat", 35), ("ziga_teck", 40), ("sapp_ara", 44), ("tomntoms", 57), ("des_wing", 59)],
                

# Ubaldo Laya
    "ubaldo": [("des_wing", 0), ("tomntoms", 59), ("lanastida", 63), ("phoenix_gas", 218), ("palao_mrkt", 67), ("puregold", 60), ("coco_pet", 63),
                ("pc_ilgn", 60), ("bdo_network", 61)], # outside bounds (areola st > city hall > c3)                


# Olas-Ubaldo Laya
    "olas": [("bdo_network", 0), ("pc_ilgn", 61), ("coco_pet", 60), ("puregold", 63), ("palao_mrkt", 60), ("phoenix_gas", 67), ("lanastida", 218), 
             ("mayo_dia", 53), ("pondoc", 47), ("new_flash", 41), ("qa_plaza", 35), ("citi_alley", 65), ("coast_wat", 35), ("ziga_teck", 40), 
             ("sapp_ara", 44), ("tomntoms", 57), ("des_wing", 59)],


# Tipanoy-Landless-Mirador
    "tipanoy_landless": [("des_wing", 0), ("tomntoms", 59), ("lanastida", 63), ("doc_uy", 46), ("mejia_bldg", 46), ("coinsaver", 208), ("chandis", 75),
                ("meat_shop", 121), ("pugaan_term", 50), ("min_burger", 45), ("mottrad_villa", 94), ("ncip", 292), ("bpi", 59), ("sec_bank", 88), ("watsons", 40), ("shoppe_24", 85), ("ortiz", 45),
                ("qa_plaza", 43), ("citi_alley", 65), ("coast_wat", 35), ("ziga_teck", 40), ("sapp_ara", 44), ("tomntoms", 57), ("des_wing", 59)],


# Abuno-Tipanoy-Celeste
    "abuno": [("des_wing", 0), ("tomntoms", 59), ("lanastida", 63), ("doc_uy", 46), ("mejia_bldg", 46), ("coinsaver", 208), ("chandis", 75),
                ("meat_shop", 121), ("pugaan_term", 50), ("min_burger", 45), ("mottrad_villa", 94), ("ncip", 292), ("bpi", 59), ("sec_bank", 88), ("watsons", 40), ("shoppe_24", 85), ("ortiz", 45),
                ("qa_plaza", 43), ("citi_alley", 65), ("coast_wat", 35), ("ziga_teck", 40), ("sapp_ara", 44), ("tomntoms", 57), ("des_wing", 59)],


# Tipanoy-Pindugangan-Mibolo
    "tipanoy-pina": [("des_wing", 0), ("tomntoms", 59), ("lanastida", 63), ("doc_uy", 46), ("mejia_bldg", 46), ("coinsaver", 208), ("chandis", 75),
                ("meat_shop", 121), ("pugaan_term", 50), ("min_burger", 45), ("mottrad_villa", 94), ("ncip", 292), ("bpi", 59), ("sec_bank", 88), ("watsons", 40), ("shoppe_24", 85), ("ortiz", 45),
                ("qa_plaza", 43), ("citi_alley", 65), ("coast_wat", 35), ("ziga_teck", 40), ("sapp_ara", 44), ("tomntoms", 57), ("des_wing", 59)],


# Tipanoy-Mibala
    "tipanoy_mibala": [("des_wing", 0), ("tomntoms", 59), ("lanastida", 63), ("doc_uy", 46), ("mejia_bldg", 46), ("coinsaver", 208), ("chandis", 75),
                ("meat_shop", 121), ("pugaan_term", 50), ("min_burger", 45), ("mottrad_villa", 94), ("ncip", 292), ("bpi", 59), ("sec_bank", 88), ("watsons", 40), ("shoppe_24", 85), ("ortiz", 45),
                ("qa_plaza", 43), ("citi_alley", 65), ("coast_wat", 35), ("ziga_teck", 40), ("sapp_ara", 44), ("tomntoms", 57), ("des_wing", 59)],


# Steeltown
    "steeltown": [("des_wing", 0), ("tomntoms", 59), ("lanastida", 63), ("phoenix_gas", 218), ("palao_mrkt", 67), ("puregold", 60), ("coco_pet", 63), ("meat_shop", 106), 
                  ("pugaan_term", 50), ("min_burger", 45), ("mottrad_villa", 94), ("ncip", 292), ("bpi", 59), ("sec_bank", 88), ("watsons", 40), ("shoppe_24", 85), ("ortiz", 45), ("qa_plaza", 43), 
                  ("citi_alley", 65), ("coast_wat", 35), ("ziga_teck", 40), ("sapp_ara", 44), ("tomntoms", 57), ("des_wing", 59)],


# Suarez-Iishai
    "sua_iishai": [("des_wing", 0), ("tomntoms", 59), ("lanastida", 63), ("phoenix_gas", 218), ("palao_mrkt", 67), ("puregold", 60), ("coco_pet", 63), ("meat_shop", 106), 
                  ("pugaan_term", 50), ("min_burger", 45), ("mottrad_villa", 94), ("ncip", 292), ("bpi", 59), ("sec_bank", 88), ("watsons", 40), ("shoppe_24", 85), ("ortiz", 45), ("qa_plaza", 43), 
                  ("citi_alley", 65), ("coast_wat", 35), ("ziga_teck", 40), ("sapp_ara", 44), ("tomntoms", 57), ("des_wing", 59)],


# Upper Tominobo-Suarez
    "upper_suarez": [("des_wing", 0), ("tomntoms", 59), ("lanastida", 63), ("phoenix_gas", 218), ("palao_mrkt", 67), ("puregold", 60), ("coco_pet", 63), ("meat_shop", 106), 
                  ("pugaan_term", 50), ("min_burger", 45), ("mottrad_villa", 94), ("ncip", 292), ("bpi", 59), ("sec_bank", 88), ("watsons", 40), ("shoppe_24", 85), ("ortiz", 45), ("qa_plaza", 43), 
                  ("citi_alley", 65), ("coast_wat", 35), ("ziga_teck", 40), ("sapp_ara", 44), ("tomntoms", 57), ("des_wing", 59)],


# Buruun
    "buruun": [("des_wing", 0), ("tomntoms", 59), ("lanastida", 63), ("phoenix_gas", 218), ("palao_mrkt", 67), ("puregold", 60), ("coco_pet", 63), ("meat_shop", 106), 
                  ("pugaan_term", 50), ("min_burger", 45), ("mottrad_villa", 94), ("ncip", 292), ("bpi", 59), ("sec_bank", 88), ("watsons", 40), ("shoppe_24", 85), ("ortiz", 45), ("qa_plaza", 43), 
                  ("citi_alley", 65), ("coast_wat", 35), ("ziga_teck", 40), ("sapp_ara", 44), ("tomntoms", 57), ("des_wing", 59)],


# Tinago-Maze Park-Tonggo
    "tinago_maze": [("des_wing", 0), ("tomntoms", 59), ("lanastida", 63), ("phoenix_gas", 218), ("palao_mrkt", 67), ("puregold", 60), ("coco_pet", 63), ("meat_shop", 106), 
                  ("pugaan_term", 50), ("min_burger", 45), ("mottrad_villa", 94), ("ncip", 292), ("bpi", 59), ("sec_bank", 88), ("watsons", 40), ("shoppe_24", 85), ("ortiz", 45), ("qa_plaza", 43), 
                  ("citi_alley", 65), ("coast_wat", 35), ("ziga_teck", 40), ("sapp_ara", 44), ("tomntoms", 57), ("des_wing", 59)],


# Tinago-Ditucalan
    "tinago_ditu": [("des_wing", 0), ("tomntoms", 59), ("lanastida", 63), ("doc_uy", 46), ("mejia_bldg", 46), ("coinsaver", 208), ("chandis", 75),
                ("meat_shop", 121), ("pugaan_term", 50), ("min_burger", 45), ("mottrad_villa", 94), ("ncip", 292), ("bpi", 59), ("sec_bank", 88), ("watsons", 40), ("shoppe_24", 85), ("ortiz", 45),
                ("qa_plaza", 43), ("citi_alley", 65), ("coast_wat", 35), ("ziga_teck", 40), ("sapp_ara", 44), ("tomntoms", 57), ("des_wing", 59)],


# Route 29 - IBJT South -> IBJT North not in bound with our map
# Route 30 - IBJT South -> IBJT North via C3 not in bound with our map

# Bayanihan-IBJT
    "bayanihan": [("des_wing", 0), ("tomntoms", 59), ("lanastida", 63), ("doc_uy", 46), ("mejia_bldg", 46), ("mshoes", 37), ("ncip", 47), ("post_off", 51), ("desmark", 52), 
                  ("emcor", 50), ("gaisano_mall", 124), ("vanitea", 192)],


# Palao-Del Carmen
    "palao_del": [("landbank", 0), ("min_burger", 116), ("mottrad_villa", 94), #("alemania", 0), ("kylas", 0), ("pbb", 0), 
                ("ncip", 292), ("bpi", 59), ("sec_bank", 88), ("watsons", 40), ("unitop", 33), ("galaxy_mart", 46), ("penshoppe", 46), ("pnb", 103), ("fire_safe", 89), 
                ("daily", 117), ("tc_circle", 261), ("gaisano_old", 193), ("ukay_market", 105), ("dunkin", 113), ("bike_ent", 96), ("pulis_agu", 39), ("mc_hotel", 63), 
                ("pater", 46), ("mot_race", 46), ("zoey", 39), ("shoppe_24", 36), ("ball_4k", 38), ("orix", 40), ("crown", 47), ("mejia_bldg", 60), ("coinsaver", 208), 
                ("chandis", 75), ("meat_shop", 121),  ("sym", 118), ("e_fix", 50), ("landbank", 50)],


# Del Carmen-Abegail
    "del_abegail": [("landbank", 0), ("min_burger", 116), ("mottrad_villa", 94), #("alemania", 0), ("kylas", 0), ("pbb", 0), 
                    ("ncip", 292), ("bpi", 59), ("sec_bank", 88), ("watsons", 40), ("unitop", 33), ("galaxy_mart", 46), ("penshoppe", 46), ("pnb", 103), ("fire_safe", 89), 
                    ("daily", 117), ("tc_circle", 261), ("gaisano_old", 193), ("ukay_market", 105), ("dunkin", 113), ("bike_ent", 96), ("pulis_agu", 39), ("mc_hotel", 63), 
                    ("pater", 46), ("mot_race", 46), ("zoey", 39), ("shoppe_24", 36), ("ball_4k", 38), ("orix", 40), ("crown", 47), ("mejia_bldg", 60), ("coinsaver", 208), 
                    ("chandis", 75), ("meat_shop", 121),  ("sym", 118), ("e_fix", 50), ("landbank", 50)],


# Pugaan
#lanbank, min_burger, pugaan_term, e_fix, landbank
    "pugaan": [("landbank", 0), ("min_burger", 116), ("pugaan_term", 45), ("e_fix", 114), ("landbank", 50)],

}
