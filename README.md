# The-Uber-way
Unsupervised Machine Learning

<img align="left" alt="Visual Studio Code" width="1080px" src="https://gazettereview.com/wp-content/uploads/2017/09/uber-taxi-for-web-0-1.jpg" />

# About

---

Uber Technologies, Inc., commonly known as Uber, is an American technology company. Its services include ride-hailing, food delivery (Uber Eats), package delivery, couriers, freight transportation. Formerly it was known as Ubercab (2009-2011). Uber’s net worth is $75 million. Currently Uber is present in 71 countries and 890 cities, with 5 major countries; US, Mexico, Brazil, Spain, and India.

<img align="left" alt="Visual Studio Code" width="1080px" src="uber.png" />

If you might have ever booked an Uber cab, you must have noticed that the process is quite simple –just press a button, set the pickup location, request a car, go for a ride and pay with a click of a button. The process is simple but there is a lot going on behind the scenes.

As it turns out, there’s a great deal of data being collected, produced, and visualized behind the scenes — all working to create a more efficient company and impact transportation as a whole.

we are going to learn how Uber saves your time in reaching your destination.

# How Uber determines Optimal Position of Cabs

---

# #1 Data Collection

---

Every time someone books a ride from Uber's application, Uber saves their location with a timestamp. Uber has been collecting this data since they begin its operations. Uber uses this data to determine the optimal position of cabs.

<img align="left" alt="Visual Studio Code" width="1080px" src="uber2.png" />

We can also plot these coordinated in a map by importing folium module

<img align="left" alt="Visual Studio Code" width="1080px" src="uber3.png" />

# #2.1 Supervised Learning

---

As the name suggests, this type of learning algorithm has a supervisor or teacher. Basically, a well labeled data is the supervisor or teacher, and the algorithm uses this data to learn patterns or features. Like in the fruit sorting problem, a child who can read was given a table of fruits and their names. He was later asked to sort the fruits in a basket. With the provided table, he was able to sort them and knows which basket contains which fruit.

# #2.2 Unsupervised Learning

---

Unlike supervised learning, there are no supervisor or teacher present i.e. algorithms use unlabelled data to find features or patterns. Consider a newborn child who can’t read. We cannot give the same table that we gave to the previous child. But when this child will be asked to sort the fruits, he/she can sort on the basis of shape, color, or weight. One thing to notice is that at the end, he was able to sort the fruits in a basket but he/she still doesn’t know which basket contains which fruit.

