# MIKSERI OSM data and service accessibility

This repository contains selected analysis scripts related to the [MIKSERI-project](https://www.syke.fi/fi-FI/Tutkimus__kehittaminen/Tutkimus_ja_kehittamishankkeet/Hankkeet/Lahiymparistojen_kehittaminen_kaupunkikudosten_ja_toiminnallisen_sekoittuneisuuden_nakokulmasta) conducted at the [Finnish Environment institute SYKE](https://www.syke.fi/en-US) in 2021. 

The MIKSERI-project (*Lähiympäristöjen kehittäminen kaupunkikudosten ja toiminnallisen sekoittuneisuuden näkökulmasta*) focuses on urban development from the perspective of functional mixes across urban fabrics. Final report of this project will be available online in Finnish [in here](https://www.syke.fi/fi-FI/Tutkimus__kehittaminen/Tutkimus_ja_kehittamishankkeet/Hankkeet/Lahiymparistojen_kehittaminen_kaupunkikudosten_ja_toiminnallisen_sekoittuneisuuden_nakokulmasta).

This repository contains code related to retrieving and analyzing service accessibility based on data from [OpenStreetMap](www.openstreetmap.org). For details related to other analysis presented in the report, please contact the authors directly. 

Maintainer: Vuokko Heikinheimo (firstname dot lastname at syke dot fi). 


## Contents of this repository

- Jupyter notebooks for running the code 
- PDF versions for viewing the code
- Case area polygons
- .yaml file for setting up a conda environment (experimental!)

 ## Referencing & References
 
If using these results / approaches in further work, please refer to: 
 
> Helminen et al. 2021. INSERT MIKSERI REPORT REFERENCE HERE

This repository builds upon several open source projects and tools, including:

>Boeing, G. 2017. "OSMnx: New Methods for Acquiring, Constructing, Analyzing, and Visualizing Complex Street Networks." Computers, Environment and Urban Systems 65, 126-139. doi:10.1016/j.compenvurbsys.2017.05.004

>Foti, F., Waddell, P., & Luxen, D. 2012. A generalized computational framework for accessibility: from the pedestrian to the metropolitan scale. In Proceedings of the 4th TRB Conference on Innovations in Travel Modeling. Transportation Research Board.



## Requirements

### Packages
The presented workflows have been run using Python 3.8 and the following packages:

  - python=3.8
  - jupyterlab
  - matplotlib
  - geopandas
  - geojson
  - xlrd
  - pysal
  - pyrosm
  - geopy
  - mapclassify
  - contextily
  - pandana

If available, recommended to install these packages from the conda-forge channel via conda. 
Disclaimer: This list and the provided .yaml file might not be exhaustive. See spesific notebooks for a detailed list of required packages. 

### Conda environment

The required packages are included in the .yaml file in this repository. You can set up your own Python environment following these steps: 

1. Install Anaconda (or Miniconda) on your computer
2. Use the provided .yaml file for creating a conda environment, see instructions from: 
    - [managing conda environments](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
    - [AutoGIS course materials](https://autogis-site.readthedocs.io/en/latest/course-info/create-python-gis-env.html)
3. Install additional / missing packages using conda (.yaml file might not be exhaustive, additional packages were installed on-the-fly. see spesific notebooks for detailed list of required packages). 
4. Activate the environment, launch jupyter lab (included in the .yaml specs) and you should be ready to run the code!



