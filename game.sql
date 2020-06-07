DROP TABLE IF EXISTS Game;

CREATE TABLE Game
(
    Questions CHAR(150), 
    Option_A CHAR(20),
    Option_B CHAR(20),
    Option_C CHAR(20),
    Option_D CHAR(20),
    Answer CHAR(20),
    PRIMARY KEY (Questions)
);

INSERT INTO Game
VALUES
    ("Which state in the United States is largest by area?", "Alaska","California","Texas","Hawaii","Alaska" ),
    ("On a radio, stations are changed by using what control?","Tuning","Volume","Bass","Treble", "Tuning"),
    ("Which material is most dense?","Silver","Styrofoam","Butter","Gold", "Gold"),
    ("What is Aurora Borealis commonly known as?","Fairy Dust","Northern Lights", "Book of ages","a Game of Thrones main character", "Northern Lights"),
    ("Oscar Awards were instituted in","1968", "1929","1901", "1965", "1929"),
    ("When is the International Workers' Day?", "1962","1963","1964", "1965", "1964"),
    ("In the U.S., if it's not Daylight Saving Time, it's what?","Borrowed time","Overtime", "Standard time", "Party time", "Standard time"),
    ("Which country is largest by area?","UK", "USA","Russia","China","Russia"),
    ("The US declared war on which country after the bombing of Pearl Harbor?","Japan","Russia","Germany","China", "Japan"),
    ("What was the first university in the United States?","Harvard","University of Washington","Yale","Oxford", "Harvard" ),
    ("When is the World's Diabetes Day?","14th November", "11th December", "15th October","1st July",  "14th November" ),
    ("What is the S.I. unit of temperature?","Kelvin","Celsius",  "Centigrade","Fahrenheit","Kelvin" ),
    ( "When did 19 NATO members and 11 'Partners for Peace' join hands for peace plan for Kosovo Crisis?","1999","1989", "1979","1969", "1999"),
    ("An albino gorilla usually has what color fur?",  "Brown","Black","White", "Golden",  "White"),
    ("What is commonly known as the 'Emerald City' in the United States?","Palos Verdes, CA","Seattle, WA","New York, NY","Dallas, TX", "Seattle, WA"),
    ("The headquarters of UN is situated at", "New York, USA", "Haque (Netherlands)", "Geneva",  "Paris", "New York, USA"),
    ("In aviation, what does UFO stand for?","Unified Flying Object","Unitary Flinging Obsession","United Flag Opposition","Unidentified Flying Object", "Unidentified Flying Object"),
    ("When did,  France became Republic?", "1789 AD","1798 AD","1792 AD","1729 AD", "1792 AD"),
    ("Of the blood groups A, B, AB and O, which one is transfused into a person whose blood group is A?",  "Group A only","Group B only","Group A and O", "Group AB only",  "Group A and O"),
    ("Numismatics is the study of", "a classed unique society",  "a united society", "a classed society", "None of the above",   "a classed society" ),
    ("What kind of animal traditionally lives in a sty?", "Cow","Pig","Fox","Teenager", "Pig"),
    ("The EPA urges people to produce less waste by engaging in efforts to reduce, reuse and what?", "Recycle", "Rewrap", "Repossess",  "Retire",   "Recycle"),
    ("What is the second most common gas in the air?","Nitrogen","Oxygen","Water","Helium", "Oxygen"),
    ("When and where was weightlifting introduced in Olympics?","1986 at Athens", "1988 at Seoul","1924 at St. Louis", "1908 at London", "1986 at Athens"),
    ("Light Year is related to", "energy",   "speed",   "distance", "intensity",  "distance" ),
    ("Lhasa airport at Tibet is the World's","largest airport","highest airport","lowest airport","busiest airport",  "highest airport"),
    ( "Which of these African countries is situated south of the equator?",   "Ethiopia", "Nigeria","Zambia",  "Chad", "Zambia")
;