def album():    
    albuns = {
        "Taylor Swift": [
            "Tim McGraw", "Picture To Burn", "Teardrops On My Guitar", "A Place in This World",
            "Cold As You", "The Outside", "Tied Together with a Smile", "Stay Beautiful", "Should've Said No", "Mary's Song (Oh My My My)", "Our Song", "I'm Only Me When I'm With You", "Invisible", "A perfect Good Heart"
        ],

        "Fearless": [
            "jump Then Fall", "Untouchble", "Forever & Always", "Come In With The Rain", "SuperStar", "The Other Side Of The Door", "Fearless", "Fifteen", "Love Story", "Hey Stephen", "White Horse", "You Belong with Me",
            "Breathe", "Tell Me Why", "You're Not Sorry", "The Way I Loved You", "Forever & Always",
            "The Best Day", "Change"
        ],

        "Speak Now": [
            "Mine", "Sparks Fly", "Back to December", "Speak Now", "Dear John", "Mean", "The Story of Us",
            "Never Grow Up", "Enchanted", "Better than Revenge", "Innocent", "Haunted", "Last Kiss",
            "Long Live", "Ours", "if This Was A Movie", "Superman"
        ],

        "Red": [
            "State of Grace", "Red", "Treacherous", "I Knew You Were Trouble", "All Too Well", "22",
            "I Almost Do", "We Are Never Ever Getting Back Together", "Stay Stay Stay", "The Last Time", "Holy Ground", "Sad Beautiful Tragic", "The Lucky One", "Everything Has Changed", "Starlight", "Begin Again", "The Moment I Knew", "Come Back...Be Here", "Girl At Home"
        ],

        "1989": [
            "Welcome to New York", "Blank Space", "Style", "Out of the Woods", "All You Had to Do Was Stay",
            "Shake It Off", "I Wish You Would", "Bad Blood", "Wildest Dreams", "How You Get The Girl", "This Love", "I Know Places", "Clean", "Wonderland", "You Are In Love", "New Romantics"
            ],
        
        "Reputation": ["...Ready For It?", "End Game", "I Did Something Bad", "Don't Blame Me", "Delicate",
            "Look What You Made Me Do", "So It Goes...", "Gorgeous", "Getaway Car", "King Of My Heart", "Dacing With Our Hands Tied", "Dress", "This Is Why We Can't Have Nice Things", "Call It What You Want", "New Year's Say"
            ],

        "Lover": ["I Forgot That You Existed", "Cruel Summer", "Lover", "The Man", "The Archer", "I Think He Knows",
            "Miss Americana & The Heartbreak Prince", "Paper Rings", "Cornelia Street", "Death by a Thousand Cuts", "London Boy", "Soon You'll Get Better", "False God", "You Need to Calm Down", "Afterglow", "ME!", "It's Nice to Have a Friend", "Daylight", "All The Girls You Loved Before"
            ],

        "Folklore": [
            "the 1", "cardigan", "the last great american dynasty", "exile", "my tears ricochet",
            "mirrorball", "seven", "august", "this is me trying", "illicit affairs", "invisible string",
            "mad woman", "epiphany", "betty", "peace", "hoax", "the lakes"
        ],

        "Evermore": [
            "willow", "champagne Problems", "gold Rush", "tis the Damn Season", "tolerate It",
            "no Body, No Crime", "happiness", "dorothea", "coney Island", "ivy", "cowboy like me", "long story short", "marjorie", "clousere", "evermore", "right where you left me", "it's time to go"
            ],

            "Midnights": [
            "Lavender Haze", "Maroon", "Anti-Hero", "Snow on the Beach", "You're on Your Own, Kid",
            "Midnight Rain", "Question...?", "Vigilante Shit", "Bejeweled", "Labyrinth", "Karma", "Sweet Nothing", "Mastermind", "The Great War", "Bigger Than The Whole World", "Paris", "High Infidelity", "Glitch", "Would've, Could've, Should've", "Dear Reader", "Hits Different", "Snow On The Beach (ft. More Lana)"
        ],

        "The Tortured Poets Department": [
            "Fortnight (feat. Post Malone)", "The Tortured Poets Department", "My Boy Only Breaks His Favorite Toys", "Down Bad", "So Long, London", "But Daddy, I Love Him", "Fresh Out the Slammer", "Florida!!! (feat. Florence + The Machine)", "Guilty as Sin?", "Who’s Afraid of Little Old Me?", "I Can Fix Him (No Really I Can)", "loml","I Can Do It With a Broken Heart", "The Smallest Man Who Ever Lived", "The Alchemy", "Clara Bow", "The Black Dog", "imgonnagetyouback", "The Albatross", "Chloe or Sam or Sophia or Marcus", "How Did It End?", "So High School", "I Hate It Here", "thanK you alMee", "I Look in People's Windows", "The prophecy", "Cassandra", "Peter", "The Bolter", "Robin", "The Manuscript"
    ],

        "The Life of a Showgirl": [
            "The Fate of Ophelia", "Elizabeth Taylor", "Opalite", "Father Figure", "Eldest Daughter",
            "Ruin the Friendship", "Actually Romantic", "Wish List", "Wood", "CANCELLED!", "Honey",
            "The Life of a Showgirl"
        ]        
    }
    return albuns

def listar_albuns():
    albuns = album()
    return list(albuns.keys())
    
def listar_musicas(album_escolhido):
    albuns = album()
    if album_escolhido not in albuns:
        return f'A loirinha não reconhece {album_escolhido} como um de seus filhos.'

    return albuns[album_escolhido]

def tocar_musica(album_escolhido, musica_escolhida):
    albuns = album()
    
    # Verifica se album existe
    if album_escolhido not in albuns:
        return f'Esse álbum não existe 😅'

    # Verifica se a música está no album
    if musica_escolhida not in albuns[album_escolhido]:
        return f'Tá certo isso? 🧐'
    
    return f'\n\033[32mTocando {musica_escolhida}... 🎶\033[m\n'
     