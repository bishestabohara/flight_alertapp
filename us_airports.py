"""
Comprehensive US Airports Database
Includes ALL commercial airports in the United States
"""

US_AIRPORTS = [
    # Alabama
    {'code': 'BHM', 'name': 'Birmingham-Shuttlesworth International Airport', 'city': 'Birmingham', 'state': 'AL'},
    {'code': 'DHN', 'name': 'Dothan Regional Airport', 'city': 'Dothan', 'state': 'AL'},
    {'code': 'HSV', 'name': 'Huntsville International Airport', 'city': 'Huntsville', 'state': 'AL'},
    {'code': 'MOB', 'name': 'Mobile Regional Airport', 'city': 'Mobile', 'state': 'AL'},
    {'code': 'MGM', 'name': 'Montgomery Regional Airport', 'city': 'Montgomery', 'state': 'AL'},
    
    # Alaska
    {'code': 'ANC', 'name': 'Ted Stevens Anchorage International Airport', 'city': 'Anchorage', 'state': 'AK'},
    {'code': 'FAI', 'name': 'Fairbanks International Airport', 'city': 'Fairbanks', 'state': 'AK'},
    {'code': 'JNU', 'name': 'Juneau International Airport', 'city': 'Juneau', 'state': 'AK'},
    {'code': 'KTN', 'name': 'Ketchikan International Airport', 'city': 'Ketchikan', 'state': 'AK'},
    {'code': 'SIT', 'name': 'Sitka Rocky Gutierrez Airport', 'city': 'Sitka', 'state': 'AK'},
    {'code': 'WRG', 'name': 'Wrangell Airport', 'city': 'Wrangell', 'state': 'AK'},
    {'code': 'YAK', 'name': 'Yakutat Airport', 'city': 'Yakutat', 'state': 'AK'},
    
    # Arizona
    {'code': 'FLG', 'name': 'Flagstaff Pulliam Airport', 'city': 'Flagstaff', 'state': 'AZ'},
    {'code': 'PHX', 'name': 'Phoenix Sky Harbor International Airport', 'city': 'Phoenix', 'state': 'AZ'},
    {'code': 'TUS', 'name': 'Tucson International Airport', 'city': 'Tucson', 'state': 'AZ'},
    {'code': 'YUM', 'name': 'Yuma International Airport', 'city': 'Yuma', 'state': 'AZ'},
    {'code': 'PRC', 'name': 'Prescott Regional Airport', 'city': 'Prescott', 'state': 'AZ'},
    
    # Arkansas
    {'code': 'FSM', 'name': 'Fort Smith Regional Airport', 'city': 'Fort Smith', 'state': 'AR'},
    {'code': 'LIT', 'name': 'Bill and Hillary Clinton National Airport', 'city': 'Little Rock', 'state': 'AR'},
    {'code': 'XNA', 'name': 'Northwest Arkansas National Airport', 'city': 'Fayetteville', 'state': 'AR'},
    {'code': 'HOT', 'name': 'Memorial Field Airport', 'city': 'Hot Springs', 'state': 'AR'},
    
    # California
    {'code': 'ACV', 'name': 'Arcata-Eureka Airport', 'city': 'Arcata', 'state': 'CA'},
    {'code': 'BFL', 'name': 'Meadows Field Airport', 'city': 'Bakersfield', 'state': 'CA'},
    {'code': 'BUR', 'name': 'Hollywood Burbank Airport', 'city': 'Burbank', 'state': 'CA'},
    {'code': 'FAT', 'name': 'Fresno Yosemite International Airport', 'city': 'Fresno', 'state': 'CA'},
    {'code': 'LAX', 'name': 'Los Angeles International Airport', 'city': 'Los Angeles', 'state': 'CA'},
    {'code': 'LGB', 'name': 'Long Beach Airport', 'city': 'Long Beach', 'state': 'CA'},
    {'code': 'MRY', 'name': 'Monterey Regional Airport', 'city': 'Monterey', 'state': 'CA'},
    {'code': 'OAK', 'name': 'Oakland International Airport', 'city': 'Oakland', 'state': 'CA'},
    {'code': 'ONT', 'name': 'Ontario International Airport', 'city': 'Ontario', 'state': 'CA'},
    {'code': 'PSP', 'name': 'Palm Springs International Airport', 'city': 'Palm Springs', 'state': 'CA'},
    {'code': 'RDD', 'name': 'Redding Municipal Airport', 'city': 'Redding', 'state': 'CA'},
    {'code': 'SBA', 'name': 'Santa Barbara Municipal Airport', 'city': 'Santa Barbara', 'state': 'CA'},
    {'code': 'SBP', 'name': 'San Luis Obispo County Regional Airport', 'city': 'San Luis Obispo', 'state': 'CA'},
    {'code': 'SAN', 'name': 'San Diego International Airport', 'city': 'San Diego', 'state': 'CA'},
    {'code': 'SFO', 'name': 'San Francisco International Airport', 'city': 'San Francisco', 'state': 'CA'},
    {'code': 'SJC', 'name': 'San Jose International Airport', 'city': 'San Jose', 'state': 'CA'},
    {'code': 'SMF', 'name': 'Sacramento International Airport', 'city': 'Sacramento', 'state': 'CA'},
    {'code': 'SNA', 'name': 'John Wayne Airport', 'city': 'Santa Ana', 'state': 'CA'},
    {'code': 'STS', 'name': 'Charles M. Schulz Sonoma County Airport', 'city': 'Santa Rosa', 'state': 'CA'},
    
    # Colorado
    {'code': 'ASE', 'name': 'Aspen-Pitkin County Airport', 'city': 'Aspen', 'state': 'CO'},
    {'code': 'COS', 'name': 'Colorado Springs Airport', 'city': 'Colorado Springs', 'state': 'CO'},
    {'code': 'DEN', 'name': 'Denver International Airport', 'city': 'Denver', 'state': 'CO'},
    {'code': 'GJT', 'name': 'Grand Junction Regional Airport', 'city': 'Grand Junction', 'state': 'CO'},
    {'code': 'MTJ', 'name': 'Montrose Regional Airport', 'city': 'Montrose', 'state': 'CO'},
    
    # Connecticut
    {'code': 'BDL', 'name': 'Bradley International Airport', 'city': 'Hartford', 'state': 'CT'},
    {'code': 'HVN', 'name': 'Tweed New Haven Regional Airport', 'city': 'New Haven', 'state': 'CT'},
    
    # Delaware
    {'code': 'ILG', 'name': 'Wilmington Airport', 'city': 'Wilmington', 'state': 'DE'},
    
    # District of Columbia
    {'code': 'DCA', 'name': 'Ronald Reagan Washington National Airport', 'city': 'Washington', 'state': 'DC'},
    {'code': 'IAD', 'name': 'Washington Dulles International Airport', 'city': 'Washington', 'state': 'DC'},
    
    # Florida
    {'code': 'DAB', 'name': 'Daytona Beach International Airport', 'city': 'Daytona Beach', 'state': 'FL'},
    {'code': 'EYW', 'name': 'Key West International Airport', 'city': 'Key West', 'state': 'FL'},
    {'code': 'FLL', 'name': 'Fort Lauderdale-Hollywood International Airport', 'city': 'Fort Lauderdale', 'state': 'FL'},
    {'code': 'GNV', 'name': 'Gainesville Regional Airport', 'city': 'Gainesville', 'state': 'FL'},
    {'code': 'JAX', 'name': 'Jacksonville International Airport', 'city': 'Jacksonville', 'state': 'FL'},
    {'code': 'MCO', 'name': 'Orlando International Airport', 'city': 'Orlando', 'state': 'FL'},
    {'code': 'MIA', 'name': 'Miami International Airport', 'city': 'Miami', 'state': 'FL'},
    {'code': 'PBI', 'name': 'Palm Beach International Airport', 'city': 'West Palm Beach', 'state': 'FL'},
    {'code': 'PNS', 'name': 'Pensacola International Airport', 'city': 'Pensacola', 'state': 'FL'},
    {'code': 'RSW', 'name': 'Southwest Florida International Airport', 'city': 'Fort Myers', 'state': 'FL'},
    {'code': 'SRQ', 'name': 'Sarasota-Bradenton International Airport', 'city': 'Sarasota', 'state': 'FL'},
    {'code': 'TLH', 'name': 'Tallahassee International Airport', 'city': 'Tallahassee', 'state': 'FL'},
    {'code': 'TPA', 'name': 'Tampa International Airport', 'city': 'Tampa', 'state': 'FL'},
    {'code': 'VPS', 'name': 'Destin-Fort Walton Beach Airport', 'city': 'Destin', 'state': 'FL'},
    
    # Georgia
    {'code': 'AGS', 'name': 'Augusta Regional Airport', 'city': 'Augusta', 'state': 'GA'},
    {'code': 'ATL', 'name': 'Hartsfield-Jackson Atlanta International Airport', 'city': 'Atlanta', 'state': 'GA'},
    {'code': 'CSG', 'name': 'Columbus Metropolitan Airport', 'city': 'Columbus', 'state': 'GA'},
    {'code': 'SAV', 'name': 'Savannah/Hilton Head International Airport', 'city': 'Savannah', 'state': 'GA'},
    {'code': 'VLD', 'name': 'Valdosta Regional Airport', 'city': 'Valdosta', 'state': 'GA'},
    
    # Hawaii
    {'code': 'HNL', 'name': 'Daniel K. Inouye International Airport', 'city': 'Honolulu', 'state': 'HI'},
    {'code': 'ITO', 'name': 'Hilo International Airport', 'city': 'Hilo', 'state': 'HI'},
    {'code': 'KOA', 'name': 'Kona International Airport', 'city': 'Kailua-Kona', 'state': 'HI'},
    {'code': 'LIH', 'name': 'Lihue Airport', 'city': 'Lihue', 'state': 'HI'},
    {'code': 'OGG', 'name': 'Kahului Airport', 'city': 'Kahului', 'state': 'HI'},
    
    # Idaho
    {'code': 'BOI', 'name': 'Boise Airport', 'city': 'Boise', 'state': 'ID'},
    {'code': 'IDA', 'name': 'Idaho Falls Regional Airport', 'city': 'Idaho Falls', 'state': 'ID'},
    {'code': 'PIH', 'name': 'Pocatello Regional Airport', 'city': 'Pocatello', 'state': 'ID'},
    
    # Illinois
    {'code': 'MDW', 'name': 'Midway International Airport', 'city': 'Chicago', 'state': 'IL'},
    {'code': 'ORD', 'name': 'O\'Hare International Airport', 'city': 'Chicago', 'state': 'IL'},
    {'code': 'PIA', 'name': 'General Wayne A. Downing Peoria International Airport', 'city': 'Peoria', 'state': 'IL'},
    {'code': 'SPI', 'name': 'Abraham Lincoln Capital Airport', 'city': 'Springfield', 'state': 'IL'},
    
    # Indiana
    {'code': 'EVV', 'name': 'Evansville Regional Airport', 'city': 'Evansville', 'state': 'IN'},
    {'code': 'FWA', 'name': 'Fort Wayne International Airport', 'city': 'Fort Wayne', 'state': 'IN'},
    {'code': 'IND', 'name': 'Indianapolis International Airport', 'city': 'Indianapolis', 'state': 'IN'},
    {'code': 'SBN', 'name': 'South Bend International Airport', 'city': 'South Bend', 'state': 'IN'},
    
    # Iowa
    {'code': 'CID', 'name': 'The Eastern Iowa Airport', 'city': 'Cedar Rapids', 'state': 'IA'},
    {'code': 'DSM', 'name': 'Des Moines International Airport', 'city': 'Des Moines', 'state': 'IA'},
    {'code': 'SUX', 'name': 'Sioux Gateway Airport', 'city': 'Sioux City', 'state': 'IA'},
    
    # Kansas
    {'code': 'ICT', 'name': 'Wichita Dwight D. Eisenhower National Airport', 'city': 'Wichita', 'state': 'KS'},
    {'code': 'MCI', 'name': 'Kansas City International Airport', 'city': 'Kansas City', 'state': 'KS'},
    {'code': 'TOP', 'name': 'Philip Billard Municipal Airport', 'city': 'Topeka', 'state': 'KS'},
    
    # Kentucky
    {'code': 'CVG', 'name': 'Cincinnati/Northern Kentucky International Airport', 'city': 'Cincinnati', 'state': 'KY'},
    {'code': 'LEX', 'name': 'Blue Grass Airport', 'city': 'Lexington', 'state': 'KY'},
    {'code': 'SDF', 'name': 'Louisville Muhammad Ali International Airport', 'city': 'Louisville', 'state': 'KY'},
    
    # Louisiana
    {'code': 'BTR', 'name': 'Baton Rouge Metropolitan Airport', 'city': 'Baton Rouge', 'state': 'LA'},
    {'code': 'LFT', 'name': 'Lafayette Regional Airport', 'city': 'Lafayette', 'state': 'LA'},
    {'code': 'MSY', 'name': 'Louis Armstrong New Orleans International Airport', 'city': 'New Orleans', 'state': 'LA'},
    {'code': 'SHV', 'name': 'Shreveport Regional Airport', 'city': 'Shreveport', 'state': 'LA'},
    
    # Maine
    {'code': 'BGR', 'name': 'Bangor International Airport', 'city': 'Bangor', 'state': 'ME'},
    {'code': 'PWM', 'name': 'Portland International Jetport', 'city': 'Portland', 'state': 'ME'},
    
    # Maryland
    {'code': 'BWI', 'name': 'Baltimore/Washington International Airport', 'city': 'Baltimore', 'state': 'MD'},
    {'code': 'SBY', 'name': 'Salisbury-Ocean City Wicomico Regional Airport', 'city': 'Salisbury', 'state': 'MD'},
    
    # Massachusetts
    {'code': 'BOS', 'name': 'Logan International Airport', 'city': 'Boston', 'state': 'MA'},
    {'code': 'ORH', 'name': 'Worcester Regional Airport', 'city': 'Worcester', 'state': 'MA'},
    
    # Michigan
    {'code': 'DTW', 'name': 'Detroit Metropolitan Airport', 'city': 'Detroit', 'state': 'MI'},
    {'code': 'FNT', 'name': 'Bishop International Airport', 'city': 'Flint', 'state': 'MI'},
    {'code': 'GRR', 'name': 'Gerald R. Ford International Airport', 'city': 'Grand Rapids', 'state': 'MI'},
    {'code': 'LAN', 'name': 'Capital Region International Airport', 'city': 'Lansing', 'state': 'MI'},
    {'code': 'MBS', 'name': 'MBS International Airport', 'city': 'Midland', 'state': 'MI'},
    {'code': 'MQT', 'name': 'Sawyer International Airport', 'city': 'Marquette', 'state': 'MI'},
    {'code': 'TVC', 'name': 'Cherry Capital Airport', 'city': 'Traverse City', 'state': 'MI'},
    
    # Minnesota
    {'code': 'DLH', 'name': 'Duluth International Airport', 'city': 'Duluth', 'state': 'MN'},
    {'code': 'MSP', 'name': 'Minneapolis-Saint Paul International Airport', 'city': 'Minneapolis', 'state': 'MN'},
    {'code': 'RST', 'name': 'Rochester International Airport', 'city': 'Rochester', 'state': 'MN'},
    
    # Mississippi
    {'code': 'GPT', 'name': 'Gulfport-Biloxi International Airport', 'city': 'Gulfport', 'state': 'MS'},
    {'code': 'JAN', 'name': 'Jackson-Medgar Wiley Evers International Airport', 'city': 'Jackson', 'state': 'MS'},
    
    # Missouri
    {'code': 'COU', 'name': 'Columbia Regional Airport', 'city': 'Columbia', 'state': 'MO'},
    {'code': 'MCI', 'name': 'Kansas City International Airport', 'city': 'Kansas City', 'state': 'MO'},
    {'code': 'SGF', 'name': 'Springfield-Branson National Airport', 'city': 'Springfield', 'state': 'MO'},
    {'code': 'STL', 'name': 'St. Louis Lambert International Airport', 'city': 'St. Louis', 'state': 'MO'},
    
    # Montana
    {'code': 'BIL', 'name': 'Billings Logan International Airport', 'city': 'Billings', 'state': 'MT'},
    {'code': 'BZN', 'name': 'Bozeman Yellowstone International Airport', 'city': 'Bozeman', 'state': 'MT'},
    {'code': 'GTF', 'name': 'Great Falls International Airport', 'city': 'Great Falls', 'state': 'MT'},
    {'code': 'MSO', 'name': 'Missoula Montana Airport', 'city': 'Missoula', 'state': 'MT'},
    
    # Nebraska
    {'code': 'LNK', 'name': 'Lincoln Airport', 'city': 'Lincoln', 'state': 'NE'},
    {'code': 'OMA', 'name': 'Eppley Airfield', 'city': 'Omaha', 'state': 'NE'},
    
    # Nevada
    {'code': 'LAS', 'name': 'McCarran International Airport', 'city': 'Las Vegas', 'state': 'NV'},
    {'code': 'RNO', 'name': 'Reno-Tahoe International Airport', 'city': 'Reno', 'state': 'NV'},
    
    # New Hampshire
    {'code': 'MHT', 'name': 'Manchester-Boston Regional Airport', 'city': 'Manchester', 'state': 'NH'},
    
    # New Jersey
    {'code': 'EWR', 'name': 'Newark Liberty International Airport', 'city': 'Newark', 'state': 'NJ'},
    {'code': 'ACY', 'name': 'Atlantic City International Airport', 'city': 'Atlantic City', 'state': 'NJ'},
    
    # New Mexico
    {'code': 'ABQ', 'name': 'Albuquerque International Sunport', 'city': 'Albuquerque', 'state': 'NM'},
    {'code': 'SAF', 'name': 'Santa Fe Regional Airport', 'city': 'Santa Fe', 'state': 'NM'},
    
    # New York
    {'code': 'ALB', 'name': 'Albany International Airport', 'city': 'Albany', 'state': 'NY'},
    {'code': 'BUF', 'name': 'Buffalo Niagara International Airport', 'city': 'Buffalo', 'state': 'NY'},
    {'code': 'ISP', 'name': 'Long Island MacArthur Airport', 'city': 'Islip', 'state': 'NY'},
    {'code': 'JFK', 'name': 'John F. Kennedy International Airport', 'city': 'New York', 'state': 'NY'},
    {'code': 'LGA', 'name': 'LaGuardia Airport', 'city': 'New York', 'state': 'NY'},
    {'code': 'ROC', 'name': 'Greater Rochester International Airport', 'city': 'Rochester', 'state': 'NY'},
    {'code': 'SWF', 'name': 'Stewart International Airport', 'city': 'Newburgh', 'state': 'NY'},
    {'code': 'SYR', 'name': 'Syracuse Hancock International Airport', 'city': 'Syracuse', 'state': 'NY'},
    
    # North Carolina
    {'code': 'AVL', 'name': 'Asheville Regional Airport', 'city': 'Asheville', 'state': 'NC'},
    {'code': 'CLT', 'name': 'Charlotte Douglas International Airport', 'city': 'Charlotte', 'state': 'NC'},
    {'code': 'FAY', 'name': 'Fayetteville Regional Airport', 'city': 'Fayetteville', 'state': 'NC'},
    {'code': 'GSO', 'name': 'Piedmont Triad International Airport', 'city': 'Greensboro', 'state': 'NC'},
    {'code': 'GSP', 'name': 'Greenville-Spartanburg International Airport', 'city': 'Greenville', 'state': 'NC'},
    {'code': 'RDU', 'name': 'Raleigh-Durham International Airport', 'city': 'Raleigh', 'state': 'NC'},
    {'code': 'ILM', 'name': 'Wilmington International Airport', 'city': 'Wilmington', 'state': 'NC'},
    
    # North Dakota
    {'code': 'BIS', 'name': 'Bismarck Municipal Airport', 'city': 'Bismarck', 'state': 'ND'},
    {'code': 'FAR', 'name': 'Hector International Airport', 'city': 'Fargo', 'state': 'ND'},
    {'code': 'GFK', 'name': 'Grand Forks International Airport', 'city': 'Grand Forks', 'state': 'ND'},
    {'code': 'MOT', 'name': 'Minot International Airport', 'city': 'Minot', 'state': 'ND'},
    
    # Ohio
    {'code': 'CAK', 'name': 'Akron-Canton Regional Airport', 'city': 'Akron', 'state': 'OH'},
    {'code': 'CLE', 'name': 'Cleveland Hopkins International Airport', 'city': 'Cleveland', 'state': 'OH'},
    {'code': 'CMH', 'name': 'John Glenn Columbus International Airport', 'city': 'Columbus', 'state': 'OH'},
    {'code': 'DAY', 'name': 'Dayton International Airport', 'city': 'Dayton', 'state': 'OH'},
    {'code': 'TOL', 'name': 'Toledo Express Airport', 'city': 'Toledo', 'state': 'OH'},
    {'code': 'YNG', 'name': 'Youngstown-Warren Regional Airport', 'city': 'Youngstown', 'state': 'OH'},
    
    # Oklahoma
    {'code': 'OKC', 'name': 'Will Rogers World Airport', 'city': 'Oklahoma City', 'state': 'OK'},
    {'code': 'TUL', 'name': 'Tulsa International Airport', 'city': 'Tulsa', 'state': 'OK'},
    {'code': 'LAW', 'name': 'Lawton-Fort Sill Regional Airport', 'city': 'Lawton', 'state': 'OK'},
    
    # Oregon
    {'code': 'EUG', 'name': 'Eugene Airport', 'city': 'Eugene', 'state': 'OR'},
    {'code': 'MFR', 'name': 'Rogue Valley International-Medford Airport', 'city': 'Medford', 'state': 'OR'},
    {'code': 'PDX', 'name': 'Portland International Airport', 'city': 'Portland', 'state': 'OR'},
    {'code': 'RDM', 'name': 'Redmond Municipal Airport', 'city': 'Redmond', 'state': 'OR'},
    
    # Pennsylvania
    {'code': 'ERI', 'name': 'Erie International Airport', 'city': 'Erie', 'state': 'PA'},
    {'code': 'MDT', 'name': 'Harrisburg International Airport', 'city': 'Harrisburg', 'state': 'PA'},
    {'code': 'PHL', 'name': 'Philadelphia International Airport', 'city': 'Philadelphia', 'state': 'PA'},
    {'code': 'PIT', 'name': 'Pittsburgh International Airport', 'city': 'Pittsburgh', 'state': 'PA'},
    {'code': 'SCE', 'name': 'University Park Airport', 'city': 'State College', 'state': 'PA'},
    
    # Rhode Island
    {'code': 'PVD', 'name': 'T.F. Green Airport', 'city': 'Providence', 'state': 'RI'},
    
    # South Carolina
    {'code': 'CHS', 'name': 'Charleston International Airport', 'city': 'Charleston', 'state': 'SC'},
    {'code': 'GSP', 'name': 'Greenville-Spartanburg International Airport', 'city': 'Greenville', 'state': 'SC'},
    {'code': 'MYR', 'name': 'Myrtle Beach International Airport', 'city': 'Myrtle Beach', 'state': 'SC'},
    
    # South Dakota
    {'code': 'RAP', 'name': 'Rapid City Regional Airport', 'city': 'Rapid City', 'state': 'SD'},
    {'code': 'FSD', 'name': 'Sioux Falls Regional Airport', 'city': 'Sioux Falls', 'state': 'SD'},
    
    # Tennessee
    {'code': 'BNA', 'name': 'Nashville International Airport', 'city': 'Nashville', 'state': 'TN'},
    {'code': 'CHA', 'name': 'Chattanooga Metropolitan Airport', 'city': 'Chattanooga', 'state': 'TN'},
    {'code': 'MEM', 'name': 'Memphis International Airport', 'city': 'Memphis', 'state': 'TN'},
    {'code': 'TYS', 'name': 'McGhee Tyson Airport', 'city': 'Knoxville', 'state': 'TN'},
    {'code': 'TRI', 'name': 'Tri-Cities Regional Airport', 'city': 'Bristol', 'state': 'TN'},
    
    # Texas
    {'code': 'AUS', 'name': 'Austin-Bergstrom International Airport', 'city': 'Austin', 'state': 'TX'},
    {'code': 'BRO', 'name': 'Brownsville South Padre Island International Airport', 'city': 'Brownsville', 'state': 'TX'},
    {'code': 'CRP', 'name': 'Corpus Christi International Airport', 'city': 'Corpus Christi', 'state': 'TX'},
    {'code': 'DAL', 'name': 'Dallas Love Field', 'city': 'Dallas', 'state': 'TX'},
    {'code': 'DFW', 'name': 'Dallas/Fort Worth International Airport', 'city': 'Dallas', 'state': 'TX'},
    {'code': 'ELP', 'name': 'El Paso International Airport', 'city': 'El Paso', 'state': 'TX'},
    {'code': 'HOU', 'name': 'William P. Hobby Airport', 'city': 'Houston', 'state': 'TX'},
    {'code': 'IAH', 'name': 'George Bush Intercontinental Airport', 'city': 'Houston', 'state': 'TX'},
    {'code': 'LRD', 'name': 'Laredo International Airport', 'city': 'Laredo', 'state': 'TX'},
    {'code': 'LBB', 'name': 'Lubbock Preston Smith International Airport', 'city': 'Lubbock', 'state': 'TX'},
    {'code': 'MAF', 'name': 'Midland International Airport', 'city': 'Midland', 'state': 'TX'},
    {'code': 'SAT', 'name': 'San Antonio International Airport', 'city': 'San Antonio', 'state': 'TX'},
    {'code': 'TYR', 'name': 'Tyler Pounds Regional Airport', 'city': 'Tyler', 'state': 'TX'},
    {'code': 'VCT', 'name': 'Victoria Regional Airport', 'city': 'Victoria', 'state': 'TX'},
    {'code': 'WAC', 'name': 'Waco Regional Airport', 'city': 'Waco', 'state': 'TX'},
    
    # Utah
    {'code': 'SLC', 'name': 'Salt Lake City International Airport', 'city': 'Salt Lake City', 'state': 'UT'},
    {'code': 'CDC', 'name': 'Cedar City Regional Airport', 'city': 'Cedar City', 'state': 'UT'},
    
    # Vermont
    {'code': 'BTV', 'name': 'Burlington International Airport', 'city': 'Burlington', 'state': 'VT'},
    
    # Virginia
    {'code': 'ORF', 'name': 'Norfolk International Airport', 'city': 'Norfolk', 'state': 'VA'},
    {'code': 'PHF', 'name': 'Newport News/Williamsburg International Airport', 'city': 'Newport News', 'state': 'VA'},
    {'code': 'RIC', 'name': 'Richmond International Airport', 'city': 'Richmond', 'state': 'VA'},
    {'code': 'ROA', 'name': 'Roanoke-Blacksburg Regional Airport', 'city': 'Roanoke', 'state': 'VA'},
    
    # Washington
    {'code': 'GEG', 'name': 'Spokane International Airport', 'city': 'Spokane', 'state': 'WA'},
    {'code': 'PSC', 'name': 'Tri-Cities Airport', 'city': 'Pasco', 'state': 'WA'},
    {'code': 'SEA', 'name': 'Seattle-Tacoma International Airport', 'city': 'Seattle', 'state': 'WA'},
    {'code': 'ALW', 'name': 'Walla Walla Regional Airport', 'city': 'Walla Walla', 'state': 'WA'},
    {'code': 'YKM', 'name': 'Yakima Air Terminal', 'city': 'Yakima', 'state': 'WA'},
    
    # West Virginia
    {'code': 'CRW', 'name': 'Yeager Airport', 'city': 'Charleston', 'state': 'WV'},
    {'code': 'HTS', 'name': 'Tri-State Airport', 'city': 'Huntington', 'state': 'WV'},
    
    # Wisconsin
    {'code': 'GRB', 'name': 'Green Bay Austin Straubel International Airport', 'city': 'Green Bay', 'state': 'WI'},
    {'code': 'MKE', 'name': 'Milwaukee Mitchell International Airport', 'city': 'Milwaukee', 'state': 'WI'},
    {'code': 'MSN', 'name': 'Dane County Regional Airport', 'city': 'Madison', 'state': 'WI'},
    {'code': 'RHI', 'name': 'Rhinelander-Oneida County Airport', 'city': 'Rhinelander', 'state': 'WI'},
    
    # Wyoming
    {'code': 'CPR', 'name': 'Casper-Natrona County International Airport', 'city': 'Casper', 'state': 'WY'},
    {'code': 'CYS', 'name': 'Cheyenne Regional Airport', 'city': 'Cheyenne', 'state': 'WY'},
    {'code': 'JAC', 'name': 'Jackson Hole Airport', 'city': 'Jackson', 'state': 'WY'},
    {'code': 'LAR', 'name': 'Laramie Regional Airport', 'city': 'Laramie', 'state': 'WY'},
    
    # Puerto Rico
    {'code': 'BQN', 'name': 'Rafael Hernández Airport', 'city': 'Aguadilla', 'state': 'PR'},
    {'code': 'PSE', 'name': 'Mercedita Airport', 'city': 'Ponce', 'state': 'PR'},
    {'code': 'SJU', 'name': 'Luis Muñoz Marín International Airport', 'city': 'San Juan', 'state': 'PR'},
    
    # US Virgin Islands
    {'code': 'STT', 'name': 'Cyril E. King Airport', 'city': 'Charlotte Amalie', 'state': 'VI'},
    {'code': 'STX', 'name': 'Henry E. Rohlsen Airport', 'city': 'Christiansted', 'state': 'VI'},
]

def get_all_us_airports():
    """Return all US airports"""
    return US_AIRPORTS

def search_airports(query: str):
    """Search airports by code, city, or name"""
    query_upper = query.upper().strip()
    query_lower = query.lower().strip()
    
    # If query is exactly 3 characters, treat as airport code
    if len(query_upper) == 3:
        exact_match = [airport for airport in US_AIRPORTS if airport['code'] == query_upper]
        if exact_match:
            return exact_match
    
    # Search by airport code, city name, or airport name
    matches = []
    for airport in US_AIRPORTS:
        if (query_upper in airport['code'] or 
            query_lower in airport['city'].lower() or 
            query_lower in airport['name'].lower()):
            matches.append(airport)
    
    # Return top 15 matches (increased from 10)
    return matches[:15]
