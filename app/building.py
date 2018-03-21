def getBuilding(src):
        classdict = {
        "CS" : ["Computer Science Building", "33.882148, -117.882660"],
        "SGMH" : ["Steven G. Mihalyo", "33.878866, -117.883385"],
        "PL" : ["Pollak Library", "33.881530, -117.885766"],
        "MH" : ["McCarthy Hall", "33.879864, -117.885550"],
        "E" : ["Engineering Building", "33.882177, -117.883186"],
        "H" : ["Humanities-Social Sciences", "33.880497, -117.884462"],
        "KHS" : ["Kinesiology & Health Science", "33.882628, -117.885890"],
        "CSH" : ["Carpenter Shop", "33.884035, -117.888246"],
        "SR" : ["Shipping & Receiving", "33.883799, -117.888730"],
        "AS" : ["Automobile Shop", "33.883739, -117.889177"],
        "MC" : ["Mailing Center", "33.884281, -117.888742"],
        "CC" : ["Children’s Center", "33.885800, -117.888476"],
        "CPAC" : ["Clayes Performing Arts Center", "33.880564, -117.886564"],
        "DBH" : ["Dan Black Hall", "33.879246, -117.886565"],
        "EC" : ["Education Classroom", "33.881104, -117.884441"],
        "G" : ["Golleher Alumni House", "33.882125, -117.889328"],
        "LH" : ["Langsdorf Hall", "33.879182, -117.884690"],
        "PLS" : ["Pollak Library South", "33.880902, -117.885368"],
        "RGC" : ["Ruby Gerontology Center", "33.883861, -117.883276"],
        "TG" : ["Titan Gymnasium", "33.883010, -117.885888"],
        "UH" : ["University Hall", "33.879530, -117.884209"],
        "VA" : ["Visual Arts", "33.880019, -117.888472"],
        "BE" : ["Baja Fresh", "33.881971, -117.887690"],
        "CJ" : ["Carls Jr", "33.879294, -117.883822"],
        "GA" : ["Gastronome", "33.883175, -117.881982"],
        "JU" : ["Juice It Up", "33.881659, -117.887810"],
        "PEX" : ["Panda Express", "33.881971, -117.887690"],
        "MST" : ["Mihaylo Starbucks", "33.878666, -117.883295"],
        "PLST" : ["Pollak Library Starbucks", "33.881488, -117.885172"],
        "TSUST" : ["TSU Starbucks", "33.881583, -117.887998"],
        "CPT" : ["College Park Togos", "33.877711, -117.883507"],
        "TSUT" : ["TSU Togos", "33.881958, -117.887737"],
        "BOFA" : ["BoFA Bank ATM", "33.881667, -117.887246"],
        "CATM" : ["Chase ATM", "33.881667, -117.887246"],
        "WATM" : ["Wells Fargo ATM", "33.881667, -117.887246"],
        "USB" : ["US-Bank", "33.881933, -117.887065"],
        "BA" : ["Becker Amphitheater","33.881278, -117.887079"],
        "ECSQ" : ["ECS Quad", "33.882277, -117.884115"],
        "Q" : ["Quad", "33.880374, -117.885378"],
        "TW" : ["Titan Walk", "33.881237, -117.886411"],
        "EHS" : ["Environment Health & Safety", "33.885158, -117.889355"],
        "TRI" : ["Trigen","33.879683, -117.887304"],
        "P" : ["Parking and Transportation Office", "33.884840, -117.889426"],
        "AS" : ["Automobile Shop","33.883890, -117.889318"],
        "CSH" : ["Carpenter Shop","33.884028, -117.888266"],
        "MC" : ["Mailing Center","33.884155, -117.888760"],
        "SR" : ["Shipping & Recieving","33.883783, -117.888760"],
        "CP" : ["College Park", "33.877731, -117.883405"],
        "CPW" : ["College Park West", "33.880918, -117.890017"],
        "SHCC": ["Student Health & Counseling Center", "33.883195, -117.884108"],
        "UP": ["University Police", "33.882790, -117.889392"],
        "ARSC": ["Admission and Records Service Center", "33.879004, -117.884702"],
        "CRC": ["Career Center", "33.879037, -117.884650"],
        "SRC": ["Student Recreation Center", "33.883453, -117.887809"],
        "RH": ["Resident Hall", "33.883628, -117.881806"],
        "SH" : ["Student Housing", "33.883637, -117.881707"],
        "TH" : ["Titan House", "33.883847, -117.884146"],
        "TROTC" : ["Titan ROTC", "33.884151, -117.884032"],
        "TSH" : ["Titan Shop", "33.881891, -117.886982"],
        "TSU" : ["Titan Student Union","33.881480, -117.888623"],
        "TS" : ["Titan Stadium", "33.886659, -117.886990"],
        "GF" : ["Goodwin Field", "33.887128, -117.885308"],
        "AF" : ["Anderson Field", "33.886000, -117.884936"],
        "PAS" : ["Parking Lot A-South", "33.885493, -117.888760"],
        "PA" : ["Parking Lot A", "33.887431, -117.888480"],
        "PC" : ["Parking Lot C", "33.878300, -117.888378"],
        "PCE" : ["Parking Lot C-East", "33.878568, -117.886755"],
        "PCW" : ["Parking Lot C-West", "33.878398, -117.888852"],
        "PE" : ["Parking Lot E", "33.882112, -117.881572"],
        "PF" : ["Parking Lot F", "33.879981, -117.883007"],
        "PG" : ["Parking Lot G", "33.888351, -117.886556"],
        "PH" : ["Parking Lot H", "33.883649, -117.883672"],
        "PI" : ["Parking Lot I", "33.881469, -117.882987"],
        "PS" : ["Parking Lot S", "33.876372, -117.883320"],
        "AP" : ["Arboritum Parking", "33.887800, -117.885210"],
        "CPFSP" : ["CPFS Parking", "33.877133, -117.883338"],
        "DDP" : ["Dumbo Down Parking", "33.884129, -117.887814"],
        "EPS" : ["Eastside Parking Structure", "33.880169, -117.881700"],
        "NPS" : ["Nutwood Parking Structure", "33.879397, -117.888491"],
        "SCPS" : ["Stage College Parking", "33.882832, -117.888769"]
        }
        abv = ""
        if len(src) > 3:
                if src[-3] in ("0", "1", "2", "3", "4", "5"):
                        src = src[:-3]
        for i in src:
                if i != "-":
                        abv = abv + i
                else:
                        break
        if abv in classdict:
                building = classdict[abv]
                #building.upper()  #makes sure upper AND lower case will work
        elif abv.upper() in classdict:
                building = classdict[abv.upper()]
        else:
                building = ['','']
        return building
