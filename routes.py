#akong pag assign sa distance is from starting point(0) + d from sp to one node
# gibase nako ang distance from the node system

import networkx as nx
from nodes import landmarks
#ILIGAN JEEPNEY ROUTES

routes = {
# Tambo-Gerona, San Roque and Hinaplanon Crossing (Route 1 and 2)
    "tambo-hinaplanon": [("vanitea", 0), ("petron", 243), ("coop_fuel", 140), ("daily", 190), ("tc_circle", 261), ("iligan_pier", 113),
                ("coast_guard", 110), ("nehal_arc", 141), ("wet_market", 37), ("pub_market", 112), ("ukay_market", 80), ("dunkin", 113), 
                ("bike_ent", 96), ("pulis_agu", 39), ("mc_hotel", 63), ("pater", 46), ("mot_race", 46), ("zoey", 39), ("unitop", 85), 
                ("techtalk", 93), ("frapella", 32), ("avila_learn", 40), ("tita_fan", 45), ("mackis", 40), ("desmark", 60), ("emcor", 50), 
                ("gaisano_mall", 124), ("vanitea", 192)],

# Hinaplanon-Cabaro (Route 3)
    "hinaplanon-cabaro": [("vanitea", 0), ("petron", 243), ("coop_fuel", 140), ("daily", 190), ("tc_circle", 261), ("iligan_pier", 113),
                ("coast_guard", 110), ("nehal_arc", 141), ("wet_market", 37), ("pub_market", 112), ("ukay_market", 80), ("dunkin", 113), 
                ("bike_ent", 96), ("pulis_agu", 39), ("mc_hotel", 63), ("pater", 46), ("mot_race", 46), ("zoey", 39), ("unitop", 85), 
                ("techtalk", 93), ("frapella", 32), ("avila_learn", 40), ("tita_fan", 45), ("mackis", 40), ("desmark", 60), ("emcor", 50), 
                ("gaisano_mall", 124), ("vanitea", 192)],

# Canaway-Santiago-Bayug (Route 4)
    "canaway": [("vanitea", 0), ("petron", 243), ("coop_fuel", 140), ("daily", 190), ("tc_circle", 261), ("iligan_pier", 113),
                ("coast_guard", 110), ("nehal_arc", 141), ("wet_market", 37), ("pub_market", 112), ("ukay_market", 80), ("dunkin", 113), 
                ("bike_ent", 96), ("pulis_agu", 39), ("mc_hotel", 63), ("pater", 46), ("mot_race", 46), ("zoey", 39), ("unitop", 85), 
                ("techtalk", 93), ("frapella", 32), ("avila_learn", 40), ("tita_fan", 45), ("mackis", 40), ("desmark", 60), ("emcor", 50),
                ("gaisano_mall", 124), ("vanitea", 192)],

# Bayug-Santiago-IBJT (Route 5)
    "bayug-santiago": [("vanitea", 0), ("petron", 243), ("coop_fuel", 140), ("daily", 190), ("tc_circle", 261), ("iligan_pier", 113),
                ("coast_guard", 110), ("nehal_arc", 141), ("wet_market", 37), ("pub_market", 112), ("ukay_market", 80), ("dunkin", 113), 
                ("bike_ent", 96), ("pulis_agu", 39), ("mc_hotel", 63), ("pater", 46), ("mot_race", 46), ("zoey", 39), ("unitop", 85), 
                ("techtalk", 93), ("frapella", 32), ("avila_learn", 40), ("tita_fan", 45), ("mackis", 40), ("desmark", 60), ("emcor", 50), 
                ("gaisano_mall", 124), ("vanitea", 192)],

# Luinab-Bahayan-Manrique (Route 6)
    "luinab_bahayan": [("vanitea", 0), ("petron", 243), ("coop_fuel", 140), ("daily", 190), ("tc_circle", 261), ("iligan_pier", 113),
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
 
# Sta. Filomena-Acmac
    "sta_fe": [("vanitea", 0), ("petron", 243), ("coop_fuel", 140), ("daily", 190), ("tc_circle", 261), ("gaisano_old", 193), ("halal_meat", 114),
                     ("dnp", 99), ("pnb", 45), ("penshoppe", 102), ("galaxy_mart", 46), ("unitop", 46), ("techtalk", 93), ("frapella", 32), 
                     ("avila_learn", 40), ("tita_fan", 45), ("mackis", 40), ("desmark", 60), ("emcor", 50), ("gaisano_mall", 124), ("vanitea", 192)],


# Dalipuga - Vista Village
    "dalipuga": [("vanitea", 0), ("petron", 243), ("coop_fuel", 140), ("daily", 190), ("tc_circle", 261), ("gaisano_old", 193), ("halal_meat", 114),
                     ("dnp", 99), ("pnb", 45), ("penshoppe", 102), ("galaxy_mart", 46), ("unitop", 46), ("techtalk", 93), ("frapella", 32), 
                     ("avila_learn", 40), ("tita_fan", 45), ("mackis", 40), ("desmark", 60), ("emcor", 50), ("gaisano_mall", 124), ("vanitea", 192)],


# Kalubihon
    "kalubihon": [("vanitea", 0), ("petron", 243), ("coop_fuel", 140), ("daily", 190), ("tc_circle", 261), ("gaisano_old", 193), ("halal_meat", 114),
                     ("dnp", 99), ("pnb", 45), ("penshoppe", 102), ("galaxy_mart", 46), ("unitop", 46), ("techtalk", 93), ("frapella", 32), 
                     ("avila_learn", 40), ("tita_fan", 45), ("mackis", 40), ("desmark", 60), ("emcor", 50), ("gaisano_mall", 124), ("vanitea", 192)],

# San Roque - Lambaguhon
    "san_lambaguhon": [("vanitea", 0), ("petron", 243), ("coop_fuel", 140), ("daily", 190), ("tc_circle", 261), ("gaisano_old", 193), ("halal_meat", 114),
                     ("dnp", 99), ("pnb", 45), ("penshoppe", 102), ("galaxy_mart", 46), ("unitop", 46), ("techtalk", 93), ("frapella", 32), 
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
    "tominobo": [("des_wing", 0), ("tomntoms", 59), ("lanastida", 63), ("phoenix_gas", 218), ("palao_mrkt", 67), ("puregold", 60), ("coco_pet", 63), ("meat_shop", 106), 
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

start_end = {
# Tambo-Gerona, San Roque and Hinaplanon Crossing (Route 1 and 2)
    "tambo-hinaplanon": ["vanitea", "gaisano_mall"],

# Hinaplanon-Cabaro (Route 3)
    "hinaplanon-cabaro": ["vanitea", "gaisano_mall"],

# Canaway-Santiago-Bayug (Route 4)
    "canaway": ["vanitea", "gaisano_mall"],

# Bayug-Santiago-IBJT (Route 5)
    "bayug-santiago": ["vanitea", "gaisano_mall"],

# Luinab-Bahayan-Manrique (Route 6)
    "luinab_bahayan": ["vanitea", "gaisano_mall"],

# Bagong Silang
    "bagong_silang": ["vanitea", "gaisano_mall"],
 
# Sta. Filomena-Acmac
    "sta_fe": ["vanitea", "gaisano_mall"],

# Dalipuga - Vista Village
    "dalipuga": ["vanitea", "gaisano_mall"],

# Kalubihon
    "kalubihon": ["vanitea", "gaisano_mall"],

# San Roque - Lambaguhon
    "san_lambaguhon": ["vanitea", "gaisano_mall"],

# Tambacan
    "tambacan": ["tambacan", "des_wing"],

# Tubod-Rosario Heights
    "tubod_rosario": ["des_wing","tomntoms"],

# Tubod-Carbide Village
    "tubod_carbide": ["des_wing","tomntoms"],

# Tubod-Orellana-C3
    "tubod_orellana": ["des_wing","tomntoms"],                   

# Baraas-Dona Maria
    "baraas": ["des_wing", "tomntoms"],
                
# Ubaldo Laya
    "ubaldo": ["des_wing", "bdo_network"], # outside bounds (areola st > city hall > c3)                

# Olas-Ubaldo Laya
    "olas": ["bdo_network", "des_wing"],

# Tipanoy-Landless-Mirador
    "tipanoy_landless": ["des_wing", "tomntoms"],

# Abuno-Tipanoy-Celeste
    "abuno": ["des_wing", "tomntoms"],

# Tipanoy-Pindugangan-Mibolo
    "tipanoy-pina": ["des_wing", "tomntoms"],

# Tipanoy-Mibala
    "tipanoy_mibala": ["des_wing", "tomntoms"],

# Steeltown
    "steeltown": ["des_wing", "tomntoms"],

# Suarez-Iishai
    "sua_iishai": ["des_wing", "tomntoms"],

# Upper Tominobo-Suarez
    "tominobo": ["des_wing", "tomntoms"],

# Buruun
    "buruun": ["des_wing", "tomntoms"],

# Tinago-Maze Park-Tonggo
    "tinago_maze":["des_wing", "tomntoms"],

# Tinago-Ditucalan
    "tinago_ditu": ["des_wing", "tomntoms"],

# Bayanihan-IBJT
    "bayanihan": ["des_wing", "vanitea"],

# Palao-Del Carmen
    "palao_del": ["landbank", "e_fix"],

# Del Carmen-Abegail
    "del_abegail": ["landbank", "e_fix"],
}
# Define the graph
iligan_graph = nx.MultiDiGraph()

# Add edges from landmarks data to the graph
for landmark, destinations in landmarks.items():
    for destination, distance in destinations:
        iligan_graph.add_edge(landmark, destination, weight=distance)



