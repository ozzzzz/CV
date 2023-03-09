# Curriculum vitae

Hi, my name is Bogdan.

I am a software developer with over 6 years of backend experience, mainly in Haskell and Python, and over 3 years of team management experience. I also have experience with frontend (mostly React), distributed systems and machine learning. But each technology for me is just a way to solve problems that can make the world a little better.

Before my experience, I would like to say a few words about my interests.

## Interests

Briefly, I have two groups of interests. In both cases, I have areas that are more interesting to me than others:

*Reduce the impact of humanity on the environment:*
  * renewable energy,
  * garbage recycling,
  * eco-packaging,
  * consumption optimization.

*Improve the quality of life of people:*
  * robotics in different areas,
  * pharmaceuticals,
  * efficient transport.


## Experience

My experience has standard CV order (last experience at the top). Read from bottom to top to see it in chronological order.

### Software developer

👉 [Nortal](https://nortal.com/) / *Belgrade, Serbia*

🗓 08.2022 – current time / *less than 1 year*

🔧 Python, Kubernetes

### Senior software developer

👉 [The Anylogic Company](https://www.anylogic.com/) / *Saint-Petersburg, Russia*

🗓 09.2021 – 08.2021 / *11 months*

🔧 Java, Python, Docker, Gitlab, NSIS

**Application redesign.** The company's main product has a complex and intricate design, and also not the latest technology stack. My job is to help rebuild, simplify and update the application so that it can continue to develop fully.

**Recreate installer.** The main product is mostly standalone application that should work on Windows, Linux and MacOS. My task was to recreate the process of the creation of installers for all OS, because it was the bottleneck in the development and release pipeline. The result is the fully documented and reproducible environments with IaC, based on the Gitlab pipelines.

### Head of bioinformatics software development group

👉 [BIOCAD](https://biocad.ru/) / *Saint-Petersburg, Russia*

🗓 02.2019 – 08.2021 / *2 years 7 months*

🔧 Haskell, Python, React, RabbitMQ, Gitlab, Kubernetes

**Biological data storage services.** During the discovery of drugs, a lot of biological data is generated: sequences of antibodies, plasmids, viruses, the results of clustering and annotations their sequences, data from real experiments, etc. The task is not only to save all this data in a proper way but also to supplement them with a lot of connections for easy analysis and rational conclusions. Together with the team, we developed two services: one for antibodies and the other for viruses.

**Laboratory algorithms and service.** [*In silico*](https://en.wikipedia.org/wiki/In_silico) modeling is a very powerful tool to make drug discovery more rational and faster. But [in vitro](https://en.wikipedia.org/wiki/In_vitro) (in glass) and [in vivo](https://en.wikipedia.org/wiki/In_vivo) (on animals) is an indispensable part of the whole process. There are many steps from a sequence on your computer to a real protein or virus in a test tube. It turns out that these steps can be done faster or more efficiently using various bioinformatics algorithms. Together with the team, we have developed (and are still developing) a couple of dozen such algorithms. In addition, we developed a service with React and [NextJS](https://nextjs.org/) frontend to make our algorithms lab-friendly. Each algorithm is written in Haskell or Python and runs on several servers using the Kubernetes queue and its API.

**Message bus, version 2.** In 2017, I developed a message bus for distributing a computationally heavy algorithm across servers. At the end of 2019, together with an intern, we developed a new version. It was based on RabbitMQ and was used not only in our department but also for interdepartmental communication. The trickiest part was providing a single entry point that could validate message types and their content for the public API.


### Lead software developer

👉 [BIOCAD](https://biocad.ru/) / *Saint-Petersburg, Russia*

🗓 01.2018 – 01.2019 / *1 year 1 month*

🔧 Haskell, Neo4j, Mongo

**Scaffold algorithm.** Sometimes we have a 3D structure for a drug candidate. In this case, we do not need to solve the protein folding problem (see below). But we have to deal with another problem -- finding valid details in other 3D structures in order to use them as inspiration for rational [*in silico*](https://en.wikipedia.org/wiki/In_silico) modeling. We solved this problem by using the entire [PDB](https://www.rcsb.org/) database. Also, a poster with this algorithm was presented at [PEGS 2019](https://www.pegsummit.com/19#).

**Algorithm for minimization.** One of the main parts of finding the correct 3D structure is the minimization problem -- you have to predict minimum energy conformation in some [force fields](https://en.wikipedia.org/wiki/Force_field_(chemistry)). One of the commonly used force fields is [OPLS](https://en.wikipedia.org/wiki/OPLS). In cooperation with the Matrosov Institute for System Dynamics and Control Theory, we have developed several optimization methods that allow us to find the local extremum faster than standard methods. The article "Algorithms for local minimization of 3D molecules OPLS force field" was also published (see below in the articles).

**Project management service.** BIOCAD has a full cycle of drug development -- from R&D to Production. This means there are many different projects going through this process. Together with the team, we developed a service with Mongo database, Haskell backend, and React frontend to manage them. An interesting part of this project was striking a balance between the ease of editing project fields and their consistency after editing.


### Senior software developer

👉 [BIOCAD](https://biocad.ru/) / *Saint-Petersburg, Russia*

🗓 01.2017 – 12.2017 / *1 year*

🔧 Haskell, ZeroMQ, Neo4j

**Protein folding.** If you are developing drugs, the candidate 3D model is very useful to make development more rational and efficient. But very often the 3D model is not known. As such, you have to predict a 3D models for your candidates using open databases (like [PDB](https://www.rcsb.org/)) and a variety of ideas and tricks. Learn more about [protein folding problem](https://en.wikipedia.org/wiki/Protein_folding), [CASP competition](https://predictioncenter.org), CASP14 winner [AlphaFold](https://deepmind.com/blog/article/AlphaFold-Using-AI-for-scientific-discovery). With my team, we have created an algorithm for predicting the 3D structure of antibodies that are used in BIOCAD as one of the types of drugs. The quality of our algorithm is comparable to [Rosetta Software](https://www.rosettacommons.org/software) and [Schrödinger Software](https://www.schrodinger.com/products/prime).

**Message bus.** Algorithms such as protein folding and many other related to structure use a lot of computational resources. Thus, you need to distribute tasks across computing services. To solve this problem, I created a message bus based on ZeroMQ with bindings for Haskell and Python (these languages are used for our structural algorithms).


### Software developer

👉 [BIOCAD](https://biocad.ru/) / *Saint-Petersburg, Russia*

🗓 05.2016 – 12.2016 / *8 months*

🔧 Scala, Julia, MySQL, Docker

**Semantic system.** I wrote backend on Scala for a service for storing and connecting various biological items. This version did not become a production solution but was a prototype for the next versions.

**Authorization.** In Scala I wrote a backend for an authorization system that stores information about users, salted and hashed passwords, groups, and so on. This authorization system was used by all services in the department and was changed to authorization [Keycloak](https://www.keycloak.org/) and [Azure](azure.microsoft.com) only in 2019.

**Asynchronous task execution.** For one of our services with a lot of computations, I made a module that allows to balance workload on a server with a lot of CPUs. This solution was based on [Sun Grid Engine](http://star.mit.edu/cluster/docs/0.93.3/guides/sge.html).

**Basecaller algorithm.** Using Julia language, I solved the [basecalling](https://en.wikipedia.org/wiki/Base_calling) problem. My solution was of the same quality as other algorithms, and slightly worse than a state-of-the-art algorithm.


### Junior software developer

👉 [Laser Systems](http://www.lsystems.ru/en/) / *Saint-Petersburg, Russia*

🗓 07.2015 – 04.2016 / *10 months*

🔧 Qt

**Position algorithm.** I created an algorithm to position the laser tool in several modes: scan, the shortest path from one point to another, and so on. This problem contains a lot of fun problems in solid geometry.

**Bus.** I wrote code for a module that connects about 20 different components of the product (motors, sensors, power, and so on). Also, this module makes a health check for all of these components with their own protocols based on protobuf.


### Mathematician

👉 [Kotlin-Novator](https://www.kotlin-novator.ru/) / *Saint-Petersburg, Russia*

🗓 01.2015 – 06.2015 / *6 months*

🔧 Python, LaTeX

**Algorithms.** I solved aircraft navigation problems and created different algorithms for them. For example, how to find the optimum trajectory to land down aircraft with a lot of restrictions such that total mass, current fuel level, height, wind direction, current aircraft velocity, and so on. Another example is the navigation problem for several aircraft: find the optimum trajectory of the aircraft relative to others (taking off, landing, cruise formation).


### Junior web-developer

👉 Mr.Brooks Private Marketing / *Saint-Petersburg, Russia*

> Small branding agency.

🗓 12.2013 – 12.2014 / *1 year*

🔧 WordPress, JavaScript, CSS, Adobe Illustrator

**Web-sites.** I made several websites, based on [WordPress](wordpress.com) CMS and customized them with JavaScript. Customers were the AAG Group of companies, Moskovsky Univermag, Mr. Brooks.

**Font.** In collaboration with designers, we created a new font. My task was to convert vector images to font format and make corrections for inter-letter spaces for all combinations of two letters.


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
* 2021, [Deep learning specialization on Coursera](https://www.coursera.org/specializations/deep-learning) ([certificate](https://coursera.org/verify/specialization/P3EHQX4ZZZJ9)):
  * [Neural Networks and Deep Learning](https://coursera.org/verify/Q2DFTK2EXP8X)
  * [Improving Deep Neural Networks: Hyperparameter Tuning, Regularization and Optimization](https://coursera.org/verify/WQUMDL3FSQUQ)
  * [Structuring Machine Learning Projects](http://coursera.org/verify/Q3GAYF59P7QJ)
  * [Convolutional Neural Networks](https://coursera.org/verify/9YXGPAWHTGHF)
  * [Sequence Models](https://coursera.org/verify/QHEHGZTULZWC)
* 2022, [Modern Robotics: Mechanics, Planning, and Control Specialization](https://www.coursera.org/specializations/modernrobotics)
  * [Foundations of Robot Motion](https://www.coursera.org/account/accomplishments/verify/KC6E93SCLJEN) 

## Presentations 

#### 02.2019 [Think like a graph / Думай как граф](https://youtu.be/BPB5omKK4Tc) (in Russian)

Presentation from *FProg SPb* meeting about Neo4j database and Haskell libraries to work with it.

## Articles

* Nazarov A.I., Neterebskii B.O. *The Multiplicity of Positive Solutions to A Quasilinear Equation Generated By The Il′in–Caffarelli–Cohn–Nirenberg Inequality.* J Math Sci 224, 448–455 (2017). https://doi.org/10.1007/s10958-017-3427-z
* Yakovlev Pavel, Anikin Anton, Bolshakova Olga, Gasnikov Alexander, Gornov Alexander, Ermak Timofei, Makarenko Dmitrii, Morozov Vladimir, Neterebskii Bogdan. *Algorithms for local minimization of 3D molecules OPLS force field.* (2018). https://arxiv.org/abs/1810.03358
