# Curriculum vitae

Hi, my name is Bogdan. I am ...

Before my experience, I would like to say a few words about my interests.

## Interests

Briefly, I have two groups of interests:
  1. reduce the impact of humanity on the environment;
  2. improve the quality of life of people.

In both cases, I have areas that are more interesting to me then others.

Reduce the impact of humanity on the environment:
* renewable energy,
* garbage recycling,
* eco packaging,
* consumption optimization.

Improve the quality of life of people:
* robotics in different areas,
* pharmaceuticals,
* efficient transport.

## Experience

### Head of bioinformatic software development group

👉 [BIOCAD](https://biocad.ru/) / *Saint-Petersburg, Russia*

🗓 02.2019 – current time / *more than 2 years*

🔧 Haskell, Python, React, RabbitMQ, Gitlab

2020
ylab2
mq4

2019
abscan
avtogene


### Lead software developer

👉 [BIOCAD](https://biocad.ru/) / *Saint-Petersburg, Russia*

🗓 01.2018 – 01.2019 / *1 year 1 month*

🔧 Haskell

project-keeper / haskell
minibabr / cuda
scaffolding / haskell


### Senior software developer

👉 [BIOCAD](https://biocad.ru/) / *Saint-Petersburg, Russia*

🗓 01.2017 – 12.2017 / *1 year*

🔧 Haskell, ZeroMQ, Neo4j

**Protein folding.** If you are developing drugs, the candidate 3D model is very useful to make development more rational and efficient. But very often 3D model is not known. As such, you have to predict 3D model for your candidates using open databases (like [PDB](https://www.rcsb.org/)) and a variety of ideas and tricks. Learn more about [protein folding problem](https://en.wikipedia.org/wiki/Protein_folding), [CASP competition](https://predictioncenter.org), CASP14 winner [AlphaFold](https://deepmind.com/blog/article/AlphaFold-Using-AI-for-scientific-discovery). With my team, we have created an algorithm for predicting the 3D structure of antibodies that are used in BIOCAD as one of types of drugs. Quality of our algorithm is comparable to [Rosetta Software](https://www.rosettacommons.org/software) and [Schrödinger Software](https://www.schrodinger.com/products/prime).

**Message bus.** Algorithms such as protein folding and many other related to structure use a lot of computational resources. Thus, you need to distribute tasks across computing services. To solve this problem, I created a message bus based on ZeroMQ with bindings for Haskell and Python (these languages are used for our structural algorithms).


### Software developer

👉 [BIOCAD](https://biocad.ru/) / *Saint-Petersburg, Russia*

🗓 05.2016 – 12.2016 / *8 months*

🔧 Scala, Julia, MySQL, Docker

**Semantic system.** I wrote backend on Scala for a service for storing and connecting various biological items.
This version did not become production solution, but was a prototype for the next versions.

**Authorization.** In Scala I wrote a backend for an authorization system that stores information about users, salted and hashed passwords, groups and so on.
This authorization system was used by all services in the department and was changed to authorization [Keycloak](https://www.keycloak.org/) and [Azure](azure.microsoft.com) only in 2019.

**Asynchronous task execution.** For one of our services with a lot of computations I made module that allows balance workload on server with a lot of CPUs.
This solution was based on [Sun Grid Engine](http://star.mit.edu/cluster/docs/0.93.3/guides/sge.html).

**Basecaller algorithm.** Using Julia language, I solved the [basecalling](https://en.wikipedia.org/wiki/Base_calling) problem.
My solution was of the same quality as other algorithms, and sligtly worse than state-of-the art algorithm.


### Junior software developer

👉 [Laser Systems](http://www.lsystems.ru/en/) / *Saint-Petersburg, Russia*

🗓 07.2015 – 04.2016 / *10 months*

🔧 Qt

**Position algorithm.** I created algorithm to position laser tool in several modes: scan, shortest path from one point to another and so on. This problem contains a lot of fun problems in stereometry.

**Bus.** I wrote code for module that connects about 20 different components of product (motors, sensors, power and so on). Also this module make a health-check for all of this components with their own protocols based on protobuf.


### Mathematician

👉 [Kotlin-Novator](https://www.kotlin-novator.ru/) / *Saint-Petersburg, Russia*

🗓 01.2015 – 06.2015 / *6 months*

🔧 Python, LaTeX

**Algorithms.** I solved aircraft navigation problems and created different algorithms for them.
For example, how to find optimum trajectory to land down aircraft with a lot of restrictions such that total mass, current fuel level, hight, wind direction, current aircraft velocity and so on.
Another example is navigation problem for several aircrafts: find the optimum trajectory of the aircraft relative to other (taking off, landing, cruise formation).


### Junior web-developer

👉 Mr.Brooks Private Marketing

🗓 12.2013 – 12.2014 / *1 year*

🗺 Saint-Petersburg, Russia

🔧 WordPress, JavaScript, CSS, Adobe Illustrator

**Web-sites.** I made several web-sites, based on [WordPress](wordpress.com) CMS and customized them with JavaScript. Customers were AAG Group of compamies, Moskovsky Univermag, Mr. Brooks.

**Font.** In collaboration with designers we created new font. My task was to convert vector images to font format and made corrections for inter-letter spaces for all combinations of two letters.


## Education

### Saint Petersburg State University, Russia

🗓 09.2010 – 06.2015

Mathematics and Mechanics Faculty

Diploma of Specialist in Mathematical Physics

### Saint Petersburg State University, Russia

🗓 09.2011 – 08.2014

Faculty of Military Studies

Lieutenant

## Diplomas and certificates

* 2009, ICYS, Silver Medal in Mathematics, Pszczyna, Poland
* 2010, ICYS, Gold Medal in Mathematics, Bali, Indonesia
* 2010, Intel ISEF, Third place in Mathematics, San Jose, USA

## Presentations 

#### 02.2019 [Think like a graph / Думай как граф](https://youtu.be/BPB5omKK4Tc) (in russian)

Presentation from *FProg SPb* meeting about Neo4j database and Haskell libraries to work with it.

## Articles

* Nazarov A.I., Neterebskii B.O. *The Multiplicity of Positive Solutions to A Quasilinear Equation Generated By The Il′in–Caffarelli–Cohn–Nirenberg Inequality.* J Math Sci 224, 448–455 (2017). https://doi.org/10.1007/s10958-017-3427-z
* Yakovlev Pavel, Anikin Anton, Bolshakova Olga, Gasnikov Alexander, Gornov Alexander, Ermak Timofei, Makarenko Dmitrii, Morozov Vladimir, Neterebskii Bogdan. *Algorithms for local minimization of 3D molecules OPLS force field.* (2018). https://arxiv.org/abs/1810.03358
