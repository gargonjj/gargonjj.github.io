# DAY 1

## REPOSITORY CREATION AND GITHUB PAGES CONFIGURATION

The first step was initializing the repository. The name "Magaro" comes
from the first two letters of our surnames (Macias, Garcia and Rodríguez).
We choose to add a README.md and the MIT License, since it is the most popular
and permissive license available on GitHub. We also added the file `_config.yml`
to set the initial configuration, such as the project name, the web theme and
a short description, in order to use GitHub Pages to post the project documentation.
The chosen subject for the store is music (CDs, vinyls and cassettes.) 

## API RESEARCH AND CHOSEN API

After doing a research on webs and APIs, we selected
two potential APIs for our website. These are:
- Discogs API: One of the worlds largest music database, offering detailed information abut vinyl records, CDs and even cassettes. It also features a public marketplace where users post their physical records.
- iTunes Search API: This API is officially provided by Apple. Working with this API seems to be really easy, since it doesn't need any complex authentication. However, it focuses exclusively on digital media.

We finally chose Discogs API over iTunes, since it focuses on physical market, which fits better our project. 

## WEB SCRAPING RESEARCH

In order to get ready to do web scraping, it is necessary to setup our project first. So the first step
in this process is to create and activate a virtual
enviroment. 

It is also necessary to install some libraries: `pip install requests beautifulsoup4 lxml selenium python-dotenv`

This is the recommended project structure:
```
project/
├── .env              
├── requirements.txt
├── scraper.py
├── api_client.py
└── data/
    └── output.json
```

The next step is to extract the data from the web or the API, using the libraries we already installed. Once we extracted the data, we dump them into a JSON file.

To make sure our work is ethical, we must respect the legal terms of service each website provides. This information is stored in the `robots.txt` file, so we must always check before we start working.

## HOW TO ENABLE SECURE HTTPS SERVER AND TWO-FACTOR AUTHENITACTION

To begin, we need to install the folowing web server:
`sudo apt install apache2`

The goal is to encrypt the connection between the user's browser and the server. To implement a secure server we must obtain an SSL/TLS certificate. Let's Encrpyt is a platform that provides free and open certificates. We also must install Certbot to install the certificate. 

The two-factor authenticator(2FA) adds an extra layer of security by requiring a temporary code in addition to the password. In order to enable the 2FA, we must install and enable the `mod_authn_otp` Apache module. Finally, we also must create a file to stores each user's keys.

## VM INSTALLATION AND CONFIGURATION

We created two virtual machines based on Linux Mint(v.21.2), one for the database and the other for the web server. The first adapter is configured as NAT to allow internet access exclusively for system maintenance and downloading web dependencies

We created a second adapter for each VM configured as 'host only' so both of the VM can communicate with each other.
 
### 1. Web Server VM:
- VM Name: Proyecto linux web server
- OS: Linux Mint (64-Bit)
- RAM: 23268 MB (23GB)
- CPU: 6 cores
- Storage: 25 GB
- System User: webadmin

### 2. Database Server VM:
- VM Name: Proyecto linux DB server
- OS: Linux Mint (64-Bit)
- RAM: 23268 MB (23GB)
- CPU: 6 cores
- Storage: 25 GB
- System User: dbadmin