import webbrowser

def album():    
    albuns = {
        "Taylor Swift": {
            "Tim McGraw": "https://youtu.be/GkD20ajVxnY?si=6nYtnOlQvpNDtp_c", 

            "Picture To Burn": "https://youtu.be/yCMqcFAigRg?si=MUiBUWMsYxi8TZwU", 

            "Teardrops On My Guitar": "https://youtu.be/xKCek6_dB0M?si=V9a53CpT7jqFaG3m",

            "A Place in This World": "https://youtu.be/pYFqLzFoHo0?si=U3X7ug1iYPPnTvom",

            "Cold As You": "https://youtu.be/SoXPvCcFibo?si=uam3RbJDo-e5unWb",

            "The Outside": "https://youtu.be/L4hOi4KvRY0?si=YssraPpiXVeMwBPo",

            "Tied Together with a Smile": "https://youtu.be/aCVHGH5sO0c?si=o9dVIGvPPA7rulGi",

            "Stay Beautiful": "https://youtu.be/6BOPfGQLUH8?si=m47dOTZdoUjtr729",

            "Should've Said No": "https://youtu.be/dUisZV--Nbs?si=AUgC38g-Ukdd79Gi",

            "Mary's Song (Oh My My My)": "https://youtu.be/NlQbK-Vu37I?si=J_zVEvrfCpBr6jI2",

            "Our Song": "https://youtu.be/Jb2stN7kH28?si=gff9l3v33QXdk7cD",

            "I'm Only Me When I'm With You": "https://youtu.be/AlTfYj7q5gQ?si=DKTl7pFQ6Z3uR7Iw",

            "Invisible": "https://youtu.be/8OOKMt0Rz1k?si=DwNRmBXS6hA9lY-R",

            "A perfect Good Heart": "https://youtu.be/vv85ZAvrVDU?si=3xVnndN5__RNWmDA"
        },

        "Fearless": {
            "jump Then Fall": "https://youtu.be/vUHDR6Rg3Y4?si=krrGCKFLZe4xmH4I",

            "Untouchble": "https://youtu.be/8bNlGwnEUAs?si=TqPONhRUeWXMvVUZ",

            "Forever & Always": "https://youtu.be/T-41vMWQTUA?si=ZvhL0Of6_SlY-LXB",

            "Come In With The Rain": "https://youtu.be/ePjcjLRHPOo?si=zWh4XMGcCYxK8fmR",

            "SuperStar": "https://youtu.be/IsCik8wznlU?si=JbyZt5czst79AGCr",

            "The Other Side Of The Door": "https://youtu.be/425n1NoRtgA?si=KOlJL9jBhppeP5db",

            "Fearless": "https://youtu.be/7lLigiVgJsE?si=-ry9e9kcJXcP4Jqh",

            "Fifteen": "https://youtu.be/rLCol1C3ouc?si=cy3WmH5Pz9XBwjJN",

            "Love Story": "https://youtu.be/aXzVF3XeS8M?si=NE68K_FFLBx73K-c",

            "Hey Stephen": "https://youtu.be/tMhiHrL7rPE?si=-GBs3mLLhvMxE7JI",

            "White Horse": "https://youtu.be/9-rKvhsjwKU?si=AkFyAFNoO2VtsAj6",

            "You Belong with Me": "https://youtu.be/vwp8Ur6tO-8?si=RYm9aFgiTZt7JWXG",

            "Breathe": "https://youtu.be/qsUK-BG5OQQ?si=w0qUEWGz1TvGb3eW",

            "Tell Me Why": "https://youtu.be/cwFbq-70EwE?si=A99-3ouh5R8NLS38",

            "You're Not Sorry": "https://youtu.be/DNaSlUYIXBg?si=drCthPAt-9wAiQEn",

            "The Way I Loved You": "https://youtu.be/DlexmDDSDZ0?si=pncydBtmss7mdyAV",

            "Forever & Always": "https://youtu.be/T-41vMWQTUA?si=nnPDWZ3CCI-v1pgQ",

            "The Best Day": "https://youtu.be/KZeI9I875Ig?si=Np2sgnG5Lk_vgtiZ",

            "Change": "https://youtu.be/jwWR1cQTKyw?si=2m_V-8VP0b55Y6aK",

            "today was a fairytale": "https://youtu.be/xSWVPqnKcXQ?si=NgLg2y8n7bx9p2vj",

            "you all over me": "https://youtu.be/XKaMUm7YwZc?si=xtc0qm0bdxinP6Re",

            "we were happy": "https://youtu.be/seU5y5EgIwk?si=OnKJ65NgUh4_RZgk",

            "don't you": "https://youtu.be/dHdAN4FXzmc?si=Ec2hB0Of0CQ8Htgf",

            "by by baby": "https://youtu.be/yuFuwXd-B9E?si=heqY8LNDXGm2ISjD"
        },

        "Speak Now": {
            "Mine": "https://youtu.be/6KnDUtPoelU?si=WPGu4HskbA07mflW",

            "Sparks Fly": "https://youtu.be/EEoxLHS9uRk?si=dk08cqdjzGqlrPAV",

            "Back to December": "https://youtu.be/oOEhHDx6xOQ?si=43fao6aVUSsEkpPT",

            "Speak Now": "https://youtu.be/rTiYSVlOQjo?si=RqIoKX23nB6aJShD",

            "Dear John": "https://youtu.be/32M2jmNjIGM?si=kPxA9PrA2kGFZc3a",

            "Mean": "https://youtu.be/U-EscA9-cKg?si=tdqyNnw7dixwSBOy",

            "The Story of Us": "https://youtu.be/s-QGeo_dpn4?si=dy359pjUcilPVfxE",

            "Never Grow Up": "https://youtu.be/TbrbQm2k4T8?si=vzipBb1nqhL2LyEA",

            "Enchanted": "https://youtu.be/7IID5YLPg7w?si=OUzgdS8lbtSExf93",

            "Better than Revenge": "https://youtu.be/MSWhTUMH3pM?si=tJBoR3LLjad4W_kA",

            "Innocent": "https://youtu.be/A2wlx7ZkkkQ?si=KOtYEcHxaVcHyJhH",

            "Haunted": "https://youtu.be/81MSlL6ORhc?si=UFFR8v2TnmTWHI3K",

            "Last Kiss": "https://youtu.be/aoreqPHfzc0?si=U_ZHzWu3Vfd9LtrR",

            "Long Live": "https://youtu.be/R_eQOYSHDi8?si=XnpqrGFjVjhCZ9om",

            "Ours": "https://youtu.be/GkLR36yWLdg?si=qdnIKkrrxHJ5Yawh",

            "if This Was A Movie": "https://youtu.be/9wZEx9A8p9k?si=vtCKyzwYEbF3YlMK", 

            "Superman": "https://youtu.be/gJBxF51bF9Y?si=WOjEmyzTfdwrhkdK",

            "eletric touch": "https://youtu.be/6ySa23nqXso?si=-w_HHU67Tj-OX3MH",

            "when emma falls in love": "https://youtu.be/3d5Zd0B2egQ?si=Mw_HcUqmwnZ7zm_o",

            "i can see you": "https://youtu.be/F42wDv5uUPo?si=YrPZUucBKKccGQwq",

            "castle crumbling": "https://youtu.be/HtDriYDIhRs?si=fltR15u24NEtUlk6",

            "foolish one": "https://youtu.be/OwHE_MjV5E4?si=vwx8NE654_6d95Wp",

            "timeless": "https://youtu.be/HzxvuB8k96Y?si=qB1SOgXpvyppbC38"
        },

        "Red": {
            "State of Grace": "https://youtu.be/gr4cqcqnAN0?si=c2WJQMfhh1v0mKMd",

            "Red": "https://youtu.be/fnI07MzNWzA?si=tpTndj2_G93obX84",

            "Treacherous": "https://youtu.be/OE2RVmaioAo?si=yeDBHttE2HFcW--X",

            "I Knew You Were Trouble": "https://youtu.be/zGTRceZ1kZw?si=3yAN9PIg3ls5RYDW",

            "All Too Well": "https://youtu.be/rX9GLnJ06F4?si=UHZckyY8JtuucByw",

            "22": "https://youtu.be/xGWTv4IQ7vQ?si=BQtR5hK0xMudf9hK",

            "I Almost Do": "https://youtu.be/VzggqDYcuVg?si=suiFVF2ycJwIW9Iu",

            "We Are Never Ever Getting Back Together": "https://youtu.be/DA5IFd2TFjQ?si=OCLsE1ojxsJO4n8G",

            "Stay Stay Stay": "https://youtu.be/QEYTzDJO_eM?si=goYm_kSZfKxMWOAs",

            "The Last Time": "https://youtu.be/CQ8L-PaDfyc?si=t2fjDDet_qdMn4ig",

            "Holy Ground": "https://youtu.be/NA90OVe2ixo?si=QTtRiYdOZTKPUAcB",

            "Sad Beautiful Tragic": "https://youtu.be/iKTSubwwq8Y?si=Hehhr-2h0DzbbD3I",

            "The Lucky One": "https://youtu.be/MOc2VuNqAQc?si=Tppvih9k23b95WLp",

            "Everything Has Changed": "https://youtu.be/SWQwtE9N5aU?si=xEjf5QmiISFcHuIK",

            "Starlight": "https://youtu.be/90JHxH7bVaQ?si=WG6d0wE7jZYHGLXB",

            "Begin Again": "https://youtu.be/bVcxtHhyfZQ?si=zCS1XKRgrRbheeIp",

            "The Moment I Knew": "https://youtu.be/wyWI1vA8WX4?si=Eh9fmkClRpMRmPWT",

            "Come Back...Be Here": "https://youtu.be/0y7FnmhZuaw?si=egifhm_tPevpr8wf",

            "Girl At Home": "https://youtu.be/Nbnuq6r90kg?si=yXT6cWRbpSll3lJg",

            "ronan": "https://youtu.be/dcNG2Ua0YSs?si=DQyLeLgJBQTPmMtm",

            "better man": "https://youtu.be/VwCQAP-XPA8?si=te227ovuTmPYiV0Y",

            "nothing new": "https://youtu.be/EsiqARpjOBQ?si=dAxNkokZ4h1_keBD",

            "babe": "https://youtu.be/3XGlNU__M68?si=C3dX3DvByAoyfY54",

            "message in a bottle": "https://youtu.be/fFMPxt-XNIk?si=38Yjoa81R_mydPgL",

            "i bet you thing about me": "https://youtu.be/Aifi_CiXDeM?si=SanABeM619gOhlF_",

            "forever winter": "https://youtu.be/UVa0YRSbK9E?si=Djf-CoUXK4IR1en_",

            "run": "https://youtu.be/b7Qse2cuHmg?si=tYofEmc5q08aLZgD",

            "the very first night": "https://youtu.be/kwYXepzkhWY?si=v8z1IHgfMY1H4nC7",

            "all too well (10 min)": "https://youtu.be/7SqC7_f_-0M?si=4Ky8Q3I0rzsLK4Xx"

        },

        "1989": {
            "Welcome to New York": "https://youtu.be/0BYUf8QDCZU?si=EF4tz2pvRrI8YQxD",
             
            "Blank Space": "https://youtu.be/-MtKC5wXqdQ?si=PKthh43v2KuQZv9a",

            "Style": "https://youtu.be/w6Y8fvBczYM?si=sjOKa8S43zpCPbIT",

            "Out of the Woods": "https://youtu.be/Qc0sEMYv620?si=c32HtNsr2VoAP4RK",

            "All You Had to Do Was Stay": "https://youtu.be/cEUCx9x8G_0?si=NnFc46JqqYnqb67P",

            "Shake It Off": "https://youtu.be/nOc68bLYe90?si=bmf1n6dx3tON_LpI",

            "I Wish You Would": "https://youtu.be/U3KmJGLSrTM?si=6ueX8m7WVEmDM1ia",

            "Bad Blood": "https://youtu.be/VCb5JPnyoHs?si=LV_BVQ8DIO-4AxsE",

            "Wildest Dreams": "https://youtu.be/K5HYyIi-jq8?si=MYQP_ddcYbilZyI0",

            "How You Get The Girl": "https://youtu.be/XQh8zhmTtBg?si=p1QW1fBRz-be6zAU",

            "This Love": "https://youtu.be/TzlQ1bH4Xw0?si=VaRNUi_o2V6Gqrjc",

            "I Know Places": "https://youtu.be/4KdM2fmNXBA?si=eElTDUmUOFiGOM0l",

            "Clean": "https://youtu.be/RKAXdSe8MYM?si=EZy2BCceBgMq99bp",

            "Wonderland": "https://youtu.be/E048L9PaZsk?si=BipSnce8sLWqzJxQ",

            "You Are In Love": "https://youtu.be/a_zwscPcDGM?si=GwUFQcpc8SISO9RD", 

            "New Romantics": "https://youtu.be/M1JzkdygfhA?si=yCYmVRs3cweYmiC-",

            "slut!": "https://youtu.be/E1Y3RD3Vt7I?si=nh4RxJLgg_vRaUh7",

            "say don't go": "https://youtu.be/uk2MKQYa4n8?si=unsmJKHU1Zhb4-WO",

            "now that we don't talk": "https://youtu.be/kaF6H9JvPiY?si=FvUOHDdg2o3pdlns",

            "suburban legends": "https://youtu.be/TujvFAda2H4?si=6_1Lst929keET52c",

            "is it over now?": "https://youtu.be/IV-jmLUe0Go?si=WEbA-RTq9vxvH70Z"
        },
        
        "Reputation": {
            "...Ready For It?": "https://youtu.be/Qf9SOEkZR9Q?si=fnRXENaFWYz48Ax1",

            "End Game": "https://youtu.be/zAiOfWu5xUk?si=lednulhnPVAMbkds",
             
            "I Did Something Bad": "https://youtu.be/xYLxUJ9v6KU?si=O5YnUJ6Ce1oT-Vyh",

            "Don't Blame Me": "https://youtu.be/kRJKB291Z1g?si=ZuiZQ0leYnXOWIkf",

            "Delicate": "https://youtu.be/5XMCHTAbwtU?si=56SMNPMNCKjq5ifY",

            "Look What You Made Me Do": "https://youtu.be/I3Fr6iKX7VI?si=WEzi644-sltYgO0V",
             
            "So It Goes...": "https://youtu.be/iAv1Y1YIwm8?si=HnKKjYmBvIompNjQ",

            "Gorgeous": "https://youtu.be/5DT_ZkSLc4o?si=uV_yzbzursiQdvLi",

            "Getaway Car": "https://youtu.be/FhPLQVlUiNQ?si=IfXajmECBYvx7pBu",

            "King Of My Heart": "https://youtu.be/5U7bF68xcRg?si=s_GQLFIHW5wJSQTa",

            "Dacing With Our Hands Tied": "https://youtu.be/erGyUphZSt8?si=zAlHVzL9P61brBOB",

            "Dress": "https://youtu.be/FNEoPctNIUE?si=Pr_xrLeOaVP9pdVX",

            "This Is Why We Can't Have Nice Things": "https://youtu.be/6Z3QJ4L1Bg0?si=Stf-oW2D6p685ZaT",

            "Call It What You Want": "https://youtu.be/J1oCCGSt6XA?si=FAnk0ORZEiErJ6OP",

            "New Year's Say": "https://youtu.be/KkvTYrFIxNM?si=8e1AYRYjfzpEYwZH"
        },

        "Lover": {
            "I Forgot That You Existed": "https://youtu.be/gLLE3B75UJw?si=5SnPJlCBKatxoQSq",

            "Cruel Summer": "https://youtu.be/aC9HkZW2hZk?si=wbOsnuCwbCrHphHX",

            "Lover": "https://youtu.be/uLL2xTK35Qc?si=SDrg3Z5WgxbIs5tC",

            "The Man": "https://youtu.be/1KZ6l73sJ0A?si=frBd15cpRZdfqYpF",

            "The Archer": "https://youtu.be/3sAdg1N-byw?si=dj_gXic2mL9hQjLa",

            "I Think He Knows": "https://youtu.be/eOn_3lSlbzU?si=mdqc0CAqCmw6Kzqz",

            "Miss Americana & The Heartbreak Prince": "https://youtu.be/2B9fBFtBXhU?si=pZs6CFq7IA-vFBUy",

            "Paper Rings": "https://youtu.be/a3FVEgsi5ag?si=oEsddr4HCj3JrhSa",

            "Cornelia Street": "https://youtu.be/bqJ9I-3MG1g?si=8OKRY8Q4YgX6SprS",

            "Death by a Thousand Cuts": "https://youtu.be/KNp1yY9s5dc?si=l-jBf5f3S0S1pvL8",

            "London Boy": "https://youtu.be/0o0WbQV6OZQ?si=u8OV7lvkcf6gKINc",

            "Soon You'll Get Better": "https://youtu.be/z64GAXlF_dg?si=JI5Iq2j4Wemtj3Fg",

            "False God": "https://youtu.be/T5quSUmWt1Y?si=532ECPZXaS2sRQEP",

            "You Need to Calm Down": "https://youtu.be/1wgr1Bjxs7E?si=lZw7XK48wlmW5f30",

            "Afterglow": "https://youtu.be/oNiyHQhYqTc?si=y4KgU8J3mDUzgdLu",

            "ME!": "https://youtu.be/M3G1Y7VL200?si=BKKLgXC3LZE2W0Aj",

            "It's Nice to Have a Friend": "https://youtu.be/pVpO3zc4Shs?si=b7FZICm2yc10BT-h",

            "Daylight": "https://youtu.be/ppqxBjkziqo?si=PIp-nuRTyXsDzPSY",

            "All The Girls You Loved Before": "https://youtu.be/SpLJl9Au3fw?si=L-1790Fv2jLh7gtt"
        },

        "Folklore": {
            "the 1": "https://youtu.be/KsZ6tROaVOQ?si=4HBDZVMVc5XB_DuI",

            "cardigan": "https://youtu.be/K-a8s8OLBSE?si=-DwA-3UmfNq_VBRT",

            "the last great american dynasty": "https://youtu.be/2s5xdY6MCeI?si=YlCL2NfdbVYZKUYt",

            "exile": "https://youtu.be/osdoLjUNFnA?si=xVmpKiPKs6lx3W5e",

            "my tears ricochet": "https://youtu.be/OWbDJFtHl3w?si=y9kqKbyErqdQlBTf",

            "mirrorball": "https://youtu.be/KaM1bCuG4xo?si=rXinycjGG-w8yEMd",

            "seven": "https://youtu.be/pEY-GPsru_E?si=VHXJAavmJfrM1GLL", 

            "august": "https://youtu.be/nn_0zPAfyo8?si=P3NA-E8Q7HrlO6Vw",

            "this is me trying": "https://youtu.be/9bdLTPNrlEg?si=471g_rrTC5k0WVo6",

            "illicit affairs": "https://youtu.be/MLV2SJKWk4M?si=gv0io3lHPBbSFYpn",

            "invisible string": "https://youtu.be/OuFnpmGwg5k?si=5CVeegyPgsR-REIt",

            "mad woman": "https://youtu.be/6DP4q_1EgQQ?si=eTO_CSf85gPsRYsw",

            "epiphany": "https://youtu.be/DUnDkI7l9LQ?si=wR8Dpjyn3sEaqnuq",

            "betty": "https://youtu.be/6TAPqXkZW_I?si=iz_bi_FJqZmh3HUw",

            "peace": "https://youtu.be/HpxX4ZE4KWE?si=azzUcNDIoOf-xvtM",

            "hoax": "https://youtu.be/ryLGxpjwAhM?si=EItBz0xJhdcIyzpy",

            "the lakes": "https://youtu.be/tOHcAc3r2kw?si=proq4HyJQCVgHUxx"
        },

        "Evermore": {
            "willow": "https://youtu.be/RsEZmictANA?si=XHlgXf2xy8-IzZ-Z",

            "champagne Problems": "https://youtu.be/wMpqCRF7TKg?si=HxS7vZ1XGVDdX22d",

            "gold Rush": "https://youtu.be/Pz-f9mM3Ms8?si=vq2VmJ8RZ-b656nO",

            "tis the Damn Season": "https://youtu.be/WuvhOD-mP8M?si=nP-v9hBUMTkQ8rmp",

            "tolerate It": "https://youtu.be/ukxEKY_7MOc?si=677bpPlnbhaVZCCv",

            "no Body, No Crime": "https://youtu.be/IEPomqor2A8?si=RLwZ_MUWYOse77TI",

            "happiness": "https://youtu.be/tP4TTgt4nb0?si=NG-qN_qc-czOlnNk",

            "dorothea": "https://youtu.be/zI4DS5GmQWE?si=Iprzxcrt7xYZ8wic",

            "coney Island": "https://youtu.be/c_p_TBaHvos?si=n2GuY5P33qWxEkkC",

            "ivy": "https://youtu.be/9nIOx-ezlzA?si=UruLm33xAzkpNhX-",

            "cowboy like me": "https://youtu.be/YPlNBb6I8qU?si=sat-brb0plFHm0zM",

            "long story short": "https://youtu.be/rqQHa2HcGtM?si=FhWBnSUmDNvWn72N",
             
            "marjorie": "https://youtu.be/hP6QpMeSG6s?si=RhWse6ML2GKnFm7l",

            "clousere": "https://youtu.be/AIFnKqIeEdY?si=x8YXvH78roxNm4P3",

            "evermore": "https://youtu.be/EXLgZZE072g?si=Cr7VesvDGO9A2HJp",

            "right where you left me": "https://youtu.be/Ur_wAcYDnuA?si=zYyXq9ddqmzon3gR",

            "it's time to go": "https://youtu.be/1iRbIYkccgw?si=XWrJMpqxQ0DHw6zq"
        },

            "Midnights": {
            "Lavender Haze": "https://youtu.be/mkR_Qwix4Ho?si=jez9QGRB4Q7gb9Q0",

            "Maroon": "https://youtu.be/lvHZjvIyqsk?si=emB_sg0J8B2M78WY",

            "Anti-Hero": "https://youtu.be/XqN2qFvY64U?si=vDJ4vY4ObhkHwcVO",

            "Snow on the Beach": "https://youtu.be/ycE7bUq3-2k?si=4uvDWEax9sPo963A",

            "You're on Your Own, Kid": "https://youtu.be/7Gbg6Z70J7E?si=5n1KYcpz-9SgOu5D",

            "Midnight Rain": "https://youtu.be/Odh9ddPUkEY?si=lei5tM-1JAorUDLF",

            "Question...?": "https://youtu.be/xxrf_QBD5DE?si=vzuAAiFDzX-bbYJT",

            "Vigilante Shit": "https://youtu.be/Uoey4W_3bos?si=HvUB_9nlLPc3g5tE",

            "Bejeweled": "https://youtu.be/XzKSPRqFg9E?si=VV4jIsfmiZqNB6Mc",

            "Labyrinth": "https://youtu.be/xTXsKMXUi7w?si=uYMKUcIPKNFPRcBP",

            "Karma": "https://youtu.be/rg18Kf4en2o?si=sYXnbtkJgSp91oB8",

            "Sweet Nothing": "https://youtu.be/rn0brgg2BpI?si=Tj8mROnQ_JLYM494",

            "Mastermind": "https://youtu.be/Tmz1lz0zcLQ?si=7I1hSGZEIKVeadNj",
             
            "The Great War": "https://youtu.be/iFX6_9h7th0?si=a9ivE3zcv7rhfHC8",

            "Bigger Than The Whole World": "https://youtu.be/ySZGZrcqvr4?si=hSp77HuX1l0F_czG",

            "Paris": "https://youtu.be/ySZGZrcqvr4?si=YtsVP2ApHWgxhFKL",

            "High Infidelity": "https://youtu.be/-qee6dFKlw4?si=kOkum3EWJWbSDmEg",

            "Glitch": "https://youtu.be/Y2a73EvnZ4s?si=zHVUSCOKOQaxzHaE",

            "Would've, Could've, Should've": "https://youtu.be/B-MfwP_RmHY?si=AClcsZq9stRN-3Zs",

            "Dear Reader": "https://youtu.be/X0Jti9F-oQA?si=Zdq_Lszr3wXjhlit",

            "Hits Different": "https://youtu.be/_f4yoKJL7IQ?si=170T6kYFig53tjod",

            "Snow On The Beach (ft. More Lana)": "https://youtu.be/2CnUYMmEHrs?si=oKuWKQT9nGKy5lR9"
            },

        "The Tortured Poets Department": {
            "Fortnight (feat. Post Malone)": "https://youtu.be/b7kmP1fsGg8?si=KaU0BFcrJuf91mIs",

            "The Tortured Poets Department": "https://youtu.be/L92Ui4LzP2U?si=rocEuAwmz_9lFhSV",

            "My Boy Only Breaks His Favorite Toys": "https://youtu.be/jwtXVmFTYVY?si=iijTkO2eiOdxDNc2",

            "Down Bad": "https://youtu.be/N61UALi1MuI?si=FdpqX3ld4xrazM3g",

            "So Long, London": "https://youtu.be/WDVCPCKPLwg?si=nB5b4EOJNiJEj50n",

            "But Daddy, I Love Him": "https://youtu.be/Q3wtBSk1YS4?si=WqNYc6htrIqWuL7A",

            "Fresh Out the Slammer": "https://youtu.be/_XGbyjwGiCA?si=y31BcbLe8VHDyF0h",

            "Florida": "https://youtu.be/m6hi8iuajzE?si=9sWSiWwiNE7AuhoY",
            
            "Guilty as Sin?": "https://youtu.be/ESFAIxZb8K4?si=D6QDDLTkoumcwo3j",

            "Who’s Afraid of Little Old Me?": "https://youtu.be/in1YgJkraEE?si=OyjWKNcQy6Bk4J85",

            "I Can Fix Him (No Really I Can)": "https://youtu.be/Ck5L06dQ060?si=U85pNw9FxuCWObMv",

            "loml": "https://youtu.be/o0NlmZg9ahI?si=BQ1iosQYOismTx4m",

            "I Can Do It With a Broken Heart": "https://youtu.be/_x8kI-aM56M?si=zKSTctb92b3dRjNi",

            "The Smallest Man Who Ever Lived": "https://youtu.be/lSCbseKwNFI?si=GuTgpfSVgAeN6FDD",

            "The Alchemy": "https://youtu.be/FK-ETNt7M7E?si=qG1k66NAt5E8NXds",

            "Clara Bow": "https://youtu.be/iJJDUmk8XNA?si=tIWbpNVM-afVBvah",

            "The Black Dog": "https://youtu.be/5-wL58HMsXo?si=rS3H3ofZh0qA88Gu",

            "imgonnagetyouback": "https://youtu.be/B8z8FRyT_lU?si=QcFr3vEBXOjl3GNN",

            "The Albatross": "https://youtu.be/TZaa2cJFBg0?si=NNQKBVmYrg_gjCsO",

            "Chloe or Sam or Sophia or Marcus": "https://youtu.be/CK4QBAOgJ6c?si=59murexOuH1r8fo1",

            "How Did It End?": "https://youtu.be/T0ltPgydMhg?si=c4GvMPuuBtpMcIQo",

            "So High School": "https://youtu.be/raBlDihTtbU?si=hky49z5SJA2mQq4i",

            "I Hate It Here": "https://youtu.be/-3r6lwB5VBI?si=jOPDyOkpygkUgI7N",

            "thanK you alMee": "https://youtu.be/grbVHCV4yYc?si=pRqSEwq_IIY3PBzP",

            "I Look in People's Windows": "https://youtu.be/n_Exoqe2xdE?si=CTx0YjiprSYzI6un",

            "The prophecy": "https://youtu.be/gKLNmXPTXMc?si=AnFGJJCkieF6u5TZ",

            "Cassandra": "https://youtu.be/rxXPPSwwhfo?si=_ywglS2LQ5-NgW7G",

            "Peter": "https://youtu.be/lEpMyK2_DU0?si=wZ_jpM1EdneVm5eb",

            "The Bolter": "https://youtu.be/WiadPYfdSL0?si=DHcbPVZf_Lf62xjK",
             
            "Robin": "https://youtu.be/XWTuqWcOJEM?si=IVdSvu9osI8GSh4s",

            "The Manuscript": "https://youtu.be/6hvDW1mt_nE?si=K-zKRY9CHvp5a9Xm"
        },

        "The Life of a Showgirl": {
            "The Fate of Ophelia": "INDISPONÍVEL", 
            "Elizabeth Taylor": "INDISPONÍVEL", 
            "Opalite": "INDISPONÍVEL", 
            "Father Figure": "INDISPONÍVEL", 
            "Eldest Daughter": "INDISPONÍVEL",
            "Ruin the Friendship": "INDISPONÍVEL", 
            "Actually Romantic": "INDISPONÍVEL", 
            "Wish List": "INDISPONÍVEL", 
            "Wood": "INDISPONÍVEL", 
            "CANCELLED!": "INDISPONÍVEL", 
            "Honey": "INDISPONÍVEL",
            "The Life of a Showgirl": "INDISPONÍVEL"
        }       
    }
    return albuns

def listar_albuns():
    return list(album().keys())
    
def listar_musicas(album_escolhido):
    albuns = album()
    if album_escolhido not in albuns:
        return []
    return list(albuns[album_escolhido].keys())

def tocar_musica(album_escolhido, musica_escolhida):
    albuns = album()
    # Verifica se album existe
    if album_escolhido not in albuns:
        return f'Esse álbum não existe 😅'

    # Verifica se a música está no album
    if musica_escolhida not in albuns[album_escolhido]:
        return f'Essa não é uma música da loirinha 😅'
    
    url = albuns[album_escolhido][musica_escolhida]
    return webbrowser.open_new(url)

