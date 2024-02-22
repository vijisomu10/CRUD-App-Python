Uppgift:
1 CRUD-app 
CRU(D)-applikation i konsol/terminal (CRUD → Create, Read, Update and Delete)
Det ska gå att kunna skapa användare. 
En användare har förnamn, efternamn, användarnamn (unikt), lösenord, address och telefonnummer [Detta ska lagras i en relationsdatabas]. 
Användare ska kunna logga in och när en användare loggar in ska det loggas till en CSV-fil (user login.csv) som för varje timme ska läsas in och långtidslagras i en realtionsdatabas(Därefter rensas så den är tom). 
När CSV-filen uppdateras ska också antalet inloggningar den timmen loggas till en Excel-fil (login history.xlsx) med info om år, månad, dag, timme och antal. 
Användare ska också kunna uppdatera sitt förnamn, efternamn(, lösenord, address och telefonnummer). 

En användare ska också kunna ”posta” meddelanden till ”väggen”. (mongo DB)
    Ett meddelande innehåller en rubrik, ett användarnamn och ett textmeddelande men kan också innehålla en bild, en video eller ett antal länkar. 
    Dessa ska sparas i MongoDB (Bild, video och länkar fejkas i vår applikation som text)!! 
Det ska också gå att kunna söka på en titel för ett meddelande och få tillbaka det från databasen. Likaså ska det gå att kolla hur många meddelande en användare har postat på väggen!! 

2 Inlämning 
Ni lämnar in genom att bjuda in mig, sebastian.ohman@systemetor.se (Sebastianmentor). 
Jag kommer maximalt köra en ”pip install -r requirements.txt” för att kunna köra erat program. Godkänt fås vid fungerande program.... 

Stegvis:
Steg 1: create user.py 