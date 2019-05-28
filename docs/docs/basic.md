## Quickstart

Eager to get started? This page gives a good introduction in how to get started with imdby. This assumes you already have imdby installed. If you do not, head over to the Installation section.

**Building a IMDb source**

Source objects are an abstraction of online multi-media content websites [IMDb](https://www.imdb.com/)

Building a Source will extract its movie, cast_and_crew, plot, plot_keywords, company, parental_guide, techincal_spec, release_info, taglines, external_sites, user_reviews for you

### Extracting IMDb Movie Information

You may also provide configuration parameters like titleid to create an instance of the IMDb class.

```Python
>>> from imdby.imdb import imdb

>>> details = imdb('tt4154796')
```

Every IMDb movie source has a set of infos like.

- Basic Movie Information
- Plot
- Plot Keywords
- Cast and Crew
- Company
- Release Info
- Taglines
- Parental Guide
- Technical Spec

The output of details directory.

![dir](https://user-images.githubusercontent.com/47944792/58303052-eb5d2180-7e0b-11e9-82c1-14627ee73ca3.PNG)

**Example of Extracting Movie Title**

```Python
>>> details.title

'Avengers: Endgame'
```

### Extracting External Sites Info

You may also provide configuration parameters like titleid to create an instance of the IMDb class.

```Python
>>> from imdby.external_sites import imdb

>>> external_sites = imdb('tt4154796')
```

Every IMDb movie external_sites source has a set of infos like.

- Official Sites
- Miscellaneous Sites
- Photographs
- Video Clips and Trailers

The output of external_sites directory.

![esdir](https://user-images.githubusercontent.com/47944792/58304230-0da56e00-7e11-11e9-8b3a-823f4cbff1d6.PNG)

**Example of Extracting Movie Official Sites**

```Python
>>> external_sites.official_sites_df.head()
```
![esdf](https://user-images.githubusercontent.com/47944792/58304291-48a7a180-7e11-11e9-9f7f-2ab1c252ec0e.PNG)

### Extracting User Reviews Info

You may also provide configuration parameters like titleid to create an instance of the IMDb class.

```Python
>>> from imdby.user_reviews import imdb

>>> user_reviews = imdb('tt4154796')
```

Every IMDb movie user_reviews source has a set of infos like.

- User Reviews
- User Reviews Sentiment Analysis

The output of user_reviews directory.

![urdir](https://user-images.githubusercontent.com/47944792/58304429-d2576f00-7e11-11e9-9d92-6c1ee010d003.PNG)

**Example of Extracting User Reviews for the Movie**

```Python
>>> user_reviews.user_reviews_df.head()
```
![urdf](https://user-images.githubusercontent.com/47944792/58304563-72ad9380-7e12-11e9-99cd-7a1fae184905.PNG)

### Extracting Critic Reviews Info

You may also provide configuration parameters like titleid to create an instance of the IMDb class.

```Python
>>> from imdby.critic_reviews import imdb

>>> critic_reviews = imdb('tt4154796')
```

Every IMDb movie critic_reviews source has a set of infos like.

- User Reviews

The output of critic_reviews directory.

![crdir](https://user-images.githubusercontent.com/47944792/58313533-6a158700-7e2b-11e9-8f82-401994d728e3.PNG)

**Example of Extracting Critic Reviews for the Movie**

```Python
>>> critic_reviews.critic_reviews_df.head()
```
![crdf](https://user-images.githubusercontent.com/47944792/58313556-7a2d6680-7e2b-11e9-99b0-4bc1e0d115a6.PNG)

### Search Person Name & Person ID

You may also provide configuration parameters like text to create an instance of the IMDb class.

```Python
>>> from imdby.search_person import imdb

>>> person = imdb('mouli')
```
**Manual Person Name selection done**

![pse](https://user-images.githubusercontent.com/47944792/58333901-0b1c3600-7e5c-11e9-846e-e5139aa8ae51.PNG)

IMDb movie search person source has a set of infos like.

- Person Name
- Person ID

The output of search_person directory.

```Python
>>> print(dir(person))
```

![pdir](https://user-images.githubusercontent.com/47944792/58333783-d5774d00-7e5b-11e9-8848-ef9dd3dce671.PNG)

**Example of Extracting Person ID**

```Python
>>> person_person_id

'nm1442514'
```

### Search Title Name & Person ID

You may also provide configuration parameters like text to create an instance of the IMDb class.

```Python
>>> from imdby.search_title import imdb

>>> title = imdb('entiran')
```
**Manual Title Name selection done**

![tse](https://user-images.githubusercontent.com/47944792/58334200-a7ded380-7e5c-11e9-87f9-709c24fb3634.PNG)

IMDb movie search title source has a set of infos like.

- Title Name
- Title ID

The output of search_title directory.

```Python
>>> print(dir(title))
```

![tdir](https://user-images.githubusercontent.com/47944792/58334175-9bf31180-7e5c-11e9-8e67-f7a4f94d8a5a.PNG)

**Example of Extracting Title ID**

```Python
>>> title_title_id

'tt1305797'
```

### Search Company Name & Person ID

You may also provide configuration parameters like text to create an instance of the IMDb class.

```Python
>>> from imdby.search_company import imdb

>>> company = imdb('warner')
```
**Manual Title Name selection done**

![cse](https://user-images.githubusercontent.com/47944792/58334557-6d296b00-7e5d-11e9-92f9-dd888f0b0284.PNG)

IMDb movie search company source has a set of infos like.

- Company Name
- Company ID

The output of search_company directory.

```Python
>>> print(dir(company))
```

![cdir](https://user-images.githubusercontent.com/47944792/58334535-64389980-7e5d-11e9-8fe8-5cdb8d800111.PNG)

**Example of Extracting Company ID**

```Python
>>> company_company_id

'co0423665'
```
