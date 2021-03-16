# Serbo/Croatian Crash Course
A Collection of language learning resources, tools, and data for Serbo-Croatian

The Goal is conversation first learning. Ideally, communicating ideas in 2 - 4 months. By focusing on the most common words immediately, communicating ideas early will be possible _(albeit with awful grammer)_

### Methodology
 - Memorize _(SRS/Flash Cards/Whatever)_ the top ~1000 words / short phrases.
 - Speak the language with native speakers from the start.
 - Progress on grammer, reading, writing after the inital rough conversations are happening.

### Resources
- [\[Free\] Johnny Harris - Fastest Way To Learn A Language](https://www.youtube.com/watch?v=3i1lNJPY-4Q)
  - Brief overview of the idea of conversation-first language learning.
- _[\[Paid\] Bright Space Course](https://brighttrip.com/course/language/)_
  - **(Optional)** Full course expanding on the ideas from Johnny's video.
- The 1000 top SerboCroatian words, collected, and corrected by a native speaker.
   - _(corrected up to line 102)_ [Top 1000 Words](top1000.csv)
   - _(unreviewed)_ [Top 100 Verbs](top100_verbs.csv)
   - _(unreviewed)_ [Top 100 Phrases](top100_phrases.csv)
 - Some sort of scripting, links to SRS / Flash Card tools to automate creating Decks of words.
   - for iPhone, try out [AnkiKun](https://apps.apple.com/us/app/ankikun-memorize-words/id1434399494) with the [AnkiKun-iPhone.zip file in the releases tab](https://github.com/tijb/SerboCroat_CrashCourse/release)!
 - Places to find a native speaker to talk to.
   - _links go here_
   - _and here_
   - _or here_

### Generating Your Own CSVs!
> This section is more technical. 
If you don't need to make them yourself look at [the releases tab](https://github.com/tijb/SerboCroat_CrashCourse/releases) for a release you can use!

**Prerequisites**
 - `python3` is used to format and create files
 - `make` is used as a task based builder.

**Steps**
Make an iPhone release for AnkiKun by:
```
git clone https://github.com/tijb/SerboCroat_CrashCourse
cd SerboCroat_CrashCourse
make zip_iphone
```

Android release will be coming when I get time to test on an Android phone.
