import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('netflix_titles.csv.zip')
df = df.dropna(subset=['type', 'release_year', 'rating', 'country', 'duration'])

type_counts = df['type'].value_counts()

plt.figure(figsize=(6,4))
plt.bar(type_counts.index, type_counts.values, color=['skyblue', 'orange'])
plt.title('Number of Movies VS TV Shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('movies_vs_tvshows.png')
plt.show()

rating_counts = df['rating'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(
    rating_counts,
    labels=rating_counts.index,
    autopct='%1.1f%%',   # <-- fixed
    startangle=90
)
plt.title('Percentage of Content Ratings') 
plt.tight_layout()
plt.savefig('content_Ratings_pie.png')
plt.show()

movie_df=df[df['type']=='Movie'].copy()
movie_df['duration_int']=movie_df['duration'].str.replace('min','').astype(int)

plt.figure(figsize=(8,6))
plt.hist(movie_df['duration_int'],bins=30,color='purple',edgecolor='black')
plt.title('Distrubutaion of movie Duration')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of movie')
plt.tight_layout()
plt.savefig('movies_duration_histogram.png')
plt.show()

release_count=df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(release_count.index,release_count.values,color='red')
plt.title('Release year VS Number of Shows')
plt.xlabel('Release year')
plt.ylabel('Number of Shows')
plt.tight_layout()
plt.savefig('release_year_Scatter.png')
plt.show() 

country_counts=df['country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_counts.index , country_counts.values , color='teal')
plt.title('Top 10 Countries by Number of Shows')
plt.xlabel('Number of shows')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('top10_countries.png')
plt.show()

content_by_year=df.groupby(['release_year','type']).size().unstack().fillna(0)
fig,ax=plt.subplots(1,2,figsize=(12,5))

ax[0].plot(content_by_year.index, content_by_year['Movie'], color='blue')
ax[0].set_title('Movies Relased Per Year')
ax[0].set_xlabel('year')
ax[0].set_ylabel('Number of Movies')

ax[1].plot(content_by_year.index, content_by_year['TV Show'], color='orange')
ax[1].set_title('TV Shows Relased Per Year')
ax[1].set_xlabel('year')
ax[1].set_ylabel('Number of Movies')

fig.suptitle('Comparsion of Movies and TV Shows Released Over Years')
plt.tight_layout()
plt.savefig('Movies_tv_shows_comparsion.png')
plt.show()