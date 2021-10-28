"""
VH Aug 2021. Script file related to the MIKSERI-project.

This file indicates filenames related to the source data (street network and service locations).
Includes  category names in Finnish which is the report language. 
You can dd services and/or study areas to the process by modifying this file. 

Dictionaries indicate filenames for 

1. Protobuf files for each study area downloaded via BBike.org (or: download from https://www.geofabrik.de/ and subset with pyrosm)
2. Service locations, shapefile input
3. Service locations, geopackage inputs (data downlaoded from OSM)

Data downloade from OSM is stored in fr"../results/downloaded_pois/OSM_{city}.gpkg" 
after running the data dowload process.

Root folder can be changed in the main notebook. 

""" 

# OSM Protobuf files (check if extent is enough!)
pbf_files = {"Lappeenranta": r"planet_27.828,60.916_28.692,61.186.osm.pbf",
             "Tampere": r"planet_22.803,61.208_24.874,61.818.osm.pbf",
             "Joensuu": r"planet_28.489,62.24_31.313,63.08.osm.pbf",
             "Kuopio": r"planet_25.396,62.554_29.431,63.641.osm.pbf",
            }

# Key:value pairs for service (in Finnish) and associated shapefile name
# These files are not included in the repository (some are restricted use). 
shapefiles = {"alakoulut": r"alakoulut.shp",
              "ylakoulut": r"ylakoulut.shp",
              "lukiot":  r"lukiot.shp",
              "vahittaiskauppa -kaikki toimialat": r"Vähittäiskaupan_toimipaikat.shp",
              "paivittaistavarakauppa": r"PT_toimipaikat.shp",
              "terveysasemat": "Terveysasemat.shp"
             }

# Key:value pairs for service (in Finnish) and associated layer name in the downloaded geopackage
osm = {"kirjastot":  r"libraries",   
       #"apteekit":  r"pharmacies", # not includedhere, but the data are good quality after Covid-time updates in Finland
       
       "museot":  r"museums",
       "hotellit": r"hotels",
       "teatterit":  r"theatres", 
       "elokuvateatterit": r"cinemas",
       
       "ravintolat":  r"restaurants",
       "kahvilat":  r"cafes",
       "pubit_klubit":  r"pubs_clubs",
      }

# These features were not included in the analyis due to data quality issues, but should be added if available
temp = {"paivakodit": "",
        "nuorisotilat":"",
        "muu_kauppa": "",
        "kauppakeskukset": ""
        }

