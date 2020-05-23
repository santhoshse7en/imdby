from imdb.utils.config import base_uri
from imdb.utils.utils import TextBlob, pd, re, unidecode


def catch(func, handle=lambda e: e, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except:
        return None


def catch_list(func, handle=lambda e: e, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except:
        return []


def catch_dict(func, handle=lambda e: e, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except:
        return {}


def index_finder(targeted_tags, text: str) -> bool:

    for index, tag in enumerate(targeted_tags):
        if text in unicode(tag.get_text()).lower():
            break
    return index


def india_index_finder(targeted_tags, text: str) -> bool:

    for index, tag in enumerate(targeted_tags):
        if text in unicode(tag.select_one('td').a.get_text()).lower():
            break
    return index


def name(targeted_tag):
    return catch(lambda: unicode(targeted_tag.select_one('td.name').a.get_text()))


def titleid(targeted_tag):
    return catch(lambda: unicode(targeted_tag.select_one('td.name').a['href'][6:15]))


def credit(targeted_tag):
    return catch(lambda: unicode(targeted_tag.select_one('td.credit').get_text()))


def uri(targeted_tag):
    return catch(lambda: unicode('%s%s' % (base_uri, targeted_tag.select_one('td.name').a['href'][1:])))


def dataframe_data(df):
    return df.dropna(how='all').reset_index(drop=True)


def characters_title(targeted_tag):

    if targeted_tag.find_all('a'):
        characters_title = catch_list(
            lambda: [unicode(name.text) for name in targeted_tag.find_all('a')])
    else:
        characters_title = catch(lambda: unicode(
            ' '.join(targeted_tag.text.split())))

    return characters_title


def characters_id(targeted_tag):

    if targeted_tag.find_all('a'):
        characters_id = catch_list(
            lambda: [unicode(name['href'][28:]) for name in targeted_tag.find_all('a')])
    else:
        characters_id = None

    return characters_id


def characters_uri(targeted_tag):

    if targeted_tag.find_all('a'):
        characters_uri = catch_list(lambda: [unicode(
            '%s%s' % (base_uri, name['href'][1:])) for name in targeted_tag.find_all('a')])
    else:
        characters_uri = None

    return characters_uri


def top_250(targeted_tag: list) -> bool:

    top_rated_movies_df = pd.DataFrame(columns=[
                                       'Rank', 'Name', 'ID', 'URI', 'Director', 'Cast', 'Year', 'Rating', 'Votes', 'Rating_Stats', 'Poster'])

    for title in targeted_tag:

        title_card = title.select_one("td.titleColumn")
        poster_card = title.select_one('.posterColumn')
        rating_card = title.select_one('.ratingColumn')

        top_rated_movies_df.loc[len(top_rated_movies_df)] = [catch(lambda: unicode(title_card.contents[0])[:-1]),
                                                             catch(lambda: unicode(
                                                                 title_card.a.get_text())),
                                                             catch(lambda: unicode(
                                                                 title_card.a['href'][7:-1])),
                                                             catch(lambda: unicode(
                                                                 "%s%s" % (base_uri, title_card.a['href'][1:]))),
                                                             catch_list(lambda: [unicode(item.replace(
                                                                 ' (dir.)', '')) for item in title_card.a['title'].split(',') if ' (dir.)' in item]),
                                                             catch_list(lambda: [unicode(item.replace(
                                                                 ' (dir.)', '')) for item in title_card.a['title'].split(',') if ' (dir.)' not in item]),
                                                             catch(lambda: int(re.findall(
                                                                 r"\d+", unicode(title_card.select_one('span.secondaryInfo').get_text()))[-1])),
                                                             catch(lambda: float(
                                                                 unicode(rating_card.strong.get_text()))),
                                                             catch(lambda: int(re.findall(
                                                                 r"\d+", unicode(rating_card.strong['title'].replace(',', '')))[-1])),
                                                             catch(
                                                                 lambda: unicode(rating_card.strong['title'])),
                                                             catch(lambda: unicode(poster_card.select_one('img')['src']))]
    top_rated_movies_df = dataframe_data(top_rated_movies_df)
    return top_rated_movies_df


def top_box_office(targeted_tag, box_office, date):

    top_box_office_df = pd.DataFrame(columns=[
        'Name', 'ID', 'URI', 'Director', 'Cast', 'Weekend', 'Gross', 'Weeks', 'Poster', 'Start_Week', 'End_Week'])

    for title in targeted_tag:

        title_card = title.select_one("td.titleColumn")
        poster_card = title.select_one('.posterColumn')

        top_box_office_df.loc[len(top_box_office_df)] = [catch(lambda: unicode(title_card.a.get_text())),
                                                         catch(lambda: unicode(
                                                             title_card.a['href'][7:-1])),
                                                         catch(lambda: unicode(
                                                             "%s%s" % (base_uri, title_card.a['href'][1:]))),
                                                         catch_list(lambda: [unicode(item.replace(
                                                             ' (dir.)', '')) for item in title_card.a['title'].split(',') if ' (dir.)' in item]),
                                                         catch_list(lambda: [unicode(item.replace(
                                                             ' (dir.)', '')) for item in title_card.a['title'].split(',') if ' (dir.)' not in item]),
                                                         catch(lambda: unicode(title.select_one(
                                                             '.ratingColumn').get_text())),
                                                         catch(lambda: unicode(title.select_one(
                                                             'span.secondaryInfo').get_text())),
                                                         catch(lambda: unicode(title.select_one(
                                                             'td.weeksColumn').get_text())),
                                                         catch(lambda: unicode(
                                                             poster_card.select_one('img')['src'])),
                                                         catch(lambda: unicode("%s %s, %s" % (date[0].split()[
                                                               0], date[0].split()[1], box_office[-4:]))),
                                                         catch(lambda: unicode("%s %s, %s" % (date[0].split()[0], date[1], box_office[-4:])))]
    top_box_office_df = dataframe_data(top_box_office_df)
    return top_box_office_df


def trending_now(soup):
    return soup.select_one('#trending-container').select('.trending-list-rank-item-data-container')


def trending_now_df(targeted_tag):
    movie_df = pd.DataFrame(
        columns=['Rank', 'Name', 'ID', 'URI', '% OF TOP 10 PAGE VIEWS'])

    for tag in targeted_tag:
        name_tag = tag.select_one('.trending-list-rank-item-name')
        movie_df.loc[len(movie_df)] = [catch(lambda: unicode(tag.select_one('.trending-list-rank-item-rank-position').get_text())),
                                       catch(lambda: unicode(
                                           name_tag.get_text())),
                                       catch(lambda: unicode(
                                           name_tag.a['href'][7:16])),
                                       catch(lambda: unicode(
                                           "%s%s" % (base_uri, name_tag.a['href'][1:]))),
                                       catch(lambda: unicode(tag.select_one('.trending-list-rank-item-share').get_text()))]
    movie_df = dataframe_data(movie_df)
    return movie_df


def sentiment_textblob(analysis):
    return 'positive' if analysis.sentiment.polarity > 0 else ('neutral' if analysis.sentiment.polarity == 0 else 'negative')


def review_df(analyser, targeted_tag):
    user_reviews_df = pd.DataFrame(columns=['Title', 'Title_URI', 'User_Name', 'User_URI', 'User_Reviews', 'Review_Date', 'Rating',
                                            'Rating_Scale', 'Review_Helpful', 'Out_of', 'Review_Ation', 'Warning', 'Sentiment', 'Sentiment Score', 'Polarity Scorce'])

    for item in targeted_tag:
        title = catch(lambda: item.select_one('.title'))
        user_name = catch(lambda: item.select_one('.display-name-link'))
        rating = catch(lambda: item.select_one(
            '.rating-other-user-rating'))
        votes = catch(lambda: unicode(item.select_one(
            'div.actions').contents[0].replace(',', '')))
        user_review = catch(lambda: unicode(
            item.select_one('.text').get_text().replace("\'", "")))
        analysis = catch(lambda: TextBlob(user_review))

        user_reviews_df.loc[len(user_reviews_df)] = [catch(lambda: unicode(title.get_text())),
                                                     catch(lambda: "%s%s" % (
                                                         base_uri, unicode(title['href'][1:]))),
                                                     catch(lambda: unicode(
                                                         user_name.get_text())),
                                                     catch(lambda: "%s%s" % (
                                                         base_uri, unicode(user_name.a['href'][1:]))),
                                                     user_review,
                                                     catch(lambda: unicode(item.select_one(
                                                         '.review-date').get_text())),
                                                     catch(lambda: int(unicode(
                                                         rating.span.get_text()))),
                                                     catch(lambda: int(unicode(rating.select_one(
                                                         'span.point-scale').get_text()[1:]))),
                                                     catch(lambda: int(
                                                         re.findall(r"\d+", votes)[0])),
                                                     catch(lambda: int(
                                                         re.findall(r"\d+", votes)[1])),
                                                     votes,
                                                     catch(lambda: unicode(item.select_one(
                                                         '.spoiler-warning').get_text())),
                                                     catch(
                                                         lambda: sentiment_textblob(analysis)),
                                                     catch(lambda: analyser.polarity_scores(
                                                         user_review)['compound']),
                                                     catch(lambda: analyser.polarity_scores(user_review))]

    user_reviews_df = dataframe_data(user_reviews_df)
    return user_reviews_df


def external_site(keyword, soup):
    sites = soup.select_one(keyword).findNext('ul').select('li')
    sites_df = pd.DataFrame(
        columns=['Name', 'URI'])
    for item in sites:
        sites_df.loc[len(sites_df)] = [catch(lambda: unicode(item.get_text())),
                                       catch(lambda: unicode('%s%s' % (base_uri, item.a['href'][1:])))]
    sites_df = dataframe_data(
        sites_df)
    return sites_df


def company_data(keyword, soup):
    company = soup.select_one(keyword).findNext('ul').select('li')
    company_df = pd.DataFrame(columns=['Name', 'ID', 'URI'])

    for tag in company:
        company_df.loc[len(company_df)] = [catch(lambda: unicode(tag.a.get_text())),
                                           catch(lambda: unicode(
                                               tag.a['href'][9:])),
                                           catch(lambda: unicode('%s%s' % (base_uri, tag.a['href'][1:])))]

    company_df = dataframe_data(company_df)
    return company_df


def cast_credit(keyword, table_tag):
    cast = table_tag[index_finder(
        table_tag, keyword)].findNext('table').select('tr')
    cast_df = pd.DataFrame(
        columns=['Name', 'Credit', 'ID', 'URI'])

    for tag in cast:
        cast_df.loc[len(cast_df)] = [name(tag),
                                     credit(tag),
                                     titleid(tag),
                                     uri(tag)]

    cast_df = dataframe_data(cast_df)
    return cast_df


def cast_non_credit(keyword, table_tag):
    cast = table_tag[index_finder(
        table_tag, keyword)].findNext('table').select('tr')
    cast_df = pd.DataFrame(
        columns=['Name', 'ID', 'URI'])

    for tag in cast:
        cast_df.loc[len(cast_df)] = [name(tag),
                                     titleid(tag),
                                     uri(tag)]

    cast_df = dataframe_data(cast_df)
    return cast_df


def full_cast(keyword, table_tag):
    cast = table_tag[index_finder(
        table_tag, keyword)].findNext('table').select('tr')
    cast_df = pd.DataFrame(columns=[
        'Image', 'Name', 'Name_ID', 'Name_URI', 'Character_Name', 'Character_ID', 'Character_URI'])

    for tag in cast:
        primary_photo = tag.select_one('td.primary_photo')
        character = tag.select_one('td.character')
        cast_df.loc[len(cast_df)] = [catch(lambda: unicode(primary_photo.a.img['src'])),
                                     catch(lambda: unicode(
                                         primary_photo.a.img['title'])),
                                     catch(lambda: unicode(
                                         primary_photo.a['href'][6:15])),
                                     catch(lambda: unicode(
                                         '%s%s' % (base_uri, primary_photo.a['href'][1:]))),
                                     catch(lambda: characters_title(
                                         character)),
                                     catch(lambda: characters_id(
                                         character)),
                                     catch(lambda: characters_uri(character))]

    cast_df = dataframe_data(cast_df)
    return cast_df


def adivsory_satus(severity):
    adivsory_status = catch_dict(lambda: {catch(lambda: unicode(severity.select_one('span.advisory-severity-vote__title').get_text())):
                                          {catch(lambda: unicode(severity.select_one('button[value="none"]').get_text())): catch(lambda: digits(unicode(severity.select_one('button[value="none"]').findNext('span').get_text()))),
                                           catch(lambda: unicode(severity.select_one('button[value="mild"]').get_text())): catch(lambda: digits(unicode(severity.select_one('button[value="mild"]').findNext('span').get_text()))),
                                           catch(lambda: unicode(severity.select_one('button[value="moderate"]').get_text())): catch(lambda: digits(unicode(severity.select_one('button[value="moderate"]').findNext('span').get_text()))),
                                           catch(lambda: unicode(severity.select_one('button[value="severe"]').get_text())): catch(lambda: digits(unicode(severity.select_one('button[value="severe"]').findNext('span').get_text())))}})
    return adivsory_status


def advisory_reviews(advisory_nudity):

    advisory_nudity_review = catch(
        lambda: advisory_nudity.select('li[class="ipl-zebra-list__item"]'))
    advisory_reviews = catch_list(
        lambda: [unicode(review.contents[0]) for review in advisory_nudity_review])
    return advisory_reviews


def technical_specs(targeted_tag):

    technical_specs_df = pd.DataFrame(columns=['Name', 'URI'])

    for tag in targeted_tag:
        technical_specs_df.loc[len(technical_specs_df)] = [catch(lambda: unicode(tag.get_text())),
                                                           catch(lambda: unicode("%s%s" % (base_uri, tag['href'][1:])))]
    technical_specs_df = dataframe_data(technical_specs_df)
    return technical_specs_df


def rating_demo(tag):
    return {"Rating": float(tag.select_one('div[class="bigcell"]').get_text()),
            "IMDb Users": digits(unicode(tag.select_one('div[class="smallcell"]').get_text())),
            "Rating Demo Link": "%s%s" % (base_uri, tag.select_one('div[class="smallcell"]').a['href'][1:])}


def rating_demo_df(targeted_tag):
    rating_demo_df = pd.DataFrame(
        columns=[tag.text for tag in targeted_tag.select('tr')[0].select('th')])

    for tag in targeted_tag.select('tr')[1:]:
        demo_tag = tag.select('td[align="center"]')

        rating_demo_df.loc[len(rating_demo_df)] = [tag.select_one('div[class="allText"]').text,
                                                   rating_demo(demo_tag[0]),
                                                   rating_demo(demo_tag[1]),
                                                   rating_demo(demo_tag[2]),
                                                   rating_demo(demo_tag[3]),
                                                   rating_demo(demo_tag[4])]
    rating_demo_df = dataframe_data(rating_demo_df)
    return rating_demo_df

def rating_demo_region_df(targeted_tag):
    rating_demo_df = pd.DataFrame(
        columns=[tag.text for tag in targeted_tag.findNext('table').select('tr')[0].select('th')])

    for tag in targeted_tag.findNext('table').select('tr')[1:]:
        demo_tag = tag.select('td[align="center"]')

        rating_demo_df.loc[len(rating_demo_df)] = [rating_demo(demo_tag[0]),
                                                   rating_demo(demo_tag[1]),
                                                   rating_demo(demo_tag[2])]
    rating_demo_df = dataframe_data(rating_demo_df)
    return rating_demo_df

def rating_df(targeted_tag):
    rating_df = pd.DataFrame(
        columns=['Rating Scale', 'Percentage', 'Votes'])

    for tag in targeted_tag.findPrevious('table').select('tr')[1:]:

        rating_df.loc[len(rating_df)] = [unicode(tag.select_one('div[class="rightAligned"]').get_text()),
                                                   unicode(tag.select_one('div[class="topAligned"]').get_text()),
                                                   unicode(tag.select_one('div[class="leftAligned"]').get_text())]
    rating_df = dataframe_data(rating_df)
    return rating_df

def critic_df(targeted_tag):
    
    df = pd.DataFrame(columns=['Rating Value', 'Publisher', 'Author', 'Publisher URI', 'Summary'])
    
    for tag in targeted_tag:
        df.loc[len(df)] = [catch(lambda: unicode(tag.select_one('span[itemprop="ratingValue"]').get_text())),
                          catch(lambda: unicode(tag.select('span[itemprop="name"]')[0].get_text())),
                          catch(lambda: unicode(tag.select('span[itemprop="name"]')[1].get_text())),
                          catch(lambda: unicode(tag.a['href'])),
                          catch(lambda: unicode(tag.select_one('div[class="summary"]').get_text()))]
        
    df = dataframe_data(df)
    return df

def unicode(text: str) -> bool:
    return unidecode.unidecode(text).strip()


def digits(text: str) -> bool:
    return int(''.join(i for i in text if i.isdigit()))
