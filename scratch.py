# landmarks
TC_Circle = ["Ludo", "Daily"]# Tomas Cabili Circle
#PPA # Phil. Port Authority
#PCG # Coast Guard
Ludo = ["TC_Circle", "Gaisano_Old", "Mon_Print"]
Mon_Print = ["Halal_Meat", "Ludo"] # Montever Printing Shop
Nehal_Arc = ["Wet_Market", "Gaisano_Old"]   # Nehal Padian Arcade
Gaisano_Old =  ["Ukay_Market", "Novo", "Nehal_Arc", "Ludo"]
Pub_Market = ["Wet_Market", "Ukay_Market"]  # Iligan Public Market
Wet_Market = ["Pub_Market", "Nehal_Arc"]    # Poblacion Wet Market
Ukay_Market = ["Gaisano_Old", "Pub_Market", "AGR_Pharm"]      # Ukay-ukay's near IPM
Daily = ["TC_Circle", "COOP_Fuel", "Fire_Safe"]  # Sabayle
AGR_Pharm = ["Novo", "Ukay_Market", "Dunkin"]    # AGR Pharmacy
Novo = ["Halal_Meat", "Gaisano_Old", "AGR_Pharm"]
Halal_Meat = ["Dunkin", "DNP", "Novo", "Mon_Print"] # Al-Barakah Meatshop
Dunkin = ["AGR_Pharm", "Bike_Ent", "Halal_Meat"]
Bike_Ent = ["DNP", "Dunkin", "Pulis_Agu"] # AYP Bicycle Enterprise
DNP = ["Hala_Meat", "Bike_Ent", "RCBC_PNB"] # DNP Photo Imaging         
Fire_Safe = ["Daily"]  # Fire Safe Marketing
RCBC_PNB = ["DNP", "Rojon"]
Pulis_Agu = ["Bike_Ent", "Learnfast", "MC_Hotel"] # Police Station Aguinaldo St.
Learnfast = ["MC_Hotel", "Pulis_Agu", "Glo_Flash", "Tambacan"] # Learnfast Computer Institute of Technology, Inc.
MC_Hotel = ["Pulis_Agu", "Pater", "Learnfast"] # Maria Cristina Hotel
Rojon = ["RCBC_PNB", "Penshoppe"] # Rojon Pharmacy
IS_Rep = ["Fire_Safe", "Octagon"]    # IS Electronical Repair Services
Tambacan = ["Learnfast", "Glo_Flash", "Fount_Acad"] # Tambacan Bridge
Glo_Fash = ["Learnfast", "Tambacan", "Red_Carp", "Pater"] # Glorious Fashion
Pater = ["Glo_Flash", "MC_Hotel", "Mot_Race"] # Pater Al-Kuwait
Penshoppe = ["Galaxy_Mart", "Rojon"]
Octagon = ["COOP_Fuel", "IS_Rep", "ABest"]
COOP_Fuel = ["Daily", "Octagon", "Petron"]
Petron = ["COOP_Fuel", "Uncle_Brew"]
Fount_Acad = ["Red_Carp", "Tambacan", "GSIS"] # Fountain of Life Academy
Red_Carp = ["Ilaya", "Fount_Acad", "Glo_Fash", "Mot_Race"] # Red Carpet (Boutique)
Mot_Race = ["Red_Carp", "Pater", "Zoey"] # Motor Race - Motor Parts
Galaxy_Mart = ["Penshoppe", "Unitop"] # Iligan Galaxy Xpress Mart
ABest = ["Octagon", "TechTalk"] # ABest Express Iligan Branch
TechTalk = ["ABest", "Frappella"] # TechTalk Computer Store
Unitop = ["Galaxy_Mart", "Watsons"]
Zoey = ["Mot_Race", "Shoppe_24", "Ilaya"]
Ilaya = ["Zoey", "Ortiz", "GSIS", "Red_Carp"] # Cafe Ilaya
GSIS = ["Fount_Acad", "Ilaya"] # Government Service Insurance System
#Concepcion # Purok Concepcion
CQ_Print = ["Coast_Wat", "Deja_Teu"] # CQ Printing Press
Coast_Wat = ["CQ_Print", "Ziga_Teck", "New_Fash"] # Coastal Waters Water Bottling Services
New_Fash = ["Coast_Wat", "Pondoc", "Dexter"] # Iligan New Fashion Shop
Dexter = ["New_Fash", "Ball_4k", "Waynsee", "Ortiz"] # Dexter's Party Lab
Ball_4k = ["Dexter", "Orix", "Shoppe_24"] # 4K Balloons
Ortiz = ["Dexter", "Ilaya", "Shoppe_24"]   # Ortiz Bldg.
Shoppe_24 = ["Ball_4k", "Zoey", "Ortiz"]
Watsons = ["Sec_Bank", "Unitop"]
Frappella = ["TechTalk", "Avila_Learn"]
Avila_Learn = ["Frappella", "Cathedral", "Tita_Fan"] # St. Therese de Avila Learning Center
Cathedral = ["Sec_Bank", "Avila_Learn"]   # St. Michael's Cathedral
Sec_Bank = ["BPI", "Watsons", "Cathedral"]    # Security Bank
Deja_Teu = ["Ziga_Teck", "ICNHS", "CQ_Print"]
ICNHS = ["Sapp_Ara", "Deja_Teu", "Des_Wing"]
Ziga_Teck = ["Deja_Teu", "Sapp_Ara", "Pondoc", "Coast_Wat"]   # Ziga Teck Computer Solutions
Pondoc = ["Ziga_Teck", "New_Fash", "Mayo_Dia", "Waynsee"]      # Pondoc Surveying Office
Waynsee = ["Pondoc", "Orix", "Pop_Rock", "Dexter"]     # Waynsee Chickenhaus
Orix = ["Ball_4k", "Waynsee", "Crown"]        # Orix Metro Leasing & Finance Corp
Tita_Fan = ["Avila_Learn", "Mackis"]    # Tita Fannies
Uncle_Brew = ["Emcor", "Petron", "Mackis"]
Mackis = ["Tita_Fan", "Epson", "Uncle_Brew", "Desmark"]
Epson = ["Mackis", "BPI", "Post_Off"]
BPI = ["St_Michaels", "Sec_Bank", "NCIP", "Epson"]
St_Michaels = ["Crown", "MShoes", "BPI"]
Crown = ["Pop_Rock", "Orix", "Mejia_Bldg", "St_Michaels"]
Pop_Rock = ["Doc_Uy", "Mayo_Dia", "Waynsee", "Crown"]
Mayo_Dia = ["Pondoc", "Lanastida", "Pop_Rock", "Sapp_Ara"]    # Mayo Diagnostics Center
Sapp_Ara = ["Mayo_Dia", "TomNToms", "Ziga_Teck", "ICNHS"]    # Sapporo Araneta St.
Des_Wing = ["ICNHS", "TomNToms"]    # Desmark Wingshop
TomNToms = ["Des_Wing", "Lanastida", "Sapp_Ara"]
Lanastida = ["TomNToms", "Mayo_Dia", "Doc_Uy"]   # Lanastida Dental Clinic
Doc_Uy = ["Mejia_Bldg", "Lanastida", "Pop_Rock"]
Mejia_Bldg = ["MShoes", "Crown", "Doc_Uy"]
MShoes = ["NCIP", "St_Michaels", "Mejia_Bldg"]
NCIP = ["Post_Off", "BPI", "PBB", "MShoes"]        # National Commission on Indigenous People
Post_Off = ["Epson", "Desmark", "NCIP"]    # Post Office
Desmark = ["Post_Off", "Mackis", "Emcor"]
Emcor = ["Desmark", "Uncle_Brew"] 
#Gaisano_Mall
PBB = ["NCIP", "Kylas"]         # Philippine Business Bank
Phoenix_Gas = ["Palao_Mrkt", "Lanastida", "CoinSaver"]
CoinSaver = ["Chandis"]
Kylas = ["PBB", "Alemania"]     # Kyla's Bistro
Alemania = ["Kylas", "MotTrad_Villa", "Bam_Doc"]    # Plaza Alemania
Chandis = ["MotTrad_Villa", "Meat_Shop", "Palao_Mrkt", "CoinSaver"]     # Chandis Cafe
MotTrad_Villa = ["Alemania", "Chandis", "Landbank"]       # MotorTrade Vilaverde Rd.
Bam_Doc = ["MercJupi_St", "Abund_Life"]             # Bamboo Doctors' Inc.
Palao_Mrkt = ["Chandis", "Ilgn_Deal", "Puregold"]
Ilgn_Deal = ["Palao_Mrkt", "COMELEC"]           # Iligan Dealers Multi-Purpose Cooperative
COMELEC = ["Ilgn_Deal", "Puregold", "Megatech"]             # Commission on Elections
Puregold = ["Palao_Mrkt", "Coco_Pet", "COMELEC"]
Megatech = ["Phoenix_LPG", "COMELEC", "Coco_Pet"]
Coco_Pet = ["Megatech", "Meat_Shop", "PC_Ilgn", "Puregold"]            # Coco Pet Station Badelles Ext
Meat_Shop = ["Coco_Pet", "SYM", "Chandis"]           # Estrella Meat Shop
Landbank = ["MotTrad_Villa", "ColorChart"]
ColorChart = ["Landbank", "SYM"]          #Color Chart Construction Supply
SYM = ["ColorChart", "Meat_Shop", "BDO_Network"]
BDO_Network = ["SYM", "PC_Ilgn"]         # BDO Network Branch
PC_Ilgn = ["BDO_Network", "Coco_Pet", "Phoenix_LPG"]          # Personal Collection Iligan
Phoenix_LPG = ["Megatech", "PC_Ilgn"]







