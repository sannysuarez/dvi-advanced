from datetime import datetime, timedelta


def custom_humanize_time(dt):
    now = datetime.now()
    diff = now - dt

    if diff < timedelta(seconds=60):
        return "just now"
    elif diff < timedelta(minutes=1):
        seconds = diff.seconds
        return f"{seconds}s"
    elif diff < timedelta(hours=1):
        minutes = diff.seconds // 60
        return f"{minute}m"
    elif diff < timedelta(days=1):
        hours = diff.seconds // 3600
        return f"{hours}h"
    elif diff < timedelta(days=30):
        days = diff.days
        return f"{days}d"
    elif diff < timedelta(days=365):
        months = diff.days // 30
        return f"{months}m"
    else:
        years = diff.days // 365
        return f"{years}y"

def get_countries():
    return [
        ("AF", "Afghanistan"),
        ("AL", "Albania"),
        ("DZ", "Algeria"),
        ("AD", "Andorra"),
        ("AO", "Angola"),
        ("AG", "Antigua and Barbuda"),
        ("AR", "Argentina"),
        ("AM", "Armenia"),
        ("AU", "Australia"),
        ("AT", "Austria"),
        ("AZ", "Azerbaijan"),
        ("BS", "Bahamas"),
        ("BH", "Bahrain"),
        ("BD", "Bangladesh"),
        ("BB", "Barbados"),
        ("BY", "Belarus"),
        ("BE", "Belgium"),
        ("BZ", "Belize"),
        ("BJ", "Benin"),
        ("BT", "Bhutan"),
        ("BO", "Bolivia"),
        ("BA", "Bosnia and Herzegovina"),
        ("BW", "Botswana"),
        ("BR", "Brazil"),
        ("BN", "Brunei"),
        ("BG", "Bulgaria"),
        ("BF", "Burkina Faso"),
        ("BI", "Burundi"),
        ("CV", "Cabo Verde"),
        ("KH", "Cambodia"),
        ("CM", "Cameroon"),
        ("CA", "Canada"),
        ("CF", "Central African Republic"),
        ("TD", "Chad"),
        ("CL", "Chile"),
        ("CN", "China"),
        ("CO", "Colombia"),
        ("KM", "Comoros"),
        ("CG", "Congo"),
        ("CD", "Congo (DRC)"),
        ("CR", "Costa Rica"),
        ("CI", "Côte d'Ivoire"),
        ("HR", "Croatia"),
        ("CU", "Cuba"),
        ("CY", "Cyprus"),
        ("CZ", "Czechia"),
        ("DK", "Denmark"),
        ("DJ", "Djibouti"),
        ("DM", "Dominica"),
        ("DO", "Dominican Republic"),
        ("EC", "Ecuador"),
        ("EG", "Egypt"),
        ("SV", "El Salvador"),
        ("GQ", "Equatorial Guinea"),
        ("ER", "Eritrea"),
        ("EE", "Estonia"),
        ("SZ", "Eswatini"),
        ("ET", "Ethiopia"),
        ("FJ", "Fiji"),
        ("FI", "Finland"),
        ("FR", "France"),
        ("GA", "Gabon"),
        ("GM", "Gambia"),
        ("GE", "Georgia"),
        ("DE", "Germany"),
        ("GH", "Ghana"),
        ("GR", "Greece"),
        ("GD", "Grenada"),
        ("GT", "Guatemala"),
        ("GN", "Guinea"),
        ("GW", "Guinea-Bissau"),
        ("GY", "Guyana"),
        ("HT", "Haiti"),
        ("HN", "Honduras"),
        ("HU", "Hungary"),
        ("IS", "Iceland"),
        ("IN", "India"),
        ("ID", "Indonesia"),
        ("IR", "Iran"),
        ("IQ", "Iraq"),
        ("IE", "Ireland"),
        ("IL", "Israel"),
        ("IT", "Italy"),
        ("JM", "Jamaica"),
        ("JP", "Japan"),
        ("JO", "Jordan"),
        ("KZ", "Kazakhstan"),
        ("KE", "Kenya"),
        ("KI", "Kiribati"),
        ("KP", "Korea (North)"),
        ("KR", "Korea (South)"),
        ("KW", "Kuwait"),
        ("KG", "Kyrgyzstan"),
        ("LA", "Laos"),
        ("LV", "Latvia"),
        ("LB", "Lebanon"),
        ("LS", "Lesotho"),
        ("LR", "Liberia"),
        ("LY", "Libya"),
        ("LI", "Liechtenstein"),
        ("LT", "Lithuania"),
        ("LU", "Luxembourg"),
        ("MG", "Madagascar"),
        ("MW", "Malawi"),
        ("MY", "Malaysia"),
        ("MV", "Maldives"),
        ("ML", "Mali"),
        ("MT", "Malta"),
        ("MH", "Marshall Islands"),
        ("MR", "Mauritania"),
        ("MU", "Mauritius"),
        ("MX", "Mexico"),
        ("FM", "Micronesia"),
        ("MD", "Moldova"),
        ("MC", "Monaco"),
        ("MN", "Mongolia"),
        ("ME", "Montenegro"),
        ("MA", "Morocco"),
        ("MZ", "Mozambique"),
        ("MM", "Myanmar"),
        ("NA", "Namibia"),
        ("NR", "Nauru"),
        ("NP", "Nepal"),
        ("NL", "Netherlands"),
        ("NZ", "New Zealand"),
        ("NI", "Nicaragua"),
        ("NE", "Niger"),
        ("NG", "Nigeria"),
        ("NO", "Norway"),
        ("OM", "Oman"),
        ("PK", "Pakistan"),
        ("PW", "Palau"),
        ("PA", "Panama"),
        ("PG", "Papua New Guinea"),
        ("PY", "Paraguay"),
        ("PE", "Peru"),
        ("PH", "Philippines"),
        ("PL", "Poland"),
        ("PT", "Portugal"),
        ("QA", "Qatar"),
        ("RO", "Romania"),
        ("RU", "Russia"),
        ("RW", "Rwanda"),
        ("KN", "Saint Kitts and Nevis"),
        ("LC", "Saint Lucia"),
        ("VC", "Saint Vincent and the Grenadines"),
        ("WS", "Samoa"),
        ("SM", "San Marino"),
        ("ST", "São Tomé and Príncipe"),
        ("SA", "Saudi Arabia"),
        ("SN", "Senegal"),
        ("RS", "Serbia"),
        ("SC", "Seychelles"),
        ("SL", "Sierra Leone"),
        ("SG", "Singapore"),
        ("SK", "Slovakia"),
        ("SI", "Slovenia"),
        ("SB", "Solomon Islands"),
        ("SO", "Somalia"),
        ("ZA", "South Africa"),
        ("SS", "South Sudan"),
        ("ES", "Spain"),
        ("LK", "Sri Lanka"),
        ("SD", "Sudan"),
        ("SR", "Suriname"),
        ("SE", "Sweden"),
        ("CH", "Switzerland"),
        ("SY", "Syria"),
        ("TW", "Taiwan"),
        ("TJ", "Tajikistan"),
        ("TZ", "Tanzania"),
        ("TH", "Thailand"),
        ("TL", "Timor-Leste"),
        ("TG", "Togo"),
        ("TO", "Tonga"),
        ("TT", "Trinidad and Tobago"),
        ("TN", "Tunisia"),
        ("TR", "Turkey"),
        ("TM", "Turkmenistan"),
        ("TV", "Tuvalu"),
        ("UG", "Uganda"),
        ("UA", "Ukraine"),
        ("AE", "United Arab Emirates"),
        ("GB", "United Kingdom"),
        ("US", "United States"),
        ("UY", "Uruguay"),
        ("UZ", "Uzbekistan"),
        ("VU", "Vanuatu"),
        ("VA", "Vatican City"),
        ("VE", "Venezuela"),
        ("VN", "Vietnam"),
        ("YE", "Yemen"),
        ("ZM", "Zambia"),
        ("ZW", "Zimbabwe"),
    ]

'''
This function mimic the username generation logic from the frontend, to further avoid clashes.
'''
def generate_username(username):
    full_name = request.form['full_name']
    # Split the full name into parts and clean it up
    name_parts = full_name.strip().split()
    first_name = name_parts[0] if name_parts else ''
    last_name = name_parts[-1] if len(name_parts) > 1 else '' # Get the last name if multiple names exist

    # Get the first 3 letters of the first name
    first_part = first_name[:3].lower() if first_name else ''

    # Get the first 3 or 4 letters of the last name
    last_part = (last_name[:4].lower() if len(last_name) >= 4 else last_name[:3].lower()) if last_name else ''

    # Generate random 4 digits
    random_digits = random.randint(1000, 9999)

    # Combine parts to form the username
    username = first_part + last_part + random_digits  # Concatenate parts

    return username





