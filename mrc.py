def generate_manga_list(selected_numbers, filename="items_list.txt"):
    manga_data = {
1:"""[b]1 - El Gallo[/b][list=1]
[*]Read a manga with an [url=https://www.mangaupdates.com/series?category=Animal+Leading+Character%2Fs]animal main character[/url]. 
[*]Read a manga about [url=https://www.mangaupdates.com/series?category=Betrayal]betrayal[/url].
[*]Read a manga featuring [url=https://myanimelist.net/manga/genre/6/Mythology]mythology[/url] or [url=https://www.mangaupdates.com/series?category=Folklore]folklore[/url]. 
[/list]""",
2:"""[b]2 - El Diablito[/b][list=1]
[*]Read a manga with a [url=https://www.mangaupdates.com/series?category=Devil%2Fs]devil character[/url]. 
[*]Read a manga by an author/artist you don't like. [color=#4682B4]- State a manga you've read by them already.[/color]
[*]Read a manga another MRC participant rated 4 or lower.  [color=#4682B4]- Link to their post and profile.[/color]
[/list]""",
3:"""[b]3 - La Dama[/b][list=1]
[*]Read a [url=https://myanimelist.net/manga/genre/42/Josei]josei[/url] or [url=https://myanimelist.net/manga/genre/25/Shoujo]shoujo[/url] manga. 
[*]Read a manga with a [url=https://www.mangaupdates.com/series?category=Strong+Female+Lead]Strong Female Lead[/url]. 
[*]Read a manga with an all female main cast.
[/list]""",
4:"""[b]4 - El Catrin[/b][list=1]
[*]Read a [url=https://myanimelist.net/manga/genre/27/Shounen]shounen[/url] or [url=https://myanimelist.net/manga/genre/41/Seinen]seinen[/url] manga. 
[*]Read a manga by an author/artist you don't know.
[*]Read a manga tagged under [url=https://www.mangaupdates.com/series?category=European+Ambience]European Ambience[/url]. [color=#4682B4]- The tag on Mangaupdates is required.[/color]
[/list]""",
5:"""[b]5 - El Paraguas[/b][list=1]
[*]Read a manga with weather conditions on the cover.  [color=#4682B4]- Such as Rain, Snow, Fog, Thunder, etc.[/color]
[*]Read a collection of short stories. [color=#4682B4]- They can be a compilation by the same author or by different authors.[/color]
[*]Read a [url=https://myanimelist.net/manga/genre/44/Gender_Bender]Gender Bender[/url] manga. [color=#4682B4]- Suggestions: [url=https://myanimelist.net/manga/genre/44/Crossdressing]Crossdressing[/url], [url=https://myanimelist.net/manga/genre/65/Magical_Sex_Shift]Magical Sex Shift[/url], [url=https://www.mangaupdates.com/series?category=Trap]Trap[/url][/color]
[/list]""",
7:"""[b]7 - La Escalera[/b][list=1]
[*]Read a manga that was [url=https://myanimelist.net/reviews.php?t=manga]recently reviewed[/url]. [color=#4682B4]- Recently reviewed means reviewed in the 3 months prior to starting it.[/color]
[*]Read a manga by an author/artist who has published 5 manga or less.
[*]Read an ongoing manga. 
[/list]""",
8: """[b]8 - La Botella[/b][list=1]
[*]Read a [url=https://myanimelist.net/manga/genre/55/Delinquents]Delinquents[/url] manga.
[*]Read a manga that started publishing in the 80s. - (1980-1989) 
[*]Read a manga based on a [url=https://www.mangaupdates.com/series?category=Based%20on%20a%20Novel]novel/light novel[/url]/[url=https://www.mangaupdates.com/series?category=Based+on+a+Web+Novel]web novel[/url].
[/list]""",
9:"""[b]9 - El Barril [/b][list=1]
[*]Read a manga that is on one of the active MRC staff's Plan to Read list.  [color=#4682B4]- Note which staff member it was as well as the date, or add a screenshot.[/color]
[*]Read a manga with an antihero or villain main character. [color=#4682B4]- Suggestions: [url=https://www.mangaupdates.com/series?category=Antihero+%2F+Antiheroine]Anti-Hero/Heroine[/url] | [url=https://www.mangaupdates.com/series?category=Villain+Protagonist]Villain Protagonist[/url] | [url=https://www.mangaupdates.com/series?category=Reincarnated+as+the+Villain%2Fess]Reincarnated as the Villain/ness[/url][/color]
[*]Read a manga that is not ranked.  [color=#4682B4]- Ranking must say N/A.[/color]
[/list]""",
10:"""[b]10 - El Arbol [/b][list=1]
[*]Read a manga with plants on the cover. 
[*]Read a manga about [url=https://www.mangaupdates.com/series?category=Nature]nature[/url]. [color=#4682B4]- Anything set in nature or about the things in nature: mountains, ocean, the arctic, etc.[/color]
[*]Read a manga that takes place in the [url=https://www.mangaupdates.com/series?category=Countryside]countryside[/url]. 
[/list]""",
11:"""[b]11 - El Melon[/b][list=1]
[*]Read a [url=https://myanimelist.net/manga/genre/52/CGDCT]CGDCT[/url] or [url=https://myanimelist.net/manga/genre/63/Iyashikei]Iyashikei[/url] manga.
[*]Read a [url=https://myanimelist.net/manga/genre/36/Slice_of_Life]Slice of Life[/url] manga.
[*]Read a manga with only one genre. 
[/list]""",
12:"""[b]12 - El Valiente[/b] [list=1]
[*]Read an [url=https://myanimelist.net/manga/genre/1/Action]Action[/url] or [url=https://myanimelist.net/manga/genre/2/Adventure]Adventure[/url] manga. 
[*]Read a manga recommended to you by another participant in the discussion thread.  [color=#4682B4]- Link to their post or add a screenshot, making sure to include their username.[/color]
[*]Read a [url=https://www.mangaupdates.com/series?category=Battle+Royale]battle royale[/url] / [url=https://www.mangaupdates.com/series?category=Survival]survival[/url] manga.
[/list]""",
13:"""[b]13 - El Gorrito[/b][list=1]
[*]Read a [url=https://myanimelist.net/manga/genre/53/Childcare]Childcare[/url] manga. 
[*]Read a manga that started publishing in the 2020s. - (2020-2025) 
[*]Read a manga with both a child and an adult main character.  [color=#4682B4]- The child has to be 12 years old or younger, and the adult has to be 18 years old or older.[/color]
[/list]""",
14:"""[b]14 - La Muerte[/b][list=1]
[*]Read a manga about a [url=https://www.mangaupdates.com/series?category=Family]family[/url].
[*]Read a manga with a [url=https://www.mangaupdates.com/series?category=Shinigami%2FGrim+Reaper]shinigami[/url] character.
[*]Read a manga with a weapon or blood on the cover. 
[/list]""",
15:"""[b]15 - La Pera[/b][list=1]
[*]Read a [url=https://myanimelist.net/topmanga.php?type=oneshots]one-shot[/url]. 
[*]Read a manga with a score of 8 or above. 
[*]Read a manga that is 1-3 volumes or 25 chapters or less in length. 
[/list]""",
16:"""[b]16 - La Bandera[/b][list=1]
[*] Read a [url=https://myanimelist.net/topmanga.php?type=manhua]Manhua[/url] or a [url=https://myanimelist.net/topmanga.php?type=manhwa]Manhwa[/url].
[*]Read a manga that takes place outside of Japan, but in the real world. 
[*]Read a [url=https://myanimelist.net/manga/genre/17/Martial_Arts]Martial Arts[/url], [url=https://myanimelist.net/manga/genre/13/Historical]Historical[/url], or [url=https://myanimelist.net/manga/genre/21/Samurai]Samurai[/url] manga. 
[/list]""",
17:"""[b]17 - El Bandolon[/b][list=1]
[*]Read a manga by your favorite author/artist.
[*]Read a manga that started publishing before or in the 70s. - (19XX-1979)
[*]Read a manga with a symbol in the title. [color=#4682B4]- Excluding punctuation (i.e., ~!@#$%&, etc.). Only symbols not on the keyboard count (i.e., ♪★☆♥△, etc.).[/color]
[/list]""",
18:"""[b]18 - El Violoncello[/b][list=1]
[*]Read a [url=https://myanimelist.net/manga/genre/14/Horror]Horror[/url] or [url=https://myanimelist.net/manga/genre/37/Supernatural]Supernatural[/url] manga. 
[*]Read a manga tagged with [url=https://www.mangaupdates.com/series?category=Dystopia]Dystopia[/url] / [url=https://www.mangaupdates.com/series?category=Apocalypse]Apocalypse[/url] / [url=https://www.mangaupdates.com/series?category=Post-Apocalyptic]Post-Apocalyptic[/url].  [color=#4682B4]- One of the mentioned tags on Mangaupdates is required.[/color]
[*]Read a manga that includes a character with a [url=https://www.mangaupdates.com/series?category=Disability%2Fies]disability[/url].  [color=#4682B4]- It has to be a non-temporary disability. Things like broken limbs don't count unless it's permanent.[/color]
[/list]""",
19:"""[b]19 - La Garza[/b][list=1]
[*]Read an [url=https://www.mangaupdates.com/series?category=Isekai]isekai[/url] manga. 
[*]Read a manga including time travel.  [color=#4682B4]- Suggestions: [url=https://www.mangaupdates.com/series?category=Time+Travel]Time Travel[/url] | [url=https://www.mangaupdates.com/series?category=Time+Traveler%2Fs]Time Traveller/s[/url][/color]
[*]Read any manga recommended to your Favorite Manga listed in profile.  [color=#4682B4]- Make sure to list your favorite manga.[/color]
[/list]""",
20:"""[b]20 - El Pajaro[/b][list=1]
[*]Read a web/[url=https://www.mangaupdates.com/series?category=4-koma%2FYonkoma]4-koma[/url] manga. 
[*]Read a colored manga. -  [color=#4682B4]- Either use a tagged manga or attach a screenshot showing the color. 
(It can't be a central single color page because of a special event or commemoration. It has to be the default state of the manga. Extra content doesn't count.) Suggestions: [url=https://www.mangaupdates.com/series?category=Full+Color]Full Color[/url] | [url=https://www.mangaupdates.com/series?category=Partially+Colored]Partially Colored[/url] | [url=https://www.mangaupdates.com/series?category=Accent+Colors]Accent Colors[/url][/color]
[*]Read a [url=https://myanimelist.net/manga/genre/68/Memoir]Memoir[/url] or [url=https://www.mangaupdates.com/series?category=Biography+%2F+Autobiography]Biography/Autobiography[/url] manga. 
[/list]""",
21:"""[b]21 - La Mano[/b][list=1]
[*]Read a manga with a score of 6 or lower. 
[*]Read a manga tagged under [url=https://www.mangaupdates.com/series?category=Atypical+Art+Style]Atypical Art Style[/url], [url=https://www.mangaupdates.com/series?category=Elaborate+Art+Style]Elaborate Art Style[/url], [url=https://www.mangaupdates.com/series?category=Sketchy+Art+Style]Sketchy Art Style[/url], or [url=https://www.mangaupdates.com/series?category=Realistic+Art+Style]Realistic Art Style[/url]. 
[*]Read a manga that got [url=https://www.mangaupdates.com/series?category=Rushed+Ending+%2F+Axed&perpage=50]cancelled/axed[/url]. 
[/list]""",
22:"""[b]22 - La Bota[/b][list=1]
[*]Read a manga by an author/artist duo. 
[*]Read a [url=https://www.mangaupdates.com/series?category=Magical+Girl%2Fs]Magical Girl[/url] or [url=https://www.mangaupdates.com/series?category=Magical+Boy%2Fs]Magical Boy[/url] manga. [color=#4682B4]- Also: [url=https://myanimelist.net/manga/genre/66/Mahou_Shoujo]Mahou Shoujo[/url][/color]
[*]Read a manga with the same first and last letter.  [color=#4682B4]- Title must be at least 2 letters long.[/color]
[/list]""",
23:"""[b]23 - La Luna[/b] [list=1]
[*]Read a doujinshi based on a series you've read.
[*]Read a [url=https://myanimelist.net/manga/genre/10/Fantasy]Fantasy[/url] or [url=https://myanimelist.net/manga/genre/7/Mystery]Mystery[/url] manga. 
[*]Read a manga with the same number of male and female main characters. 
[/list]""",
24:"""[b]24 - El Cotorro[/b][list=1]
[*]Read a manga from a mangaka that shares your birthday month. 
[*]Read a manga that has been [url=https://myanimelist.net/clubs.php?cid=5450]adapted to live action[/url]. [color=#4682B4]- You can also check out the "adapted to [url=https://www.mangaupdates.com/series?category=Adapted+to+Chinese+Drama]Chinese drama[/url]/[url=https://www.mangaupdates.com/series?category=Adapted+to+Kdrama]Kdrama[/url]/[url=https://www.mangaupdates.com/series?category=Adapted+to+Live+Action]live action[/url]/[url=https://www.mangaupdates.com/series?category=Adapted+to+Taiwanese+drama]Taiwanese drama[/url]" tags on mangaupdates for ideas.[/color]
[*]Read a manga related to something you previously read. [color=#4682B4]- Make a note of the previous manga.[/color]
[/list]""",
27:"""[b]27 - El Corazon[/b][list=1]
[*]Read a [url=https://myanimelist.net/manga/genre/8/Drama]Drama[/url] or [url=https://myanimelist.net/manga/genre/22/Romance]Romance[/url] manga.
[*]Read a manga ranked in the top 1000. 
[*]Read a manga from the ones listed under manga relations in the [url=https://myanimelist.net/clubs.php?cid=8776]Hidden Gems of Manga club[/url]. 
[/list]""",
28:"""[b]28 - La Sandia[/b][list=1]
[*]Read a manga by an author/artist who has published 10 manga or more. 
[*]Read a [url=https://www.mangaupdates.com/series?category=Food]Food[/url] or [url=https://myanimelist.net/manga/genre/47/Gourmet]Gourmet[/url] manga. 
[*]Read an [url=https://www.mangaupdates.com/series?category=Award-Winning+Work]award-winning[/url] manga.  [color=#4682B4]- Make a note of which award the manga won.[/color]
[/list]""",
29:"""[b]29 - El Tambor[/b][list=1]
[*]Read a manga about [url=https://www.mangaupdates.com/series?category=Music]Music[/url], or [url=https://www.mangaupdates.com/series?category=Art]Art[/url].
[*]Read a manga with the same number of volumes as letters in your username.
[*]Read a manga with a main character that is a professional in their field.  [color=#4682B4]- The MC needs to earn a living with it.[/color]
[/list]""",
30:"""[b]30 - El Camaron[/b][list=1]
[*]Read a manga another MRC participant rated 9 or higher.  [color=#4682B4]- Link to their post and profile.[/color]
[*]Read a manga with a one word title.
[*]Read a manga from a magazine with less than 50 titles in the database.
[/list]""",
31:"""[b]31 - Las Jaras[/b][list=1]
[*]Read a manga that started publishing in the 90s. - (1990-1999) 
[*]Read a [url=https://myanimelist.net/manga/genre/30/Sports]Sports[/url] or [url=https://www.mangaupdates.com/series?category=Game%2Fs]Games[/url] manga.  [color=#4682B4]- See also [url=https://myanimelist.net/manga/genre/59/High_Stakes_Game]High Stakes Game[/url], [url=https://myanimelist.net/manga/genre/11/Strategy_Game]Strategy Game[/url], [url=https://myanimelist.net/manga/genre/80/Video_Game]Video Game[/url][/color]
[*]Read a [url=https://myanimelist.net/manga/genre/67/Medical]Medical[/url] or [url=https://www.mangaupdates.com/series?category=Illness]Illness[/url] manga.
[/list]""",
32:"""[b]32 - El Musico[/b][list=1]
[*]Read a [url=https://myanimelist.net/manga/genre/23/School]School[/url] manga. 
[*]Read a manga with no characters on the cover. 
[*]Read a manga with a listed cast of 8 or more people. 
[/list]""",
33:"""[b]33 - La Arana[/b][list=1]
[*]Read a [url=https://myanimelist.net/manga/genre/31/Super_Power]Super Power[/url], [url=https://www.mangaupdates.com/series?category=Demon%2Fs]Demon[/url], or [url=https://myanimelist.net/manga/genre/32/Vampire]Vampire[/url] manga.
[*]Read a [url=https://myanimelist.net/manga/genre/40/Psychological]Psychological[/url] or [url=https://myanimelist.net/manga/genre/45/Suspense]Suspense[/url] manga. 
[*]Read a manga with both a human and a non-human main character. [color=#4682B4]- Any character that isn't human counts, even if they have a human appearance.[/color]
[/list]""",
34:"""[b]34 - El Soldado[/b][list=1]
[*]Read a [url=https://myanimelist.net/manga/genre/18/Mecha]Mecha[/url], [url=https://myanimelist.net/manga/genre/39/Detective]Detective[/url], or [url=https://myanimelist.net/manga/genre/38/Military]Military[/url] manga. 
[*]Read a manga with a Japanese honorific in the title (e.g. chan, san, kun, sama, etc.)
[*]Read a manga that started publishing in the 2000s. - (2000-2009)
[/list]""",
35:"""[b]35 - La Estrella[/b][list=1]
[*]Read a [url=https://myanimelist.net/manga/genre/24/Sci-Fi]Sci-Fi[/url] or [url=https://myanimelist.net/manga/genre/29/Space]Space[/url] manga.
[*]Read a manga ranked ABOVE [url=https://myanimelist.net/topmanga.php?limit=2000]2,000[/url][color=#4682B4]- Example:1998,1999, ... , etc. It has to be ranked. (No N/A!).[/color]
[*]Read a manga featuring [url=https://www.mangaupdates.com/series?category=Magic]Magic[/url] or [url=https://www.mangaupdates.com/series?category=Wizard%2Fs]Wizards[/url]. 
[/list]""",
36:"""[b]36 - El Cazo[/b][list=1]
[*]Read a manga with more users listed in PTR than Completed.
[*]Read a manga with more than 10,000 completed members.
[*]Read a manga with an older main character (i.e. 40+).  [color=#4682b4]- Suggestions: [url=https://www.mangaupdates.com/series?category=Older+Male+Lead]Older Male Lead[/url], [url=https://www.mangaupdates.com/series?category=Older+Female+Lead]Older Female Lead[/url], [url=https://www.mangaupdates.com/series?category=Older+Protagonist]Older Protagonist[/url][/color]
[/list]""",
37:"""[b]37 - El Mundo[/b][list=1]
[*]Read a [url=https://myanimelist.net/manga/genre/28/Boys_Love]BL[/url] or [url=https://myanimelist.net/manga/genre/26/Girls_Love]GL[/url] manga. 
[*]Read a manga featuring [url=https://www.mangaupdates.com/series?category=LGBT+Themes]LGBT themes[/url]. [color=#4682b4]- Also [url=https://www.mangaupdates.com/series?category=LGBT+Issues]LGBT Issues[/url][/color]
[*]Read a manga with a vehicle on the cover.  [color=#4682B4]- Cars, Trains, Bicycles, Airplanes, etc.[/color]
[/list]""",
38:"""[b]38 - El Apache[/b][list=1]
[*]Read a manga that takes place in feudal Japan. [color=#4682B4]- Suggestions: [url=https://www.mangaupdates.com/series?category=Feudal+Japan]Feudal Japan[/url] | [url=https://www.mangaupdates.com/series?category=Sengoku%20Era]Sengoku Era[/url] | [url=https://www.mangaupdates.com/series?category=Edo+Period]Edo Period[/url][/color]
[*]Read a manga about [url=https://www.mangaupdates.com/series?category=Zombie%2Fs]zombies[/url]. 
[*]Read a manga featuring [url=https://www.mangaupdates.com/series?category=Curse%2Fs]Curses[/url]. 
[/list]""",
39:"""[b]39 - El Nopal[/b][list=1]
[*]Read a manga that has not been adapted in any way. 
[*]Read a manga with a [url=https://www.mangaupdates.com/series?category=Tsundere+Character%2Fs]tsundere[/url] character.
[*]Read a manga with 6 or more words in its title. 
[/list]""",
40:"""[b]40 - El Alacran[/b][list=1]
[*]Read a manga focused on [url=https://www.mangaupdates.com/series?category=Revenge]revenge[/url]. 
[*]Read a manga based on a one-shot.
[*]Read a manga tagged with your least favorite genre(s).
[/list]""",
41:"""[b]41 - La Rosa[/b][list=1]
[*]Read a manga with a [url=https://www.mangaupdates.com/series?category=Love+Confession%2Fs]love confession[/url].
[*]Read a manga with more than 30,000 total members.
[*]Read a manga with a main cast of [url=https://myanimelist.net/manga/genre/50/Adult_Cast]18+ year-olds[/url]. [color=#4682B4]- The whole main cast must be 18+ years old.[/color]
[/list]""",
42:"""[b]42 - La Calavera[/b][list=1]
[*]Read a manga with a main character that wears glasses.  [color=#4682B4]- Suggestions: [url=https://www.mangaupdates.com/series?category=Glasses-Wearing+Male+Lead]Male MC[/url] | [url=https://www.mangaupdates.com/series?category=Glasses-Wearing+Female+Lead]Female MC[/url][/color]
[*]Read a manga [url=https://www.mangaupdates.com/series?category=Based+on+an+Anime]based on an anime[/url]. 
[*]Read a manga series you can finish in one day. 
[/list]""",
43:"""[b]43 - La Campana[/b][list=1]
[*]Read a manga suggested by MAL or by [url=https://anime.plus/]Anime+[/url].
[*]Read a manga that an active MRC staff member has rated 9 or higher. [color=#4682B4]- Note which staff member it was as well as the date, or add a screenshot.[/color]
[*]Read a manga recommended by any MRC staff. [color=#4682B4]- Anywhere is fine, add a screenshot and/or link to prove a staff member suggested it to you. Suggestions: [url=https://myanimelist.net/forum/?topicid=2070401]discussion thread[/url] | [url=https://discord.com/invite/9mwFDfF]our discord server[/url][/color]
[/list]""",
44:"""[b]44 - El Canarito[/b][list=1]
[*]Re-read a manga. 
[*]Read a manga that has at least 2 anime seasons. 
[*]Read a manga with more listed supporting characters than main characters. 
[/list]""",
45:"""[b]45 - El Venado[/b][list=1]
[*]Read a manga about characters with [url=https://www.mangaupdates.com/series?category=Animal+Characteristics]animal characteristics[/url]. [color=#4682B4]- Personality or physical characteristics.[/color]
[*]Read a manga that's been the source of one of your completed anime. [color=#4682B4]- The anime should have "manga" as its source and be completed before you read the manga. You can use the [url=https://www.mangaupdates.com/series?category=Adapted%20to%20Anime]Adapted to anime[/url] tag on mangaupdates for ideas. [/color] 
[*]Read a manga with an all male main cast. 
[/list]""",
46:"""[b]46 - El Sol[/b][list=1]
[*]Read a manga with more than 500 favorites. 
[*]Read a [url=https://myanimelist.net/featured/search?q=manga]featured[/url] manga. 
[*]Read a manga with an element in the title (e.g. fire, water, earth, air, etc.).  [color=#4682b4]- The element can be present in an alternative title or not in English. Specify the title used for this item in case it's not the main title.[/color]
[/list]""",
47:"""[b]47 - La Corona[/b][list=1]
[*]Read a manga with about [url=https://www.mangaupdates.com/series?category=Royalty]Royalty[/url]. 
[*]Read a manga that is scored higher than its anime adaptation. 
[*]Read the first or earliest work of your favorite creator. 
[/list]""",
48:"""[b]48 - La Chalupa[/b][list=1]
[*]Read a manga that started publishing on the day you joined MAL (any month/year). 
[*]Read a manga that started publishing in the month you joined MAL (any year). 
[*]Read a manga that started publishing in the year you joined MAL.
[/list]""",
49:"""[b]49 - El Pino[/b][list=1]
[*]Read a manga with five or more genres.
[*]Read a manga that is 10+ volumes or 200 chapters or more in length
[*]Read a manga recommended to another manga you've read for this challenge. [color=#4682B4]- Make a note of the previous manga.[/color]
[/list]""",
50:"""[b]50 - El Pescado[/b][list=1]
[*]Read a favorite from one of your MAL friends - so they finally stop telling you to do it. [color=#4682B4]- Link to their profile.[/color]
[*]Read a manga with an animal on the cover.
[*]Read a manga that has been [url=https://www.mangaupdates.com/series?category=Adapted+to+Game]Adapted to Game[/url].  [color=#4682b4]- Also: [url=https://www.mangaupdates.com/series?category=Adapted+to+Visual+Novel]Adapted to Visual Novel[/url][/color]
[/list]""",
51:"""[b]51 - La Palma [/b][list=1]
[*]Read a manga based on a game.  [color=#4682b4]- Suggestions: [url=https://www.mangaupdates.com/series?category=Based+on+a+Video+Game]Based on a Video Game[/url], [url=https://www.mangaupdates.com/series.?category=Adapted+to+Game]Adapted to Game[/url], [url=https://www.mangaupdates.com/series?category=Based+on+an+Otome+Game]Based on an Otome Game[/url], [url=https://www.mangaupdates.com/series?category=Based+on+a+Card+Game]Based on a Card Game[/url][/color]
[*]Read an active [url=https://myanimelist.net/about.php?go=team]MAL staff[/url] member's listed favorite manga. 
[*]Read a manga tagged with one of the explicit genres (Ecchi, Erotica, Hentai). 
[/list]""",
52:"""[b]52 - La Maceta[/b][list=1]
[*]Read a manga used in one of the MRC badges of any year.
[*]Read a manga that combines a tag that you like AND one that you dislike. 
[*]Read a manga that appears when putting in your username.  [color=#4682B4]- Advanced search, skip/exclude Hentai, Yaoi, Yuri if you wish - Add the following url to your form (replace both YOURUSERNAME with your username):[url=https://myanimelist.net/manga.php?cat=manga&q=YOURUSERNAME&type=0&score=0&status=2&mid=0&sm=0&sd=0&sy=0&em=0&ed=0&ey=0&c%5B%5D=a&c%5B%5D=b&c%5B%5D=c&c%5B%5D=f]YOURUSERNAME[/url][/color] 
[/list]""",
53:"""[b]53 - El Arpa[/b][list=1]
[*]Read a manga that started publishing in the 2010s. - (2010-2019)
[*]Read a manga with less than 2,000 total members. 
[*]Read a manga from a magazine with less than 250 titles in the database. 
[/list]""",
54:"""[b]54 - La Rana[/b][list=1]
[*]Read a manga where the main character is the gender opposite to the demographic. [color=#4682B4]- E.g. male MC in a shoujo [i]or[/i] female MC in a seinen. Suggestions: [url=https://www.mangaupdates.com/series?category=Male+Demographic+with+Female+Lead]Male Demographic with Female Lead[/url] | [url=https://www.mangaupdates.com/series?category=Female+Demographic+with+Male+Lead]Female Demographic with Male Lead[/url][/color]
[*]Read a [url=https://myanimelist.net/manga/genre/4/Comedy]Comedy[/url] manga.  
[*]Read a manga featured in an [url=https://myanimelist.net/stacks/search?type=manga]interest stack[/url].
[/list]"""
    }

    with open(filename, "w", encoding="utf-8") as file:
        for num in selected_numbers:
            if num in manga_data:
                file.write(manga_data[num] + "\n\n")
            else:
                file.write(f"[b]{num} - Not Found[/b]\n\n")

    print(f"Items list saved to {filename}")


selected_numbers = [20,23,3,16,7,33,39,17,44,32,24,21,31,37,53,43]
generate_manga_list(selected_numbers)
