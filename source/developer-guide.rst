.. _developer_guide:

Developer Guide
===========================================

This developer guide is to help potential contributors understand how RHoMIS 2.0 components generally work
and how they interact with one another. It does not cover installation, testing, and contributions. Nor does 
it cover the specifics of the source code. For a more in depth look at how to install, test, and contribute, we
recommend looking at the GitHub repositories for each of the individual components. 

Summary of the RHoMIS 2.0 System
-------------------------------------------

RHoMIS 2.0 us made up of a series of interoperable applications. See below for a simple summary of these components
and how they interact:

.. image:: images/system_summary.png

Each component of the RHoMIS system is summarised below. Users can interact with these components in a range of ways. However, generally we expect users to interact with components in the following order:

#. Survey builder
#. ODK system
#. Data querying dashboard

Survey Builder
******************************

Generally, this should be the first point the user lands. When accessing the survey builder, the user will be prompted to create an account or login. Using the :ref:`user_authentication_summary`. Once a user is identified by their ID, the user will be able to make projects, make forms, and send this information off to ODK central, ready for data collection. The user will also enter project meta-data, which is used later for data processing, querying, and management.

ODK Central
******************************

For data collection and data management, RHoMIS currently relies on `ODK collect <https://docs.getodk.org/collect-intro/>`_ and `ODK central <https://docs.getodk.org/central-intro/>`_. Users should not have to use ODK central, and should instead create projects and forms through the survey builder application. 

Analysis Package
******************************

RHoMIS 2.0 relies on the R programming language for it's automated processing, calculations, and reporting. An `R-package <https://github.com/l-gorman/rhomis-R-package>`_ has been developed for RHoMIS 2.0 data processing. This package, is designed for use on the data-processing server, as well as for use by the wider community who hope to analyse rhomis data themselves.


RHoMIS database
******************************

RHoMIS 2.0 uses MongoDB, a popular NoSQL database. This central database stores:

* Processed data from ODK central
* Meta data from the survey builder
* User information from the authentication server
* User inputs from the data querying application


Data Querying Dashboard
******************************

This is a simple GUI application which allows users to access their processed data, and query the public RHoMIS database. 

.. _user_authentication_summary:

User Authentication System
*******************************

To create an account or login, an application makes a request to the user authentication server. When logging in, the authentication server returns a token which can be decoded to give a user ID. This user ID is used by each RHoMIS application to manage survey projects.



