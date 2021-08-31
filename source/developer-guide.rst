.. _developer_guide:

Developer Guide
===========================================

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

For data collection and data management, RHoMIS currently relies on `ODK collect <https://docs.getodk.org/collect-intro/>`_ and `ODK central <https://docs.getodk.org/central-intro/>`_. To make projects and 

Analysis Scripts
******************************

RHoMIS database
******************************

Data Querying Dashboard
******************************

.. _user_authentication_summary:

User Authentication System
*******************************

To create an account or login, the survey builder makes a call to the user authentication server. When logging in, the authentication server returns a token which can be decoded to give a user ID. This user ID is shared between the survey builder, the RHoMIS database, and the authentication system to manage survey projects.



