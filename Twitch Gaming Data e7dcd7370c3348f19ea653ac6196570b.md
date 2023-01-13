# Twitch Gaming Data

[Twitch](https://www.twitch.tv/) is the world’s leading live streaming platform for gamers, with 15 million daily active users. Using data to understand its users and products is one of the main responsibilities of the Twitch Science Team

Data was shared on [Github](https://github.com/sonnynomnom/Codecademy-Learn-SQL-from-Scratch/tree/master/Twitch), as a .csv file (800,000 rows) by the Twitch Science Team

Data tables used

- Stream table
- Chat table

1. Let’s get stated by getting a feel for the `stream` table and the `chat` table

Stream data schema

![Screenshot 2022-07-26 at 11.34.01.png](Twitch%20Gaming%20Data%20e7dcd7370c3348f19ea653ac6196570b/Screenshot_2022-07-26_at_11.34.01.png)

Chat data schema

![Screenshot 2022-07-26 at 11.36.10.png](Twitch%20Gaming%20Data%20e7dcd7370c3348f19ea653ac6196570b/Screenshot_2022-07-26_at_11.36.10.png)

```sql
--1.  Get a feel of the stream and chat tables
SELECT * FROM stream limit 20;
select * from chat limit 20;
```

1. Now let’s see the distinct list of games from the stream table

There are 20 unique games as shown below;

game

---

League of Legends

---

DayZ

---

Dota 2

---

Heroes of the Storm

---

Counter-Strike: Global Offensive

---

Hearthstone: Heroes of Warcraft

---

The Binding of Isaac: Rebirth

---

Agar.io

---

Gaming Talk Shows

---

---

Rocket League

---

World of Tanks

---

ARK: Survival Evolved

---

SpeedRunners

---

Breaking Point

---

Duck Game

---

Devil May Cry 4: Special Edition

---

Block N Load

---

Fallout 3

---

Batman: Arkham Knight

---

1. Any unique channels in the stream??

channel

---

frank

---

george

---

estelle

---

morty

---

kramer

---

jerry

---

helen

---

newman

---

elaine

---

susan

---

```sql
SELECT DISTINCT(channel)
FROM stream;
```

# Aggregate Functions:

1. Popular games in the stream

[Popular games on streams](https://www.notion.so/f0bb58b703d948f5b61ab7b2ef9812f6)

Top 3 performing games represent 61.5% of all viewers of the stream

- League of legends
- Dota 2
- Counter-Strike: Global offensive

```sql
select game, count(*)
from stream
group by 1
order by 2 desc;
```

---

1. With League of Legends (LoL) having significant viewers, let’s see where they are from

[Top streams of LoL](https://www.notion.so/3c0e590e1d6d4ea6af933959904756b6)

```sql
select country, count(*)
from stream
where game = 'League of Legends'
group by 1
order by 2 desc;
```

1. The `player` column contains the source the user is using to view the stream (`site`, `iphone`, `android`, etc). 

Create a list of `player`s and their number of streamers.

[Player sources](https://www.notion.so/9d90c1d56a4a4a6ca13f3ff93ec4ef97)

```sql
select player, count(*)
from stream
group by 1
order by 2 desc;
```

1. Create a new column named `genre` for each of the games.

Group the games into their genres: Multiplayer Online Battle Arena (MOBA), First Person Shooter (FPS), Survival, and Other.

Using `CASE`, your logic should be:

- If `League of Legends` → MOBA
- If `Dota 2` → MOBA
- If `Heroes of the Storm` → MOBA
- If `Counter-Strike: Global Offensive` → FPS
- If `DayZ` → Survival
- If `ARK: Survival Evolved` → Survival
- Else → Other

Use `GROUP BY` and `ORDER BY` to showcase only the unique game titles.

[Genres](https://www.notion.so/c247be4bda51416ba7077b5699f91bfa)

```sql
SELECT game,
CASE
 WHEN game = 'League of Legends' THEN 'MOBA'
 WHEN game = 'Dota 2' THEN 'MOBA'
 WHEN game = 'Heroes of the Storm' THEN 'MOBA'
 WHEN game = 'Counter-Strike: Global Offensive' THEN 'FPS'
 WHEN game = 'DayZ' THEN 'Survival'
 WHEN game = 'ARK: Survival Evolved' THEN 'Survival'
 ELSE 'Other'
 END AS 'genre',
 COUNT(*)
FROM stream
GROUP BY 1
ORDER BY 3 desc;
```

****How does view count change in the course of a day?****

1. Before we get started, let’s run this query and take a look at the `time` column from the `stream` table:

```sql
SELECT time
FROM stream
LIMIT 10;
```

The data type of the `time` column is `DATETIME`. It is for storing a date/time value in the database.

Notice that the values are formatted like:

`2015-01-01 18:33:52`

So the format is:

`YYYY-MM-DD HH:MM:SS`

1. SQLite comes with a `strftime()` function - a very powerful function that allows you to return a formatted date.

It takes two arguments:

`strftime(format, column)`

Let’s test this function out:

```sql
SELECT time,
   strftime('%S', time)
FROM stream
GROUP BY 1
LIMIT 20;
```

What do you think this does? Open the hint if you’d like to learn more.

- Returns the seconds from the timestamp column

1. Okay, now we understand how `strftime()` works. Let’s write a query that returns two columns:
- The hours of the `time` column
- The view count for each hour

Lastly, filter the result with only the users in *your country* using a `WHERE` clause.

Well I am originally from Tanzania, TZ, but this is not included in the stream data, presumably all other countries have been summed in the Null category

As for the country I am currently residing and studying in, United Kingdom represented as GB

[Stream in UK](https://www.notion.so/936eeeea2b2e4d06985a6eacb13f6d22)

```sql
SELECT strftime('%H', time), count(*)
FROM stream
WHERE country = 'UK'
GROUP BY 1;
```

**Joining two tables**

1. The `stream` table and the `chat` table share a column: `device_id`. Let’s join the two tables on that column.

```sql
SELECT *
FROM stream
JOIN chat
ON stream.device_id = chat.device_id;
```

1. Woohoo! You have completed the the guided practice, see what else you can dig up. For example:
- What are your favorite games? Can you find some insights about its viewers and chat room users?
- Is there anything you can do after joining the two tables?

The dataset **.csv** files are on [GitHub](https://github.com/sonnynomnom/Codecademy-Learn-SQL-from-Scratch/tree/master/Twitch).

P.S. Shout out to June Dershewitz ([@jdersh](https://twitter.com/jdersh)), Head of Data Governance and Analytics, for working with us on this project!

<aside>
🤓 Mission to create a dashboard!

</aside>