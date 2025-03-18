def generate_manga_list(selected_numbers, filename="items_list.txt"):
    manga_data = {
    1: """[b]1 - El Gallo[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with an [url=https://www.mangaupdates.com/series?category=Animal+Leading+Character%2Fs]animal main character[/url]. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga about [url=https://www.mangaupdates.com/series?category=Betrayal]betrayal[/url].
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga featuring [url=https://myanimelist.net/manga/genre/6/Mythology]mythology[/url] or [url=https://www.mangaupdates.com/series?category=Folklore]folklore[/url]. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    2:"""[b]2 - El Diablito[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with a [url=https://www.mangaupdates.com/series?category=Devil%2Fs]devil character[/url]. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga by an author/artist you don't like. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga another MRC participant rated 4 or lower.  
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    3:"""[b]3 - La Dama[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a [url=https://myanimelist.net/manga/genre/42/Josei]josei[/url] or [url=https://myanimelist.net/manga/genre/25/Shoujo]shoujo[/url] manga.
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with a [url=https://www.mangaupdates.com/series?category=Strong+Female+Lead]Strong Female Lead[/url]. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with an all female main cast.
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    4:"""[b]4 - El Catrin[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a [url=https://myanimelist.net/manga/genre/27/Shounen]shounen[/url] or [url=https://myanimelist.net/manga/genre/41/Seinen]seinen[/url] manga. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga by an author/artist you don't know.
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga tagged under [url=https://www.mangaupdates.com/series?category=European+Ambience]European Ambience[/url]. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    5:"""[b]5 - El Paraguas[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with weather conditions on the cover.  
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a collection of short stories.
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a [url=https://myanimelist.net/manga/genre/44/Gender_Bender]Gender Bender[/url] manga. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    7:"""[b]7 - La Escalera[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga that was [url=https://myanimelist.net/reviews.php?t=manga]recently reviewed[/url].
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga by an author/artist who has published 5 manga or less.
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read an ongoing manga. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    8:"""[b]8 - La Botella[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a [url=https://myanimelist.net/manga/genre/55/Delinquents]Delinquents[/url] manga.
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga that started publishing in the 80s. - (1980-1989) 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga based on a [url=https://www.mangaupdates.com/series?category=Based%20on%20a%20Novel]novel/light novel[/url]/[url=https://www.mangaupdates.com/series?category=Based+on+a+Web+Novel]web novel[/url].
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    9:"""[b]9 - El Barril [/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga that is on one of the active MRC staff's Plan to Read list. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with an antihero or villain main character. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga that is not ranked. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    10:"""[b]10 - El Arbol [/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with plants on the cover. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga about [url=https://www.mangaupdates.com/series?category=Nature]nature[/url]. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga that takes place in the [url=https://www.mangaupdates.com/series?category=Countryside]countryside[/url]. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    11:"""[b]11 - El Melon[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a [url=https://myanimelist.net/manga/genre/52/CGDCT]CGDCT[/url] or [url=https://myanimelist.net/manga/genre/63/Iyashikei]Iyashikei[/url] manga.
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a [url=https://myanimelist.net/manga/genre/36/Slice_of_Life]Slice of Life[/url] manga.
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with only one genre. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    12:"""[b]12 - El Valiente[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read an [url=https://myanimelist.net/manga/genre/1/Action]Action[/url] or [url=https://myanimelist.net/manga/genre/2/Adventure]Adventure[/url] manga. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga recommended to you by another participant in the discussion thread. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a [url=https://www.mangaupdates.com/series?category=Battle+Royale]battle royale[/url] / [url=https://www.mangaupdates.com/series?category=Survival]survival[/url] manga.
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    13:"""[b]13 - El Gorrito[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a [url=https://myanimelist.net/manga/genre/53/Childcare]Childcare[/url] manga. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga that started publishing in the 2020s. - (2020-2025) 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with both a child and an adult main character. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    14:"""[b]14 - La Muerte[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga about a [url=https://www.mangaupdates.com/series?category=Family]family[/url].
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with a [url=https://www.mangaupdates.com/series?category=Shinigami%2FGrim+Reaper]shinigami[/url] character.
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with a weapon or blood on the cover. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    15:"""[b]15 - La Pera[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a [url=https://myanimelist.net/topmanga.php?type=oneshots]one-shot[/url]. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with a score of 8 or above. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga that is 1-3 volumes or 25 chapters or less in length. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    16:"""[b]16 - La Bandera[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a [url=https://myanimelist.net/topmanga.php?type=manhua]Manhua[/url] or a [url=https://myanimelist.net/topmanga.php?type=manhwa]Manhwa[/url].
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga that takes place outside of Japan, but in the real world. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a [url=https://myanimelist.net/manga/genre/17/Martial_Arts]Martial Arts[/url], [url=https://myanimelist.net/manga/genre/13/Historical]Historical[/url], or [url=https://myanimelist.net/manga/genre/21/Samurai]Samurai[/url] manga. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    17:"""[b]17 - El Bandolon[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga by your favorite author/artist.
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga that started publishing before or in the 70s. - (19XX-1979)
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with a symbol in the title. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    18:"""[b]18 - El Violoncello[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a [url=https://myanimelist.net/manga/genre/14/Horror]Horror[/url] or [url=https://myanimelist.net/manga/genre/37/Supernatural]Supernatural[/url] manga.
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url] 
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga tagged with [url=https://www.mangaupdates.com/series?category=Dystopia]Dystopia[/url] / [url=https://www.mangaupdates.com/series?category=Apocalypse]Apocalypse[/url] / [url=https://www.mangaupdates.com/series?category=Post-Apocalyptic]Post-Apocalyptic[/url]. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga that includes a character with a [url=https://www.mangaupdates.com/series?category=Disability%2Fies]disability[/url]. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    19:"""[b]19 - La Garza[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read an [url=https://www.mangaupdates.com/series?category=Isekai]isekai[/url] manga. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga including time travel.  
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read any manga recommended to your Favorite Manga listed in profile. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    20:"""[b]20 - El Pajaro[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a web/[url=https://www.mangaupdates.com/series?category=4-koma%2FYonkoma]4-koma[/url] manga. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a colored manga. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a [url=https://myanimelist.net/manga/genre/68/Memoir]Memoir[/url] or [url=https://www.mangaupdates.com/series?category=Biography+%2F+Autobiography]Biography/Autobiography[/url] manga. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    21:"""[b]21 - La Mano[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with a score of 6 or lower. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga tagged under [url=https://www.mangaupdates.com/series?category=Atypical+Art+Style]Atypical Art Style[/url], [url=https://www.mangaupdates.com/series?category=Elaborate+Art+Style]Elaborate Art Style[/url], [url=https://www.mangaupdates.com/series?category=Sketchy+Art+Style]Sketchy Art Style[/url], or [url=https://www.mangaupdates.com/series?category=Realistic+Art+Style]Realistic Art Style[/url]. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga that got [url=https://www.mangaupdates.com/series?category=Rushed+Ending+%2F+Axed&perpage=50]cancelled/axed[/url]. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    22:"""[b]22 - La Bota[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga by an author/artist duo. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a [url=https://www.mangaupdates.com/series?category=Magical+Girl%2Fs]Magical Girl[/url] or [url=https://www.mangaupdates.com/series?category=Magical+Boy%2Fs]Magical Boy[/url] manga. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with the same first and last letter. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    23:"""[b]23 - La Luna[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a doujinshi based on a series you've read.
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a [url=https://myanimelist.net/manga/genre/10/Fantasy]Fantasy[/url] or [url=https://myanimelist.net/manga/genre/7/Mystery]Mystery[/url] manga. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with the same number of male and female main characters. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    24:"""[b]24 - El Cotorro[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga from a mangaka that shares your birthday month. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga that has been [url=https://myanimelist.net/clubs.php?cid=5450]adapted to live action[/url]. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga related to something you previously read.
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    27:"""[b]27 - El Corazon[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a [url=https://myanimelist.net/manga/genre/8/Drama]Drama[/url] or [url=https://myanimelist.net/manga/genre/22/Romance]Romance[/url] manga.
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga ranked in the top 1000. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga from the ones listed under manga relations in the [url=https://myanimelist.net/clubs.php?cid=8776]Hidden Gems of Manga club[/url].
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url] """,

    28:"""[b]28 - La Sandia[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga by an author/artist who has published 10 manga or more. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a [url=https://www.mangaupdates.com/series?category=Food]Food[/url] or [url=https://myanimelist.net/manga/genre/47/Gourmet]Gourmet[/url] manga. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read an [url=https://www.mangaupdates.com/series?category=Award-Winning+Work]award-winning[/url] manga.  [color=#4682B4]- Make a note of which award the manga won.[/color]
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    29:"""[b]29 - El Tambor[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga about [url=https://www.mangaupdates.com/series?category=Music]Music[/url], or [url=https://www.mangaupdates.com/series?category=Art]Art[/url].
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with the same number of volumes as letters in your username.
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with a main character that is a professional in their field.  
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    30:"""[b]30 - El Camaron[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga another MRC participant rated 9 or higher. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with a one word title.
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga from a magazine with less than 50 titles in the database.
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    31:"""[b]31 - Las Jaras[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga that started publishing in the 90s. - (1990-1999) 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a [url=https://myanimelist.net/manga/genre/30/Sports]Sports[/url] or [url=https://www.mangaupdates.com/series?category=Game%2Fs]Games[/url] manga. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a [url=https://myanimelist.net/manga/genre/67/Medical]Medical[/url] or [url=https://www.mangaupdates.com/series?category=Illness]Illness[/url] manga.
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    32:"""[b]32 - El Musico[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a [url=https://myanimelist.net/manga/genre/23/School]School[/url] manga.
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url] 
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with no characters on the cover. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with a listed cast of 8 or more people. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    33:"""[b]33 - La Arana[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a [url=https://myanimelist.net/manga/genre/31/Super_Power]Super Power[/url], [url=https://www.mangaupdates.com/series?category=Demon%2Fs]Demon[/url], or [url=https://myanimelist.net/manga/genre/32/Vampire]Vampire[/url] manga.
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a [url=https://myanimelist.net/manga/genre/40/Psychological]Psychological[/url] or [url=https://myanimelist.net/manga/genre/45/Suspense]Suspense[/url] manga. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with both a human and a non-human main character. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    34:"""[b]34 - El Soldado[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a [url=https://myanimelist.net/manga/genre/18/Mecha]Mecha[/url], [url=https://myanimelist.net/manga/genre/39/Detective]Detective[/url], or [url=https://myanimelist.net/manga/genre/38/Military]Military[/url] manga. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with a Japanese honorific in the title (e.g. chan, san, kun, sama, etc.)
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga that started publishing in the 2000s. - (2000-2009)
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    35:"""[b]35 - La Estrella[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a [url=https://myanimelist.net/manga/genre/24/Sci-Fi]Sci-Fi[/url] or [url=https://myanimelist.net/manga/genre/29/Space]Space[/url] manga.
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga ranked ABOVE [url=https://myanimelist.net/topmanga.php?limit=2000]2,000[/url]
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga featuring [url=https://www.mangaupdates.com/series?category=Magic]Magic[/url] or [url=https://www.mangaupdates.com/series?category=Wizard%2Fs]Wizards[/url]. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    36:"""[b]36 - El Cazo[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with more users listed in PTR than Completed.
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with more than 10,000 completed members.
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with an older main character (i.e. 40+).  
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    37:"""[b]37 - El Mundo[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a [url=https://myanimelist.net/manga/genre/28/Boys_Love]BL[/url] or [url=https://myanimelist.net/manga/genre/26/Girls_Love]GL[/url] manga. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga featuring [url=https://www.mangaupdates.com/series?category=LGBT+Themes]LGBT themes[/url].
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with a vehicle on the cover. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    38:"""[b]38 - El Apache[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga that takes place in feudal Japan.
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga about [url=https://www.mangaupdates.com/series?category=Zombie%2Fs]zombies[/url]. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga featuring [url=https://www.mangaupdates.com/series?category=Curse%2Fs]Curses[/url]. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    39:"""[b]39 - El Nopal[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga that has not been adapted in any way. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with a [url=https://www.mangaupdates.com/series?category=Tsundere+Character%2Fs]tsundere[/url] character.
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with 6 or more words in its title. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    40:"""[b]40 - El Alacran[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga focused on [url=https://www.mangaupdates.com/series?category=Revenge]revenge[/url]. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga based on a one-shot.
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga tagged with your least favorite genre(s).
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    41:"""[b]41 - La Rosa[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with a [url=https://www.mangaupdates.com/series?category=Love+Confession%2Fs]love confession[/url].
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with more than 30,000 total members.
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with a main cast of [url=https://myanimelist.net/manga/genre/50/Adult_Cast]18+ year-olds[/url]. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    42:"""[b]42 - La Calavera[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with a main character that wears glasses. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga [url=https://www.mangaupdates.com/series?category=Based+on+an+Anime]based on an anime[/url]. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga series you can finish in one day. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    43:"""[b]43 - La Campana[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga suggested by MAL or by [url=https://anime.plus/]Anime+[/url].
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga that an active MRC staff member has rated 9 or higher. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga recommended by any MRC staff. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    44:"""[b]44 - El Canarito[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Re-read a manga. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga that has at least 2 anime seasons. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with more listed supporting characters than main characters. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    45:"""[b]45 - El Venado[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga about characters with [url=https://www.mangaupdates.com/series?category=Animal+Characteristics]animal characteristics[/url]. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga that's been the source of one of your completed anime.
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with an all male main cast. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    46:"""[b]46 - El Sol[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with more than 500 favorites. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a [url=https://myanimelist.net/featured/search?q=manga]featured[/url] manga. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with an element in the title (e.g. fire, water, earth, air, etc.).  
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    47:"""[b]47 - La Corona[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with about [url=https://www.mangaupdates.com/series?category=Royalty]Royalty[/url]. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga that is scored higher than its anime adaptation. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read the first or earliest work of your favorite creator. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    48:"""[b]48 - La Chalupa[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga that started publishing on the day you joined MAL (any month/year). 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga that started publishing in the month you joined MAL (any year). 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga that started publishing in the year you joined MAL.
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    49:"""[b]49 - El Pino[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with five or more genres.
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga that is 10+ volumes or 200 chapters or more in length
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga recommended to another manga you've read for this challenge.
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    50:"""[b]50 - El Pescado[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a favorite from one of your MAL friends - so they finally stop telling you to do it. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with an animal on the cover.
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga that has been [url=https://www.mangaupdates.com/series?category=Adapted+to+Game]Adapted to Game[/url]. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    51:"""[b]51 - La Palma [/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga based on a game. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read an active [url=https://myanimelist.net/about.php?go=team]MAL staff[/url] member's listed favorite manga. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga tagged with one of the explicit genres (Ecchi, Erotica, Hentai). 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    52:"""[b]52 - La Maceta[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga used in one of the MRC badges of any year.
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga that combines a tag that you like AND one that you dislike. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga that appears when putting in your username. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    53:"""[b]53 - El Arpa[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga that started publishing in the 2010s. - (2010-2019)
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga with less than 2,000 total members. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga from a magazine with less than 250 titles in the database. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]""",

    54:"""[b]54 - La Rana[/b]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga where the main character is the gender opposite to the demographic. 
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a [url=https://myanimelist.net/manga/genre/4/Comedy]Comedy[/url] manga.  
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]
    [*][color=DIMGRAY][Started: DATE] [Finished: DATE][/color]Read a manga featured in an [url=https://myanimelist.net/stacks/search?type=manga]interest stack[/url].
    [url=http://myanimelist.net/manga/ID_NUM]MANGA_TITLE[/url]"""
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
