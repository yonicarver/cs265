

{

	'artist1':
		{
			'release_date1':
				{
					'album11': ['song111', 'song112', 'song113']
				},
			'release_date2':
				{
					'album12': ['song121', 'song122', 'song123']
				}
		},

	'artist2': 
		{
			'release_date3':
				{
					'album21': ['song211', 'song212', 'song213']
				},
			'release_date4':
				{
					'album22': ['song221', 'song222', 'song223']
				}
		}

}





{'artist1':{'release_date1':{'album11': ['song111', 'song112', 'song113']},'release_date2':{'album12': ['song121', 'song122','song123']}},'artist2':{'release_date3':{'album21': ['song211', 'song212', 'song213']},'release_date4':{'album22': ['song221', 'song222', 'song223']}}}


>>> for i in range(len(contents)):
...   d.update({contents[i].splitlines()[0]:{contents[i].splitlines()[1][0:4]:{contents[i].splitlines()[1][5:]:[contents[i].splitlines()[2:][i][1:]]}}})


[
	{
		'artist': 'Led Zeppelin'
		'album': 'In Through the Outdoor',
		'release_date': '1979',
		'songs':
			[
				'In the Evening',
				'South Bound Saurez',
				'Fool in the Rain',
				'Hot Dog',
				'Carouselambra',
				'All My Love',
				"I'm Gonna Crawl"
			]
	}
	{
		'artist': 'Led Zeppelin'
		'album': 'II',
		'release_date': '1969',
		'songs':
			[
				'Whole Lotta Love',
				'What Is and What Should Never Be',
				'The Lemon Song',
				'Thank You',
				'Heartbreaker',
				"Living Loving Maid (She's Just a Woman)",
				'Ramble On',
				'Moby Dick',
				'Bring It on Home',
			]
	}
	{
		'artist': 'Bob Dylan'
		'album': 'Blonde on Blonde',
		'release_date': '1966',
		'songs':
			[
				'Rainy Day Women #12 & 35',
				'Pledging My Time',
				'Visions of Johanna',
				'One of Us Must Know (Sooner or Later)',
				'I Want You',
				'Stuck Inside of Mobile with the Memphis Blues Again',
				'Leopard-Skin Pill-Box Hat',
				'Just Like a Woman',
				"Most Likely You Go Your Way (And I'll Go Mine)",
				'Temporary Like Achilles',
				'Absolutely Sweet Marie',
				'4th Time Around',
				'Obviously 5 Believers',
				'Sad Eyed Lady of the Lowlands',
			]
	}
]



"""
Led Zeppelin
1979 In Through the Outdoor
-In the Evening
-South Bound Saurez
-Fool in the Rain
-Hot Dog
-Carouselambra
-All My Love
-I'm Gonna Crawl

Led Zeppelin
1969 II
-Whole Lotta Love
-What Is and What Should Never Be
-The Lemon Song
-Thank You
-Heartbreaker
-Living Loving Maid (She's Just a Woman)
-Ramble On
-Moby Dick
-Bring It on Home

Bob Dylan
1966 Blonde on Blonde
-Rainy Day Women #12 & 35
-Pledging My Time
-Visions of Johanna
-One of Us Must Know (Sooner or Later)
-I Want You
-Stuck Inside of Mobile with the Memphis Blues Again
-Leopard-Skin Pill-Box Hat
-Just Like a Woman
-Most Likely You Go Your Way (And I'll Go Mine)
-Temporary Like Achilles
-Absolutely Sweet Marie
-4th Time Around
-Obviously 5 Believers
-Sad Eyed Lady of the Lowlands

"""




TODO:
- make sure when incorrect argument is entered, print usage message
- be able to read files that do not end in '\n\n' (EOF)

