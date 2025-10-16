#1
EmptyList = []

#2
FiveList = [1,2,3,4,5]

#3
print(len(FiveList))

#4
print(f"{FiveList[0]}, {FiveList[2]}, {FiveList[4]}")

#5
mixed_data_types = ["Victor", 19, 70, "Single", "Address"]

#6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#7
print(it_companies)

#8
print(len(it_companies))

#9
print(f"{it_companies[0]}, {it_companies[3]}, {it_companies[6]}")

#10
it_companies[1] = "Meta"
print(it_companies)

#11
it_companies.append("Google")

#12
it_companies.insert(4, "NVidia")

#13
it_companies[0] = it_companies[0].upper()

#14
it_companies = it_companies + ["#; "]

#15
TRUTH =  ("Google") in it_companies

#16
it_companies = it_companies.sort()

#17
it_companies = it_companies.sort(reverse=True)

#18
FirstThree = it_companies[0:2]

#19
LastThree = it_companies[-3:]

#20
Middle = it_companies[len(it_companies)/2]

#21
it_companies = it_companies.pop(0)

#22
it_companies = it_companies.pop(len(it_companies)/2)

#23
it_companies = it_companies.pop()

#24
it_companies = it_companies.clear()

#25
del it_companies

#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
Joined = front_end + back_end

#27
full_stack = Joined.copy()
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")

#Big Exercise
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages = ages.sort()
min = ages[0]
max = ages[len(ages)-1]
average = sum(ages)/len(ages)
range = max-min
compare = abs(min-average) - abs(max-average)

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

middle = countries[len(countries)/2]
FirstHalf = countries[0:len(countries)/2]
SecondHalf = countries[len(countries)/2:]
MiniCountries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
a, b, c, *scandic = MiniCountries